from django import forms
from .models import Post, Catagory
cats = Catagory.objects.all().values_list('name', 'name')
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header_image', 'title', 'title_tag', 'author', 'catagory', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': cats}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'catagory': forms.Select(choices=cats, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'this is title place holder stuff'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }