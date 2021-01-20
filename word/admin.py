from django.contrib import admin
from import_export import resources
from .models import WordsDefining
from import_export.admin import ImportExportModelAdmin


class WordResource(resources.ModelResource):
    class Meta:
        model = WordsDefining


class WordAdmin(ImportExportModelAdmin):
    list_display = ['word', 'category', 'ranking']
    list_display_links = ['word', 'category']
    list_filter = ['category']
    search_fields = ['word', 'category', 'ranking']

    resource_class = WordResource


admin.site.register(WordsDefining , WordAdmin)
