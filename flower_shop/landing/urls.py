from django.urls import path
from .views import home, by_rubric, BbCreateView
urlpatterns = [
    path('', home, name='home'),
    path('<int:rubric_id>', by_rubric, name='by_rubric'),
    path('create/', BbCreateView.as_view(), name='create'),
]