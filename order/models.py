from goods.models import Goods
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    # 구매자
    customer = models.ForeignKey(User, verbose_name=("customer"), on_delete=models.CASCADE, null=False, default=None)
    # 상품 id
    goods_id = models.ForeignKey(Goods, verbose_name=("goods"), on_delete=models.CASCADE, null=False, default=None)
    # 주소
    address = models.CharField(("ADDRESS"), max_length=50)
    # 수량
    quantity = models.IntegerField(("QUANTITY"))
    # 휴대전화
    sellphone = models.CharField(("phonenumber"), max_length=50,  null=False, default=None)
    customer_name = models.CharField(("customer_name"), max_length=50, null=False, default=None)
    
    class Meta:
        pass

    def __str__(self):
        pass