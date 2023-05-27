from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from products.models import Basket
from .forms import OrderCreateForm
from users.forms import UserProfileForm
from users.models import User
from .models import Order
# Create your views here.
def orders(request):
    return render(request, 'orders/orders.html')


def success(request):
    return render(request, 'orders/success.html')

def create_order(request):
    if request.method == 'POST':
        form = OrderCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(HttpResponseRedirect(reverse('orders_:success')))
    else:
        form = OrderCreateForm
        form2 = UserProfileForm(instance=request.user)
    context = {
        'baskets' : Basket.objects.filter(user=request.user),
        'formOrder' : form,
        'formUser' : form2,
        }
    return render(request, 'orders/order-create.html', context)