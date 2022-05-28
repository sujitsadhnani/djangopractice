from django.contrib import admin
from home import models
# Register your models here.

class adminuser(admin.ModelAdmin):
    list_display = ['email']

# class adminmed_post()

admin.site.register(models.user, adminuser)
admin.site.register(models.med_post)
admin.site.register(models.like)


