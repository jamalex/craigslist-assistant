from django.db import models
from django.utils.safestring import SafeString, SafeUnicode, mark_safe

statuses = (("Unchecked", "Unchecked"),
            ("Ignored", "Ignored"),
            ("Wrong area", "Wrong area"),
            ("To contact!", "To contact!"),
            ("Contact later", "Contact later"),
            ("Left message", "Left message"),
            ("Scheduled", "Scheduled"),
            ("Emailed", "Emailed"),
            ("No answer", "No answer"),
            ("Taken", "Taken"),
            ("Liked", "Liked"),
            ("Disliked", "Disliked"),
            ("Blacklist", "Blacklist"))

class Apartment(models.Model):
    postid = models.IntegerField(primary_key=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    date_posted = models.DateField(null=True)
    rating = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=50, blank=True)
    square_feet = models.IntegerField(blank=True, null=True)
    bedrooms = models.IntegerField(null=True)
    small_notes = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=statuses, default="Unchecked")

