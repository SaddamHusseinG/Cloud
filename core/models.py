# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model that extends Django's default AbstractUser.
    """
    ACCOUNT_TYPE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='user')
    storage_quota_gb = models.PositiveIntegerField(default=5, help_text="Storage quota in GB")

    def __str__(self):
        return self.username

class UploadedFile(models.Model):
    """
    Represents a file uploaded by a user.
    """
    # Links each file to a User. If a User is deleted, their files are also deleted.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    
    # The actual file stored in the location defined by MEDIA_ROOT or S3.
    file = models.FileField(upload_to='uploads/')
    
    # Automatically records the time when the file is uploaded.
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns just the filename from the path for display purposes.
        return self.file.name.split('/')[-1]

    @property
    def size(self):
        # Returns the file size in a human-readable format.
        try:
            return self.file.size
        except FileNotFoundError:
            return 0