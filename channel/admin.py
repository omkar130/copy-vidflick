from django.contrib import admin
from import_export.admin import ImportExportModelAdmin   
from  channel.models import Channel


class ChannelAdmin(ImportExportModelAdmin):
    list_display = ["channel_name","user","status"]    # to export the list of channels and their subscribers
    

admin.site.register(Channel,ChannelAdmin)
