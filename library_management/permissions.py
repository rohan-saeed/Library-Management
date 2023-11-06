from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and (request.user.is_librarian or request.user.is_staff)
