from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    air_date = models.IntegerField(null=True, blank=True)
    version = models.CharField(max_length=150, null=True, blank=True, default='5.05, 6.72, 7.55 , 9.00 +')
    category = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=False, unique=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=False, unique=True)

    def __str__(self):
        return self.name


class HeroSection(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    intro = models.CharField(max_length=300, null=True, blank=True)
    image =  models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name