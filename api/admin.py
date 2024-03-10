from django.contrib import admin
from .models import Race,Airline

admin.site.register(Airline)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ['flight','id','source_city','destination_city','day']

    class Meta:
        model = Race