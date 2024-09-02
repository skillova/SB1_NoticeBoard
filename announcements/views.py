from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, \
    DeleteView
from django.views.generic.edit import FormMixin

from .forms import AnnouncementForm, CommentForm
from .models import Announcement, Comment


# Create your views here.
class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    success_url = reverse_lazy('announcements:list')

    def form_valid(self, form):
        if form.is_valid():
            formset = form.save(commit=False)
            formset.author = self.request.user
            formset.save()
        return super().form_valid(form)


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    success_url = reverse_lazy('announcements:list')


class AnnouncementListView(ListView):
    model = Announcement


class AnnouncementDetailView(FormMixin, DetailView):
    model = Announcement
    form_class = CommentForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('announcements:view', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ad = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = reverse_lazy('announcements:list')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment:list')

    def form_valid(self, form):
        post = form.save()
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comment:list')


class CommentListView(ListView):
    model = Comment


class CommentDetailView(DetailView):
    model = Comment


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment:list')
