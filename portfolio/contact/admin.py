from django.contrib import admin
from .models import contact
# Register your models here.
class Contact_Admin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'message'
    ]


admin.site.register(contact, Contact_Admin)