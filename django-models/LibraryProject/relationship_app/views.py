# from typing import Any
from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Library
from .models import Book
from .import utils
# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect

def list_books(request):
    return render(request, 'relationship_app/list_books.html')


class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs: Book) -> dict[str, Book]:
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['library'] = Library.objects.all()
        return context
    
# class Register(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

# @login_required
# def home(request):
#     return render(request, "home.html", {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


@user_passes_test(utils.is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')




@user_passes_test(utils.is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(utils.is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
