from django.contrib import admin
from core.models import *


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'cnpj', 'rg', 'born_date']


@admin.register(AreopagusBusiness)
class AreopagusBusinessAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CommunicationTool)
class CommunicationToolAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ValueCollaborator)
class ValueCollaboratorAdmin(admin.ModelAdmin):
    list_display = ['value', 'collaborator_id', 'date_end']


@admin.register(Justify)
class JustifyAdmin(admin.ModelAdmin):
    list_display = ['description', 'date_time']


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(StatusContract)
class StatusContractAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CollaboratorContract)
class CollaboratorContractAdmin(admin.ModelAdmin):
    list_display = ['contract_id', 'status']


@admin.register(TaskTool)
class TaskToolAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SourceCodeTool)
class SourceCodeToolAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(StatusProject)
class StatusProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(StatusTask)
class StatusTaskAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(TaskToolContract)
class TaskToolContractAdmin(admin.ModelAdmin):
    list_display = ['contract_id', 'task_tool_id', 'link']


@admin.register(SourceCodeToolContract)
class SourceCodeToolContractAdmin(admin.ModelAdmin):
    list_display = ['contract_id', 'source_code_tool_id', 'link']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'contract_id',
                    'status_project_id', 'doc_link']


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ['link', 'ssh_link', 'project_id']


@admin.register(Commits)
class CommitsAdmin(admin.ModelAdmin):
    list_display = ['task_repository_id', 'description', 'date_time']


@admin.register(TaskRepository)
class TaskRepositoryAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'repository_id', 'total_commits']


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['date', 'task_id', 'status',
                    'is_english', 'is_levi_signature', 'is_pr']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date_in_todo', 'date_in_progress', 'date_in_review', 'date_done', 'date_blocked',
                    'date_expected', 'status_task_id', 'project_id', 'estimate', 'link_branch', 'pr_link', 'total_commits', 'link_video']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['cnpj', 'playlist_link', 'meet_id', 'tech_lead_name', 'communication_tool_id', 'coorporative_email', 'estate_id',
                    'status_contract_id', 'begin_date_contract', 'date_end_contract', 'hours_control_link', 'is_full_time', 'is_international', 'value']
