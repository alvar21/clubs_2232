from django.contrib import admin
from clubs.models import Club

class UsersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Club)
