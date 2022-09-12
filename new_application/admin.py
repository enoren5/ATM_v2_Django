from django.contrib import admin
from new_application.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # fields = ['year','brand']
    fieldsets = [
        ('TIME INFORMATION', {'pk':['id']}),
    ]
    
admin.site.register(User)