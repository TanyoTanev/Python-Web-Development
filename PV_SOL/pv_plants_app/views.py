from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, TemplateView, FormView, UpdateView

from .decorators import group_required
from .forms import PVCreateForm, RegisterForm, LoginForm, FilterForm, ProfileForm, ForecastForm, PVUpdateForm
from .models import PV_Plant
from .view_mixins import GroupRequiredMixin


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order':order,
        'text': text,
    }

class IndexView(ListView):
    template_name = 'index.html'
    model = PV_Plant
    context_object_name = 'pv_plants'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''


    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        #self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']

        return super().dispatch(request, *args,**kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-name'
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['pv_plants'] = sorted(context['pv_plants'], key=lambda x:x.name, reverse=not self.order_by_asc)
        context['filter_form'] = FilterForm(initial={'order': self.order_by,
                                                     'text': self.contains_text
                                                            })
        return context


@method_decorator(group_required(groups=['Owners group']), name='dispatch')
class PVCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = PVCreateForm
    template_name = 'create.html'
    groups = ['User']

    def get_success_url(self):
        success_url = reverse_lazy('index', kwargs={})
        return success_url

    def form_valid(self, form):
        pv_plant = form.save(commit=False)
        pv_plant.owner = self.request.user
        pv_plant.save()

        return super().form_valid(form)


class RegisterView(TemplateView):
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_form'] = RegisterForm()
        context['profile_form'] = ProfileForm()

        return context

    def post(self, request):

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


@login_required(login_url='login user')
def pv_plant_details(request, pk):
    pv_plant = PV_Plant.objects.get(pk=pk)
    context = {
        'pv_plant': pv_plant,
            }
    return render(request, 'pv_plants_details.html',context)

#@method_decorator(group_required(groups=['Owners group']), name='dispatch')
class PVUpdateView(GroupRequiredMixin,LoginRequiredMixin, FormView): #
    form_class = PVUpdateForm
    template_name = 'pv_update.html'
    success_url = reverse_lazy('index')
    groups = ['User']

    def form_valid(self, form):
        #contact = form.save(commit=False)
        #contact.owner = request.user
        #contact.save()

        form.save() # оригинално така да се каже
        return super().form_valid(form)

# allowed only if the user id is creator or admin, checked in template
def pv_plant_edit(request, pk):
    pv_plant = PV_Plant.objects.get(pk=pk)
    form = PVCreateForm(request.POST or None, instance=pv_plant)
    if form.is_valid():
        pv_plant.owner = request.user
        form.save()
        return redirect('index')
    return render(request, 'pv_update.html', context={'form':form})

# allowed only if the user id is creator or admin, checked in template
def pv_plant_delete(request, pk):
    pv_plant = PV_Plant.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pv_plant': pv_plant,
                   }
        return render(request, 'delete.html', context)
    else:
        pv_plant.delete()
        return redirect('index')


class PVPlantUpdate(ListView):
    fields = ['name']
    template_name = 'pv_update.html'
    model = PV_Plant


@method_decorator(group_required(groups=['Owners group']), name='dispatch')
class GenerationForecast(ListView):
    template_name = 'forecast.html'
    model = PV_Plant
    context_object_name = 'pv_plants'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['user_id'] = PV_Plant.objects(self.request.user)
        #object_list = self.object_list
        #queryset = kwargs.pop('object_list', None)
        #if queryset is None:
        #    self.object_list = self.PV_Plant.objects.all()
        #object_list = self.object_list
        context['form'] = ForecastForm()
        #context['pv_plants'] = object_list
        return context


   # def get(self, request, *args, **kwargs):
        #context = super().get_context_data(**kwargs)
       # id=self.request.get('id')
        #context['id']=id
        #return context

def pv_plant_forecast(request, pk):

    pv_plant = PV_Plant.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pv_plant': pv_plant,
        }
        return render(request, 'forecast.html', context)
    else:
        return render(request, 'forecast.html', {})



@method_decorator(group_required(groups=['Owners group']), name='dispatch')
class BusinessView(ListView):
    template_name = 'business_client.html'
    model = PV_Plant
    context_object_name = 'pv_plants'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''


    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        #self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']


        return super().dispatch(request, *args,**kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-power'
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['pv_plants'] = sorted(context['pv_plants'], key=lambda x:x.name, reverse=not self.order_by_asc)
        context['filter_form'] = FilterForm(initial={'order': self.order_by,
                                                     'text': self.contains_text
                                                     })
        return context


class LoginView(CreateView):

    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):

        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

            return redirect('index')

    def get(self, request, *args, **kwargs):
        context = { 'login_form': LoginForm(),
                }
        return render(request, 'login.html', context)


class Logout(LogoutView):
    next_page = reverse_lazy('index')



