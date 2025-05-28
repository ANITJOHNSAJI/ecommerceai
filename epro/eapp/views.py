# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login,logout
# from django.core.mail import send_mail
# from django.conf import settings
# import random
# from django.urls import reverse
# from datetime import datetime, timedelta
# from .models import *
# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required
# from .vectorize import vectorize_product_with_reviews,vectorize_user_with_search,pd
# from django.shortcuts import render
# from .models import *
# from .read_content import *
# from django.http import JsonResponse
# from django.conf import settings
# import razorpay
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from sentence_transformers import SentenceTransformer
# from django.db.models import Case, When
# import numpy as np
# from django.db.models import Q
# import torch
# from .vectorize import vectorize_product_with_reviews


# from django.shortcuts import render
# from django.db.models import Q
# import pandas as pd
# import json
# from sentence_transformers import SentenceTransformer
# from .models import Product, users, SearchHistory, ViewHistory



# import json
# import logging
# import pickle
# import random
# from datetime import datetime, timedelta

# import numpy as np
# import pandas as pd
# import torch
# from django.conf import settings
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from django.db.models import Case, When, Q
# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
# from sentence_transformers import SentenceTransformer, util

# from .models import Product, users, SearchHistory, ViewHistory, Cart, Address, Order, OrderItem, reviews
# from .vectorize import vectorize_product_with_reviews, vectorize_user_with_search

# def getuser(request):
#     return request.session.get('user')





# # def types(request):
# #     type2 = []
# #     for i in Product.objects.all():
# #         if i.name and i.type not in type2:
# #             type2.append(i.type)
# #     return type2

# # def index(request):
# #     # Get latest products
# #     products = Product.objects.all().order_by('-id')[:4]

# #     # Collect product vectors for recommendations
# #     product_ids = []
# #     product_vectors = []
# #     for pro in products:  # Use products instead of undefined 'data'
# #         if pro.vector_data:  # Check if vector_data is not None or empty
# #             try:
# #                 vector = json.loads(pro.vector_data)
# #                 product_ids.append(pro.pk)
# #                 product_vectors.append(vector)
# #             except json.JSONDecodeError:
# #                 continue  # Skip invalid JSON

# #     # Convert product vectors to tensor
# #     product_vectors = torch.tensor(product_vectors) if product_vectors else torch.tensor([])

# #     # Initialize recommended products
# #     recommended_products = []

# #     # Generate recommendations for authenticated user
# #     if request.user.is_authenticated:
# #         try:
# #             user_obj = users.objects.get(user=request.user)
# #             if user_obj.vector_data:  # Check if user has vector_data
# #                 user_vector = torch.tensor(json.loads(user_obj.vector_data))
# #                 if product_vectors.numel() > 0:  # Ensure there are product vectors
# #                     recommended = recommend_product(user_vector, product_vectors, product_ids, top_n=4)
# #                     product_pks = [rec[0] for rec in recommended]
# #                     # Preserve order of recommended products
# #                     preserved_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(product_pks)])
# #                     recommended_products = Product.objects.filter(pk__in=product_pks).order_by(preserved_order)
# #         except users.DoesNotExist:
# #             pass  # No users object, skip recommendations
# #         except json.JSONDecodeError:
# #             pass  # Invalid user vector_data, skip recommendations

# #     # Fallback: If no recommendations, select random products
# #     if not recommended_products:
# #         recommended_products = Product.objects.order_by('?')[:4]

# #     # Get other product sets for display
# #     gallery_images = Product.objects.all().order_by('-id')[:4]  # Latest 4 products
# #     data2 = Product.objects.all()[:8]  # First 8 products
# #     data3 = Product.objects.all().order_by('-id')[:3]  # Latest 3 products

# #     # Cart item count
# #     cart_item_count = Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0

# #     return render(request, 'index.html', {
# #         'gallery_images': gallery_images,
# #         'recommended_products': recommended_products,  # Renamed for clarity
# #         'all_products': data2,  # Renamed for clarity
# #         'latest_products': data3,  # Renamed for clarity
# #         'user': request.user if request.user.is_authenticated else None,  # Replaced getuser
# #         'type': Product.TYPE_CHOICES,  # Replaced types with Product.TYPE_CHOICES
# #         'cart_item_count': cart_item_count
# #     })




# def types(request):
#     type2 = []
#     for i in Product.objects.all():
#         if i.name and i.type not in type2:
#             type2.append(i.type)
#     return type2

# def index(request):
#     # Get latest products
#     products = Product.objects.all().order_by('-id')[:4]

#     # Collect product vectors for recommendations
#     product_ids = []
#     product_vectors = []
#     for pro in products:
#         if pro.vector_data:
#             try:
#                 vector = json.loads(pro.vector_data)
#                 product_ids.append(pro.pk)
#                 product_vectors.append(vector)
#             except json.JSONDecodeError:
#                 continue

#     # Convert product vectors to tensor
#     product_vectors = torch.tensor(product_vectors) if product_vectors else torch.tensor([])

#     # Initialize recommended products
#     recommended_products = []

#     # Generate recommendations for authenticated user
#     if request.user.is_authenticated:
#         try:
#             user_obj = users.objects.get(user=request.user)
#             if user_obj.vector_data:
#                 user_vector = torch.tensor(json.loads(user_obj.vector_data))
#                 if product_vectors.numel() > 0:
#                     recommended = recommend_product(user_vector, product_vectors, product_ids, top_n=4)
#                     product_pks = [rec[0] for rec in recommended]
#                     preserved_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(product_pks)])
#                     recommended_products = Product.objects.filter(pk__in=product_pks).order_by(preserved_order)
#         except users.DoesNotExist:
#             pass
#         except json.JSONDecodeError:
#             pass

#     # Fallback: If no recommendations, select random products
#     if not recommended_products:
#         recommended_products = Product.objects.order_by('?')[:4]

#     # Get other product sets for display
#     gallery_images = Product.objects.all().order_by('-id')[:4]
#     data2 = Product.objects.all()[:8]
#     data3 = Product.objects.all().order_by('-id')[:3]

#     # Cart item count
#     cart_item_count = Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0

#     return render(request, 'index.html', {
#         'gallery_images': gallery_images,
#         'recommended_products': recommended_products,
#         'all_products': data2,
#         'latest_products': data3,
#         'user': request.user if request.user.is_authenticated else None,
#         'type': Product.TYPE_CHOICES,
#         'cart_item_count': cart_item_count
#     })






# model = SentenceTransformer('all-MiniLM-L6-v2')
# def product(request, id):
#     # Get the product or return 404
#     product = get_object_or_404(Product, pk=id)

#     # Initialize variables
#     cart_item_ids = []
#     gallery_images = []

#     if request.user.is_authenticated:
#         # Get or create user profile
#         user_name, created = users.objects.get_or_create(user=request.user)

#         # Track view history
#         ViewHistory.objects.create(user=user_name, product=product)

#         # Prepare view history data for vectorization
#         existing_user_data = ViewHistory.objects.filter(user=user_name)
#         existing_products = [history.product.name for history in existing_user_data]
#         data = [{
#             'user_id': user_name.id,
#             'product': ','.join(existing_products) if existing_products else '',
#             'search': ''  # Empty search since this is view-based
#         }]
#         df = pd.DataFrame(data)

