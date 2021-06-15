from django import forms
from .models import Cinema
class ShowTimeSearchForms(forms.Form):
    movie_name = forms.CharField(max_length=100, label='movie name',
                                required=False)
    available_sales = forms.BooleanField(label="currently available sales",
                                        required=False)
    less_than_10 = '1'
    between_10_and_20 = '2'
    between_20_and_30 = '3'
    more_than_30 = '4'
    choices = (
        ('1', 'less than 10'),
        ('2', 'between 10 and 20'),
        ('3', 'between 20 and 30'),
        ('4', 'more than 30')
    )
    price_levels = forms.ChoiceField(choices=choices,
                                    label='price levels',
                                    required=False)
    cinema = forms.ModelChoiceField(label='cinemas',
                                    queryset=Cinema.objects.all(),
                                    required=False)

    def get_price_boundries(self):
        price_level = self.cleaned_data['price_levels']
        if price_level == ShowTimeSearchForms.less_than_10:
            return None, 10
        elif price_level == ShowTimeSearchForms.between_10_and_20:
            return 10, 20
        elif price_level == ShowTimeSearchForms.between_20_and_30:
            return 20, 30
        elif price_level == ShowTimeSearchForms.more_than_30:
            return 30, None
        else:
            return None, None
