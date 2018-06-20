from django.db import models


# customer database
class customer(models.Model):
    username = models.CharField(max_length=400)
    password = models.CharField(max_length=400)
    email_id = models.CharField(max_length=600)
    def __str__(self):
        return self.username

# task or event information
class taskDetails(models.Model):
    taskName = models.CharField(max_length=1000)
    taskDate = models.DateField('date set',null=True)
    taskTime = models.TimeField('time set',null=True)
    location = models.CharField(max_length=1000)
    customersInvolved = models.ManyToManyField(customer, through='joiningTask', null=True)

    def __str__(self):
        return self.taskName

# the model which will be used to connect the tasks to the customers through the many to many relation
class joiningTask(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    taskDetails = models.ForeignKey(taskDetails, on_delete=models.CASCADE)
    dateOfJoining = models.DateField('date set',null=True)


