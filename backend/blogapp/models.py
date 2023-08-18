from django.utils import timezone



from django.db import models
class Blog(models.Model):
    blog_title=models.CharField(max_length=50)
    blog_post=models.TextField(max_length=500)
    # author=
    date_published=models.DateTimeField(timezone.now())
    def __str__():
        return self.blogTitle
# Create your models here.
