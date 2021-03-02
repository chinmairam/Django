from django.db import models

# Create your models here.


class User_Profile(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField(default=None)
    # display_picture = models.ImageField(upload_to='tmp')
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ', ' + self.lname + ', ' + str(self.age)
