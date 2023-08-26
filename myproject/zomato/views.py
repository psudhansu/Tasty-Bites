from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Order
from django.http import HttpResponse
from .forms import DishForm, OrderForm

# Create your views here.
# def welcome(request):
#     return HttpResponse("welcome welcome")

# views.py
# from django.shortcuts import render, redirect
# from .models import Dish

# def dish_list(request):
#     dishes = Dish.objects.all()
#     return render(request, 'dish_list.html', {'dishes': dishes})

# def add_dish(request):
#     if request.method == 'POST':
#         print(request.POST,request.POST.get('availability', False))
#         dish_name = request.POST['dish_name']
#         price = request.POST['price']
#         availability = True if request.POST.get('availability', False) == "on" else False
        
#         Dish.objects.create(dish_name=dish_name, price=price, availability=availability)
#         return redirect('dish_list')
#     return render(request, 'add_dish.html')

# def edit_dish(request, dish_id):
#     dish = Dish.objects.get(id=dish_id)
#     if request.method == 'POST':
#         dish.dish_name = request.POST['dish_name']
#         dish.price = request.POST['price']
#         dish.availability = True if request.POST.get('availability', False) == "on" else False
#         dish.save()
#         return redirect('dish_list')
#     return render(request, 'edit_dish.html', {'dish': dish})

# def delete_dish(request, dish_id):
#     dish = Dish.objects.get(id=dish_id)
#     dish.delete()
#     return redirect('dish_list')
def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'add_dish.html', {'form': form})

def edit_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'edit_dish.html', {'form': form, 'dish': dish})

def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'confirm_delete.html', {'dish': dish})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
    

# def take_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             customer_name = form.cleaned_data['customer_name']
#             selected_dishes = request.POST.getlist('dishes')
            
#             for dish_id in selected_dishes:
#                 dish = Dish.objects.get(pk=dish_id)
#                 order = Order.objects.create(customer_name=customer_name, dish=dish, status='received')
#                 order.save()
            
#             return redirect('order_list')
#     else:
#         form = OrderForm()
#     dishes = Dish.objects.all()
#     return render(request, 'take_order.html', {'dishes': dishes})
def take_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            selected_dishes = form.cleaned_data['dishes']
            
            unavailable_dishes = []
            for dish in selected_dishes:
                if not dish.availability:
                    unavailable_dishes.append(dish.dish_name)
            
            if unavailable_dishes:
                error_message = f"The following dishes are not available: {', '.join(unavailable_dishes)}"
                return HttpResponse(error_message)
                # form.add_error(None, error_message)
            else:
                order = form.save(commit=False)
                order.status = 'received'
                order.save()
                return redirect('order_list')
    else:
        form = OrderForm()
    dishes = Dish.objects.all()
    return render(request, 'take_order.html', {'form': form, 'dishes': dishes})


# def take_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.status = 'received'
#             order.save()
#             return redirect('order_list')
#     else:
#         form = OrderForm()
#     dishes = Dish.objects.all()
#     print(dishes)
#     return render(request, 'take_order.html', {'form': form, 'dishes': dishes})



def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        print(order.order_status)
        order.order_status = new_status
        print(order.order_status)
        order.save()
        return redirect('order_list')
    
    return render(request, 'update_order_status.html', {'order': order})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_delete.html', {'order': order})