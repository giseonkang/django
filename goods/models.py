from goods.Validators import validate_score
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Goods(models.Model):
    # 상품명
    name = models.CharField(("NAME"), max_length=50)
    # 썸네일
    thumbnail = models.ImageField(("THUMBNAIL"), upload_to='photos/')
    # 상품설명
    goods_content = models.TextField(("CONTENT"))
    # 재고
    stock = models.IntegerField(("STOCK"))
    # 가격
    price = models.IntegerField("PRICE", default=None)
    # 관리자
    staff = models.ForeignKey(User, verbose_name="STAFF", on_delete=models.CASCADE, null=False, default=None)

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods:detail', args=(self.id,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
        
    def save(self, *args, **kwargs):
        # 필드 조정 필요시 작성
        super().save(*args, **kwargs)


class Review(models.Model):
    # 리뷰 쓴 사람
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # 상품
    goods = models.ForeignKey("Goods", on_delete=models.CASCADE, blank=True, null=True)
    # 내용
    content = models.TextField(("content"))
    # 별점
    score = models.FloatField(("score"), default=None, null=True, validators=[validate_score])

    class Meta:
        pass

    def __str__(self):
        self.content