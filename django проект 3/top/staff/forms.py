from django import forms
from store.bulma_mixin import BulmaMixin
from store.models import Order, STATUS


class OrderEditForm(BulmaMixin, forms.ModelForm):
    address = forms.CharField(label='Изменить адрес')
    status = forms.ChoiceField(label='Изменить статус', choices=STATUS)

    class Meta:
        model = Order
        fields = ['address', 'status']
