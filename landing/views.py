from django.shortcuts import render
from random import randint

from django.utils import timezone
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import ExpressionHistory, StrHistory, Student
from .forms import CalcForm, StrForm, StudentForm


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


class IndexView(TemplateView):
    """
    View-class для рендера главной страницы сайта
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu_context()
        context['title'] = 'Главная'
        return context


class RiddleView(TemplateView):
    """
    View-class для рендера страницы с загадкой
    """
    template_name = 'riddle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu_context()
        context['title'] = 'Загадка'
        return context


class AnswerView(TemplateView):
    """
    View-class для рендера страницы с ответом на загадку
    """
    template_name = 'answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu_context()
        context['title'] = 'Ответ на загадку'
        return context


class MultiplyView(TemplateView):
    """
    View-class для рендера страницы с таблицей умножения числа number от 1 до 10
    """
    template_name = 'multiply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu_context()
        number = self.request.GET.get('value', None)

        if number is None or not str(number).isnumeric():
            context.update({'has_data': False})
        else:
            context.update({'has_data': True})
            table = list()

            for i in range(1, 11):
                table.append(str(i) + ' * ' + str(number) + ' = ' + str(number * i))

            context.update({'table': table, 'title': 'Умножение'})

        return context


class ExpressionView(TemplateView):
    """
    View-class для рендера страницы со случайно сгенерированным выражением и сохранением его в БД
    """
    template_name = 'expression.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer = 0
        expr = ''

        for i in range(randint(2, 4)):
            num = randint(-100, 100)
            if num < 0:
                expr += '-' + str(num) + ' '
                answer -= num
            else:
                if i == 0:
                    expr += str(num) + ' '
                else:
                    expr += '+ ' + str(num) + ' '
                    answer += num
        expr += '= ' + str(answer)

        record = ExpressionHistory(expression=expr)
        record.save()
        context.update({
            'expression': expr,
            'expression_ans': answer,
            'menu': get_menu_context()
        })
        return context


class CalculatorView(View):
    """
    View-class для рендера страницы с калькулятором суммы
    """
    def get(self, request):
        """
        Функция, которая обрабатывается при получении GET-запроса
        :param request: Запрос
        :return: Рендер веб-страницы
        """
        context = {
            'menu': get_menu_context(),
            'has_data': False,
            'form': CalcForm()
        }
        return render(self.request, 'calculator.html', context)

    def post(self, request, *args, **kwargs):
        """
        Функция, которая обрабатывается при получении POST-запроса
        :param request: Запрос
        :return: Рендер веб-страницы
        """
        context = {'menu': get_menu_context()}
        form = CalcForm(self.request.POST)

        if form.is_valid():
            a = form.data['first']
            b = form.data['second']

            context.update({
                'a': a,
                'b': b,
                'c': int(a) + int(b),
                'has_data': True
            })
        else:
            context['error'] = True

        context['form'] = form
        return render(self.request, 'calculator.html', context)


class ExpressionHistoryView(ListView):
    """
        View-class для страциы с историей выражений на основе модели ExpressionHistory
    """
    model = ExpressionHistory
    template_name = 'expression_history.html'

    def get_context_data(self, **kwargs):
        """
        Получение контекста страницы
        :param kwargs: Дополнительные аргументы
        :return: Контекст
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'menu': get_menu_context(),
            'title': 'История выражений'
        })
        return context


class StrHistoryView(ListView):
    """
    View для рендера истории запросов на анализ текста
    :param request: запрос
    :return: выдает историю запросов пользователя
    """
    model = StrHistory
    template_name = 'str_history.html'

    def get_context_data(self, **kwargs):
        """
        Получение контекста страницы
        :param kwargs: дополнительные аргументы
        :return: контекст
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'menu': get_menu_context(),
            'title': 'История запросов'
        })
        return context


def strCount(request):
    """
    View для рендера анализа текста
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
    return render(request, 'landing/templates/str2words.html', context)


def Clicker(request):
    """
    View для игры на JS - симулятор студента
    :param request: запрос, для сохранения на сервер должен включать
    :return: выдает страницу с игрой
    """
    context = {}

    # TODO: Loading from DB
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            record = Student(
                HP=form.data['HP'],
                IQ=form.data['IQ'],
                FUN=form.data['FUN']
            )
            record.save()
        context['form'] = form

    elif request.method == 'GET':
        context['form'] = StudentForm()

    context['menu'] = get_menu_context()
    return render(request, 'student.html', context)
