from django.http import Http404
from django.urls import reverse
from django.utils.http import urlencode
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
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        query_params = (
            "email__icontains",
            "name__icontains",
            "ordering",
            "paginate_by",
        )
        for query_param in query_params:
            if query_param in self.request.GET:
                context_data[query_param] = self.request.GET[query_param]
        query_dict = {
            filter_: self.request.GET[filter_]
            for filter_ in ("email__icontains", "name__icontains")
            if filter_ in self.request.GET
        }
        context_data["query_string"] = urlencode(query_dict)
        return context_data

    def get_ordering(self):
        return self.request.GET.get("ordering") or super().get_ordering()

    def get_paginate_by(self, queryset):
        if (
            "paginate_by" in self.request.GET
            and int(self.request.GET["paginate_by"]) <= 1000
        ):
            return self.request.GET["paginate_by"]
        return super().get_paginate_by(queryset)

    def get_queryset(self):
        filters = ("email__icontains", "name__icontains")
        filter_dict = {}
        for filter_ in filters:
            if filter_ in self.request.GET:
                filter_dict[filter_] = self.request.GET[filter_]
        return super().get_queryset().filter(**filter_dict)


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name_suffix = "_update_form"
