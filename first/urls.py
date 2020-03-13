"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from index.views import *
from demand.views import *

urlpatterns = [
    path('', login_view.as_view()),
    path('admin/', admin.site.urls),
    path("register", register_view.as_view()),
    path("upload", uploadView.as_view()),
    path("lookupall", lookupall.as_view()),
    path("lookup0", lookup0.as_view()),
    path("lookup1", lookup1.as_view()),
    path("lookup2", lookup2.as_view()),
    path("changes", changeView.as_view()),
    path("delete", deleteView.as_view()),
]
