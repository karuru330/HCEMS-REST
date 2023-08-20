from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, ExpenditureSerializer, StageSerializer
from .models import Category, Expenditure, Stage
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status

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
            return Response({"message":"Category added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StageAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = StageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Stage has been added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        stages = Stage.objects.all()
        serializer = StageSerializer(stages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ExpenditureAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = ExpenditureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Expenditure has been added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request):
        expenditures = Expenditure.objects.all()
        serializer = ExpenditureSerializer(expenditures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        data = request.data
        obj = Expenditure.objects.get(id=data["id"])
        if obj:
            serializer = ExpenditureSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Expenditure has been updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"No records exists"}, status=status.HTTP_400_BAD_REQUEST)