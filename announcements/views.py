from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, \
    DeleteView

from .forms import AnnouncementForm
from .models import Announcement


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


class AnnouncementDetailView(DetailView):
    model = Announcement


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = reverse_lazy('announcements:list')
