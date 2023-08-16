from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    def validate_category_name(self, category_name):
        categories = Category.objects.filter(category_name=category_name)
        if len(categories) > 0:
            raise serializers.ValidationError("The category is already exists")
        return category_name