#         # Vectorize and save
#         try:
#             user_vectors = vectorize_user_with_search(df)
#             user_name.vector_data = json.dumps(user_vectors[0].tolist())
#             user_name.save()
#         except Exception as e:
#             logger.error(f"Vectorization failed for user {user_name.id}: {e}")

#         # Get cart items for the user
#         cart_items = Cart.objects.filter(user=request.user, product=product)
#         cart_item_ids = [item.product.id for item in cart_items]
#     else:
#         user_name = None

#     # Fetch reviews
#     rs = reviews.objects.filter(pname=product)

#     # Check if user has reviewed
#     isReviewed = reviews.objects.filter(uname__user=request.user, pname=product).exists() if request.user.is_authenticated else False

#     # Prepare gallery images (all non-null images)
#     gallery_images = [
#         product.image.url if product.image else None,
#         product.image1.url if product.image1 else None,
#         product.image2.url if product.image2 else None,
#         product.image3.url if product.image3 else None,
#         product.image4.url if product.image4 else None,
#         product.image5.url if product.image5 else None
#     ]
#     gallery_images = [img for img in gallery_images if img]  # Remove None values

#     context = {
#         'product': product,
#         'gallery_images': gallery_images,
#         'cart_product_ids': cart_item_ids,
#         'isReviewed': isReviewed,
#         'reviews': rs,
#         'user': request.user if request.user.is_authenticated else None
#     }
#     return render(request, 'product.html', context)


# @login_required
# def profile_view(request):
#     addresses = Address.objects.filter(user=request.user)
#     orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
#     return render(request, 'profile.html', {
#         'email': request.user.email,
#         'addresses': addresses,
#         'orders': orders
#     })

# @login_required
# def add_address(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         address = request.POST.get('address', '')
#         phone = request.POST.get('phone', '')
#         errors = {}
#         if not name:
#             errors['name'] = 'Name is required.'
#         if not address:
#             errors['address'] = 'Address is required.'
#         if not phone:
#             errors['phone'] = 'Phone number is required.'
#         if not errors:
#             Address.objects.create(
#                 user=request.user,
#                 name=name,
#                 address=address,
#                 phone=phone
#             )
#             messages.success(request, 'Address added successfully!')
#             return redirect('profile')
#         else:
#             return render(request, 'address.html', {
#                 'errors': errors,
#                 'name': name,
#                 'address': address,
#                 'phone': phone,
#                 'action': 'Add'
#             })
#     return render(request, 'address.html', {'action': 'Add'})

# @login_required
# def edit_address(request, address_id):
#     address_obj = get_object_or_404(Address, id=address_id, user=request.user)
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         address = request.POST.get('address', '')
#         phone = request.POST.get('phone', '')
#         errors = {}
#         if not name:
#             errors['name'] = 'Name is required.'
#         if not address:
#             errors['address'] = 'Address is required.'
#         if not phone:
#             errors['phone'] = 'Phone number is required.'
#         if not errors:
#             address_obj.name = name
#             address_obj.address = address
#             address_obj.phone = phone
#             address_obj.save()
#             messages.success(request, 'Address updated successfully!')
#             return redirect('profile')
#         else:
#             return render(request, 'address.html', {
#                 'errors': errors,
#                 'name': name,
#                 'address': address,
#                 'phone': phone,
#                 'action': 'Edit'
#             })
#     return render(request, 'address.html', {
#         'name': address_obj.name,
#         'address': address_obj.address,
#         'phone': address_obj.phone,
#         'action': 'Edit'
#     })

# @login_required
# def delete_address(request, address_id):
#     address = get_object_or_404(Address, id=address_id, user=request.user)
#     if request.method == 'POST':
#         address.delete()
#         messages.success(request, 'Address deleted successfully!')
#         return redirect('profile')
#     return render(request, 'confirm_delete.html', {'address': address})

# @login_required
# def edit_email(request):
#     user = request.user
#     if request.method == 'POST':
#         email = request.POST.get('email', '')
#         errors = {}
#         if not email:
#             errors['email'] = 'Email is required.'
#         elif '@' not in email:
#             errors['email'] = 'Please enter a valid email address.'
#         if not errors:
#             user.email = email
#             user.save()
#             messages.success(request, 'Email updated successfully!')
#             return redirect('profile')
#         else:
#             return render(request, 'email.html', {
#                 'errors': errors,
#                 'email': email
#             })
#     return render(request, 'email.html', {
#         'email': user.email
#     })

# @login_required
# def edit_username(request):
#     user = request.user
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         errors = {}
#         if not username:
#             errors['username'] = 'Username is required.'
#         elif len(username) < 4:
#             errors['username'] = 'Username should be at least 4 characters long.'
#         elif User.objects.filter(username=username).exists():
#             errors['username'] = 'This username is already taken.'
#         if not errors:
#             user.username = username
#             user.save()
#             messages.success(request, 'Username updated successfully!')
#             return redirect('profile')
#         else:
#             return render(request, 'username.html', {
#                 'errors': errors,
#                 'username': username
#             })
#     return render(request, 'username.html', {
#         'username': user.username
#     })

# def product_list(request):
#     products = Product.objects.all()
#     gender = request.GET.get('gender')
#     if gender:
#         products = products.filter(gender=gender)
#     product_type = request.GET.get('display_type')
#     if product_type:
#         products = products.filter(type=product_type)
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')
#     if min_price:
#         try:
#             min_price = float(min_price)
#             products = products.filter(price__gte=min_price)
#         except ValueError:
#             pass
#     if max_price:
#         try:
#             max_price = float(max_price)
#             products = products.filter(price__lte=max_price)
#         except ValueError:
#             pass
#     return render(request, 'allproduct.html', {'products': products})

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def search_func(request):
#     if request.method == 'GET':
#         inp = request.GET.get('q', '').strip()  # Get search query, default to empty string
#         if not inp:
#             return render(request, 'search.html', {
#                 'error': 'Please enter a search query.',
#                 'type': Product.TYPE_CHOICES,  # Use Product.TYPE_CHOICES for types
#                 'user': request.user if request.user.is_authenticated else None
#             })

#         # Handle user search history and vectorization
#         if request.user.is_authenticated:
#             try:
#                 user = users.objects.get(user=request.user)  # Changed Users to users
#                 # Save search query to SearchHistory
#                 SearchHistory.objects.create(query=inp, user=user)

#                 # Get user search and view history
#                 user_search = [s.query for s in SearchHistory.objects.filter(user=user)]
#                 user_products = [s.product.name for s in ViewHistory.objects.filter(user=user)]
                
#                 # Prepare data for vectorization
#                 user_data = [{
#                     'user_id': user.id,
#                     'product': ','.join(user_products) if user_products else '',
#                     'search': ','.join(user_search) if user_search else ''
#                 }]
                
#                 # Generate and save user vector
#                 df = pd.DataFrame(user_data)
#                 user_vectors = vectorize_user_with_search(df)
#                 user.vector_data = json.dumps(user_vectors[0].tolist())
#                 user.save()
#             except users.DoesNotExist:  # Changed Users to users
#                 pass  # Handle case where users object doesn't exist for the user

