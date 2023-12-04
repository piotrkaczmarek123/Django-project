from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    login_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} - {self.id}"
    
class Note(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.content}"
    
    def is_longer_then(self ,min_lenght):
        return len(self.content) > min_lenght