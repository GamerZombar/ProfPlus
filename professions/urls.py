from django.urls import path


from . import views

urlpatterns = [
    path('', views.ProfessionView.as_view(), name='index'),
]