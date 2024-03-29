# File created at 2022-03-02 14:45:52 UTC

import jwt
from django.conf import settings
from django.test import TestCase
from users.models import User, Roles, Assistant, Admin
from users.test import factories


class TestUserModel(TestCase):

    def setUp(self):
        self.user = factories.UserFactory(email='test@gmail.com', username='test_user')

    def test_email_title(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email address')

    def test_email_max_length(self):
        user = User.objects.get(id=self.user.id)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_email_unique(self):
        user = User.objects.get(id=self.user.id)
        unique = user._meta.get_field('email').unique
        self.assertTrue(unique)

    def test_email_db_index(self):
        user = User.objects.get(id=self.user.id)
        db_index = user._meta.get_field('email').db_index
        self.assertTrue(db_index)

    def test_username_title(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_username_unique(self):
        user = User.objects.get(id=self.user.id)
        unique = user._meta.get_field('username').unique
        self.assertTrue(unique)

    def test_username_max_length(self):
        user = User.objects.get(id=self.user.id)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)

    def test_user_full_name(self):
        user = User.objects.get(id=self.user.id)
        user.first_name = 'John'
        user.last_name = 'Doe'
        full_name = user.get_full_name()
        self.assertEqual(full_name, 'John Doe')

    def test_role_title(self):
        user = User.objects.get(id=self.user.id)
        field_label = user._meta.get_field('role').verbose_name
        self.assertEqual(field_label, 'role')

    def test_role_field_type(self):
        user = User.objects.get(id=self.user.id)
        field_type = user._meta.get_field('role').get_internal_type()
        self.assertEqual(field_type, 'CharField')

    def test_role_choices(self):
        user = User.objects.get(id=self.user.id)
        choices = user._meta.get_field('role').choices
        self.assertEqual(choices, Roles.choices)

    def test_role_default(self):
        user = User.objects.get(id=self.user.id)
        default = user._meta.get_field('role').default
        self.assertEqual(default, Roles.ASSISTANT)

    def test_user_token(self):
        user = User.objects.get(id=self.user.id)
        token = user.token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        self.assertEqual(str(payload['id']), str(user.id))


class TestAssistantModel(TestCase):

    def setUp(self):
        self.assistant = factories.AssistantFactory()

    def test_role_is_assistant(self):
        assistant = Assistant.objects.get(id=self.assistant.id)
        self.assertEqual(assistant.role, Roles.ASSISTANT)

    def test_assistant_profile(self):
        assistant = Assistant.objects.get(id=self.assistant.id)
        self.assertEqual(assistant.profile.__class__.__name__, 'AssistantProfile')
        self.assertEqual(assistant.profile.assistant.id, assistant.id)


class TestAdminModel(TestCase):

    def setUp(self):
        self.admin = factories.AdminFactory()

    def test_role_is_admin(self):
        admin = Admin.objects.get(id=self.admin.id)
        self.assertEqual(admin.role, Roles.ADMIN)
