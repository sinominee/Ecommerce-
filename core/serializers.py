from rest_framework import serializers
# from rest_framework.validators import validate

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()

    # def validate_password(self, value):
    #     if len(value) < 8:
    #        raise serializers.ValidationError(
    #            "The password must be at least 8 characters"
    #        )
    #     return value

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'password': "The password and confirm password does not match"
            })
        return super().validate(attrs)
           