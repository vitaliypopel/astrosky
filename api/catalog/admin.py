from typing import Any

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeString

from .models import Catalog, Constellation, Star


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


@admin.register(Constellation)
class ConstellationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'ra', 'dec', 'area', 'area_pct')
    ordering = ('name',)
    search_fields = ('name', 'code')


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = (
        'get_name',
        'get_catalog_link',
        'source_id',
        'get_constellation_link',
        'ra',
        'dec',
        'dist',
        'mag',
    )
    list_filter = ('name', 'catalog__code', 'constellation__code')
    ordering = ('source_id',)
    search_fields = (
        'name',
        'hip',
        'hd',
        'hr',
        'gl',
        'bf',
        'constellation__name',
        'constellation__code',
    )

    def get_name(self, star: Star) -> str:
        return str(star)

    get_name.admin_order_field = 'name'
    get_name.short_description = 'Name'

    def get_catalog_link(self, star: Star) -> SafeString | Any:
        catalog_admin_name = 'admin:catalog_catalog_change'
        catalog_url = reverse(catalog_admin_name, args=(star.catalog.id,))
        catalog_name = str(star.catalog)
        return format_html('<a href="{}">{}</a>', catalog_url, catalog_name)

    get_catalog_link.admin_order_field = 'catalog'
    get_catalog_link.short_description = 'Catalog'

    def get_constellation_link(self, star: Star) -> SafeString | Any:
        if not star.constellation:
            return 'Unknown'

        constellation_admin_name = 'admin:catalog_constellation_change'
        constellation_url = reverse(
            constellation_admin_name,
            args=(star.constellation.id,),
        )
        constellation_name = str(star.constellation)
        return format_html('<a href="{}">{}</a>', constellation_url, constellation_name)

    get_constellation_link.admin_order_field = 'constellation'
    get_constellation_link.short_description = 'Constellation'
