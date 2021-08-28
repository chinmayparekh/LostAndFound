from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ItemLost
from .forms import Lost
from django.core.mail import send_mail


@login_required
def itemfound(request):
    context = {
        'items': ItemLost.objects.filter(found=True)
    }
    return render(request, 'findme/found.html', context)


@login_required
def home(request):
    context = {
        'items': ItemLost.objects.filter(found=False)
    }
    return render(request, 'findme/home.html', context)


def about(request):
    return render(request, 'findme/about.html', {'title': 'About'})

@login_required
def found(request, ItemID):
    item = ItemLost.objects.get(ItemID=ItemID)
    itemlost_author = item.name
    itemfound_author = request.user
    if request.method == "POST":
        if itemlost_author != itemfound_author:
            location = request.POST.get("location")
            found_user = request.user
            email_id = item.name.email

            item.found = True
            print(request.POST)
            send_mail(
                "Item Found!", f"found at {location} by {found_user}", "emailID@gmail.com", [email_id],
                fail_silently=False,
            )
            item.found_location = request.POST.get('location')
        else:
            messages.info(request, "An item cannot be lost and found by the same person")
    item.save()

    return redirect('findme-home')


class ItemDetailView(LoginRequiredMixin,DetailView):
    model = ItemLost
    context_object_name = 'item'
    template_name = 'findme/item.html'


class ItemDetail(LoginRequiredMixin,DetailView):
    model = ItemLost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = ItemLost
    template_name = 'findme/item_form.html'
    form_class = Lost

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemLost
    form_class = Lost
    template_name = 'findme/item_form.html'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.name:
            return True
        return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ItemLost
    template_name = 'findme/itemdelete_form.html'
    success_url = '/'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.name:
            return True
        return False

