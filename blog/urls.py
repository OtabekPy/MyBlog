from django.urls import path
from .views import home, blog, about, maqola

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('maqola/<int:pk>/', maqola),
]
