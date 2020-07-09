from rest_framework import serializers
from .models import (
    Product, Project, Requisition, RequisitionMeta
)

# Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'qty', 'serial_number', 'created_at', 'updated_at']
        read_only_fields = ['serial_number', 'created_at', 'updated_at']

# Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'serial_number', 'created_at', 'updated_at']
        read_only_fields = ['serial_number', 'created_at', 'updated_at']

# Requisition
class RequisitionMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionMeta
        fields = ['id', 'qty', 'expected_delivery_date', 'requisition_price', 'requisition_price', 'product', 'created_at']
        read_only_fields = ['requisition', 'created_at']

class RequisitionSerializer(serializers.ModelSerializer):
    items = RequisitionMetaSerializer(many=True)
    class Meta:
        model = Requisition
        fields = ['id', 'project', 'foreman', 'serial_number', 'created_at', 'items']
        read_only_fields = ['serial_number', 'created_at', 'foreman', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        validated_data['foreman'] = self.context['request'].user
        requisition = Requisition.objects.create(**validated_data)
        for item_data in items_data:
            RequisitionMeta.objects.create(requisition=requisition, **item_data)
        return requisition

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     data  = **validated_data
    #     purchase = Purchase.objects.create(**validated_data)
    #     for item_data in items_data:
    #         PurchaseMeta.objects.create(purchase=purchase, **item_data)
    #     return purchase