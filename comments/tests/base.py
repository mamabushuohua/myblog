

from django.apps import apps
from django.test import TestCase

from blog.models import Category, Post
from users.models import User


class CommentDataTestCase(TestCase):
    def setUp(self):
        apps.get_app_config("haystack").signal_processor.teardown()
        self.user = User.objects.create_superuser(
            username="admin", email="admin@hellogithub.com", password="admin"
        )
        self.cate = Category.objects.create(name="测试")
        self.post = Post.objects.create(
            title="测试标题", body="测试内容", category=self.cate, author=self.user,
        )
