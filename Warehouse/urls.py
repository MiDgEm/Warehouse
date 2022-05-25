from firstapp import views
from django.urls import path


urlpatterns = {
    path('find/', views.find),
    path('find/edit/<int:id>/', views.edit),
    path('edit/<int:id>/', views.edit),
    path('find/edit/<int:id>/delete/', views.delete),
    path('edit/<int:id>/delete/', views.delete),
    path('add/', views.add),
    path('document/', views.createDocumentDOCX),
    path('', views.index),
}
