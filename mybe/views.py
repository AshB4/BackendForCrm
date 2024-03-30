from django.shortcuts import render
from rest_framework import generics, status
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
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

def delete_equipment_type(request, type_id):
    # Retrieve the equipment type object or return 404 if not found
        equipment_type = get_object_or_404(EquipmentType, pk=type_id)
# Perform deletion logic
        equipment_type.delete()
 # Return success response
        return JsonResponse({'message': 'Equipment type deleted successfully'}, status=204)


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
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerList.objects.all()
    serializer_class = CustomerSerializer


class SalesRepresentativeListCreate(generics.ListCreateAPIView):
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer


class SalesRepresentativeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer


def delete_sales_rep(request, type_id):
    # Retrieve the equipment type object or return 404 if not found
    delete_sales_rep = get_object_or_404(SalesRepresentative, pk=type_id)
    # Perform deletion logic
    delete_sales_rep.delete()
    # Return success response
    return JsonResponse({"message": "Sales Representative deleted successfully"}, status=204)


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SearchList(generics.ListAPIView):
    serializer_class = CustomerSerializer

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


def index(request):
    return home(request)


# HttpResponse("Welcome to the backend of your CRM application.")


def home(request):
    return render(request, "home.html")
