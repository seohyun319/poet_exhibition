from django.contrib import admin
from .models import Post, VisitForm
# Register your models here.
admin.site.register(Post)

class VisitAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'phone' ]
admin.site.register(VisitForm, VisitAdmin)