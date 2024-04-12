from rest_framework import serializers
from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    CustomerList,
    SalesRepresentative,
    Transaction,
)


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__' #["type_id", "type_name"]


class EquipmentListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentListing
        fields = ["listing_id", "type_id", "make", "model", "year", "price"]


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ["order_id", "listing_id", "customer", "quantity", "total_price"]


class CustomerListSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()

    class Meta:
        model = CustomerList
        fields = ["customer_id", "name", "contact", "email", "phone"]


class SalesRepresentativeSerializer(serializers.ModelSerializer):
    # formatted_phone = serializers.CharField()
    # formatted_email = serializers.EmailField()

    class Meta:
        model = SalesRepresentative
        fields = [
            "rep_id",
            "name",
            "email",
            "phone",
        ]


class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.CharField()

    class Meta:
        model = Transaction
        fields = [
            "transaction_id",
            "order_id",
            "payment_method",
            "amount",
            "status",
            # "formatted_amount",
        ]
