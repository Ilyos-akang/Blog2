from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

class Article(models.Model):
    title=models.CharField(max_length=200)
    sumary=models.CharField(max_length=200,blank=True)
    body=RichTextField()
    photo=models.ImageField(upload_to='images/',blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.id)])
    
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    comment=models.CharField(max_length=200)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )


    def __str__(self):
        words=self.comment.split()
        if len(words) > 2:
            return f"{" ".join(words[:2])}..."
        return self.comment
    

    def get_absolute_irl(self):
        return reverse('article_list')