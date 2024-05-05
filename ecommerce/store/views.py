from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages 
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import CreateUserForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
# Create your views here.

#@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(
                     user=user,
                     name=user.username,
                     email=user.email,
                )
            

                messages.success(request,'Account was created for ' + username)
                return redirect('login')
        context = {'form':form}
        return render(request, 'store/signup.html', context)

#@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
        else:
             messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'store/signin.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    data = cartData(request)
    cartItems = data['cartItems']

    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form, 'cartItems': cartItems}
    return render(request, 'store/account_settings.html', context)

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    context = {'customer':customer}
    return render(request, 'home/account_settings.html', context)

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
       
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False) # new
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product) # new

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)
            
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def search_view(request):
    query = request.GET.get('q')
    results = []
    cartItems = 0

    if query:
        data = cartData(request)
        cartItems = data['cartItems']
        
        # Use Q objects to search in both title and description
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'results': results,
        'cartItems': cartItems
    }

    return render(request, 'store/search_results.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Retrieve cart data using your cartData function or method
    data = cartData(request)
    
    # Get the number of items in the cart
    cartItems = data['cartItems']
    
    context = {
        'product': product,
        'cartItems': cartItems,
    }
    
    return render(request, 'store/product_detail.html', context)

#def details(request):
    # You can pass any context variables to the template if needed
 #   context = {}
 #   return render(request, 'store/details.html', context)

'''def details(request):
    if request.method == 'POST':
        form = Details(request.POST)
       # if form.is_valid():
        form.save()  # Save the shipping address to the database
            #messages.success(request, "Shipping information submitted successfully!")
           # return redirect('some_redirect_url')  # Redirect the user to another page
        #else:
        #    messages.error(request, "There was an error with your submission. Please try again.")
    
    else:
        form = Details()

    # Render a template with the form, if necessary
    return render(request, 'store/details.html', {'form': form})

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'store/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'store/home.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'store/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)'''

#def signin_view(request):
 #   if request.method == 'POST':
  #      email = request.POST['email']
  #      password = request.POST['password']

  #      user = auth.authenticate(request, username=email, password=password)
  #      if user is not None:
  #          auth.login(request, user)
  #          messages.success(request, "Welcome back!")
   #         request.session['username'] = user.username
   #         return redirect('store')
   #     else:
   #         messages.error(request, "Invalid credentials")
   #         return redirect('signin')

   # return render(request, 'store/signin.html')


#def signup_view(request):
   # if request.method == 'POST':
   #     full_name = request.POST['full_name']
   #     email = request.POST['email']
    #    password1 = request.POST['password1']
    #    password2 = request.POST['password2']

    #    if password1 != password2:
    #        messages.error(request, "Passwords do not match.")
    #        return redirect('signup')  # Redirect back to the sign-up page

     #   # Check if a user with the given email already exists
     #   if User.objects.filter(email=email).exists():
     #       messages.error(request, "An account with this email already exists.")
     #       return redirect('signup')

        # Create the user account
      #  user = User.objects.create_user(username=email, email=email, password=password1)
       # user.full_name = full_name
       # user.save()

        # Create associated Customer instance
       # customer = Customer(user=user)
       # customer.save()
        
       # messages.success(request, "Account created successfully. You can now sign in.")
       # return redirect('signin')  # Redirect to the sign-in page
#
   # return render(request, 'store/signup.html')

#def logout_view(request):
 #   logout(request)
 #   if 'username' in request.session:
 #       del request.session['username']
  #  return redirect('store') 

#def search_view(request):
#    query = request.GET.get('q')
#    results = []
 #   cartItems = 0  # Initialize cartItems here
#
 #   if query:
  #      data = cartData(request)
  #      cartItems = data['cartItems']
  #      results = Product.objects.filter(name__icontains=query)
#
 #   context = {
  #      'results': results,
 #       'cartItems': cartItems  # Include cartItems in the context
 #   }

  #  return render(request, 'store/search_results.html', context)


