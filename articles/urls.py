from   django.urls import path
from .views import ArticleViewList ,ArticUpdateleView , ArticleDeleteView , ArticDetailleView ,ArticleCreateView
urlpatterns=[
        path('<int:pk>/edit/',ArticUpdateleView.as_view(),name='article_edit'),
        path('<int:pk>/',ArticDetailleView.as_view(),name='article_detail'),
        path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
        path('new/',ArticleCreateView.as_view(),name='article_new'),
        path("",ArticleViewList.as_view(),name='article_list'),
]