from django import forms
from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    CustomerList,
    SalesRepresentative,
    Transaction,
)


class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = EquipmentType
        fields = "__all__"


class EquipmentListingForm(forms.ModelForm):
    class Meta:
        model = EquipmentListing
        fields = "__all__"


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerList
        fields = "__all__"


class SalesRepresentativeForm(forms.ModelForm):
    class Meta:
        model = SalesRepresentative
        fields = "__all__"


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
