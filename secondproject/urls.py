from django.contrib import admin
from django.urls import path, include
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),

    # path('portfolio/home', portfolio.views.home, name='home'),
    # path('portfolio/post/<int:post_id>/', portfolio.views.detail, name='detail'),
    # path('portfolio/post/new/', portfolio.views.post_new, name='new'),
]
