from django.contrib import admin
from .models import Ad, Response


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'dateCreation']
    list_filter = ('author', 'dateCreation')


admin.site.register(Response)
admin.site.register(Ad, AdAdmin)
