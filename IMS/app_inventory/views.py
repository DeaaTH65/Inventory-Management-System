from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ContactForm
from app_users.models import User


# Create your views here.
def show_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product:
        return render(request, 'app_inventory/product.html', {'product': product})      
    return redirect('home')


def buy_product(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=pk)
        current_user = User.objects.get(id=request.user.id)
        form = ContactForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            house_no = form.cleaned_data['house_no']
            buyer = save(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, house_no=house_no)
            return redirect('home')
            
        context = {'product': product, 'form': form}
        return render(request, 'app_inventory/purchase.html', context)
    
    return redirect('login')