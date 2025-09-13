# from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.
def BookView(request):
    return render(request, 'relationship_app/list_books.html')


class LibraryBookView(DetailView):
    template_name = "relationship_app/library_detail.y"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['library'] = Library.objects.all()
        return context