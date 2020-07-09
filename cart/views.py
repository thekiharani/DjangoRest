import csv
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import (
    Product, Project, Requisition, RequisitionMeta
)
from .serializers import (
    ProductSerializer, ProjectSerializer, RequisitionSerializer, RequisitionMetaSerializer
)


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RequisitionView(viewsets.ModelViewSet):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

class RequisitionMetaView(viewsets.ModelViewSet):
    queryset = RequisitionMeta.objects.all()
    serializer_class = RequisitionMetaSerializer

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Name', 'Price', 'Quantity', 'Serial No.', 'Date Created', 'Last Updated'])
    for product in Product.objects.all().values_list('name', 'price', 'qty', 'serial_number', 'created_at', 'updated_at'):
        writer.writerow(product)

    response['Content-Disposition'] = 'attachment; filename="Products.csv"'
    return response