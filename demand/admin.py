from django.contrib import admin
from .models import *

# Register your models here.


class DemandAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'requirement', 'client', 'number', 'status', 'time')
    list_filter = ('requirement', 'client', 'number', 'status', 'time')
    search_fields = ('code', 'requirement', 'client', 'status', 'time')
    fields = ('code', 'requirement', 'client', 'number', 'status', 'time')


admin.site.register(Demand, DemandAdmin)
