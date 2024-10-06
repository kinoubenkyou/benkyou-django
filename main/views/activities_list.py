from django.views.generic import ListView


class ActivitiesListView(ListView):
    form_class = None
    ordering = ("-timestamp",)
    paginate_by = 10

    def __init__(self, *args, **kwargs):
        self.form = None
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.form = self.form_class(data=self.request.GET)
        self.form.is_valid()
        return super().get(request, *args, **kwargs)

    def get_ordering(self):
        return self.form.cleaned_data.get("sort_by") or super().get_ordering()

    def get_paginate_by(self, queryset):
        return self.form.cleaned_data.get("per_page") or super().get_paginate_by(
            queryset,
        )

    def get_queryset(self):
        if not self.form.is_valid():
            return self.queryset.none()
        return (
            super()
            .get_queryset()
            .select_models("user")
            .filter(
                **{
                    key: value
                    for key, value in self.form.cleaned_data.items()
                    if value and key not in ("per_page", "sort_by")
                },
            )
        )

    def get_context_data(self, **kwargs):
        return super().get_context_data(form=self.form, **kwargs)
