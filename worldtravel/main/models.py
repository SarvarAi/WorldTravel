from django.db import models


# Create your models here.


class EmailSubscription(models.Model):
    """
    This model is responsible for keeping track of all emails that are subscribed.
    """

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email подписка'
        verbose_name_plural = 'Email подписки'

    email = models.EmailField(max_length=255, verbose_name='Email')


class PageCategory(models.Model):
    """
    Class for pages with their primary keys
    """

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.page

    page = models.CharField(max_length=255, verbose_name='Страница')


class InfoPages(models.Model):
    """
    This class is responsible for info pages such as about us, contact us,
    our motivation etc.
    """

    def __str__(self):
        return self.page.page

    class Meta:
        verbose_name = 'Страница информации'
        verbose_name_plural = 'Страницы информации'

    page = models.ForeignKey(PageCategory, on_delete=models.CASCADE, verbose_name='Страница')
    information = models.TextField(verbose_name='Информация')
