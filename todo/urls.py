from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('delete/<str:id>', views.delete, name='delete' ),
    path('check/<str:id>', views.check, name='check' ),
]
