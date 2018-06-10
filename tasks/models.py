from django.db import models

class customer(models.Model):
    username = models.CharField(max_length=400)
    password = models.CharField(max_length=400)
    email_id = models.EmailField(max_length=600)

    def __str__(self):
        return self.username
  #  tasks_associated = solve this conundrum


class taskDetails(models.Model):
    taskName = models.CharField(max_length=1000)
    taskDate = models.DateField('date set',null=True)
    taskTime = models.TimeField('time set',null=True)
    location = models.CharField(max_length=1000)
    customersInvolved = models.ManyToManyField(customer, through='joiningTask', null=True)

    def __str__(self):
        return self.taskName

class joiningTask(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    taskDetails = models.ForeignKey(taskDetails, on_delete=models.CASCADE)
    dateOfJoining = models.DateField('date set',null=True)


