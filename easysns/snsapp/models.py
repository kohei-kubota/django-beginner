# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
# from django.utils import timezone


class SnsModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=100)
  # 画像をアップロード時にはpillowライブラリが使われるので、pipでインストールする必要あり
  images = models.ImageField(upload_to='') # どこのディレクトリに画像をアップロードするかの設定
  # 前提としてブランクの時にはどうするかの設定をsettings.pyに書き込む必要あり
  good = models.IntegerField()
  read = models.IntegerField()
  readtext = models.CharField(max_length=200)


 
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password):
#         if not email:
#             raise ValueError('Users must have an email address')
         
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
         
#     def create_superuser(self, email, password):
#         user = self.create_user(email=email, password=password)
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
 
# class MyUser(AbstractBaseUser):
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
     
#     email = models.EmailField(unique=True, max_length=255)
#     username = models.CharField(max_length=150, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
     
#     objects = MyUserManager()