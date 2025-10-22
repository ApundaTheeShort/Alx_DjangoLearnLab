from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics, viewsets
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, ProfileUpdateForm, PostForm
from .models import Post, CustomUser
from .serializers import PostSerializer, CustomUserSerializer


def home(request):
    return render(request, 'blog/home.html')


def posts(request):
    return render(request, 'blog/posts.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'blog/profile.html', context)


class CreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def validate(self, attrs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this post.")
        return super().validate(attrs)

# class CreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
