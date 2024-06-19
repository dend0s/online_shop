from django import forms
from .models import Order

DELIVERY_METHODS = [
    ("0", "Самовывоз"),
    ("500", "Доставка по городу и области +500 рублей"),
    # ("1000", "Доставка по РФ +1000 рублей"),
]

PAYMENT_METHODS = [
    ("Offline", "При получении"),
    ("Online", "Онлайн банковской картой"),
]


class OrderCreateForm(forms.ModelForm):
    delivery = forms.ChoiceField(choices=DELIVERY_METHODS, widget=forms.RadioSelect())
    pay_method = forms.ChoiceField(choices=PAYMENT_METHODS, widget=forms.RadioSelect())

    class Meta:
        model = Order
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'city', 'address', 'delivery', 'pay_method']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.capitalize()

    def clean_city(self):
        clean_city = self.cleaned_data['city']
        return clean_city.capitalize()

    def clean_address(self):
        address = self.cleaned_data['address']
        return address.capitalize()
