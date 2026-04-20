from django.db.models import BooleanField
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product

class StyleFormMixin:
    """Класс стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    """Класс формы создания/изменения товара"""

    list_forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                            "радар"]
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def clean_name(self):
        """Метод проверки отсутствия запрещенных слов в названии при создании/редактировании товара"""
        name = self.cleaned_data.get('name')
        for word in self.list_forbidden_words:
            if word in name:
                raise ValidationError(f'В названии товара нельзя использовать {word}')
        return name

    def clean_description(self):
        """Метод проверки отсутствия запрещенных слов в описании при создании/редактировании товара"""
        description = self.cleaned_data.get('description')
        for word in self.list_forbidden_words:
            if word in description:
                raise ValidationError(f'В описании товара нельзя использовать {word}')
        return description

    def clean_price(self):
        """Метод проверки цены создаваемого/редактироваемого товара на положительность"""
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена товара должна быть положительной')
        return price

