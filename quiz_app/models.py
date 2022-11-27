from django.db import models


class Answer(models.Model):
	text = models.TextField('Текст ответа')
	true_or_false = models.BooleanField('Правильность')
	question = models.ForeignKey('Question', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Ответы'
		verbose_name_plural = 'Ответ'

	def __str__(self):
		return self.text

class Question(models.Model):
	text = models.TextField('Текст вопроса')

	class Meta:
		verbose_name = 'Вопросы'
		verbose_name_plural = 'Вопрос'

	def __str__(self):
		return self.text

class Test(models.Model):
	title = models.CharField('Тема', max_length=255)
	questions = models.ManyToManyField(Question)

	class Meta:
		verbose_name = 'Темы тестов'
		verbose_name_plural = 'Тема тестов'

	def __str__(self):
		return self.title

