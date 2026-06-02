from typing import Any

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeString

from .models import Catalog, Star


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'get_description', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    ordering = ('created_at',)
    search_fields = ('name', 'code', 'description')

    def get_description(self, catalog: Catalog) -> str:
        return '%s...' % catalog.description[:50].strip()

    get_description.admin_order_field = 'description'
    get_description.short_description = 'Description'


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_catalog_link',
        'source_id',
        'con',
        'ra',
        'dec',
        'dist',
        'mag',
    )
    list_filter = ('name', 'catalog__code', 'con')
    ordering = ('source_id',)
    search_fields = ('name', 'con')

    def get_catalog_link(self, star: Star) -> SafeString | Any:
        catalog_admin_name = 'admin:catalog_catalog_change'
        catalog_url = reverse(catalog_admin_name, args=(star.catalog.id,))
        catalog_name = str(star.catalog)
        return format_html('<a href="{}">{}</a>', catalog_url, catalog_name)

    get_catalog_link.admin_order_field = 'catalog'
    get_catalog_link.short_description = 'Catalog'
