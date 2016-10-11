from django.db.models.signals import post_save
from like.models import LikeMixin
from like.models import Like


def after_save_like_handler(sender, **kwargs):
    instance = kwargs['instance']
    obj = instance.item_type.get_object_for_this_type(
        id=int(instance.item_id))
    obj.likes_count += 1
    obj.save()



post_save.connect(after_save_like_handler, Like)
