from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from application.views import ProjectViewset, UserViewset, IssueViewset, CommentViewset

router = DefaultRouter()
router.register(r'projects', ProjectViewset, basename='projects')

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'users', UserViewset, basename='users')
project_router.register(r'issues', IssueViewset, basename='issues')

issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', CommentViewset, basename='comments')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(project_router.urls)),
    path(r'', include(issue_router.urls)),
]
