from django.urls import path
from server import views

urlpatterns = [
    path('api/books', views.bookCreateReadAPIView),
    path('api/books/<int:bookId>', views.bookUpdateAPIView),
]