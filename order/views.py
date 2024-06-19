from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from .models import Order, OrderProduct
from cart.models import CartProducts


@login_required
def create_order(request):
    user = request.user
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order.save()
            for item in user.cart_products.all():
                OrderProduct.objects.create(order=order, product=item.product,
                                            price=item.product.price, quantity=item.quantity)
            total_price = sum(product.get_total_price() for product in OrderProduct.objects.filter(order=order))
            order.total_price = total_price + int(order.delivery)
            order.save()
            CartProducts.objects.filter(user=user).delete()
            return redirect('index')
    else:
        form = OrderCreateForm()
        total_price = sum([item.get_total_price() for item in CartProducts.objects.filter(user=user)])
        context = {'form': form, 'total_price': total_price}
        return render(request, 'create_order.html', context)


@login_required
def order_active_list(request):
    orders = Order.objects.filter(user=request.user, completed=False)
    return render(request, 'order_list_active.html', {'orders': orders})


@login_required
def order_completed_list(request):
    orders = Order.objects.filter(user=request.user, completed=True)
    return render(request, 'order_list_completed.html', {'orders': orders})


@login_required
def cancel_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('orders_active')
