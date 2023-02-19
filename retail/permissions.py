from rest_framework.permissions import BasePermission


class IsActivePermission(BasePermission):
    """
    Создаем класс для доступа только активных пользователей. Хотя вроде и без него все работает как надо.
    """
    message = "This user is not active. Contact administrator."

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
