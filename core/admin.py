from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UploadedFile

# This line tells Django to show the User model on the admin page.
admin.site.register(User, UserAdmin)

# This line will register your UploadedFile model as well.
admin.site.register(UploadedFile)