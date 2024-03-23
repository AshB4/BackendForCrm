from django.shortcuts import render, viewsets, status
from rest_framework import generics , status
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    Customers,
    SalesRepresentative,
    Transaction,
)
from .serializers import (
    EquipmentTypeSerializer,
    EquipmentListingSerializer,
    CustomerOrderSerializer,
    CustomerSerializer,
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
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


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
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customers.objects.all()
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
    
class TransactionViewSet(viewsets.ViewSet):

     def list(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def retrieve(self, request, pk=None):
            queryset = Transaction.objects.all()
            transaction = get_object_or_404(queryset, pk=pk)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)

        def update(self, request, pk=None):
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def partial_update(self, request, pk=None):
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def destroy(self, request, pk=None):
            transaction = Transaction.objects.get(pk=pk)
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
