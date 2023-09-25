from django import forms

from catalog.models import Product, Version

FORBIDDEN_PRODUCTS = [
	'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class StyleFormMixin:
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

	class Meta:
		model = Product
		fields = '__all__'

	def clean_name(self):
		cleaned_data = self.cleaned_data['name']
		for word in FORBIDDEN_PRODUCTS:
			if word in cleaned_data.lower():
				raise forms.ValidationError('Продукт из списка запретных')
		return cleaned_data


class VersionForm(forms.ModelForm):

	class Meta:
		model = Version
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field_name in ('version_number', 'version_name'):
				field.widget.attrs['class'] = 'form-control'
