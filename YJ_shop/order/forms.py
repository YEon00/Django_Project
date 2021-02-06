from django import forms
from .models import Order
from product.models import Product
from user.models import YJuser


class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명', widget=forms.HiddenInput
    )
    
    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if quantity and product and user:
            order = Order(
                quantity = quantity,
                product = Product.objects.get(pk=product),
                user = YJuser.objects.get(email=user)
            )
            order.save()
        else:
            self.product = str(product)
            self.add_error('quantity','값이 없습니다.')
            self.add_error('product','값이 없습니다.')


        