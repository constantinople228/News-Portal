from django.urls import path
from .views import (PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, upgrade_me, logout_user,
                    IndexView, CategoryView, subscribe)

urlpatterns = [
   path('news/', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='post_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('user_page/', IndexView.as_view(), name='user_page'),
   path('logout/user', logout_user, name='logout_user'),
   path('category/<int:pk>', CategoryView.as_view(), name='category_list'),
   path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
]
