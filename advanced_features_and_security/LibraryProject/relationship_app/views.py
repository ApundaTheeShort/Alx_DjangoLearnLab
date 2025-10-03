from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def home(request):
    return render(request, 'home.html')

def list_books(request):
    """
    Function-based view to list all books.
    """
    books = Book.objects.all()
    return render(request,"relationship_app/list_books.html", {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based view to show details of a specific library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # Redirect to home or a success page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form, 'form_title': 'Register'})


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('list_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Add Book'
        return context
    

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('list_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Book'
        return context

class BookDelete(DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('list_books')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return BookCreate.as_view()(request)

@permission_required('relationship_app.can_change_book')
def change_book(request, pk):
    return BookUpdate.as_view()(request, pk=pk)

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    return BookDelete.as_view()(request, pk=pk)

