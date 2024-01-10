from django.core.files.storage import FileSystemStorage
from django.shortcuts import  render, redirect
from crm.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Регстрация прошла успешно!" )
			return redirect("index")
		messages.error(request, "Не корректные данные.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f'Вы вошли как {username}.')
				return redirect('index')
			else:
				messages.error(request, 'Не корректные данные')
		else:
			messages.error(request, 'Не корректные данные')
	form = AuthenticationForm()
	return render(request=request, template_name='registration/login.html', context={'login_form':form})

def logout_request(request):
	logout(request)
	messages.info(request, 'Вы вышли из аккаунта')
	return redirect('index')
			

def index(request):
    return render(request=request, template_name='index.html')

def torg12(request):
	
	return render(request=request, template_name='torg-12.html')


def new_order(request):
	return render(request=request, template_name='new-order.html')