from django.contrib import admin
from .models import City, Race,Airline

admin.site.register(Airline)
admin.site.register(City)
# admin.site.register(Race)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ['flight','id','source_city','destination_city']

    class Meta:
        model = Race