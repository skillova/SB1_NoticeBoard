from django import forms

from .models import Announcement, Comment


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'price', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