#         # Search products by name or type (case-insensitive)
#         products = Product.objects.filter(
#             Q(name__icontains=inp) | Q(type__icontains=inp)
#         ).distinct()

#         # Get unique categories
#         categories = list(products.values_list('type', flat=True).distinct())

#         # Pass results to template
#         context = {
#             'products': products,
#             'categories': categories,
#             'query': inp,
#             'type': Product.TYPE_CHOICES,  # Use Product.TYPE_CHOICES for types
#             'user': request.user if request.user.is_authenticated else None
#         }
#         return render(request, 'search.html', context)

#     return render(request, 'search.html', {
#         'type': Product.TYPE_CHOICES,  # Use Product.TYPE_CHOICES for types
#         'user': request.user if request.user.is_authenticated else None
#     })

# def usersignup(request):
#     if request.method == 'POST':  # Use request.method for clarity
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         confirmpassword = request.POST.get('confpassword')

#         # Validation checks
#         if not all([username, email, password, confirmpassword]):
#             messages.error(request, 'All fields are required.')
#         elif confirmpassword != password:
#             messages.error(request, "Passwords do not match.")
#         elif User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#         else:
#             try:
#                 # Create and save the Django User
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()

#                 # Create meaningful initial data for the user vector
#                 user_datas = [{
#                     "user_id": user.id,
#                     "product": "new_user",  # Placeholder; replace with meaningful data if possible
#                     "search": "initial_signup"  # Placeholder; replace with meaningful data if possible
#                 }]
#                 df = pd.DataFrame(user_datas)

#                 # Generate the vector using the vectorize_user_with_search function
#                 user_vectors = vectorize_user_with_search(df)

#                 # Check if vectors were successfully created
#                 if user_vectors and len(user_vectors) > 0:
#                     # Create a users model instance
#                     user_profile = users.objects.create(
#                         user=user,
#                         vector_data=json.dumps(user_vectors[0].tolist())
#                     )
#                     user_profile.save()
#                     print(f"Vector created and saved successfully for user: {username}")
#                 else:
#                     print(f"Failed to create vector for user: {username}")

#                 messages.success(request, "Account created successfully!")
#                 return redirect('userlogin')

#             except Exception as e:
#                 # Log the error but allow user creation
#                 print(f"Error creating vector for user {username}: {str(e)}")
#                 # Still create a users model instance without vector data
#                 user_profile = users.objects.create(user=user, vector_data=None)
#                 user_profile.save()
#                 messages.success(request, "Account created successfully, but personalization data could not be initialized.")
#                 return redirect('userlogin')

#     return render(request, "register.html")

# def userlogin(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('firstpage')
#             return redirect('index')
#         else:
#             messages.error(request, "Invalid credentials.")
#     return render(request, 'userlogin.html')

# def logoutuser(request):
#     logout(request)
#     request.session.flush()
#     return redirect('userlogin')

# def verifyotp(request):
#     if request.method == "POST":
#         otp = request.POST.get('otp')
#         otp1 = request.session.get('otp')
#         otp_time_str = request.session.get('otp_time')
#         if otp_time_str:
#             otp_time = datetime.fromisoformat(otp_time_str)
#             otp_expiry_time = otp_time + timedelta(minutes=5)
#             if datetime.now() > otp_expiry_time:
#                 messages.error(request, 'OTP has expired. Please request a new one.')
#                 del request.session['otp']
#                 del request.session['otp_time']
#                 return redirect('verifyotp')
#         if otp == otp1:
#             del request.session['otp']
#             del request.session['otp_time']
#             return redirect('passwordreset')
#         else:
#             messages.error(request, 'Invalid OTP. Please try again.')
#     otp = ''.join(random.choices('123456789', k=6))
#     request.session['otp'] = otp
#     request.session['otp_time'] = datetime.now().isoformat()
#     message = f'Your email verification code is: {otp}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [request.session.get('email')]
#     send_mail('Email Verification', message, email_from, recipient_list)
#     return render(request, "otp.html")

# def getusername(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         try:
#             user = User.objects.get(username=username)
#             request.session['email'] = user.email
#             return redirect('verifyotp')
#         except User.DoesNotExist:
#             messages.error(request, "Username does not exist.")
#             return redirect('getusername')
#     return render(request, 'getusername.html')

# def passwordreset(request):
#     if request.method == 'POST':
#         password = request.POST.get('password')
#         confirmpassword = request.POST.get('confpassword')
#         if confirmpassword != password:
#             messages.error(request, "Passwords do not match.")
#         else:
#             email = request.session.get('email')
#             try:
#                 user = User.objects.get(email=email)
#                 user.set_password(password)
#                 user.save()
#                 del request.session['email']
#                 messages.success(request, "Your password has been reset successfully.")
#                 user = authenticate(username=user.username, password=password)
#                 if user is not None:
#                     login(request, user)
#                 return redirect('userlogin')
#             except User.DoesNotExist:
#                 messages.error(request, "No user found with that email address.")
#                 return redirect('getusername')
#     return render(request, "passwordreset.html")

# # def admin_bookings(request):
# #     if request.method == 'POST':
# #         order_id = request.POST.get('order_id')
# #         order = get_object_or_404(Order, id=order_id)
# #         order.status = 'Confirmed'
# #         order.save()
# #         return redirect('admin_bookings')
# #     orders = Order.objects.all().order_by('-date_ordered')
# #     return render(request, 'admin_bookings.html', {'orders': orders})




# def admin_bookings(request):
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id')
#         action = request.POST.get('action')
#         order = get_object_or_404(Order, id=order_id)
        
#         if action == 'confirm' and order.status == 'Pending':
#             order.status = 'Confirmed'
#             order.save()
            
#             # Send email to user
#             subject = 'Your WATCHCART Order Confirmation'
#             message = f"""
# Dear {order.name},

# Your order (ID: {order.id}) has been confirmed! Below are the details:

# **Shipping Address:** {order.shipping_address}
# **Payment Method:** {order.payment_method}
# **Total Price:** ₹{order.total_price}

# **Order Items:**
# """
#             for item in order.items.all():
#                 message += f"- {item.product.name} (Brand: {item.product.brand}, Colour: {item.product.colour}, Quantity: {item.quantity}, Price: ₹{item.product.offerprice})\n"
            
#             message += "\nThank you for shopping with WATCHCART!"
            
#             try:
#                 send_mail(
#                     subject,
#                     message,
#                     settings.DEFAULT_FROM_EMAIL,
#                     [order.user.email],
#                     fail_silently=False,
#                 )
#             except Exception as e:
#                 # Log the error if needed, but don't interrupt the flow
#                 print(f"Failed to send email: {e}")
                
#         return redirect('admin_bookings')
    
#     orders = Order.objects.all().order_by('-date_ordered')
#     return render(request, 'admin_bookings.html', {'orders': orders})



# def delete_g(request, id):
#     product = get_object_or_404(Product, pk=id)
#     product.delete()
#     return redirect('firstpage')

