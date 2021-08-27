from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ItemLost
from .forms import Lost
from django.core.mail import send_mail


# Create your views here.
class ItemListView(ListView):
    model = ItemLost
    template_name = 'findme/home.html'
    context_object_name = 'items'
    ordering = ['-lost_date']


class ItemFoundView(ListView):
    model = ItemLost
    template_name = 'findme/found.html'
    context_object_name = 'items'
    print('items')
    ordering = ['-lost_date']


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


def found(request, ItemID):
    item = ItemLost.objects.get(ItemID=ItemID)
    itemlost_author = item.name
    itemfound_author = request.user
    if request.method == "POST":
        if itemlost_author != itemfound_author:
            c = request.POST.get("location")
            d = item.name
            # print(item.name)
            # print(item.name.email)
            b = request.user
            a = item.name.email
            e=item
            item.found = True
            print(request.POST)
            send_mail(
                "Item Found!", f"found at {c} by {b}", "chinmayparekh11@gmail.com", [a], fail_silently=False,
            )
            item.found_location = request.POST.get('location')
        else:
            messages.info(request, "An item cannot be lost and found by the same person")
    item.save()

    return redirect('findme-home')


class ItemDetailView(DetailView):
    model = ItemLost
    context_object_name = 'item'
    template_name = 'findme/item.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = ItemLost
    template_name = 'findme/item_form.html'
    form_class = Lost

    # fields = ['title', 'description', 'location', 'image']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


# Not used
class CreateItemView(CreateView):
    model = ItemLost
    template_name = 'findme/item_form.html'
    form_class = Lost
    #
    # class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #     model = Post
    #     fields = ['title', 'content']
    #
    #     def form_valid(self, form):
    #         form.instance.author = self.request.user
    #         return super().form_valid(form)
    #
    #     def test_func(self):
    #         post = self.get_object()
    #         if self.request.user == post.author:
    #             return True
    #         return False
    #
    #
    # class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    #     model = Post
    #     success_url = '/'
    #
    #     def test_func(self):
    #         post = self.get_object()
    #         if self.request.user == post.author:
    #             return True
    # return False
