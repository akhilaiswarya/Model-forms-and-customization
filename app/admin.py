from django.contrib import admin

from app.models import *
# Register your models here.

class custimizeWebPageForm(admin.ModelAdmin):
    list_display=['topic_name','name','url','gmail']
    list_display_links=['name','gmail']
    list_editable=['topic_name','url']
    list_filter=['name']
    list_per_page=1
    search_fields=['name']




admin.site.register(Topic)

admin.site.register(WebPage,custimizeWebPageForm)

admin.site.register(AccessRecord)

