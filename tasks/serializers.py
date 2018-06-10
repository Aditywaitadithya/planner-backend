from rest_framework import serializers
from tasks.models import customer,taskDetails, joiningTask

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('username', 'password', 'email_id')


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = taskDetails
        fields = ('taskName', 'taskDate', 'taskTime', 'location', 'customersInvolved')


class joiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = joiningTask
        fields = ('customer', 'taskDetails', 'dateOfJoining')



