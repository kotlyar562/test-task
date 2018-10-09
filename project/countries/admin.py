from django.contrib import admin
from . models import Country, City


class CityInline(admin.TabularInline):
    model = City
    extra = 1

class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('title', 'text')
    inlines = [CityInline, ]

admin.site.register(Country, CountryAdmin)
