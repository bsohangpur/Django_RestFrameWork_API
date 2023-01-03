from django.urls import path

from MainApi import views


urlpatterns = [
    path('languages/', views.LanguageViewSet.as_view()),
    path('projects/', views.ProjectViewSet.as_view()),
    path('images/', views.ProjectImageViewSet.as_view()),
    path('contact/', views.ContactViewSet.as_view()),
    path('services/', views.ServiceViewsSet.as_view()),
    path('skills/', views.SkillViewsSet.as_view()),
]
