from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request, 'home.html', {})
from .models import Post, Catagory
from .forms import PostForm, EditForm


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def CatagoryView(request, cat):
    catagory_posts = Post.objects.filter(catagory=cat)
    return render(request, 'catagory.html', {'cat':cat.title(), 'catagory_posts':catagory_posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id', '-post_date']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Catagory.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Catagory.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = False
        else:
            liked = True

        context["total_likes"] = total_likes
        context["cat_menu"] = cat_menu
        context["liked"] = liked
        return context

class AddCatagoryView(CreateView):
    model = Catagory
    # form_class = PostForm
    fields = '__all__'
    template_name = 'add_catagory.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    # form_class = PostForm
    form_class =EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
