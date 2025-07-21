from django.db import models
#One-to-Many
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Song(models.Model):
    title=models.CharField(max_length=100)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')
    duration = models.IntegerField()
# on_delete=models.CASCADE: If a singer is deleted, all their songs are deleted too.
    def __str__(self):
        return self.title