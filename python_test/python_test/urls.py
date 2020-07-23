"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import (
    ClientList,
    ClientDelete,
    ClientUpdate,
    ClientCreate,
    ClientDetail,
    ClientSearchListView,
    ClientOrderListView,
)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    path("", ClientList.as_view(), name="client_list"),
    path("view/<int:pk>", ClientDetail.as_view(), name="client_view"),
    path("new", ClientCreate.as_view(), name="client_new"),
    path("edit/<int:pk>", ClientUpdate.as_view(), name="client_edit"),
    path("delete/<int:pk>", ClientDelete.as_view(), name="client_delete"),
    path("client_search", ClientSearchListView.as_view(), name="client_search_list_view"),
    path("client_order", ClientOrderListView.as_view(), name="client_order_list_view"),
]
