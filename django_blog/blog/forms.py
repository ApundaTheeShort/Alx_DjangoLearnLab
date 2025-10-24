from django import forms
from .models import CustomUser, Post, Comment
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'bio', 'profile_picture']


from taggit.forms import TagWidget


class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(), help_text='A comma-separated list of tags.')

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tags'].initial = ', '.join(
                [t.name for t in self.instance.tags.all()])

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        tags = self.cleaned_data.get('tags')
        if tags:
            instance.tags.set(*[tag.strip() for tag in tags.split(',')])
        return instance



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
