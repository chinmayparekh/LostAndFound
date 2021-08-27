from django.urls import path
from . import views
from .views import ItemListView, PostCreateView, ItemFoundView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name='findme-home'),
    path('', views.home, name='findme-home'),
    path('found/', views.itemfound, name='findme-found'),
    path('about/', views.about, name='findme-about'),
    path('create/', PostCreateView.as_view(), name='create'),
    # path('create/', views.CreateItemView.as_view(), name='create'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('found/<int:ItemID>', views.found, name='found'), ]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
