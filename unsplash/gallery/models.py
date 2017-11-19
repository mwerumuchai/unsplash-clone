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

    def __str__(self):
        return self.name

class Gallery(models.Model):
    location = models.CharField(max_length = 60)
    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tags)
    upload_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to = 'photos/')

    @classmethod
    def new_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(upload_date__date = today)
        return gallery

    @classmethod
    def trending_now(cls, date):
        gallery = cls.objects.filter(upload_date__date = date)
        return gallery

    @classmethod
    def search_by_title(cls,search_term):
        gallery = cls.objects.filter(title__icontains=search_term)
        return gallery

    @classmethod
    def get_images(cls):
        gallery = cls.objects.all()
        return gallery



    def __str__(self):
        return self.location
