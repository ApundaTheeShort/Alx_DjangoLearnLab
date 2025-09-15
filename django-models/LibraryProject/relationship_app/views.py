# from typing import Any
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

def list_books(request):
    return render(request, 'relationship_app/list_books.html')


class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['library'] = Library.objects.all()
        return context
    
class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

