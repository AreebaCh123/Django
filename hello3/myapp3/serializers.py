from rest_framework import serializers
from .models import Student , Profile
#validators
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'age']
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('name should start with r')
'''class StudentSerializer(serializers.Serializer):
    profile = ProfileSerializer(required=False)  # ✅ Make it optional
    name = serializers.CharField(max_length=100, validators= [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city', 'profile']'''

class StudentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city','profile']

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('seat full')
        return value
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    def validate(self,data):#data is dict
        nm= data.get('name')
        ct = data.get('city')
        if nm.lower() == 'areeba' and ct.lower()!= 'multan':
            raise serializers.ValidationError('city must be multan')
        return data
    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)  # ✅ Avoid KeyError
        if profile_data:
            profile = Profile.objects.create(**profile_data)
            student = Student.objects.create(profile=profile, **validated_data)
        else:
            student = Student.objects.create(**validated_data)
        return student