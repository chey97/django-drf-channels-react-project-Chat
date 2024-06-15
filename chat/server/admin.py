from django.contrib import admin

# Register your models here.

from .models import Channel, Category, Server


class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "server")

    class Meta:
        model = Channel


class ServerAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "category", "description")

    class Meta:
        model = Server


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category)
admin.site.register(Server, ServerAdmin)
