from django.db import models


class Vcard(models.Model):
        name_card = models.CharField(max_length=100)
        price_card = models.IntegerField(default=36)


class Creator (models.Model):
        creator_name = models.CharField(max_length=100)
        creator_card = models.CharField(max_length=100)
