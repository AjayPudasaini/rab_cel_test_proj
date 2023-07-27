from rest_framework import serializers
from rab_test_cel.users.models import User
import debugpy

debugpy.listen(("0.0.0.0",5678))

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "name", "email", "password", "is_admin", "is_customer" ]


    def create(self, validated_data):
        a = 10
        b = 30
        if b>a:
            s = a+b
        else:
            s = None
        print("18", s)
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
