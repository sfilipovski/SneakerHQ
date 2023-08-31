from django import forms
from .models import Sneaker

SNEAKER_MODELS = [
    ("Nike", "Nike"),
    ("Adidas", "Adidas"),
    ("Reebok", "Reebok"),
    ("Puma", "Puma"),
    ("Converse", "Converse"),
]

SNEAKER_SIZES = [
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
]

SNEAKER_COLORS = [
    ("White", "White"),
    ("Black", "Black"),
    ("Red", "Red"),
    ("Gray", "Gray"),
    ("Light Blue", "Light Blue"),
]


class SneakerForm(forms.ModelForm):
    size = forms.TextInput(attrs={'class': 'form-control'})
    image = forms.ImageField()

    class Meta:
        model = Sneaker
        fields = ('name', 'model', 'price', 'size', 'color', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}, choices=SNEAKER_MODELS),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

            'color': forms.Select(attrs={'class': 'form-control'}, choices=SNEAKER_COLORS),
        }
