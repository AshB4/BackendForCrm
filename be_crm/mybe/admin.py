from django.contrib import admin
from .models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    CustomerList,
    SalesRepresentative,
    Transaction,
)

# Register your models here
admin.site.register(EquipmentType)
admin.site.register(EquipmentListing)
admin.site.register(CustomerOrder)
admin.site.register(CustomerList)
admin.site.register(SalesRepresentative)
admin.site.register(Transaction)


# Register your models here.
# Then make migraton after this
# what this does => (automated code gen. that will move it to your db)
# python3 manage.py makemigrations
# python3 manage.py migrate

# This Python script is a part of a Django project and is responsible for registering Django models with the Django admin interface.

# **For Non-Technical Individuals:**
# This script essentially tells Django's admin interface about the models (think of them as database tables) that we want to manage through the admin site. Each model represents a specific type of data in the database. By registering these models, we enable functionalities such as creating, reading, updating, and deleting (CRUD operations) directly from the Django admin panel. This makes it easier for non-technical users to manage the application's data without needing to write complex database queries.

# **For Technical Individuals:**
# In Django, the admin interface is a powerful tool for managing application data. This script imports the necessary models from the application and registers them with the admin site using the `admin.site.register()` method. This allows Django to generate appropriate admin interfaces for each registered model, including forms for data entry and display pages for viewing existing data. After registering the models, we typically run the `makemigrations` and `migrate` commands to create and apply the necessary database migrations, ensuring that the database schema reflects the changes made to the models.

# This script automates the process of integrating Django models with the admin interface, providing a convenient way to manage application data during development and deployment.
