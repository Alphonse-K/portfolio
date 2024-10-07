from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, UpdateView
from django.views.generic.detail import DetailView
from django.views import View
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import F





class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'single_post'
    form_class = CommentForm


    def get_success_url(self):
        return reverse_lazy('blog:blogpost', kwargs={'pk': self.object.pk })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:8]
        context['comments'] = self.object.comments.all()
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            messages.success(
                request,
                "commentaire enregistre avec succes"
            )
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)
        

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'blog/update_comment.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:blogpost', kwargs={'pk': self.object.post.id})
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Commentaire actualise"
        )
        return response
    

class LikesIncrementView(View):

    def get_success_url(self):
        return reverse('blog:blogpost', kwargs={'pk': self.kwargs.get('pk')})
    
    def post(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        post = Post.objects.get(id=pk)
        post.likes = F('likes') + 1
        post.save()

        return redirect(self.get_success_url())
