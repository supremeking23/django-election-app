from django.contrib import admin

from .models import Position,Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
	list_display = ['name','title','votes']

	#Don't filter on a ForeignKey field itself!	
	search_fields = ['name']

	list_filter = ['title']



admin.site.register(Position)
admin.site.register(Person,PersonAdmin)