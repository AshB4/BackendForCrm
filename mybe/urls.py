from django.urls import path
from .views import (
    home,
    index,
    EquipmentTypeListCreate,
    EquipmentTypeRetrieveUpdateDestroy,
    delete_equipment_type,
    EquipmentListingListCreate,
    EquipmentListingRetrieveUpdateDestroy,
    CustomerOrderListCreate,
    CustomerOrderRetrieveUpdateDestroy,
    CustomerListCreate,
    CustomerRetrieveUpdateDestroy,
    SalesRepresentativeListCreate,
    SalesRepresentativeRetrieveUpdateDestroy,
    TransactionListCreate,
    TransactionRetrieveUpdateDestroy,
)

# Define URL patterns
urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),  # Change the URL pattern to avoid whitespace
    path(
        "equipment/types/",
        EquipmentTypeListCreate.as_view(),
        name="equipment-type-list-create",
    ),
    path(
        "equipment/types/<int:pk>/",
        EquipmentTypeRetrieveUpdateDestroy.as_view(),
        name="equipment-type-detail",
    ),
    path(
        "equipment/listings/",
        EquipmentListingListCreate.as_view(),
        name="equipment-listing-list-create",
    ),
    path(
        "equipment/listings/<int:pk>/",
        EquipmentListingRetrieveUpdateDestroy.as_view(),
        name="equipment-listing-detail",
    ),
    path(
        "customer/orders/",
        CustomerOrderListCreate.as_view(),
        name="customer-order-list-create",
    ),
    path(
        "customer/orders/<int:pk>/",
        CustomerOrderRetrieveUpdateDestroy.as_view(),
        name="customer-order-detail",
    ),
    path("customer-list/", CustomerListCreate.as_view(), name="customer-list-create"),
    path(
        "customers-list<int:pk>/",
        CustomerRetrieveUpdateDestroy.as_view(),
        name="customer-detail",
    ),
    path(
        "sales-representatives/",
        SalesRepresentativeListCreate.as_view(),
        name="sales-representative-list-create",
    ),
    path(
        "sales-representatives/<int:pk>/",
        SalesRepresentativeRetrieveUpdateDestroy.as_view(),
        name="sales-representative-detail",
    ),
    path(
        "transactions/", TransactionListCreate.as_view(), name="transaction-list-create"
    ),
    path(
        "transactions/<int:pk>/",
        TransactionRetrieveUpdateDestroy.as_view(),
        name="transaction-detail",
    ),
]
