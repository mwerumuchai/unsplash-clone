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

    def __str__(self):
        return self.location
