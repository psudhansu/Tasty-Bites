from django.db import models

# Create your models here.
# models.py

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish, through='OrderDish')
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('received', 'Received'),
            ('preparing', 'Preparing'),
            ('ready', 'Ready for Pickup'),
            ('delivered', 'Delivered')
        ],
        default='received'
    )

    def __str__(self):
        return f"Order {self.id} for {self.customer_name}"

class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.dish.dish_name} in Order {self.order.id}"

