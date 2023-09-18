from django import forms
from store.bulma_mixin import BulmaMixin
from store.models import Order, STATUS,Product,Category, Brand

class OrderEditForm(BulmaMixin, forms.ModelForm):
    address = forms.CharField(label='Изменить адрес')
    status = forms.ChoiceField(label = 'Изменить статус', choices = STATUS)

    class Meta:
        model = Order
        fields = ['address', 'status']


class ProductForm(BulmaMixin, forms.ModelForm):
    name = forms.CharField(label='Имя продукта')
    slug = forms.CharField(label='slug продукта')
    description = forms.CharField(label='Описание')
    price = forms.IntegerField(label='Цена')
    is_new = forms.CharField(widget=forms.CheckboxInput(), label='Новый продукт')
    is_discounted = forms.CharField(widget=forms.CheckboxInput(), label='Скидка')
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    image = forms.ImageField()

    class Meta:
            model = Product
            fields = [
                 'name',
                 'slug',
                 'description',
                 'price',
                 'is_new',
                 'is_discounted',
                 'category',
                 'brand',
                 'image',
            ]




# создайте форму OrderForm(с bulma mixin)
# с полями address - CharField(добавьте placeholder)
# STATUS - ChoiceField(choices=STATUS)

# добавьте class Meta (указать модель и поля)

# создайте вид и шаблонизатор с формой