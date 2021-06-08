from django.shortcuts import render
from random import randint

from django.utils import timezone

from landing.models import ExpressionHistory, StrHistory, Student
from landing.forms import CalcForm, StrForm, StudentForm


def get_menu_context():
    """
    :return: все адреса с названиями для меню в виде кортежа из словарей
    """
    return [
        {'url': '/', 'label': 'Главная'},
        {'url': '/riddle/', 'label': 'Загадка'},
        {'url': '/answer/', 'label': 'Ответ'},
        {'url': '/multiply/', 'label': 'Умножение'},
        {'url': '/expression/', 'label': 'Выражение'},
        {'url': '/exphistory/', 'label': 'История выражений'},
        {'url': '/calculator/', 'label': 'Какулятор'},
        {'url': '/str2words/', 'label': 'Анализ текста'},
        {'url': '/str_history/', 'label': 'История запросов'},
        {'url': '/clicker/', 'label': 'Симулятор студента'}
    ]


def index(request):
    """
    :param request: запрос
    :return: выдает главную страницу
    """
    context = {'menu': get_menu_context()}
    return render(request, 'index.html', context)


def riddle(request):
    """
    :param request: запрос
    :return:  выдает страницу с загадкой
    """
    context = {'menu': get_menu_context()}
    return render(request, 'riddle.html', context)


def answer(request):
    """
    :param request: запрос
    :return: выдает страницу с ответом на загадку
    """
    context = {'menu': get_menu_context()}
    return render(request, 'answer.html', context)


def multiply(request):
    """
    :param request: запрос, должен включать в себя число для вывода таблицы.
    :return:  выдает страницу с таблицей, если данных нет выдает ошибку
    """
    number = request.GET.get('value', None)
    context = {}
    if (number is None):
        context['has_data'] = False
    else:
        number = int(number)
        context['has_data'] = True
        table = list()
        for i in range(1, 11):
            table.append(str(i) + ' * ' + str(number) + ' = ' + str(number * i))
        context.update({'table': table})
    context['menu'] = get_menu_context()
    return render(request, 'multiply.html', context)


def expression(request):
    """
    :param request: запрос
    :return: выдает страницу с выражением
    """
    nums = list()
    answer = 0
    expr = ''

    for i in range(randint(2, 4)):
        nums.append(randint(10, 100))
        if randint(0, 1) == 1:
            expr += '-' + str(nums[i]) + ' '
            answer -= nums[i]
        else:
            if i == 0:
                expr += str(nums[i]) + ' '
            else:
                expr += '+ ' + str(nums[i]) + ' '
                answer += nums[i]
    expr += '= ' + str(answer)

    record = ExpressionHistory(expression=expr)
    record.save()
    context = {
        'expression': expr,
        'expression_ans': answer,
        'menu': get_menu_context()
    }
    return render(request, 'expression.html', context)


def calculator(request):
    """
    :param request: запрос, для подсчёта суммы должны быть 2 числа(a, b)
    :return: страница с калькулятором
    """
    context = {}

    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            a = form.data['first']
            b = form.data['second']
            context.update({
                'a': a,
                'b': b,
                'c': int(a) + int(b)
            })
            context['has_data'] = True
        else:
            context['error'] = True
        context['form'] = form

    elif request.method == 'GET':
        context['has_data'] = False
        context['form'] = CalcForm()
    context['menu'] = get_menu_context()
    return render(request, 'calculator.html', context)


def exp_history(request):
    """
    :param request: запрос
    :return: выдает страницу с историей выражений
    """
    context = {
        'history': ExpressionHistory.objects.all(),
        'menu': get_menu_context()
    }
    return render(request, 'exphistory.html', context)


def str_history(request):
    """
    :param request: запрос
    :return: выдает историю запросов пользователя
    """
    context = {
        'history': StrHistory.objects.filter(Author=request.user),
        'menu': get_menu_context()
    }
    return render(request, 'str_history.html', context)


def strCount(request):
    """
    :param request: запрос, для анализа текста должен включать текст(Text)
    :return: выдает страницу с аналилзом текста
    """
    context = {}
    if request.method == 'POST':
        form = StrForm(request.POST)
        if form.is_valid():
            string = str(form.data['Text'])
            words = list()
            words_count = 0
            nums = list()
            nums_count = 0

            for word in string.split():
                if word.isdigit():
                    if not (word in nums):
                        nums.append(word)
                        nums_count += 1
                else:
                    if not (word in words):
                        words.append(word)
                        words_count += 1

            record = StrHistory(
                Text=string,
                Words=words_count,
                Nums=nums_count,
                Author=request.user
            )
            record.save()

            context.update({
                'string': string,
                'words': words_count,
                'numbers': nums_count,
                'unique_words': sorted(words),
                'unique_nums': sorted(nums)
            })
            context['has_data'] = True
        else:
            context['error'] = True
        context['form'] = form

    elif request.method == 'GET':
        context['has_data'] = False
        context['form'] = StrForm()
    context['menu'] = get_menu_context()
    return render(request, 'str2words.html', context)


def Clicker(request):
    """
    :param request: запрос, для сохранения на сервер должен включать
    :return: выдает страницу с игрой
    """
    context = {}

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            record = Student(
                HP=form.data['HP'] ,
                IQ=form.data['IQ'],
                FUN=form.data['FUN']
            )
            record.save()
        context['form'] = form

    elif request.method == 'GET':
        context['form'] = StudentForm()

    context['menu'] = get_menu_context()
    return render(request, 'student.html', context)
