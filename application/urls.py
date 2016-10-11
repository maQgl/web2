"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from rest_framework import routers
from client.views import ClientViewSet
from chat.views import ChatViewSet
from community.views import CommunityViewSet
from comment.views import CommentViewSet
from feed.views import EventViewSet
from friendship.views import FriendshipViewSet
from like.views import LikeViewSet
from message.views import MessageViewSet
from photo.views import PhotoViewSet
from post.views import PostViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'communities', CommunityViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed', EventViewSet)
router.register(r'friendships', FriendshipViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
