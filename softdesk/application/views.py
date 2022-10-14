from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from application.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from application.models import Project, Contributor, Issue, Comment
from application.permissions import IsContributor, IsAuthorizedToAddContributor
from authentication.models import User
from django.shortcuts import render

class ProjectViewset(ModelViewSet):
    """
    A ViewSet for viewing projects.
    """
    permission_classes = [IsAuthenticated & IsContributor]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save()
        user_email = self.request._user.email
        user = User.objects.get(email=user_email)
        contributor = Contributor(
            project=project,
            user=user,
            role="author",
        )
        contributor.save()


class UserViewset(ModelViewSet):
    """
    A ViewSet for viewing users.
    """
    permission_classes = [IsAuthenticated & IsContributor & IsAuthorizedToAddContributor]
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
    permission_classes = [IsAuthenticated & IsContributor]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(id=project_id)
        user_email = self.request._user.email
        user = User.objects.get(email=user_email)
        serializer.save(project=project, author=user)


class CommentViewset(ModelViewSet):
    """
    A ViewSet for viewing comments.
    """
    permission_classes = [IsAuthenticated & IsContributor]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user_email = self.request._user.email
        user = User.objects.get(email=user_email)
        issue_id = self.kwargs.get('issue_pk')
        issue = Issue.objects.get(id=issue_id)
        serializer.save(author=user, issue=issue)

