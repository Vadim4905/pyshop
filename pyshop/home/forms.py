from django.forms import ModelForm

from home.models import Category


class CategoryForm(ModelForm):
    # CamelCase moment тут ще

    class Meta:
        model = Category
        fields = (
            "name",
            "image",
        )
