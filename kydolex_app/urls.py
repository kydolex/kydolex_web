from django.urls import path
from kydolex_app import views

urlpatterns = [
    path('', views.Kydolex_View.as_view(), name='index'),
    path('index', views.Kydolex_View.as_view(), name='index'),
    path('blog/', views.Kydolex_Blog_View.as_view(), name='blog'),
    path('about/', views.Kydolex_About_View.as_view(), name='about'),
    path('service/', views.Kydolex_Service_View.as_view(), name='service'),
    path('designlist/', views.Kydolex_designlist_View.as_view(), name='designlist'),
    path('rate/', views.Kydolex_Rate_View.as_view(), name='rate'),
    path('contact/', views.Kydolex_Contact_View.as_view(), name='contact'),
    path('none/', views.Kydolex_none_View.as_view(), name='none'),
]