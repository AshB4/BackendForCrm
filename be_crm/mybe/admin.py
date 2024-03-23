from django.contrib import admin
from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    Customers,
    SalesRepresentative,
    Transaction,
)

# Register your models here
admin.site.register(EquipmentType)
admin.site.register(EquipmentListing)
admin.site.register(CustomerOrder)
admin.site.register(Customers)
admin.site.register(SalesRepresentative)
admin.site.register(Transaction)


# Register your models here.
# Then make migraton after this
# what this does => (automated code gen. that will move it to your db)
# python3 manage.py makemigrations
# python3 manage.py migrate
