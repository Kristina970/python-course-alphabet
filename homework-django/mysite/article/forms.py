from django import forms
from .models import Article, Comment, ReplyComment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Custom Title',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author_name', 'comment',)
        labels = {
            'comment': 'your text',
            'author_name': 'author',

        }


class ReplyCommentForm(forms.ModelForm):

    class Meta:
        model = ReplyComment
        fields = ('comment', 'reply_text')
        widgets = {
            'comment': forms.HiddenInput(),
        }

        labels = {
            'comment': 'your reply',
        }

    def __init__(self, *args, comment=None, **kwargs):
        super(ReplyCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].initial = comment