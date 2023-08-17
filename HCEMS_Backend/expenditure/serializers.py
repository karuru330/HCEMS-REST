from rest_framework import serializers
from .models import Category, Stage, Expenditure

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    def validate_category_name(self, category_name):
        categories = Category.objects.filter(category_name=category_name)
        if len(categories) > 0:
            raise serializers.ValidationError("The category is already exists")
        return category_name
    
class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"
    def validate_stage_name(self, stage_name):
        stages = Stage.objects.filter(stage_name=stage_name)
        if len(stages) > 0:
            raise serializers.ValidationError("The stage is already exists")
        return stage_name
    
class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = "__all__"