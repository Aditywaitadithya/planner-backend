from rest_framework import serializers
from tasks.models import customer,taskDetails, joiningTask


# file added to add the modelserializer to all the classes of the database
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('username', 'password', 'email_id','id')


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = taskDetails
        fields = ('taskName', 'taskDate', 'taskTime', 'location','id','customersInvolved','isAlarmTrue')


class joiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = joiningTask
        fields = ('customer', 'taskDetails', 'dateOfJoining','id')



