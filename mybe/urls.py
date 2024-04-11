from django.urls import path
from .views import (
    home,
    index,
    EquipmentTypeListCreate,
    EquipmentTypeRetrieveUpdateDestroy,
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

urlpatterns = [
    # Home and index paths
    path("", index, name="index"),
    path("home/", home, name="home"),
    # Equipment type paths
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
    # Equipment listing paths
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
    # Customer order paths
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
    # Customer paths
    path("customer-list/", CustomerListCreate.as_view(), name="customer-list-create"),
    path(
        "customer-list/<int:pk>/",
        CustomerRetrieveUpdateDestroy.as_view(),
        name="customer-detail",
    ),
    
    # Sales representative paths
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
    # Transaction paths
    path(
        "transactions/", TransactionListCreate.as_view(), name="transaction-list-create"
    ),
    path(
        "transactions/<int:pk>/",
        TransactionRetrieveUpdateDestroy.as_view(),
        name="transaction-detail",
    ),
]
