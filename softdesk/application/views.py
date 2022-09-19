from rest_framework.viewsets import ModelViewSet
from application.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from application.models import Project, Contributor, Issue, Comment
from authentication.models import User
from django.shortcuts import render

class ProjectViewset(ModelViewSet):
    """
    A ViewSet for viewing projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save()
        user_email = self.request._user.email
        user = User.objects.get(email=request_user)
        role = "author"
        Contributor.objects.create(
            project=project,
            user=user,
            role=role,
        )


class UserViewset(ModelViewSet):
    """
    A ViewSet for viewing users.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(id=project_id)
        serializer.save(project=project, role='contributor')

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])


class IssueViewset(ModelViewSet):
    """
    A ViewSet for viewing issues.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(id=project_id)
        user_email = self.request._user.email
        user = User.objects.get(email=request_user)
        serializer.save(project=project, author=user)


class CommentViewset(ModelViewSet):
    """
    A ViewSet for viewing issues.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

