from goods.models import Review
from django import forms

class ReviewForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        
        model = Review
        fields = [
            'content',
            'goods',
        ]
        labels = {
            'content' : '',
        }

        help_text ={
            'content' : '',
        }

        widgets = {
            'goods' : forms.HiddenInput(),
        }
    def save(self, **kwargs):
        review = super().save(commit=False)         # 부모메서드 호출 
        review.writer = kwargs.get('writer', None)
        review.save()