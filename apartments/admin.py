from django.contrib import admin

from .models import *

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("title", "_postid", "status", "rating", "small_notes", "phone_number", "date_posted", "price", "district", "square_feet",)
    list_filter = ("status", "phone_number", "area")
    list_editable = ("status", "small_notes", "phone_number", "rating")
    search_fields = ["title", "small_notes", "phone_number", "district", "notes"]

    def _postid(self, obj):
         return mark_safe("<a href='%s' target='_blank'>%s</a>" % (obj.url, obj.postid))
    _postid.allow_tags = True
    _postid.admin_order_field = "postid"

admin.site.register(Apartment, ApartmentAdmin)