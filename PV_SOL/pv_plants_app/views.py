from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PVCreateForm, RegisterForm, LoginForm, FilterForm, ProfileForm
from .models import PV_Plant


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order':order,
        'text': text,
    }

# Create your views here.
#def index(request):
#    params = extract_filter_values(request.GET)
#    order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
#    pv_plants = PV_Plant.objects.filter(name__icontains=params['text']).order_by(order_by)

#    context = {'pv_plants': pv_plants,
#              'current_page': 'home',
#              'filter_form':FilterForm(),
#               }
#    return render(request, 'index.html', context)

#@login_required(login_url='login user')
class IndexView(ListView):
    template_name = 'index.html'
    model = PV_Plant
    context_object_name = 'pv_plants'
    order_by='name'

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        return super().dispatch(request, *args,**kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pv_plants'] = sorted(context['pv_plants'], key=lambda x:x.name, reverse=not self.order_by_asc)
        context['filter_form'] = FilterForm(initial={'order': self.order_by_asc})
        return context



def create(request):
    if request.method == 'GET':
        form = PVCreateForm()
        context = {'form': form,
                   'current_page':'create',
                   }
        return render(request, 'create.html', context )
    else:
        form = PVCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            pv_plant = form.save()
            pv_plant.save()
            return redirect('index')


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
                    'user_form': RegisterForm(),
                    'profile_form': ProfileForm(),
        }
        return render(request, 'register.html', context )
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
    return render(request, 'register.html', context)

#class RegisterView(CreateView):
#    form_class = UserCreationForm
#    template_name = 'register.html'
#    success_url = reverse_lazy('index.html')

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)

#        context['user_forms'] = context['forms'],
#        context['profile_forms'] = ProfileForm()
#
#        return context



def login_user(request):
    if request.method == 'GET':
       context = { 'login_form': LoginForm(),
                 }
       return render(request, 'login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

            return redirect('index')

        context = {
            'login_form':login_form,
        }

def logout_user(request):
    logout(request)
    return redirect('index')
