from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    Customers,
    SalesRepresentative,
    Transaction,
)


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ["type_id", "type_name"]


class EquipmentListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentListing
        fields = ["listing_id", "type_id", "make", "model", "year", "price"]


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ["order_id", "listing_id", "customer", "quantity", "total_price"]


class CustomerSerializer(serializers.ModelSerializer):
    formatted_phone = serializers.CharField()

    class Meta:
        model = Customers
        fields = ["customer_id", "name", "contact", "email", "phone", "formatted_phone"]


class SalesRepresentativeSerializer(serializers.ModelSerializer):
    formatted_phone = serializers.CharField()
    formatted_email = serializers.EmailField()

    class Meta:
        model = SalesRepresentative
        fields = [
            "rep_id",
            "name",
            "email",
            "phone",
            "formatted_phone",
            "formatted_email",
        ]


class TransactionSerializer(serializers.ModelSerializer):
    formatted_amount = serializers.CharField()

    class Meta:
        model = Transaction
        fields = [
            "transaction_id",
            "order_id",
            "payment_method",
            "amount",
            "status",
            "formatted_amount",
        ]
