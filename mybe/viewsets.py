from rest_framework import viewsets

from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    CustomerList,
    SalesRepresentative,
    Transaction,
)

from .serializers import (
    EquipmentTypeSerializer,
    EquipmentListingSerializer,
    CustomerOrderSerializer,
    CustomerListSerializer,
    SalesRepresentativeSerializer,
    TransactionSerializer,
)

class EquipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer

class EquipmentListingViewSet(viewsets.ModelViewSet):
    queryset = EquipmentListing.objects.all()
    serializer_class = EquipmentListingSerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

class CustomerListViewSet(viewsets.ModelViewSet):
    queryset = CustomerList.objects.all()
    serializer_class = CustomerListSerializer

class SalesRepresentativeViewSet(viewsets.ModelViewSet):
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class EquipmentTypeListCreate(viewsets.ModelViewSet):
    queryset =EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentTypeRetrieveUpdateDestroy(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentListingRetrieveUpdateDestroy(viewsets.ModelViewSet):
    queryset = EquipmentListing.objects.all()
    serializer_class = EquipmentListingSerializer

class CustomerOrderListCreate(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
