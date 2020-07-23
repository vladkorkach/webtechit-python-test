import operator
from functools import reduce
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Client


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    fields = [
        "name",
        "street",
        "suburb",
        "postcode",
        "state",
        "contact_name",
        "email",
        "phone",
    ]
    success_url = reverse_lazy("client_list")


class ClientUpdate(UpdateView):
    model = Client
    fields = [
        "name",
        "street",
        "suburb",
        "postcode",
        "state",
        "contact_name",
        "email",
        "phone",
    ]
    success_url = reverse_lazy("client_list")


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy("client_list")


class ClientSearchListView(ClientList):

    def get_queryset(self):
        result = super(ClientSearchListView, self).get_queryset()

        query = self.request.GET.get("q")
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_, (Q(name__icontains=q) for q in query_list))
                | reduce(operator.and_, (Q(email__icontains=q) for q in query_list))
                | reduce(operator.and_, (Q(phone__icontains=q) for q in query_list))
                | reduce(operator.and_, (Q(suburb__icontains=q) for q in query_list))
            )

        return result


class ClientOrderListView(ClientList):

    def get_queryset(self):
        result = super(ClientOrderListView, self).get_queryset()

        field = self.request.GET.get("q")
        if field:
            result = result.order_by(field)

        return result
