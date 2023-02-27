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


class Vacancies(models.Model):
    """
    Information of WorldTravel's vacancies.
    """

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    work_experience = models.CharField(max_length=255, verbose_name='Опыт работы')
    from_salary = models.CharField(max_length=15, verbose_name='Зарплата от', null=True, blank=True)
    to_salary = models.CharField(max_length=15, verbose_name='Зарплата до', null=True, blank=True)
    from_age = models.CharField(max_length=3, verbose_name='Возраст от')
    to_age = models.CharField(max_length=3, verbose_name='Возраст до')
    description = models.TextField(verbose_name='Описание вакансии')
    skills = models.CharField(max_length=255, verbose_name='Навыки')
    education = models.TextField(verbose_name='Образование')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')


class Help(models.Model):
    """
    This class responsible for the help messages,
    in order to register them in database
    """
    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощи'

    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=255, verbose_name='Имя')
    Email = models.EmailField(max_length=255, verbose_name='E-mail')
    Problem = models.TextField(verbose_name='Описание проблемы')


