from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name="작성자")
    
    title = models.CharField(max_length=100, verbose_name="제목")
    message = models.TextField(verbose_name="내용")
    image = models.ImageField(upload_to='post_images/', blank=True)

    # 카테고리가 삭제되도 관련된 Post는 그대로 유지, category 필드는 NULL로 설정
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL,
         blank=True, null=True,
         related_name="category_posts", verbose_name='카테고리'
         )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

