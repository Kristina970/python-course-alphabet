from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Article, Comment, ReplyComment
from .forms import ArticleForm, CommentForm, ReplyCommentForm
from .models import Profile
from .mixins import FormMessageMixin
from django.core.paginator import Paginator


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles_list = Article.objects.all()
        paginator = Paginator(articles_list, 5)  # Show 5 contacts per page
        page = self.request.GET.get('page')
        articles_list = paginator.get_page(page)
        return articles_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'View all'
        return context


class ArticleCreateView(FormMessageMixin, CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm
    form_valid_message = 'Article created successfully!'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm(initial={'author_name': self.request.user.username})
        context['reply_form'] = ReplyCommentForm()
        return context

    def post(self, request, article_id):
        post = get_object_or_404(Article, pk=article_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', article_id=article_id)
        return render(request, 'detail.html', {'comment_form': form})


class ArticleUpdateView(FormMessageMixin, UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'
    form_valid_message = 'Updated successfully!'
    form_valid_message = 'Updated successfully!'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    pk_url_kwarg = 'article_id'
    template_name = 'article/confirm_delete.html'
    context_object_name = 'article'


class ArticleCommentView(FormMessageMixin, CreateView):
    model = Comment
    template_name = 'article/detail.html'
    form_class = CommentForm
    form_valid_message = 'Comment created successfully!'

    def post(self, request, article_id):
        post = get_object_or_404(Article, pk=article_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', article_id=article_id)
        return render(request, 'detail.html', {'form': form})


class CommentReplyView(FormMessageMixin, CreateView):
    model = ReplyComment
    template_name = 'article/detail.html'
    form_class = ReplyCommentForm
    form_valid_message = 'Reply to comment created successfully!'

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        kwargs = {
            'comment': comment
        }
        reply_form = ReplyCommentForm(request.POST, **kwargs)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.comment = comment
            reply.save()

        return redirect('detail', article_id=comment.post_id)
        # return render(request, 'detail.html', {'form': reply_form})











