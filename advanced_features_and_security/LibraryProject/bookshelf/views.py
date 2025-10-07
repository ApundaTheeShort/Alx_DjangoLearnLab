from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ExampleForm

from .models import Book
# Create your views here.


def index(request): return HttpResponse("Welcome to bookshelf")


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/book_list.html', context)


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'bookshelf/book_details.html', context)


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted successfully.")

    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

#  Example view to demonstrate the use of ExampleForm


@login_required
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            char_field = form.cleaned_data['char_field']
            email_field = form.cleaned_data['email_field']
            return HttpResponse(f"Received: {char_field}, {email_field}")
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
