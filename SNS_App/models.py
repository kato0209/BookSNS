from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models
from django.core.files.base import ContentFile
from sorl.thumbnail import get_thumbnail, delete
from django.utils import timezone
import uuid
from SNS_project import settings

class CustomUserManager(UserManager):
    use_in_migrations = True
 
    def _create_user(self,email, username, password, **extra_fields):
        
        if not email:
            raise ValueError('email must be set')

        if not username:
            raise ValueError('username must be set')

        if not password:
            raise ValueError('password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
 
        return user
 
    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email=None, username=None ,password=None, **extra_fields):
 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
 
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
 
        return self._create_user(email, username, password, **extra_fields)


class BookData(models.Model):
    ISBNcode=models.CharField(primary_key=True,max_length=30)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=30)
    itemPrice=models.CharField(max_length=30)
    itemUrl=models.CharField(max_length=100)
    imageUrl=models.CharField(max_length=100)

class CustomUser(AbstractUser):

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=10, blank=False)
    profile=models.TextField(max_length=150,blank=True,null=True)
    ProfileImage=models.ImageField(upload_to='',default=settings.Default_image)
    reserved_books = models.ManyToManyField(BookData, through='ReserveRegistration', related_name='reserved_books')
    finished_books = models.ManyToManyField(BookData, through='FinishRegistration', related_name='finished_books')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class ReserveRegistration(models.Model):
    book = models.ForeignKey('BookData', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    registered_at=models.DateTimeField(default=timezone.now)

class FinishRegistration(models.Model):
    book = models.ForeignKey('BookData', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    registered_at=models.DateTimeField(default=timezone.now)


class TweetModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now,blank=True)
    content=models.TextField()
    user=models.ForeignKey(CustomUser,verbose_name='紐づくユーザー',on_delete=models.CASCADE,blank=True)
    rating=models.IntegerField()
    book=models.ForeignKey(BookData,verbose_name='紐づく本',on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.content[:10]


class Comment(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text=models.TextField(max_length=150)
    tweet=models.ForeignKey(TweetModel,verbose_name='紐づくツイート',on_delete=models.CASCADE)

class Like(models.Model):
    tweet=models.ForeignKey(TweetModel,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE,null=True)

class Connection(models.Model):
    following = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE,null=True)
    followed = models.ForeignKey(CustomUser, related_name='followed', on_delete=models.CASCADE,null=True)

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(default=timezone.now)
    room_member = models.ManyToManyField(
        'CustomUser',
        through='Entries',
        )

class Entries(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    joined_at=models.DateTimeField(default=timezone.now)

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Room,blank=True,null=True,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    

