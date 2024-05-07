from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return f"Profile for user{self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Book(models.Model):
    status_book = [
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    title = models.CharField(max_length=250)
    outher = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_outher = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    # bookk = models.UUIDField(default=uuid.uuid4)
    open_book = models.FileField(upload_to='files')
    description = models.TextField()
    views = models.IntegerField(default=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # data = models.DateTimeField(null=True, blank=True)
    # rating = models.RatingField(range=5)
    # rating = models.IntegerField(default=0)
    # rating = models.FloatField(default=0)  # تقييم الكتاب
    # url_book = models.URLField(open_book)
    # bbbb= models.ImageField(upload_to='photos', null=True, blank=True _('first name'))
    def __str__(self):
        return self.title
class chat_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mas = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.mas


# الدردشة
class ChatMessage(models.Model):
       sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
       receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
       message = models.TextField()
       timestamp = models.DateTimeField(auto_now_add=True)