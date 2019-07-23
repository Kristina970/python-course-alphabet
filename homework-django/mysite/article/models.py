from django import forms
from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    author_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_date']

    def approve(self):
        self.approved_comment_text = True
        self.save()

    def __str__(self):
        return self.comment


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    reply_text = models.CharField(max_length=250)
    reply_created_date = models.DateTimeField(default=timezone.now)
    author_name = models.CharField(max_length=100, null=True, blank=True)



# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
#
# @receiver(post_save, sender=Article)
# def notify_author(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Article Created'
#         body = 'Your article created successfully!'
#         send_from = settings.DEFAULT_FROM_EMAIL
#         send_to = 'albert.li.das@gmail.com'
#         print('email sent')
#         send_mail(subject, body, send_from, [send_to])