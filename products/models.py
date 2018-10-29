from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    url=models.URLField()
    icon=models.ImageField(upload_to='images/')
    image=models.ImageField(upload_to='images/')
    votes=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def date_pretty(self):
        return self.date.strftime('%b %e %T')
