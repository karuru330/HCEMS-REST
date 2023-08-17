from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, ExpenditureSerializer, StageSerializer
from .models import Category, Expenditure, Stage
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

# Create your views here.
from .models import Category

class CategoryAPI(APIView):
    permission_classes = [IsAuthenticated,]

    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        category_name = request.data.get("category_name")
        category_image = request.data.get("category_image")
        print(category_name, category_image)
        data = {
            "category_name":category_name,
            "category_image": category_image
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status_code":200, "message":"Category added successfully"})
        else:
            return Response(serializer.errors)
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class StageAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = StageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status_code":200, "message":"Stage has been added successfully"})
        else:
            return Response(serializer.errors)
        
    def get(self, request):
        stages = Stage.objects.all()
        serializer = StageSerializer(stages, many=True)
        return Response(serializer.data)
        
class ExpenditureAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = ExpenditureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status_code":200, "message":"Expenditure has been added successfully"})
        else:
            return Response(serializer.errors)
    
    def get(self, request):
        expenditures = Expenditure.objects.all()
        serializer = ExpenditureSerializer(expenditures, many=True)
        return Response(serializer.data)