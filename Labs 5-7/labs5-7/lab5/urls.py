"""lab5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from my_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^orders/', include('my_app.urls')),
    url(r'^orders/', OrdersView.as_view(), name='orders_url'),
    url(r'^^$', main, name='main_url'),
    url(r'^main/', main, name='main_url'),
    url(r'^(?P<id>\d+)', card_info, name='card_info_url'),
    url(r'^db/', db, name='db_url'),
    url(r'^cards/', VcardView.as_view(), name='cards_url'),
    url(r'^creator/',CreatorView.as_view(), name='creator_url'),
    url(r'^registration/', registration, name='registration_url'),
    url(r'^registration2/', registration2, name='registration2_url'),
    url(r'^login/', login, name='login_url'),
    url(r'^success/', success, name='success_url'),
    url(r'^logout/', logout, name='logout_url'),

]