# def edit_g(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         colour = request.POST.get('colour')
#         price = request.POST.get('price')
#         offerprice = request.POST.get('offerprice')
#         description = request.POST.get('description')
#         gender = request.POST.get('gender')
#         type = request.POST.get('type')
#         brand = request.POST.get('brand')
#         quantity = request.POST.get('quantity')
#         image = request.FILES.get('image')
#         image1 = request.FILES.get('image1')
#         image2 = request.FILES.get('image2')
#         image3 = request.FILES.get('image3')
#         image4 = request.FILES.get('image4')
#         image5 = request.FILES.get('image5')
#         if gender not in dict(Product.GENDER_CHOICES):
#             messages.error(request, 'Invalid gender choice.')
#             return redirect('edit_g', id=id)
#         if type not in dict(Product.TYPE_CHOICES):
#             messages.error(request, 'Invalid type choice.')
#             return redirect('edit_g', id=id)
#         product.name = name
#         product.colour = colour
#         product.price = price
#         product.offerprice = offerprice
#         product.description = description
#         product.gender = gender
#         product.type = type
#         product.brand = brand
#         product.quantity = quantity
#         if image:
#             product.image = image
#         if image1:
#             product.image1 = image1
#         if image2:
#             product.image2 = image2
#         if image3:
#             product.image3 = image3
#         if image4:
#             product.image4 = image4
#         if image5:
#             product.image5 = image5
#         product.save()
#         messages.success(request, "Product updated successfully!")
#         return redirect('firstpage')
#     return render(request, 'add.html', {
#         'data1': product,
#     })

# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         colour = request.POST.get('colour')
#         price = request.POST.get('price')
#         offerprice = request.POST.get('offerprice')
#         description = request.POST.get('description')
#         gender = request.POST.get('gender')
#         type = request.POST.get('type')
#         brand = request.POST.get('brand')
#         quantity = request.POST.get('quantity')
#         image = request.FILES.get('image')
#         image1 = request.FILES.get('image1')
#         image2 = request.FILES.get('image2')
#         image3 = request.FILES.get('image3')
#         image4 = request.FILES.get('image4')
#         image5 = request.FILES.get('image5')

#         # Validate gender and type choices
#         if gender not in dict(Product.GENDER_CHOICES):
#             messages.error(request, 'Invalid gender choice.')
#             return redirect('add_product')
#         if type not in dict(Product.TYPE_CHOICES):
#             messages.error(request, 'Invalid type choice.')
#             return redirect('add_product')

#         # Create and save the Product object
#         product = Product.objects.create(
#             name=name, 
#             colour=colour, 
#             price=price, 
#             offerprice=offerprice,
#             description=description, 
#             gender=gender, 
#             type=type, 
#             brand=brand, 
#             quantity=quantity,
#             image=image, 
#             image1=image1, 
#             image2=image2, 
#             image3=image3, 
#             image4=image4, 
#             image5=image5
#         )

#         # Prepare data for vectorization
#         pro_data = [{
#             "pro_id": product.id,
#             "name": name,
#             "rating": 0,
#             "description": description,  # Fixed typo
#             "reviews": '',
#             "type": type  # Use the type field instead of undefined model
#         }]
        
#         # Convert to DataFrame and generate vector
#         df = pd.DataFrame(pro_data)
#         product_vector = vectorize_product_with_reviews(df)
        
#         # Save vector data to the product
#         product.vector_data = json.dumps(product_vector[0].tolist())
#         product.save()
        
#         return redirect('firstpage')
    
#     return render(request, 'add.html')

# @login_required(login_url='userlogin')
# def add_to_cart(request, id):
#     product = get_object_or_404(Product, id=id)
#     cart_item, created = Cart.objects.get_or_create(user=request.user, product=product, defaults={'quantity': 1})
#     if not created and cart_item.quantity < product.quantity:
#         cart_item.quantity += 1
#         cart_item.save()
#         messages.success(request, f"Quantity of {product.name} updated in your cart.")
#     elif created:
#         messages.success(request, f"{product.name} has been added to your cart.")
#     else:
#         messages.error(request, "Sorry, this product is out of stock.")
#     return redirect('cart_view')

# @login_required(login_url='userlogin')
# def increment_cart(request, id):
#     cart_item = get_object_or_404(Cart, id=id, user=request.user)
#     if cart_item.quantity < cart_item.product.quantity:
#         cart_item.quantity += 1
#         cart_item.save()
#         messages.success(request, "Quantity updated.")
#     else:
#         messages.error(request, "No more stock available.")
#     return redirect('cart_view')

# @login_required(login_url='userlogin')
# def decrement_cart(request, id):
#     cart_item = get_object_or_404(Cart, id=id, user=request.user)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#         messages.success(request, "Quantity updated.")
#     else:
#         cart_item.delete()
#         messages.success(request, "Item removed from cart.")
#     return redirect('cart_view')

# @login_required(login_url='userlogin')
# def delete_cart_item(request, id):
#     cart_item = get_object_or_404(Cart, id=id, user=request.user)
#     cart_item.delete()
#     messages.success(request, "Item removed from cart.")
#     return redirect('cart_view')

# @login_required(login_url='userlogin')
# def cart_view(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     total_price = sum(item.get_total_price() for item in cart_items)
#     return render(request, 'cart.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     })

# @login_required(login_url='userlogin')
# def checkout_cart(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     total_price = sum(item.get_total_price() for item in cart_items)
#     default_address = Address.objects.filter(user=request.user, is_default=True).first()
#     return render(request, 'checkout.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#         'default_address': default_address
#     })

# @login_required(login_url='userlogin')
# def checkout_single(request, id):
    
#     product = get_object_or_404(Product, id=id)
#     print('Processing checkout...')
#     cart_items = [{
#         'product': product,
#         'quantity': 1,
#         'get_total_price': lambda: product.offerprice
#     }]
#     total_price = product.offerprice
#     default_address = Address.objects.filter(user=request.user, is_default=True).first()
#     return render(request, 'checkout.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#         'is_single': True,
#         'product_id': product.id,
#         'default_address': default_address
#     })

# @login_required(login_url='userlogin')
# def process_checkout(request):
   
#     if request.method == 'POST':
#         address_choice = request.POST.get('address_choice')
#         payment_method = request.POST.get('payment_method')
#         is_single = request.POST.get('is_single') == 'True'
#         product_id = request.POST.get('product_id')
#         if address_choice == 'default':
#             user_address = Address.objects.filter(user=request.user).first()
#             if not user_address:
#                 messages.error(request, "No default address found.")
#                 return redirect('checkout_cart')
#             shipping_address = user_address.address
#             name = user_address.name
#             phone = user_address.phone
#         else:
#             shipping_address = request.POST.get('address')
#             name = request.POST.get('name')
#             phone = request.POST.get('phone')
#         if is_single and product_id:
#             product = get_object_or_404(Product, id=product_id)
#             total_price = product.offerprice
#             order = Order.objects.create(
#                 user=request.user,
#                 name=name,
#                 phone=phone,
#                 shipping_address=shipping_address,
#                 payment_method=payment_method,
#                 total_price=total_price
#             )
#             OrderItem.objects.create(order=order, product=product, quantity=1)
#         else:
#             cart_items = Cart.objects.filter(user=request.user)
#             total_price = sum(item.get_total_price() for item in cart_items)
#             order = Order.objects.create(
#                 user=request.user,
#                 name=name,
#                 phone=phone,
#                 shipping_address=shipping_address,
#                 payment_method=payment_method,
#                 total_price=total_price
#             )
#             for item in cart_items:
#                 OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
#             cart_items.delete()
#         if payment_method == 'cod':
#             order.is_paid = False
#             order.save()
#             return redirect('order_confirmation', order_id=order.id)
#         else:
#             return redirect('start_razorpay_payment', order_id=order.id)
#     return redirect('cart_view')

