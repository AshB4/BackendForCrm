
from rest_framework import generics
from django.db.models import Q
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


class EquipmentTypeListCreate(generics.ListCreateAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer

class EquipmentListingListCreate(generics.ListCreateAPIView):
    queryset = EquipmentListing.objects.all()
    serializer_class = EquipmentListingSerializer


class EquipmentListingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentListing.objects.all()
    serializer_class = EquipmentListingSerializer


class CustomerOrderListCreate(generics.ListCreateAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class CustomerOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class CustomerListCreate(generics.ListCreateAPIView):
    queryset = CustomerList.objects.all()
    serializer_class = CustomerListSerializer


class CustomerListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerList.objects.all()
    serializer_class = CustomerListSerializer


class SalesRepresentativeListCreate(generics.ListCreateAPIView):
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer


class SalesRepresentativeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SearchList(generics.ListAPIView):
    serializer_class = CustomerListSerializer

    def get_queryset(self):
        queryset = CustomerList.objects.all()
        search_query = self.request.query_params.get("q", None)
        if search_query:
            queryset = queryset.filter(
                Q(field1__icontains=search_query)
                | Q(field2__icontains=search_query)  # Add more fields if needed
            )
        return queryset


class EquipmentListingSearchList(generics.ListAPIView):
    serializer_class = EquipmentListingSerializer

    def get_queryset(self):
        queryset = EquipmentListing.objects.all()
        search_query = self.request.query_params.get("q", None)
        if search_query:
            queryset = queryset.filter(
                Q(make__icontains=search_query) | Q(model__icontains=search_query)
            )
        return queryset
