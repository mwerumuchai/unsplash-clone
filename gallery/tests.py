from django.test import TestCase
from .models  import User, Gallery, Tags

# Class user tests
class UserTestClass(TestCase):
    def setUp(self):
        self.mweru = User(first_name = 'Mweru', last_name = 'Muchai', email = 'mwerumu@gmail.com', phone_number = '')

         # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_gallery= Gallery(location = 'Test Nairobi',user = self.mweru)
        self.new_gallery.save()

        self.new_gallery.tags.add(self.new_tag)

    def tearDown(self):
        User.objects.all().delete()
        Gallery.objects.all().delete()
        Tags.objects.all().delete()

# testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mweru,User))

    def test_save_method(self):
        self.mweru.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

    # testing delete method
    def test_delete_method(self):
        self.mweru.save_user()
        users = User.objects.all()
        self.mweru.delete_user()
        self.assertTrue(len(users) == 0)

    def test_display_method(self):
        self.mweru.save_user()
        users = User.objects.all()
        self.assertTrue(User.display_user())
