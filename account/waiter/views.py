from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Order


def home(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'waiter/home.html', context)

class OrderListView(ListView):
    model = Order
    template_name = 'waiter/home.html'  
    context_object_name = 'orders'
    ordering = ['-date']


class OrderDetailView(DetailView):
    model = Order


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['table', 'order']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['table', 'order']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.customer:
            return True
        return False


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.customer:
            return True
        return False

def about(request):
    return render(request, 'waiter/about.html', {'table': 'About'})