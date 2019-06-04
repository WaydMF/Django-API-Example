from rest_framework.permissions import BasePermission
from rolepermissions.checkers import has_permission


class LibrarianPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Librarian').exists() or request.user.groups.filter(name='HallManager').exists()


class HallManagerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='HallManager').exists()
