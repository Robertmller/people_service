from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 

from core import models
from core.api import serializers


class AreopagusBusinessViewSet(ModelViewSet):
    queryset = models.AreopagusBusiness.objects.all() 
    serializer_class = serializers.AreopagusBusinessSerializer
    
    # authentication
    #permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly ] 


class TypeViewSet(ModelViewSet):
    queryset = models.Type.objects.all() 
    serializer_class = serializers.TypeSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class CommunicationToolViewSet(ModelViewSet):
    queryset = models.CommunicationTool.objects.all() 
    serializer_class = serializers.CommunicationToolSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class CollaboratorViewSet(ModelViewSet):
    queryset = models.Collaborator.objects.all() 
    serializer_class = serializers.CollaboratorSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly ]
    
        

class ValueCollaboratorViewSet(ModelViewSet):
    queryset = models.ValueCollaborator.objects.all() 
    serializer_class = serializers.ValueCollaboratorSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly ] 


class JustifyViewSet(ModelViewSet):
    queryset = models.Justify.objects.all() 
    serializer_class = serializers.JustifySerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class EstateViewSet(ModelViewSet):
    queryset = models.Estate.objects.all() 
    serializer_class = serializers.EstateSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class CalendarViewSet(ModelViewSet):
    queryset = models.Calendar.objects.all() 
    serializer_class = serializers.CalendarSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class CommitsViewSet(ModelViewSet):
    queryset = models.Commits.objects.all() 
    serializer_class = serializers.CommitsSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class RepositoryViewSet(ModelViewSet):
    queryset = models.Repository.objects.all() 
    serializer_class = serializers.RepositorySerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class StatusTaskViewSet(ModelViewSet):
    queryset = models.StatusTask.objects.all() 
    serializer_class = serializers.StatusTaskSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class StatusProjectViewSet(ModelViewSet):
    queryset = models.StatusProject.objects.all() 
    serializer_class = serializers.StatusProjectSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all() 
    serializer_class = serializers.ProjectSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class SourceCodeToolContractViewSet(ModelViewSet):
    queryset = models.SourceCodeToolContract.objects.all() 
    serializer_class = serializers.SourceCodeToolContractSerializer
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class SourceCodeToolViewSet(ModelViewSet):
    queryset = models.SourceCodeTool.objects.all() 
    serializer_class = serializers.SourceCodeToolSerializer
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class TaskRepositoryViewSet(ModelViewSet):
    queryset = models.TaskRepository.objects.all() 
    serializer_class = serializers.TaskRepositorySerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all() 
    serializer_class = serializers.TaskSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class TaskToolContractViewSet(ModelViewSet):
    queryset = models.TaskToolContract.objects.all() 
    serializer_class = serializers.TaskToolContractSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class TaskToolViewSet(ModelViewSet):
    queryset = models.TaskTool.objects.all() 
    serializer_class = serializers.TaskToolSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 


class CollaboratorContractViewSet(ModelViewSet):
    queryset = models.CollaboratorContract.objects.all() 
    serializer_class = serializers.CollaboratorContractSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly ] 


class ContractViewSet(ModelViewSet):
    queryset = models.Contract.objects.all() 
    serializer_class = serializers.ContractSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly ] 


class StatusContractViewSet(ModelViewSet):
    queryset = models.StatusContract.objects.all() 
    serializer_class = serializers.StatusContractSerializer 
    
    # authentication
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly] 
        