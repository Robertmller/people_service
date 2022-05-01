from rest_framework.serializers import ModelSerializer

from core import models


class AreopagusBusinessSerializer(ModelSerializer):
    class Meta:
        model = models.AreopagusBusiness
        fields = "__all__" 


class TypeSerializer(ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__" 


class CommunicationToolSerializer(ModelSerializer):
    class Meta:
        model = models.CommunicationTool
        fields = "__all__" 


class CollaboratorSerializer(ModelSerializer):
    class Meta:
        model = models.Collaborator
        fields = "__all__" 


class ValueCollaboratorSerializer(ModelSerializer):
    class Meta:
        model = models.ValueCollaborator
        fields = "__all__" 


class JustifySerializer(ModelSerializer):
    class Meta:
        model = models.Justify
        fields = "__all__" 


class EstateSerializer(ModelSerializer):
    class Meta:
        model = models.Estate
        fields = "__all__" 


class CalendarSerializer(ModelSerializer):
    class Meta:
        model = models.Calendar
        fields = "__all__" 


class CommitsSerializer(ModelSerializer):
    class Meta:
        model = models.Commits
        fields = "__all__" 


class RepositorySerializer(ModelSerializer):
    class Meta:
        model = models.Repository
        fields = "__all__" 


class StatusTaskSerializer(ModelSerializer):
    class Meta:
        model = models.StatusTask
        fields = "__all__" 


class StatusProjectSerializer(ModelSerializer):
    class Meta:
        model = models.StatusProject
        fields = "__all__" 


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = models.Project
        fields = "__all__" 


class SourceCodeToolContractSerializer(ModelSerializer):
    class Meta:
        model = models.SourceCodeToolContract
        fields = "__all__" 


class SourceCodeToolSerializer(ModelSerializer):
    class Meta:
        model = models.SourceCodeTool
        fields = "__all__" 


class TaskRepositorySerializer(ModelSerializer):
    class Meta:
        model = models.TaskRepository
        fields = "__all__" 


class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__" 


class TaskToolContractSerializer(ModelSerializer):
    class Meta:
        model = models.TaskToolContract
        fields = "__all__" 


class TaskToolSerializer(ModelSerializer):
    class Meta:
        model = models.TaskTool
        fields = "__all__" 


class CollaboratorContractSerializer(ModelSerializer):
    class Meta:
        model = models.CollaboratorContract
        fields = "__all__" 


class ContractSerializer(ModelSerializer):
    class Meta:
        model = models.Contract
        fields = "__all__" 


class StatusContractSerializer(ModelSerializer):
    class Meta:
        model = models.StatusContract
        fields = "__all__" 
        