
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import login


# import your new form
from .forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Category, Product, Order
from django.contrib import messages

def logout_view(request):
    """
    Logs out the current user and redirects to the product list page.
    """
    logout(request)
    return redirect('product_list')

def product_list(request):
    """
    Displays a list of all products, optionally filtered by category.
    Shows a dropdown to select category and lists products with images.
    """
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')
    if selected_category_id:
        products = Product.objects.filter(category_id=selected_category_id)
    else:
        products = Product.objects.all()
    return render(request, 'store/product_list.html', {
        'categories': categories,
        'products': products,
        'selected_category_id': selected_category_id
    })

def product_detail(request, pk):
    """
    Shows the details for a single product, including all images and description.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def register(request):
    """
    Handles user registration using Django's built-in User model.
    Collects first name, last name, email, and password.
    On success, saves the user and redirects to login page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save yet
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            
            login(request, user) # Automatically log in the user after registration
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('product_list')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def order_history(request):
    """
    Shows the logged-in user's order history, ordered by most recent.
    Only accessible to authenticated users.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})
