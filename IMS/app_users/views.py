from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .forms import SignUpForm, ProfilePicForm
from django.contrib import messages
from app_inventory.models import Product, Purchase



# Create your views here.
def home(request):
    products = Product.objects.all().order_by("-id")
    context = {'products': products}
    return render(request, 'home.html', context)


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'app_users/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out.!"))
    return redirect('home')


def register_user(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
		else:
			form = SignUpForm()
			return render(request, 'app_users/register.html', {'form':form})

	return render(request, 'app_users/register.html', {'form':form})


def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		profile_user = Profile.objects.get(user__id=request.user.id)
		# Get Forms
		user_form = SignUpForm(request.POST or None, instance=current_user)
		profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

			login(request, current_user)
			messages.success(request, ("Your Profile Has Been Updated!"))
			return redirect('home')

		return render(request, "app_users/update_user.html", {'user_form':user_form, 'profile_form': profile_form})
	else:
		messages.success(request, ("You Must Be Logged In To View That Page..."))
		return redirect('home')


def user_profile(request, pk):
    purchase = Purchase.objects.all()
    return render(request, 'app_users/profile.html', {'purchase': purchase})