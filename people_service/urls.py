
from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# My App
from core.api import viewsets


router = routers.DefaultRouter()

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API-CRUD Areopagus ",
        default_version='v1',
        description="Lorem Ipsum",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contatorobertmull@gmail.com"),
        license=openapi.License(name="Aeropagus License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router.register(r'type', viewsets.TypeViewSet)
router.register(r'areopagusbusiness', viewsets.AreopagusBusinessViewSet)
router.register(r'communicationtool', viewsets.CommunicationToolViewSet)
router.register(r'collaborator', viewsets.CollaboratorViewSet)
router.register(r'valuecollaborator', viewsets.ValueCollaboratorViewSet)
router.register(r'estate', viewsets.EstateViewSet)
router.register(r'statuscontract', viewsets.StatusContractViewSet)
router.register(r'justify', viewsets.JustifyViewSet)
router.register(r'contract', viewsets.ContractViewSet)
router.register(r'collaboratorcontract', viewsets.CollaboratorContractViewSet)
router.register(r'tasktool', viewsets.TaskToolViewSet)
router.register(r'tasktoolcontract', viewsets.TaskToolContractViewSet)
router.register(r'task', viewsets.TaskViewSet)
router.register(r'taskrepository', viewsets.TaskRepositoryViewSet)
router.register(r'sourcecodetool', viewsets.SourceCodeToolViewSet)
router.register(r'sourcecodetoolcontract', viewsets.SourceCodeToolContractViewSet)
router.register(r'project', viewsets.ProjectViewSet)
router.register(r'statusproject', viewsets.StatusProjectViewSet)
router.register(r'statustask', viewsets.StatusTaskViewSet)
router.register(r'repository', viewsets.RepositoryViewSet)
router.register(r'commits', viewsets.CommitsViewSet)
router.register(r'calendar', viewsets.CalendarViewSet)



urlpatterns = [
    # Admin Panel Controll
    path('admin/', admin.site.urls),
]

urlpatterns += [   
    # Endpoints
    path('api/v1/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
 ]

urlpatterns += [   
    # Authentication
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += [
    # Swagger
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [ 
    # Documentation Index
    path('', include("core.urls")),
    path('', include("users.urls")),

]
