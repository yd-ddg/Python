from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(r'' , views.index,name = "index")
    path(r'', views.index),
    re_path('^article/(?P<article_id>[0-9]+)/$',
            views.article_page, name="article_page"),
    re_path('^edit/(?P<article_id>[0-9]+)/$',
            views.edit_page, name='edit_page'),
    path(r'edit/action', views.edit_action, name='edit_action'),
]
app_name = "blog_web"
