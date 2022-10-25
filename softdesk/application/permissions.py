from rest_framework.permissions import BasePermission, SAFE_METHODS
from application.models import Project, Contributor

class IsContributor(BasePermission):
    def has_permission(self, request, view):
        """
        Allow any user to perform a POST and a GET if the endpoint is /projects/, else it
        allows only its contributors.
        """
        project_id = view.kwargs.get('project_pk', view.kwargs.get('pk'))
        contributors = [contributor.user.id for contributor in Contributor.objects.filter(project=project_id)]
        if project_id is None:
            return True
        elif request.user.id in contributors:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Allow any user to perform a GET.
        Allow only the author of the project to perform a POST, PUT and DEL on the project and its contributors.
        Allow only the author of the object to perform a POST, PUT and DEL.
        """
        if request.method in SAFE_METHODS:
            return True
        elif type(obj) == Project or type(obj) == Contributor:
            project_id = view.kwargs.get('project_pk', view.kwargs.get('pk'))
            try:
                Contributor.objects.get(project=project_id, user=request.user.id, role='author')
                return True
            except Contributor.DoesNotExist:
                return False
        elif obj.author.id == request.user.id:
            return True
        return False


class IsAuthorizedToAddContributor(BasePermission):
    def has_permission(self, request, view):
        """
        Allow any user to perform a GET.
        Allow only the author of the project to perform a POST.
        """
        project_id = view.kwargs.get('project_pk')
        try:
            author = Contributor.objects.get(project=project_id, role='author')
            author_id = author.user.id
        except Contributor.DoesNotExist:
            author_id = None
        if request.method in SAFE_METHODS:
            return True
        elif author_id == request.user.id:
            return True
        return False
        
    def has_object_permission(self, request, view, obj):
        """
        Forbid any user to perform a GET and a PUT.
        Allow any user to perform a DEL.
        """
        if request.method in ['GET', 'PUT']:
            return False
        return True
        