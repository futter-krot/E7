from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from ads.forms import AddPostForm, AddTagForm, AddCommentForm
from ads.models import Ad, Comment, Tag


class AdView(ListView):
    model = Ad
    template_name = "index.html"
    context_object_name = "ads"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'home'
        return context


class AddAd(CreateView):
    form_class = AddPostForm
    template_name = "add.html"
    success_url = reverse_lazy("ads:ad-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'hole'
        return context


class AdDetail(DetailView):
    model = Ad
    template_name = "detail.html"
    context_object_name = "det"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(ad=context['object']).count()
        context["tags"] = Tag.objects.filter(ad=context['object']).count()
        return context


class AddComment(CreateView):
    form_class = AddCommentForm
    template_name = "add_comment.html"

    def get_success_url(self):
        return reverse_lazy('ads:ad-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form, **kwargs):
        form.instance.ad_id = self.kwargs['pk']
        return super().form_valid(form)


class AddTag(CreateView):
    form_class = AddTagForm
    template_name = "add_tag.html"

    def get_success_url(self):
        return reverse_lazy('ads:ad-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form, **kwargs):
        form.instance.ad_id = self.kwargs['pk']
        return super().form_valid(form)


def get_ad(request, pk):
    current = Ad.objects.get(id=pk)
    return render(request, 'get.html', {'current': current})
