from django.shortcuts import render, redirect
from store.models import Order
from .forms import OrderEditForm, ProductForm

def home(request):
    orders = Order.objects.all()
    return render(request, 'admin.html', {'orders': orders})

def order(request, pk):
    order_data = Order.objects.get(pk=pk)
    return render(request, 'order.html', {'order': order_data})


def order_edit(request, pk):
    order_data = Order.objects.get(pk=pk)
    form = OrderEditForm(request.POST or None, instance=order_data)

    if not request.POST.get('address'):
        form.address=order_data.address

    if form.is_valid():
        form.save()
        return redirect('staff:order', pk=pk)
    return render(request, 'order_edit.html', {'form': form, 'order':order_data })

def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save
        return redirect('store:home')
    return render(request, 'product_create.html' , {'form':form})