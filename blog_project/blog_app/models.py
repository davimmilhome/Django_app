from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='publicated')

class Post(models.Model):

    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250)
    author  = models.ForeignKey(User,
                               on_delete= models.CASCADE)
    content     = models.TextField()
    publicated = models.DateTimeField(default=timezone.now)
    criate      = models.DateTimeField(auto_now_add=True)
    altered     = models.DateTimeField(auto_now=True)
    status      = models.CharField(max_length=10,choices=STATUS,default='rascunho')


    objects     = models.Manager()
    published   = PublishedManager()

    class Meta:
        ordering = ('-publicated',)

    def __str__(self):
        return self.title