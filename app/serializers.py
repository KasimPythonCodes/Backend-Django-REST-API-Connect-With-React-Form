from rest_framework import serializers
from app.models import Registration

class ResigtrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields =['first_name','last_name','email','password']
        
    # def validate(self, attrs):
    #     password = attrs['password']
    #     confirm_password = attrs['confirm_password']  
    #     if password != confirm_password:
    #         raise serializers.ValidationError("password and comfirm password are not match")  
    #     return attrs
    
# class SetPasswordSerializers(serializers.ModelSerializer):
#     password =serializers.CharField()
#     confirm_password =serializers.CharField()

#     def validate(self, attrs):
#         password = attrs['password']
#         confirm_password = attrs['confirm_password']  
#         if password != confirm_password:
#             raise serializers.ValidationError("password and comfirm password are not match")  
#         return attrs