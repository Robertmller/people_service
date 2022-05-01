#from localflavor.br.models import BRCPFField, BRCNPJField 
from django.db import models
from django.core.mail import send_mail
from model_utils.models import TimeStampedModel


class AreopagusBusiness(TimeStampedModel):
    name = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Areopagus Business'
        verbose_name_plural = 'Areopagus Business'

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'Type'
        verbose_name_plural = 'Typies'

    def __str__(self):
        return self.name


class CommunicationTool(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'Communication Tool'
        verbose_name_plural = 'Communication Tools'

    def __str__(self):
        return self.name

class Collaborator(TimeStampedModel):
    name = models.CharField(max_length=255)
    areopagus_business_id = models.ForeignKey(AreopagusBusiness, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, default=0)
    cnpj = models.CharField(max_length=14, default=0)
    rg = models.CharField(max_length=255)
    born_date = models.DateTimeField()
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Collaborator'
        verbose_name_plural = 'Collaborators'

    def __str__(self):
        return self.name


class ValueCollaborator(TimeStampedModel):
    value = models.FloatField()
    collaborator_id = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    date_end = models.DateTimeField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Collaborator'
        verbose_name_plural = 'Collaborator Values '

    def __str__(self):
        return self.value

class Justify(TimeStampedModel):
    collaborator_id = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    description = models.TextField()
    date_time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Justify'
        verbose_name_plural = 'Justifies'
    def __str__(self):
        return self.description

class Estate(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'Estate'
        verbose_name_plural = 'Estates'

    def __str__(self):
        return self.name

class StatusContract(TimeStampedModel):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Status Contract'
        verbose_name_plural = 'Status Contracts'

    def __str__(self):
        return self.name


class Contract(TimeStampedModel):
    cnpj = models.CharField(max_length=255, default=0)
    playlist_link = models.CharField(max_length=500)
    meet_id = models.IntegerField()
    tech_lead_name = models.CharField(max_length=255)
    communication_tool_id = models.ForeignKey(CommunicationTool, on_delete=models.CASCADE)
    coorporative_email = models.CharField(max_length=255)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    status_contract_id = models.ForeignKey(StatusContract, on_delete=models.CASCADE)
    begin_date_contract = models.DateTimeField()
    date_end_contract = models.DateTimeField()
    hours_control_link = models.TextField()
    is_full_time = models.BooleanField(default=False)
    is_international = models.BooleanField(default=False)
    value = models.FloatField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return self.cnpj

class CollaboratorContract(TimeStampedModel):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    collaborator_id = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    status = models.IntegerField() 

    class Meta:
        ordering = ['id']
        verbose_name = 'Collaborator Contract'
        verbose_name_plural = 'Collaborators Contract'

    def __str__(self):
        return self.status

class TaskTool(TimeStampedModel):
    name = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        verbose_name = 'Task Tool'
        verbose_name_plural = 'Task Tools'

    def __str__(self):
        return self.name


class TaskToolContract(TimeStampedModel):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    task_tool_id = models.ForeignKey(TaskTool, on_delete=models.CASCADE)
    link = models.CharField(max_length=500, default="")

    class Meta:
        ordering = ['id']
        verbose_name = 'Task Tool Contract'
        verbose_name_plural = 'Task Tool Contracts'

    def __str__(self):
        return self.link

class SourceCodeTool(TimeStampedModel):
    name = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        verbose_name = 'Source Code Tool'
        verbose_name_plural = 'Source Code Tools'

    def __str__(self):
        return self.name

class SourceCodeToolContract(TimeStampedModel):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    source_code_tool_id = models.ForeignKey(SourceCodeTool, on_delete=models.CASCADE)
    link = models.CharField(max_length=500, default="")

    class Meta:
        ordering = ['id']
        verbose_name = 'Source Code Tool Contract'
        verbose_name_plural = 'Source Code Tool Contracts'

    def __str__(self):
        return self.link

class StatusProject(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'Status Project'
        verbose_name_plural = 'Status Projects'

    def __str__(self):
        return self.name

class Project(TimeStampedModel):
    name = models.CharField(max_length=255)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    status_project_id = models.ForeignKey(StatusProject, on_delete=models.CASCADE)
    documentaion_id = models.IntegerField()
    doc_link = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

class StatusTask(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'Status Task'
        verbose_name_plural = 'Status Tasks'

    def __str__(self):
        return self.name

class Repository(TimeStampedModel):
    link = models.CharField(max_length=500, default="")
    ssh_link = models.CharField(max_length=500, default="")
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)    

    class Meta:
        ordering = ['id']
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'

    def __str__(self):
        return self.link

class Commits(TimeStampedModel):
    task_repository_id = models.ForeignKey(Repository, on_delete=models.CASCADE)
    description = models.TextField()
    date_time = models.DateTimeField()
    collaborator_id = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Commit'
        verbose_name_plural = 'Commits'

    def __str__(self):
        return self.description

class Task(TimeStampedModel):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date_in_todo = models.DateTimeField()
    date_in_progress = models.DateTimeField()
    date_in_review = models.DateTimeField()
    date_done = models.DateTimeField()
    date_blocked = models.DateTimeField()
    date_expected = models.DateTimeField()
    status_task_id = models.ForeignKey(StatusTask, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    estimate = models.IntegerField()
    link_branch = models.CharField(max_length=500, default="")
    pr_link = models.CharField(max_length=500, default="")
    total_commits = models.IntegerField()
    link_video = models.CharField(max_length=500, default="")

    class Meta:
        ordering = ['id']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title

class TaskRepository(TimeStampedModel):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    repository_id = models.ForeignKey(Repository, on_delete=models.CASCADE)
    total_commits = models.IntegerField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Task Repository'
        verbose_name_plural = 'Task Repositories'

    def __str__(self):
        return self.total_commits

class Calendar(TimeStampedModel):
    date = models.DateField()
    collaborator_id = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.IntegerField()
    is_english = models.BooleanField(default=False)
    is_levi_signature = models.BooleanField(default=False)
    is_pr = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendars'

    def __str__(self):
        return self.date