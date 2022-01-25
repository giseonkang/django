from order.models import Order
from django import forms


class OrderForm(forms.ModelForm):

    class Meta:
        
        model = Order

        fields = [
            'customer_name',
            'address',
            'quantity',
            'goods_id',
            'sellphone',
        ]

        labels = {
            'customer_name' : '이름',
            "address" : '주소',
            'quantity' : '수량',
            'sellphone': '휴대전화',
        }

        help_text ={
            'customer_name' : '이름',
            "address" : '주소를 입력해 주세요',
            'quantity' : '수량을 입력해 주세요',
            'sellphone': '휴대전화번호를 입력해 주세요',
        }

        widgets = {
            'goods_id' : forms.HiddenInput(),
        }
    def save(self, **kwargs):
        order = super().save(commit=False)         # 부몽메서드 호출 
        order.customer = kwargs.get('customer', None)
        order.save()
