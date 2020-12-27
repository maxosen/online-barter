from django.db import models

# Create your models here.
# TODO: add a foreign key to the person trading / uploading this item
class Item(models.Model):
    NEW = 'NW'
    USED = 'US'
    ITEM_CONDITION_CHOICES = [
        (NEW, 'New'),
        (USED, 'Used')
    ]
    title = models.CharField(max_length=120)
    condition = models.CharField(
        max_length=2,
        choices=ITEM_CONDITION_CHOICES,
        default=NEW
    )
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
