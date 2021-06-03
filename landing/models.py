from django.db import models

# Create your models here.
from django.utils import timezone


class ExpressionHistory(models.Model):
    """
    :param expression: выражение
    """
    expression = models.CharField(max_length=255)


class StrHistory(models.Model):
    """
    :param Date: дата создания записи
    :param Text: текст для анализа
    :param Words: кол-во слов
    :param Nums: кол-во цифр
    :param Author: автор, т.е. тот, кто запросил анализ
    """
    Date = models.DateTimeField(default=timezone.now)
    Text = models.CharField(max_length=1000)
    Words = models.IntegerField()
    Nums = models.IntegerField()
    Author = models.CharField(max_length=256)


class Student(models.Model):
    """
    :param Date: дата создания записи
    :param HP: кол-во очков здоровья
    :param IQ: кол-во очков интеллекта
    :param FUN: кол-во очков радости
    """
    Date = models.DateTimeField(default=timezone.now)
    HP = models.IntegerField(null=True)
    IQ = models.IntegerField(null=True)
    FUN = models.IntegerField(null=True)