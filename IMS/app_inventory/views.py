from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Purchase
from .forms import PurchaseForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product:
        return render(request, 'app_inventory/product.html', {'product': product})      
    return redirect('home')


@login_required
def buy_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.product = product
            purchase.user = request.user
            purchase.total_amount = product.price * purchase.quantity
            purchase.save()
            return redirect('billing', purchase_id=purchase.id)
    else:
        form = PurchaseForm(initial={'product': product})

    context = {'product': product, 'form': form}
    return render(request, 'app_inventory/buy_product.html', context)

@login_required
def billing(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    return render(request, 'app_inventory/billing.html', {'purchase': purchase})

