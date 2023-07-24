from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)


class ProfileInLine(admin.StackedInline):
    model = Profile
    
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    inlines = [ProfileInLine]
    
        
admin.site.register(User, UserAdmin)