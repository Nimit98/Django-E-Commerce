from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

Categories = (
    ("Sh", "Shirts"),
    ("Tr", 'Trousers'),
    ('Bl', 'Blazzer')
)


class Items(models.Model):
    product = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    category = models.CharField(choices=Categories, default='Bl', max_length=2)

    def __str__(self):
        return self.product


class ItemOrder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='item_ordered')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} has {self.quantity} of {self.item}"


class OrderPlaced(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
