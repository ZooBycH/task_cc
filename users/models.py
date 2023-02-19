from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Наследуем своего пользователя от django AbstractUser, для авторизации/аутентификации и создания пользователей
    используются библиотеки Djoser и Simple-JWT.
    В условии задачи не до конца понятно, нужна ли необходимость связывать пользователей с компаниями.
    Если потребуется, можно будет расширить данную модель, добавив поле
        company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=True)
        или, если нужна связь с сетью, то
        network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='employees', null=True)
    """
    pass