from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('quotes', views.quotes),
    path('write_quote', views.write_quote),
    path('users/<int:id>', views.user_profile),
    path('favorite/<int:id>', views.favorite),
    path('unfavorite/<int:id>', views.unfavorite),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('edit_quote/<int:id>', views.edit_quote),
]
