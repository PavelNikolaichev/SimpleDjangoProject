from django import forms


class CalcForm(forms.Form):
    """
    Форма для калькулятора
    :param first: первое число(мин=-9999, макс=9999)
    :param second: второе число(мин=-9999, макс=9999)
    """
    first = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Первое число', min_value=-9999, max_value=9999, required=True
    )
    second = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Второе число', min_value=-9999, max_value=9999, required=True
    )


class StrForm(forms.Form):
    """
    Форма для входных данных на анализ текста
    :param Text: текст(максимальное кол-во знаков = 1000)
    """
    Text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Текст', min_length=0, max_length=1000, required=True
    )


class StudentForm(forms.Form):
    """
    Форма для игры на JS - симулятора студента
    :param HP: кол-во очков здоровья(макс=100)
    :param IQ: кол-во очков интеллекта(макс=100)
    :param FUN: кол-во очков радости(макс=100)
    """
    HP = forms.IntegerField(min_value=0, max_value=100, required=True)
    IQ = forms.IntegerField(min_value=0, max_value=100, required=True)
    FUN = forms.IntegerField(min_value=0, max_value=100, required=True)