# @login_required(login_url='userlogin')
# def start_razorpay_payment(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     if order.payment_method != 'online':
#         messages.error(request, "Invalid payment method.")
#         return redirect('cart_view')
#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#     amount = int(order.total_price * 100)  # Convert to paise
#     data = {
#         'amount': amount,
#         'currency': 'INR',
#         'receipt': f'order_{order.id}',
#         'payment_capture': 1  # Auto capture
#     }
#     try:
#         razorpay_order = client.order.create(data=data)
#         order.razorpay_payment_id = razorpay_order['id']
#         order.save()
#         return render(request, 'payment.html', {
#             'order': order,
#             'razorpay_order_id': razorpay_order['id'],
#             'razorpay_key_id': settings.RAZORPAY_KEY_ID,
#             'amount': amount,
#             'currency': 'INR',
#             'name': order.name,
#             'email': request.user.email,
#             'contact': order.phone,
#             'callback_url': request.build_absolute_uri(reverse('razorpay_callback')),
#         })
#     except Exception as e:
#         messages.error(request, f"Error initiating payment: {str(e)}")
#         return redirect('cart_view')

# @csrf_exempt
# def razorpay_callback(request):
#     if request.method == 'POST':
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         payment_data = request.POST
#         try:
#             client.utility.verify_payment_signature({
#                 'razorpay_order_id': payment_data.get('razorpay_order_id'),
#                 'razorpay_payment_id': payment_data.get('razorpay_payment_id'),
#                 'razorpay_signature': payment_data.get('razorpay_signature')
#             })
#             order = get_object_or_404(Order, razorpay_payment_id=payment_data.get('razorpay_order_id'))
#             order.is_paid = True
#             order.status = 'Confirmed'
#             order.razorpay_payment_id = payment_data.get('razorpay_payment_id')
#             order.save()
#             messages.success(request, "Payment successful!")
#             return redirect('order_confirmation', order_id=order.id)
#         except Exception as e:
#             messages.error(request, f"Payment verification failed: {str(e)}")
#             return redirect('cart_view')
#     return redirect('cart_view')

# @login_required(login_url='userlogin')
# def order_confirmation(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     return render(request, 'order_confirmation.html', {'order': order})

# def order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     return render(request, 'order_detail.html', {'order': order})

# def first_page(request):
#     products = Product.objects.all()
#     return render(request, 'firstpage.html', {'products': products})


import json
import logging
import pickle
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import torch
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Case, When, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from sentence_transformers import SentenceTransformer, util
import razorpay

from .models import Product, users, SearchHistory, ViewHistory, Cart, Address, Order, OrderItem, reviews
from .vectorize import vectorize_product_with_reviews, vectorize_user_with_search

logger = logging.getLogger(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Unchanged views (for context)
def recommend_product(user_input, product_vectors, product_ids, top_n=3):
    """Recommend products based on user input."""
    user_vector = user_input
    product_vectors = product_vectors.float()
    similarities = util.cos_sim(user_vector, product_vectors)
    similarity_scores = similarities[0].cpu().numpy()
    sorted_indices = np.argsort(similarity_scores)[::-1]
    recommended_products = [(product_ids[idx], similarity_scores[idx]) for idx in sorted_indices[:top_n]]
    return recommended_products

def types(request):
    type2 = []
    for i in Product.objects.all():
        if i.name and i.type not in type2:
            type2.append(i.type)
    return type2

def index(request):
    products = Product.objects.all().order_by('-id')[:4]
    product_ids = []
    product_vectors = []
    for pro in products:
        if pro.vector_data:
            try:
                vector = json.loads(pro.vector_data)
                product_ids.append(pro.pk)
                product_vectors.append(vector)
            except json.JSONDecodeError:
                continue
    product_vectors = torch.tensor(product_vectors) if product_vectors else torch.tensor([])
    recommended_products = []
    if request.user.is_authenticated:
        try:
            user_obj = users.objects.get(user=request.user)
            if user_obj.vector_data:
                user_vector = torch.tensor(json.loads(user_obj.vector_data))
                if product_vectors.numel() > 0:
                    recommended = recommend_product(user_vector, product_vectors, product_ids, top_n=4)
                    product_pks = [rec[0] for rec in recommended]
                    preserved_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(product_pks)])
                    recommended_products = Product.objects.filter(pk__in=product_pks).order_by(preserved_order)
        except users.DoesNotExist:
            pass
        except json.JSONDecodeError:
            pass
    if not recommended_products:
        recommended_products = Product.objects.order_by('?')[:4]
    gallery_images = Product.objects.all().order_by('-id')[:4]
    data2 = Product.objects.all()[:8]
    data3 = Product.objects.all().order_by('-id')[:3]
    cart_item_count = Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'index.html', {
        'gallery_images': gallery_images,
        'recommended_products': recommended_products,
        'all_products': data2,
        'latest_products': data3,
        'user': request.user if request.user.is_authenticated else None,
        'type': Product.TYPE_CHOICES,
        'cart_item_count': cart_item_count
    })

def product(request, id):
    product = get_object_or_404(Product, pk=id)
    cart_item_ids = []
    gallery_images = []
    if request.user.is_authenticated:
        user_name, created = users.objects.get_or_create(user=request.user)
        ViewHistory.objects.create(user=user_name, product=product)
        existing_user_data = ViewHistory.objects.filter(user=user_name)
        existing_products = [history.product.name for history in existing_user_data]
        data = [{
            'user_id': user_name.id,
            'product': ','.join(existing_products) if existing_products else '',
            'search': ''
        }]
        df = pd.DataFrame(data)
        try:
            user_vectors = vectorize_user_with_search(df)
            user_name.vector_data = json.dumps(user_vectors[0].tolist())
            user_name.save()
        except Exception as e:
            logger.error(f"Vectorization failed for user {user_name.id}: {e}")
        cart_items = Cart.objects.filter(user=request.user, product=product)
        cart_item_ids = [item.product.id for item in cart_items]
    else:
        user_name = None
    rs = reviews.objects.filter(pname=product)
    isReviewed = reviews.objects.filter(uname__user=request.user, pname=product).exists() if request.user.is_authenticated else False
    gallery_images = [
        product.image.url if product.image else None,
        product.image1.url if product.image1 else None,
        product.image2.url if product.image2 else None,
        product.image3.url if product.image3 else None,
        product.image4.url if product.image4 else None,
        product.image5.url if product.image5 else None
    ]
    gallery_images = [img for img in gallery_images if img]
    context = {
        'product': product,
        'gallery_images': gallery_images,
        'cart_product_ids': cart_item_ids,
        'isReviewed': isReviewed,
        'reviews': rs,
        'user': request.user if request.user.is_authenticated else None
    }
    return render(request, 'product.html', context)

@login_required
def profile_view(request):
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    return render(request, 'profile.html', {
        'email': request.user.email,
        'addresses': addresses,
        'orders': orders
    })

