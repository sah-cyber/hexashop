from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from categoriya.models import Category


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.PUBLISHED)


class Product(models.Model):


    class Status(models.TextChoices):
        DRAFT = 'DF','DRAFT'
        PUBLISHED = 'PD','PUBLISHED'

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,unique_for_date='publish')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True,null=True)
    stock = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Derc edilme tarixi')
    updated = models.DateTimeField(auto_now=True,verbose_name='Yenilenme tarixi')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering =['-publish']
        indexes = [models.Index(fields=['-publish'])]





    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('homeshop:product_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug,self.id])

