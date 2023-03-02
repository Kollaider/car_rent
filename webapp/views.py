from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from webapp.forms import RegisterUserForm
from webapp.models import Car


def index(request):
    cars = Car.objects.all()[:3]
    main_car = Car.objects.filter(is_main=True).first()
    context = {
        'cars': cars,
        'main_car': main_car
    }
    return render(request, 'webapp/index.html', context=context)


class AboutView(TemplateView):
    template_name = 'webapp/about.html'


class ServicesView(TemplateView):
    template_name = 'webapp/services.html'


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'webapp/contact.html'


class CarListView(ListView):
    """Car List View for getting list objects"""
    template_name = 'webapp/cars.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        paginator = Paginator(context['object_list'], 4)
        page_objs = paginator.get_page(page_number)
        context['page_objs'] = page_objs
        return super().get_context_data(**context)


    def get_queryset(self):
        return Car.objects.all()


class CarDetailView(DetailView):
    """Car List View for getting detail object"""
    model = Car
    template_name = 'webapp/car_detail.html'


class CRLoginView(LoginView):
    template_name = 'webapp/login.html'
    redirect_authenticated_user = True


class CRLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'webapp/logout.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'webapp/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('webapp:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'webapp/register_done.html'