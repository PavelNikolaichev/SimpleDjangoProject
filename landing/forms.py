from django import forms


class CalcForm(forms.Form):
    """
    :param first: первое число(мин=-9999, макс=9999)
    :param second: второе число(мин=-9999, макс=9999)
    """
    first = forms.IntegerField(label='Первое число', min_value=-9999, max_value=9999, required=True)
    second = forms.IntegerField(label='Второе число', min_value=-9999, max_value=9999, required=True)


class StrForm(forms.Form):
    """
    :param Text: текст(максимальное кол-во знаков = 1000)
    """
    Text = forms.CharField(label='Текст', min_length=0, max_length=1000, required=True)


class StudentForm(forms.Form):
    """
    :param HP: кол-во очков здоровья(макс=100)
    :param IQ: кол-во очков интеллекта(макс=100)
    :param FUN: кол-во очков радости(макс=100)
    """
    HP = forms.IntegerField(min_value=0, max_value=100, required=True)
    IQ = forms.IntegerField(min_value=0, max_value=100, required=True)
    FUN = forms.IntegerField(min_value=0, max_value=100, required=True)
