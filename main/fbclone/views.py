from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# Create your views here.

# Home view: Displays all posts in the homepage.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'fbclone/home.html', context)


# PostListView: Handles displaying the list of posts in the homepage, ordered by date.
class PostListView(ListView):
    model = Post
    template_name = 'fclone/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order posts by most recent


# PostDetailView: Displays the details of a single post.
class PostDetailView(DetailView):
    model = Post


# PostCreateView: Allows users to create a new post. Only logged-in users can access this view.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'video']

    # Override the form_valid method to associate the post with the current logged-in user.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# PostUpdateView: Allows users to update their own posts. Only the author of the post can update it.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'video']

    # Override the form_valid method to associate the post with the current logged-in user.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Check if the user is the author of the post before allowing the update.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# PostDeleteView: Allows users to delete their own posts. Only the author can delete the post.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect to homepage after deletion

    # Check if the user is the author of the post before allowing deletion.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Video view: Renders the video page.
def video(request):
    return render(request, 'fbclone/video.html')


# Marketplace view: Renders the marketplace page.
def marketplace(request):
    return render(request, 'fbclone/marketplace.html')


# Groups view: Renders the groups page.
def groups(request):
    return render(request, 'fbclone/groups.html')


# Gaming view: Renders the gaming page.
def gaming(request):
    return render(request, 'fbclone/gaming.html')


# Home view (again, this was defined twice): Displays all posts ordered by date.
def home(request):
    posts = Post.objects.all().order_by('-date_posted')  # Order by the date posted
    return render(request, 'fbclone/home.html', {'posts': posts})


# Logout view: Logs out the user and redirects to the logout page.
def logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')


# Video view (again, with login required): Renders the video page.
@login_required
def video(request):
    return render(request, 'fbclone/video.html')


# Marketplace view (again, with login required): Renders the marketplace page.
@login_required
def marketplace(request):
    return render(request, 'fbclone/marketplace.html')


# Groups view (again, with login required): Renders the groups page.
@login_required
def groups(request):
    return render(request, 'fbclone/groups.html')


# Gaming view (again, with login required): Renders the gaming page.
@login_required
def gaming(request):
    return render(request, 'fbclone/gaming.html')
