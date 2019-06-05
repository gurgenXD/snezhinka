from django.db import models


class CallBack(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время заяки')

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'

    def __str__(self):
        return '%s' % self.phone


class FeedBack(models.Model):
    email = models.EmailField(max_length=250, verbose_name='E-mail')
    name = models.CharField(max_length=250, verbose_name='Имя')
    message = models.TextField(verbose_name='Текст сообщения')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время заяки')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return "%s - %s" % (self.email, self.name)