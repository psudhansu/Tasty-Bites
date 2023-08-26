from django import forms
from .models import Dish, Order

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'price', 'availability']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'dishes']
