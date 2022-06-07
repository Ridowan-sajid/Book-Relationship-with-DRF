from django.contrib import admin
from django.urls import path, include
from Book import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('book',views.BookViewSet,basename='book')
router.register('author',views.AuthorViewSet,basename='author')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/',views.BookViewSet.as_view({'get': 'list'}),name='BookView'),
    # path('author/',views.AuthorViewSet.as_view({'get': 'list'}),name='AuthorView'),
    path('',include(router.urls)),
]
