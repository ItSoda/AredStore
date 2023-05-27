from django.db import models
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Paid for')
    address = models.CharField(max_length=128)
    created_time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.User | self.Status 