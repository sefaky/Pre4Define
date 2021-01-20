from django.contrib import admin
from import_export import resources
from .models import ColorDefining
from import_export.admin import ImportExportModelAdmin


class ColorResource(resources.ModelResource):
    class Meta:
        model = ColorDefining


class ColorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'category', 'ranking', 'pegi', 'firstHex']
    list_display_links = ['id', 'category', 'ranking']
    list_filter = ['category', 'pegi']
    search_fields = ['category', 'ranking']
    resource_class = ColorResource


admin.site.register(ColorDefining , ColorAdmin)



