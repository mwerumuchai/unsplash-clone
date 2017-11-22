from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def display_user():
        user = User.objects.all()

        return user

    class Meta:
        ordering = ['first_name']

class Tags(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.name

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    @classmethod
    def display_tags(cls):
        all_tags = cls.objects.all()
        return all_tags

    @classmethod
    def search_for_tag(cls,search_term):
        tags = cls.objects.filter(name__icontains=search_term)
        return tags

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length = 60)
    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tags)
    upload_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()

    @classmethod
    def get_images(cls):
        gallery = cls.objects.all()
        return gallery

    @classmethod
    def search_by_title(cls,search_term):
        gallery = cls.objects.filter(tags__icontains=search_term)
        return gallery
