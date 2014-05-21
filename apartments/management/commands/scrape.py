from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from BeautifulSoup import BeautifulSoup
import urllib
import re, sys, json
from datetime import datetime

from apartments.models import Apartment

from craigslist_assistant.settings import *

site = "https://%s.craigslist.org/search/apa/%s?catAbb=apa&minAsk=%d&maxAsk=%d&bedrooms=%d&query=" % (CRAIGSLIST_CITY, CRAIGSLIST_AREA, MIN_PRICE, MAX_PRICE, BEDROOMS)
coords_site = "http://%s.craigslist.org/jsonsearch/apa/%s/" % (CRAIGSLIST_CITY, CRAIGSLIST_AREA)

# rect format: (bottom_left_lat, bottom_left_long, top_right_lat, top_right_long)

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36"

urllib._urlopener = AppURLopener()

class Command(BaseCommand):

    def handle(self, *args, **options):

        print "Loading coordinates..."

        coords = json.loads(urllib.urlopen(coords_site).read())[0]
        coord_lookup = {c["PostingID"]: c for c in coords}

        html = ""
        for i in range(0, 100 * NUM_PAGES_TO_REQUEST, 100):
            print "Loading page for results %d-%d..." % (i, i+99)
            html += urllib.urlopen(site + "&s=%d" % i).read().replace("&amp;", "&")

        print "Finished loading pages!"

        soup = BeautifulSoup(html)
        postings = soup('p')

        for post in postings:

            content = post.text.lower()

            area = ""

            longitude = coord_lookup.get(post["data-pid"], {"Longitude": ""})["Longitude"]
            latitude = coord_lookup.get(post["data-pid"], {"Latitude": ""})["Latitude"]
            # print "%r, %r" % (longitude, latitude)

            for a in GOOD_AREAS:

                if longitude and latitude:
                    rect = a["rectangle"]
                    if (rect[0] < float(latitude) < rect[2]) and (rect[1] < float(longitude) < rect[3]):
                        area = a["name"]
                        break
                else:
                    if any([item in content for item in a["district_names"]]):
                        area = a["name"]
                        break

            if not area:
                continue

            if any([item in content for item in BLACKLIST]):
                continue

            apt, new = Apartment.objects.get_or_create(postid=post["data-pid"])

            if longitude and latitude:
                apt.longitude = longitude
                apt.latitude = latitude

            apt.area = area

            district_node = post.findChild(attrs={"class":"pnr"}).findChild("small")
            apt.district = district_node and district_node.text.strip("()").lower() or ""

            if not apt.title:
                print "NEW:", post('a')[1].contents[0]

            apt.title = post('a')[1].contents[0]

            apt.price = post.findChild(attrs={"class":"price"}).text.split(";")[-1]

            apt.url = "https://sandiego.craigslist.org" + post('a')[1]['href']

            sqft = re.findall("\d+ft", post.text)
            if sqft and isinstance(sqft[0], basestring):
                apt.square_feet = sqft[0].replace("ft", "")

            rooms = re.findall("\dbr", post.text)
            if rooms and isinstance(rooms[-1], basestring):
                apt.bedrooms = rooms[-1].replace("br", "")

            apt.date_posted = datetime.strptime("%s, %d" % (post.findChild(attrs={"class":"date"}).text, datetime.now().year), "%b %d, %Y")

            apt.save()