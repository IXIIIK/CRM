from django.shortcuts import render, redirect, get_object_or_404
from crm.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from .models import Order, Catalog
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views import View

#New order view
class OrderCreateView(CreateView):
	model = Order
	template_name = 'order/create_order.html'
	fields = ['first_name', 'last_name', 'phoneNumber', 'order_status', 'order_catalog']
	success_url = 'index.html'

	def post(self, request):
		if request.method == 'POST':
			order = Order.objects.get_or_create(
				first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),
				order_status = request.POST.get('order_status'),
				order_catalog = Catalog.objects.get(id=request.POST.get('order_catalog')),
				phoneNumber = request.POST.get('phoneNumber')
			)
		return redirect('index')
	
#detail order
class DetailOrder(View):

	def get(self, request, pk):
		order_details = get_object_or_404(Order, pk=pk)
		context = {
			'order': order_details,
				}
		return render(request, template_name='order/details_order.html', context=context)

#registration view
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
	return render(request=request, template_name="registration/register.html", context={"register_form":form})

#authenticate view
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

#logout view
def logout_request(request):
	logout(request)
	messages.info(request, 'Вы вышли из аккаунта')
	return redirect('index')


#index view
def index(request):
	orders = Order.objects.all()
	return render(request=request, template_name='index.html', context={'orders': orders})