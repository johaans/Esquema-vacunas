from django.contrib import admin

from .models import userdate, vacuna,frequently
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = vacuna
    extra = 2


class userAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['names']}),
        (None,               {'fields': ['surname']}),
        (None,               {'fields': ['surname2']}),
        (None,               {'fields': ['Doc']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('BirthDate information',{'fields':['birthday'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('Doc','birthday')
    list_filter = ['Doc']
    search_fields = ('Doc',)

admin.site.register(userdate, userAdmin)
admin.site.register(frequently)
