from django.http import Http404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from main.forms import UserCreateForm, UserUpdateForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    template_name_suffix = "_create_form"


class UserDeleteView(DeleteView):
    model = User

    def get(self, request, *args, **kwargs):
        raise Http404

    def get_success_url(self):
        return reverse("user-list")


class UserDetailView(DetailView):
    model = User


class UserListView(ListView):
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(object_list=object_list, **kwargs)
        lookups = ("email__icontains", "name__icontains")
        for lookup in lookups:
            if lookup in self.request.GET:
                context_data[lookup] = self.request.GET[lookup]
        return context_data

    def get_ordering(self):
        return self.request.GET.get("ordering") or super().get_ordering()

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by") or super().get_paginate_by(queryset)

    def get_queryset(self):
        lookups = ("email__icontains", "name__icontains")
        filter_ = {}
        for lookup in lookups:
            if lookup in self.request.GET:
                filter_[lookup] = self.request.GET[lookup]
        return super().get_queryset().filter(**filter_)


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name_suffix = "_update_form"
