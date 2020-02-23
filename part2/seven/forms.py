from django.forms import Form, CharField, TextInput
from django.core import validators


class SevenForm(Form):
    numbers = CharField(
        widget=TextInput(
            attrs={'class': 'input'}
        ),
        validators=[validators.validate_comma_separated_integer_list]
    )