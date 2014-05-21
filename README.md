craigslist-assistant
====================

Setup:

1. Preferably in a virtualenv, run: `pip install -r requirements.txt`
2. `./manage.py syncdb --migrate`
3. Edit the bottom of settings.py with your own specifications about the needs for your apartment (area, price, rooms, etc)
4. Run `./manage.py scrape` to load the latest Craigslist listings into your local DB
5. Run `./manage.py runserver` to get the server going.
6. Load `http://127.0.0.1:8000` in the browser; it will autoredirect to the admin interface. Login.
7. Use the filters on the right to select "Unchecked" (ones you haven't categorized yet).
8. Click the number under "postid" (2nd column) to jump to the Craiglist posting page.
9. Click the title (first column) to load the Django model for the record.
10. Edit stuff (category, notes, etc) right from the admin listing page, and click save at the bottom.
11. Run the "scrape" management command whenever you want to load new stuff.
12. Find your new perfect home.
