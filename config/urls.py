"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bis/', include('src.apps.bis.urls'), name="bis_"),
    path('blacklist/', include('src.apps.blacklist.urls'), name="blacklist_"),
    path('boss/', include('src.apps.boss.urls'), name="boss_"),
    path('combat_type/', include('src.apps.combat_type.urls'), name="combat_type_"),
    path('grade/', include('src.apps.grade.urls'), name="grade_"),
    path('loot/', include('src.apps.loot.urls'), name="loot_"),
    path('loot_type/', include('src.apps.loot_type.urls'), name="loot_type_"),
    path('member/', include('src.apps.member.urls'), name="member_"),
    path('roadster/', include('src.apps.roadster.urls'), name="roadster_"),
    path('stuff/', include('src.apps.stuff.urls'), name="stuff_"),
    path('weapon/', include('src.apps.weapon.urls'), name="weapon_"),
]
