from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone

class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
  prefectures = [ 
    ("北海道"  ,"北海道"  ),  
    ("青森県"  ,"青森県"  ),  
    ("岩手県"  ,"岩手県"  ),  
    ("宮城県"  ,"宮城県"  ),  
    ("秋田県"  ,"秋田県"  ),  
    ("山形県"  ,"山形県"  ),  
    ("福島県"  ,"福島県"  ),  
    ("茨城県"  ,"茨城県"  ),  
    ("栃木県"  ,"栃木県"  ),  
    ("群馬県"  ,"群馬県"  ),  
    ("埼玉県"  ,"埼玉県"  ),  
    ("千葉県"  ,"千葉県"  ),  
    ("東京都"  ,"東京都"  ),  
    ("神奈川県","神奈川県"),
    ("新潟県"  ,"新潟県"  ),  
    ("富山県"  ,"富山県"  ),  
    ("石川県"  ,"石川県"  ),  
    ("福井県"  ,"福井県"  ),  
    ("山梨県"  ,"山梨県"  ),  
    ("長野県"  ,"長野県"  ),  
    ("岐阜県"  ,"岐阜県"  ),  
    ("静岡県"  ,"静岡県"  ),  
    ("愛知県"  ,"愛知県"  ),  
    ("三重県"  ,"三重県"  ),  
    ("滋賀県"  ,"滋賀県"  ),  
    ("京都府"  ,"京都府"  ),  
    ("大阪府"  ,"大阪府"  ),  
    ("兵庫県"  ,"兵庫県"  ),  
    ("奈良県"  ,"奈良県"  ),  
    ("和歌山県","和歌山県"),
    ("鳥取県"  ,"鳥取県"  ),  
    ("島根県"  ,"島根県"  ),  
    ("岡山県"  ,"岡山県"  ),  
    ("広島県"  ,"広島県"  ),  
    ("山口県"  ,"山口県"  ),  
    ("徳島県"  ,"徳島県"  ),  
    ("香川県"  ,"香川県"  ),  
    ("愛媛県"  ,"愛媛県"  ),  
    ("高知県"  ,"高知県"  ),  
    ("福岡県"  ,"福岡県"  ),  
    ("佐賀県"  ,"佐賀県"  ),  
    ("長崎県"  ,"長崎県"  ),  
    ("熊本県"  ,"熊本県"  ),  
    ("大分県"  ,"大分県"  ),  
    ("宮崎県"  ,"宮崎県"  ),  
    ("鹿児島県","鹿児島県"),
    ("沖縄県"  ,"沖縄県"  ),  
  ]
  email = models.EmailField('メールアドレス', unique=True)
  nickname = models.CharField(("ニックネーム"), max_length=30, blank=True)
  address = models.CharField(("居住地"), choices=prefectures, max_length=4, blank=True)

  is_staff = models.BooleanField(
      ('staff status'),
      default=False,
      help_text=('Designates whether the user can log into this admin site.'),
  )
  is_active = models.BooleanField(
      ('active'),
      default=True,
      help_text=(
          'Designates whether this user should be treated as active. '
          'Unselect this instead of deleting accounts.'
      ),
  )

  objects = UserManager()
  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = []

  class Meta:
      verbose_name = ('user')
      verbose_name_plural = ('users')

  def clean(self):
      super().clean()
      self.email = self.__class__.objects.normalize_email(self.email)