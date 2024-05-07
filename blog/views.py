from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .forms import LoginForm , UserRegistrationForm
from .forms import *
import os
# from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from channels.security.websocket import AllowedHostsOriginValidator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # إرسال البريد الإلكتروني
        send_mail(
            'رسالة من صفحة اتصل بنا',
            f'اسم: {name}\nالبريد الإلكتروني: {email}\n\n{message}',
            'mohammed@gmail.com',  # البريد الإلكتروني الذي سيتم إرسال الرسالة من خلاله
            ['mohammed@gmail.com'],  # البريد الإلكتروني الذي سيتم إرسال الرسالة إليه
        )
        
        return HttpResponse('تم إرسال الرسالة بنجاح')
    else:
        return render(request, 'home/contact_us.html')  # قم بإنشاء قالب HTML لصفحة اتصل بنا وقم بتسليمه هنا

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse("ffffffffddddddddd")
#             else:
#                 return HttpResponse("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
#         else:
#                 return HttpResponse("nnnnnnnnnnbbbbbbbbbbbnnnnnnnnnnnnnnnnnnnnnn")
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form':form})
# تسجيل دخول المستخدم

def users_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # تحويل المستخدم إلى صفحة العرض بعد تسجيل الدخول بنجاح
            return redirect('product')
        else:
            pass
            # عرض رسالة خطأ في حالة بيانات تسجيل الدخول غير صحيحة
    return render(request, 'login_account/login_sn.html')

# انشا حساب المستخدم

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# تسجيل الادمن
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            # تحويل إلى صفحة إدارة النظام بعد تسجيل الدخول
            return redirect('home')
        else:
            pass
            # عرض رسالة خطأ في حالة بيانات تسجيل الدخول غير صحيحة أو ليست للإداري
    return render(request, 'login_account/login_admin.html', {'user':login})
# @@@@@@@@@@@@@
# انشاء حساب
def registration(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/login_sn')

	return render(request, 'login_account/registration.html', {"user_form": form})

def forgot_password(request):
	# form = RegistrationForm(request.POST or None)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect('/login_sn')

	return render(request, 'login_account/forgot-password.html')
# 222222222   
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/login_sn')
            # return render(request, "account/register_done.html", {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'login_account/register.html', {'user_form':user_form})



def signout(request):
    logout(request)
    return redirect('home')	

@login_required
def PasswordChange(request):
	user = request.user
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data.get('new_password')
			user.set_password(new_password)
			user.save()
			update_session_auth_hash(request, user)
			return redirect('change-password-done')
	else:
		form = ChangePasswordForm(instance=user)

	context = {
		'form': form,
	}

	return render(request, 'login_account/change_password.html', context)
def PasswordChangeDone(request):
	return render(request, 'login_account/change_password_done.html')
def your_view(request):
    # page_number = request.GET.get('page')  # احصل على رقم الصفحة من الطلب النموذجي
    # items_per_page = 6  # عدد العناصر لكل صفحة

    # all_items = Book.objects.all()  # احصل على جميع البيانات التي تريد عرضها
    # paginator = Paginator(all_items, items_per_page)  # جهز التقسيم

    # page_obj = paginator.get_page(page_number)  # احصل على الصفحة المحددة
    context ={
        # 'page_obj': page_obj,
        # 'Category': Category.objects.all(),
        # 'formcat':CategoryForm(),
        'user':User.objects.all(),
        # 'book': Book.objects.all(),
        # 'allbooks':Book.objects.filter(active=True).count(),
        # 'booksold':Book.objects.filter(status='sold').count(),
        # 'bookrental':Book.objects.filter(status='rental').count(),
        # 'bookncailble':Book.objects.filter(status='availble').count(),

    }

    return render(request, 'home/homes.html', context)


def home(request):
    page_number = request.GET.get('page')  # احصل على رقم الصفحة من الطلب النموذجي
    items_per_page = 6  # عدد العناصر لكل صفحة
    all_items = Book.objects.all()  # احصل على جميع البيانات التي تريد عرضها
    paginator = Paginator(all_items, items_per_page)  # جهز التقسيم
    page_obj = paginator.get_page(page_number)  # احصل على الصفحة المحددة




    context = {
        # 'posts':posts,
        'page_obj': page_obj,
        'Category': Category.objects.all(),
        'formcat':CategoryForm(),
        'user':User.objects.all(),
        'book': Book.objects.all(),
        
        'allbooks':Book.objects.filter(active=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookncailble':Book.objects.filter(status='availble').count(),
    }
    return render(request, 'home/home.html', context)
def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('home')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form': book_save,
    }
    return render(request, 'home/update.html', context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('home')
    return render(request, 'home/delete.html')


def product(request):
    search = Book.objects.all()
    title = None
    
    page_number = request.GET.get('page')  # احصل على رقم الصفحة من الطلب النموذجي
    items_per_page = 6  # عدد العناصر لكل صفحة
    all_items = Book.objects.all()  # احصل على جميع البيانات التي تريد عرضها
    paginator = Paginator(all_items, items_per_page)  # جهز التقسيم
    page_obj = paginator.get_page(page_number)  # احصل على الصفحة المحددة
    
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    context = {
        'page_obj': page_obj,
        'Category': Category.objects.all(),
        'book': search,
        # 'books': book_views,
        'viewss':Book.objects.filter(views=True).count(),
        # 'book_views': book_views,
        'cat':CategoryForm(),
    }
    return render(request, 'home/product.html', context)

def product_detail(request, id):
    book_view = get_object_or_404(Book, id=id)
    book_view.views += 1
    book_view.save()

    file_path = book_view.open_book.path
    size_in_bytes = os.path.getsize(file_path)
    size_in_mb = size_in_bytes
    
    
    page_number = request.GET.get('page')  # احصل على رقم الصفحة من الطلب النموذجي
    items_per_page = 6  # عدد العناصر لكل صفحة
    all_items = Book.objects.all()  # احصل على جميع البيانات التي تريد عرضها
    paginator = Paginator(all_items, items_per_page)  # جهز التقسيم
    page_obj = paginator.get_page(page_number)  # احصل على الصفحة المحددة
    context = {
        'Category': Category.objects.all(),
        'book':Book.objects.all(),
        'books': book_view,
        # 'viewss':Book.objects.filter(views=True).count(),
        # 'book_views': book_view,
        'size': size_in_mb,
        'page_obj': page_obj,
    }
    return render(request, 'home/product-detail.html', context)

   


def login_sg(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user.is_active:
                login(request, user)
                return redirect('home')
                # return HttpResponse("home")
            else:
                return HttpResponse("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        else:
                return HttpResponse("nnnnnnnnnnbbbbbbbbbbbnnnnnnnnnnnnnnnnnnnnnn")
    else:
        form = LoginForm()
    return render(request, 'login_account/login_sn.html', {'form':form})

def add_book(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'Category': Category.objects.all(),
        'book': Book.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookncailble':Book.objects.filter(status='availble').count(),
    }
    return render(request, 'home/add_book.html', context)

def chat_user(request):
    if request.method == 'POST':
        chat = Chat_form(request.POST, request.FILES)
        if chat.is_valid():
            chat.save()
    context = {
        'chats': chat_model.objects.all(),
        'chat': Chat_form(),

    }
    
    return render(request, 'home/chat.html', context)
