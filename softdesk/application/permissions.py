from rest_framework.permissions import BasePermission, SAFE_METHODS
from application.models import Project, Contributor

class IsContributor(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk', view.kwargs.get('pk'))
        contributors = [contributor.user.id for contributor in Contributor.objects.filter(project=project_id)]
        if project_id is None:
            return True
        elif request.user.id in contributors:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        print(type(obj))
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