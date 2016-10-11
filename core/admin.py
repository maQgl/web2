from django.contrib import admin
from chat.models import Chat
from client.models import Client
from comment.models import Comment
from community.models import Community
from feed.models import Event
from friendship.models import Friendship
from like.models import Like
from message.models import Message
from photo.models import Photo
from post.models import Post

admin.site.register(Chat)
admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Event)
admin.site.register(Friendship)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Photo)
admin.site.register(Post)
