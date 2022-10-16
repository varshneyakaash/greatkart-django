from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    
    #When we want to display the fields in the front page
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')

    #Make these fields as clickable
    list_display_links=('email','first_name','last_name')

    #Make these fields as read only
    readonly_fields=('last_login','date_joined')

    #Ordering the fields (For descending use -)
    ordering=('-date_joined',)

    #Make passwords read only
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account, AccountAdmin)
