from rest_framework import serializers
from django.contrib.auth import get_user_model

from apiappTest.models import Blog

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = get_user_model()
        fields = ["id", "username", "email", "password", "first_name", "last_name" ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = get_user_model()
        new_user = user.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        new_user.set_password(password)
        new_user.save()
        return new_user
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id","title", "slug","author",
                  "category", "content", "featured_img",
                  "published_date","created_at","updated_at","is_draf"]