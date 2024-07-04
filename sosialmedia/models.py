from django.db import models

class SosialMedia(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    url_inst = models.URLField(blank=True,verbose_name='Instagram')
    url_face = models.URLField(blank=True,verbose_name='Facebook')
    url_teleq = models.URLField(blank=True,verbose_name='Telegram')
    sosial_image = models.ImageField(upload_to='sosial_media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
