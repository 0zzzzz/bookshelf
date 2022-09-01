from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class BelongsToUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser
