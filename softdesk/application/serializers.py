from rest_framework.serializers import ModelSerializer
from application.models import Project, Contributor, Issue, Comment

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        read_only_fields = ('project', 'role')

    def to_representation(self, instance):
        representation = super(ContributorSerializer, self).to_representation(instance)
        representation['project'] = instance.project.title
        representation['user'] = instance.user.email
        return representation


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ('project', 'author')

    def to_representation(self, instance):
        representation = super(IssueSerializer, self).to_representation(instance)
        representation['project'] = instance.project.title


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'issue')