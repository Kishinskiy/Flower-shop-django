from django.urls import path
from .views import home, by_rubric
urlpatterns = [
    path('', home, name='home'),
    path('<int:rubric_id>', by_rubric, name='by_rubric'),
]