@login_required
def add_address(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        errors = {}
        if not name:
            errors['name'] = 'Name is required.'
        if not address:
            errors['address'] = 'Address is required.'
        if not phone:
            errors['phone'] = 'Phone number is required.'
        if not errors:
            Address.objects.create(
                user=request.user,
                name=name,
                address=address,
                phone=phone
            )
            messages.success(request, 'Address added successfully!')
            return redirect('profile')
        else:
            return render(request, 'address.html', {
                'errors': errors,
                'name': name,
                'address': address,
                'phone': phone,
                'action': 'Add'
            })
    return render(request, 'address.html', {'action': 'Add'})

@login_required
def edit_address(request, address_id):
    address_obj = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        errors = {}
        if not name:
            errors['name'] = 'Name is required.'
        if not address:
            errors['address'] = 'Address is required.'
        if not phone:
            errors['phone'] = 'Phone number is required.'
        if not errors:
            address_obj.name = name
            address_obj.address = address
            address_obj.phone = phone
            address_obj.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('profile')
        else:
            return render(request, 'address.html', {
                'errors': errors,
                'name': name,
                'address': address,
                'phone': phone,
                'action': 'Edit'
            })
    return render(request, 'address.html', {
        'name': address_obj.name,
        'address': address_obj.address,
        'phone': address_obj.phone,
        'action': 'Edit'
    })

@login_required
def delete_address(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        address.delete()
        messages.success(request, 'Address deleted successfully!')
        return redirect('profile')
    return render(request, 'confirm_delete.html', {'address': address})

@login_required
def edit_email(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST.get('email', '')
        errors = {}
        if not email:
            errors['email'] = 'Email is required.'
        elif '@' not in email:
            errors['email'] = 'Please enter a valid email address.'
        if not errors:
            user.email = email
            user.save()
            messages.success(request, 'Email updated successfully!')
            return redirect('profile')
        else:
            return render(request, 'email.html', {
                'errors': errors,
                'email': email
            })
    return render(request, 'email.html', {
        'email': user.email
    })

@login_required
def edit_username(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username', '')
        errors = {}
        if not username:
            errors['username'] = 'Username is required.'
        elif len(username) < 4:
            errors['username'] = 'Username should be at least 4 characters long.'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'This username is already taken.'
        if not errors:
            user.username = username
            user.save()
            messages.success(request, 'Username updated successfully!')
            return redirect('profile')
        else:
            return render(request, 'username.html', {
                'errors': errors,
                'username': username
            })
    return render(request, 'username.html', {
        'username': user.username
    })

def product_list(request):
    products = Product.objects.all()
    gender = request.GET.get('gender')
    if gender:
        products = products.filter(gender=gender)
    product_type = request.GET.get('display_type')
    if product_type:
        products = products.filter(type=product_type)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        try:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
        except ValueError:
            pass
    if max_price:
        try:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
        except ValueError:
            pass
    return render(request, 'allproduct.html', {'products': products})

def search_func(request):
    if request.method == 'GET':
        inp = request.GET.get('q', '').strip()
        if not inp:
            return render(request, 'search.html', {
                'error': 'Please enter a search query.',
                'type': Product.TYPE_CHOICES,
                'user': request.user if request.user.is_authenticated else None
            })
        if request.user.is_authenticated:
            try:
                user = users.objects.get(user=request.user)
                SearchHistory.objects.create(query=inp, user=user)
                user_search = [s.query for s in SearchHistory.objects.filter(user=user)]
                user_products = [s.product.name for s in ViewHistory.objects.filter(user=user)]
                user_data = [{
                    'user_id': user.id,
                    'product': ','.join(user_products) if user_products else '',
                    'search': ','.join(user_search) if user_search else ''
                }]
                df = pd.DataFrame(user_data)
                user_vectors = vectorize_user_with_search(df)
                user.vector_data = json.dumps(user_vectors[0].tolist())
                user.save()
            except users.DoesNotExist:
                pass
        products = Product.objects.filter(
            Q(name__icontains=inp) | Q(type__icontains=inp)
        ).distinct()
        categories = list(products.values_list('type', flat=True).distinct())
        context = {
            'products': products,
            'categories': categories,
            'query': inp,
            'type': Product.TYPE_CHOICES,
            'user': request.user if request.user.is_authenticated else None
        }
        return render(request, 'search.html', context)
    return render(request, 'search.html', {
        'type': Product.TYPE_CHOICES,
        'user': request.user if request.user.is_authenticated else None
    })


logger = logging.getLogger(__name__)

@login_required(login_url='userlogin')
def addReview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        description = request.POST.get('description', '').strip()
        # Validate inputs
        if not rating or not description:
            messages.error(request, "Rating and review are required.")
            return redirect('product', id=pk)
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError:
            messages.error(request, "Invalid rating. Please select a rating between 1 and 5.")
            return redirect('product', id=pk)
        # Create review
        user = users.objects.get(user=request.user)
        data = reviews.objects.create(
            rating=rating,
            description=description,
            uname=user,
            pname=product
        )
        # Update product rating
        rev = reviews.objects.filter(pname=product)
        total = [i.rating for i in rev]
        if total:
            product.rating = round(sum(total) / len(total), 1)
        else:
            product.rating = rating
        product.save()
        # Vectorize reviews
        pro_data = [{
            "pro_id": product.id,
            "name": product.name,
            "rating": product.rating,
            "type": product.type,
            "description": product.description,
            "reviews": ','.join([i.description for i in rev])
        }]
        df = pd.DataFrame(pro_data)
        try:
            product_vector = vectorize_product_with_reviews(df)
            product.vector_data = json.dumps(product_vector[0].tolist())
            product.save()
        except Exception as e:
            logger.error(f"Vectorization failed for product {product.id}: {e}")
        messages.success(request, "Review submitted successfully!")
        return redirect('product', id=pk)
    return redirect('product', id=pk)


def usersignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')
        if not all([username, email, password, confirmpassword]):
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_datas = [{
                    "user_id": user.id,
                    "product": "new_user",
                    "search": "initial_signup"
                }]
                df = pd.DataFrame(user_datas)
                user_vectors = vectorize_user_with_search(df)
                if user_vectors and len(user_vectors) > 0:
                    user_profile = users.objects.create(
                        user=user,
                        vector_data=json.dumps(user_vectors[0].tolist())
                    )
                    user_profile.save()
                    print(f"Vector created and saved successfully for user: {username}")
                else:
                    print(f"Failed to create vector for user: {username}")
                messages.success(request, "Account created successfully!")
                return redirect('userlogin')
            except Exception as e:
                print(f"Error creating vector for user {username}: {str(e)}")
                user_profile = users.objects.create(user=user, vector_data=None)
                user_profile.save()
                messages.success(request, "Account created successfully, but personalization data could not be initialized.")
                return redirect('userlogin')
    return render(request, "register.html")

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('firstpage')
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'userlogin.html')

def logoutuser(request):
    logout(request)
    request.session.flush()
    return redirect('userlogin')

def verifyotp(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        otp1 = request.session.get('otp')
        otp_time_str = request.session.get('otp_time')
        if otp_time_str:
            otp_time = datetime.fromisoformat(otp_time_str)
            otp_expiry_time = otp_time + timedelta(minutes=5)
            if datetime.now() > otp_expiry_time:
                messages.error(request, 'OTP has expired. Please request a new one.')
                del request.session['otp']
                del request.session['otp_time']
                return redirect('verifyotp')
        if otp == otp1:
            del request.session['otp']
            del request.session['otp_time']
            return redirect('passwordreset')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    otp = ''.join(random.choices('123456789', k=6))
    request.session['otp'] = otp
    request.session['otp_time'] = datetime.now().isoformat()
    message = f'Your email verification code is: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.session.get('email')]
    send_mail('Email Verification', message, email_from, recipient_list)
    return render(request, "otp.html")

def getusername(request):
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            request.session['email'] = user.email
            return redirect('verifyotp')
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('getusername')
    return render(request, 'getusername.html')

def passwordreset(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')
        if confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        else:
            email = request.session.get('email')
            try:
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                del request.session['email']
                messages.success(request, "Your password has been reset successfully.")
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('userlogin')
            except User.DoesNotExist:
                messages.error(request, "No user found with that email address.")
                return redirect('getusername')
    return render(request, "passwordreset.html")

def admin_bookings(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')
        order = get_object_or_404(Order, id=order_id)
        if action == 'confirm' and order.status == 'Pending':
            order.status = 'Confirmed'
            order.save()
            subject = 'Your WATCHCART Order Confirmation'
            message = f"""
Dear {order.name},

Your order (ID: {order.id}) has been confirmed! Below are the details:

**Shipping Address:** {order.shipping_address}
**Payment Method:** {order.payment_method}
**Total Price:** ₹{order.total_price}

**Order Items:**
"""
            for item in order.items.all():
                message += f"- {item.product.name} (Brand: {item.product.brand}, Colour: {item.product.colour}, Quantity: {item.quantity}, Price: ₹{item.product.offerprice})\n"
            message += "\nThank you for shopping with WATCHCART!"
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [order.user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email: {e}")
        return redirect('admin_bookings')
    # Fetch both Pending and Confirmed orders
    orders = Order.objects.filter(status__in=['Pending', 'Confirmed']).order_by('-date_ordered')
    return render(request, 'admin_bookings.html', {'orders': orders})
def delete_g(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('firstpage')

def edit_g(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        colour = request.POST.get('colour')
        price = request.POST.get('price')
        offerprice = request.POST.get('offerprice')
        description = request.POST.get('description')
        gender = request.POST.get('gender')
        type = request.POST.get('type')
        brand = request.POST.get('brand')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        if gender not in dict(Product.GENDER_CHOICES):
            messages.error(request, 'Invalid gender choice.')
            return redirect('edit_g', id=id)
        if type not in dict(Product.TYPE_CHOICES):
            messages.error(request, 'Invalid type choice.')
            return redirect('edit_g', id=id)
        product.name = name
        product.colour = colour
        product.price = price
        product.offerprice = offerprice
        product.description = description
        product.gender = gender
        product.type = type
        product.brand = brand
        product.quantity = quantity
        if image:
            product.image = image
        if image1:
            product.image1 = image1
        if image2:
            product.image2 = image2
        if image3:
            product.image3 = image3
        if image4:
            product.image4 = image4
        if image5:
            product.image5 = image5
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('firstpage')
    return render(request, 'add.html', {
        'data1': product,
    })

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        colour = request.POST.get('colour')
        price = request.POST.get('price')
        offerprice = request.POST.get('offerprice')
        description = request.POST.get('description')
        gender = request.POST.get('gender')
        type = request.POST.get('type')
        brand = request.POST.get('brand')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        if gender not in dict(Product.GENDER_CHOICES):
            messages.error(request, 'Invalid gender choice.')
            return redirect('add_product')
        if type not in dict(Product.TYPE_CHOICES):
            messages.error(request, 'Invalid type choice.')
            return redirect('add_product')
        product = Product.objects.create(
            name=name, 
            colour=colour, 
            price=price, 
            offerprice=offerprice,
            description=description, 
            gender=gender, 
            type=type, 
            brand=brand, 
            quantity=quantity,
            image=image, 
            image1=image1, 
            image2=image2, 
            image3=image3, 
            image4=image4, 
            image5=image5
        )
        pro_data = [{
            "pro_id": product.id,
            "name": name,
            "rating": 0,
            "description": description,
            "reviews": '',
            "type": type
        }]
        df = pd.DataFrame(pro_data)
        product_vector = vectorize_product_with_reviews(df)
        product.vector_data = json.dumps(product_vector[0].tolist())
        product.save()
        return redirect('firstpage')
    return render(request, 'add.html')

@login_required(login_url='userlogin')
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product, defaults={'quantity': 1})
    if not created and cart_item.quantity < product.quantity:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Quantity of {product.name} updated in your cart.")
    elif created:
        messages.success(request, f"{product.name} has been added to your cart.")
    else:
        messages.error(request, "Sorry, this product is out of stock.")
    return redirect('cart_view')

@login_required(login_url='userlogin')
def increment_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    if cart_item.quantity < cart_item.product.quantity:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Quantity updated.")
    else:
        messages.error(request, "No more stock available.")
    return redirect('cart_view')

@login_required(login_url='userlogin')
def decrement_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, "Quantity updated.")
    else:
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    return redirect('cart_view')

@login_required(login_url='userlogin')
def delete_cart_item(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart_view')

@login_required(login_url='userlogin')
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

@login_required(login_url='userlogin')
def checkout_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('cart_view')
    total_price = sum(item.get_total_price() for item in cart_items)
    default_address = Address.objects.filter(user=request.user, is_default=True).first()
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'default_address': default_address
    })

@login_required(login_url='userlogin')
def checkout_single(request, id):
    product = get_object_or_404(Product, id=id)
    cart_items = [{
        'product': product,
        'quantity': 1,
        'get_total_price': lambda: product.offerprice
    }]
    total_price = product.offerprice
    default_address = Address.objects.filter(user=request.user, is_default=True).first()
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'is_single': True,
        'product_id': product.id,
        'default_address': default_address
    })

@login_required(login_url='userlogin')
def process_checkout(request):
    if request.method == 'POST':
        address_choice = request.POST.get('address_choice')
        payment_method = request.POST.get('payment_method')
        is_single = request.POST.get('is_single') == 'True'
        product_id = request.POST.get('product_id')
        errors = {}

        # Initialize variables to avoid UnboundLocalError
        name = ''
        shipping_address = ''
        phone = ''

        if address_choice == 'default':
            user_address = Address.objects.filter(user=request.user, is_default=True).first()
            if not user_address:
                errors['address_choice'] = "No default address found. Please add an address or enter a new one."
            else:
                shipping_address = user_address.address
                name = user_address.name
                phone = user_address.phone
        else:
            name = request.POST.get('name', '').strip()
            shipping_address = request.POST.get('address', '').strip()
            phone = request.POST.get('phone', '').strip()
            if not name:
                errors['name'] = "Full name is required."
            if not shipping_address:
                errors['address'] = "Shipping address is required."
            if not phone:
                errors['phone'] = "Phone number is required."

        if not payment_method:
            errors['payment_method'] = "Please select a payment method."

        # Stock validation
        if is_single and product_id:
            product = get_object_or_404(Product, id=product_id)
            if product.quantity < 1:
                errors['stock'] = f"{product.name} is out of stock."
        else:
            cart_items = Cart.objects.filter(user=request.user)
            if not cart_items:
                errors['cart'] = "Your cart is empty."
            else:
                for item in cart_items:
                    if item.quantity > item.product.quantity:
                        errors['stock'] = f"Not enough stock for {item.product.name}. Available: {item.product.quantity}."

        if errors:
            cart_items = Cart.objects.filter(user=request.user) if not is_single else [{
                'product': get_object_or_404(Product, id=product_id),
                'quantity': 1,
                'get_total_price': lambda: get_object_or_404(Product, id=product_id).offerprice
            }]
            total_price = sum(item.get_total_price() for item in cart_items) if not is_single else get_object_or_404(Product, id=product_id).offerprice
            return render(request, 'checkout.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'default_address': Address.objects.filter(user=request.user, is_default=True).first(),
                'is_single': is_single,
                'product_id': product_id,
                'errors': errors,
                'name': name if address_choice == 'new' else '',
                'address': shipping_address if address_choice == 'new' else '',
                'phone': phone if address_choice == 'new' else '',
                'address_choice': address_choice,
                'payment_method': payment_method
            })

        # Order creation and stock update
        if is_single and product_id:
            product = get_object_or_404(Product, id=product_id)
            total_price = product.offerprice
            order = Order.objects.create(
                user=request.user,
                name=name,
                phone=phone,
                shipping_address=shipping_address,
                payment_method=payment_method,
                total_price=total_price,
                status='Pending'
            )
            OrderItem.objects.create(order=order, product=product, quantity=1)
            product.quantity -= 1
            product.save()
        else:
            cart_items = Cart.objects.filter(user=request.user)
            total_price = sum(item.get_total_price() for item in cart_items)
            order = Order.objects.create(
                user=request.user,
                name=name,
                phone=phone,
                shipping_address=shipping_address,
                payment_method=payment_method,
                total_price=total_price,
                status='Pending'
            )
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                item.product.quantity -= item.quantity
                item.product.save()
            cart_items.delete()

        # Send order confirmation email
        subject = 'Your WATCHCART Order Placed'
        message = f"""
Dear {order.name},

Your order (ID: {order.id}) has been placed successfully! Below are the details:

**Shipping Address:** {order.shipping_address}
**Payment Method:** {order.payment_method}
**Total Price:** ₹{order.total_price}
**Status:** {order.status}

**Order Items:**
"""
        for item in order.items.all():
            message += f"- {item.product.name} (Brand: {item.product.brand}, Colour: {item.product.colour}, Quantity: {item.quantity}, Price: ₹{item.product.offerprice})\n"
        message += "\nThank you for shopping with WATCHCART!"
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [order.user.email],
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Failed to send order placement email for order {order.id}: {e}")

        if payment_method == 'cod':
            order.is_paid = False
            order.save()
            return redirect('order_confirmation', order_id=order.id)
        else:
            return redirect('start_razorpay_payment', order_id=order.id)
    return redirect('cart_view')

@login_required(login_url='userlogin')
def start_razorpay_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.payment_method != 'online':
        messages.error(request, "Invalid payment method.")
        logger.warning(f"Invalid payment method for order {order.id}: {order.payment_method}")
        return redirect('cart_view')
    if not hasattr(settings, 'RAZORPAY_KEY_ID') or not hasattr(settings, 'RAZORPAY_KEY_SECRET'):
        messages.error(request, "Payment gateway is not configured properly.")
        logger.error("Razorpay keys are missing in settings.")
        return redirect('cart_view')
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    amount = int(order.total_price * 100)  # Convert to paise
    data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': f'order_{order.id}',
        'payment_capture': 1  # Auto capture
    }
    try:
        razorpay_order = client.order.create(data=data)
        order.razorpay_payment_id = razorpay_order['id']
        order.save()
        return render(request, 'payment.html', {
            'order': order,
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'amount': amount,
            'currency': 'INR',
            'name': order.name,
            'email': request.user.email,
            'contact': order.phone,
            'callback_url': request.build_absolute_uri(reverse('razorpay_callback')),
        })
    except razorpay.errors.BadRequestError as e:
        messages.error(request, f"Payment initiation failed: Invalid order details.")
        logger.error(f"Razorpay BadRequestError for order {order.id}: {str(e)}")
        return redirect('cart_view')
    except razorpay.errors.ServerError as e:
        messages.error(request, f"Payment gateway is currently unavailable. Please try again later.")
        logger.error(f"Razorpay ServerError for order {order.id}: {str(e)}")
        return redirect('cart_view')
    except Exception as e:
        messages.error(request, f"Error initiating payment: {str(e)}")
        logger.error(f"Unexpected error in start_razorpay_payment for order {order.id}: {str(e)}")
        return redirect('cart_view')

@csrf_exempt
def razorpay_callback(request):
    if request.method == 'POST':
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment_data = request.POST
        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': payment_data.get('razorpay_order_id'),
                'razorpay_payment_id': payment_data.get('razorpay_payment_id'),
                'razorpay_signature': payment_data.get('razorpay_signature')
            })
            order = get_object_or_404(Order, razorpay_payment_id=payment_data.get('razorpay_order_id'))
            order.is_paid = True
            order.status = 'Confirmed'
            order.razorpay_payment_id = payment_data.get('razorpay_payment_id')
            order.save()
            subject = 'Your WATCHCART Payment Confirmation'
            message = f"""
Dear {order.name},

Your payment for order (ID: {order.id}) has been confirmed! Below are the details:

**Shipping Address:** {order.shipping_address}
**Payment Method:** {order.payment_method}
**Total Price:** ₹{order.total_price}
**Status:** {order.status}

**Order Items:**
"""
            for item in order.items.all():
                message += f"- {item.product.name} (Brand: {item.product.brand}, Colour: {item.product.colour}, Quantity: {item.quantity}, Price: ₹{item.product.offerprice})\n"
            message += "\nThank you for shopping with WATCHCART!"
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [order.user.email],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f"Failed to send payment confirmation email for order {order.id}: {e}")
            messages.success(request, "Payment successful!")
            return redirect('order_confirmation', order_id=order.id)
        except razorpay.errors.SignatureVerificationError as e:
            messages.error(request, "Payment verification failed: Invalid signature.")
            logger.error(f"SignatureVerificationError in razorpay_callback: {str(e)}")
            return redirect('cart_view')
        except Order.DoesNotExist:
            messages.error(request, "Order not found.")
            logger.error(f"Order not found for razorpay_order_id: {payment_data.get('razorpay_order_id')}")
            return redirect('cart_view')
        except Exception as e:
            messages.error(request, f"Payment verification failed: {str(e)}")
            logger.error(f"Unexpected error in razorpay_callback: {str(e)}")
            return redirect('cart_view')
    return redirect('cart_view')

@login_required(login_url='userlogin')
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})

@login_required(login_url='userlogin')
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

def first_page(request):
    products = Product.objects.all()
    return render(request, 'firstpage.html', {'products': products})