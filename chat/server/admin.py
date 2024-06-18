from django.contrib import admin

# Register your models here.

from .models import Channel, Category, Server


class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "server")

    class Meta:
        model = Channel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")

    class Meta:
        model = Category


class ServerAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "category", "description")

    class Meta:
        model = Server


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Server, ServerAdmin)
