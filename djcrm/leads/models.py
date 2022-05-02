from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=(
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    ), max_length=100)

    profile_pic = models.ImageField(blank=True, null=True)
    special_files = model.models.FileField(blank=True, null=True)

    