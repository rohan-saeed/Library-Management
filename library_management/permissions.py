from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_librarian:
            if user.has_perm("library_management.add_book"):
                return True
            if user.has_perm("library_management.view_book"):
                return True
            if user.has_perm("library_management.delete_book"):
                return True
            if user.has_perm("library_management.change_book"):
                return True

        if user.is_librarian == False:
            if user.has_perm("library_management.add_book"):
                return True
            if user.has_perm("library_management.view_book"):
                return True
            if user.has_perm("library_management.delete_book"):
                return False
            if user.has_perm("library_management.change_book"):
                return False
        return False
