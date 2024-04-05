import os
import sqlite3
from django.core.management.base import BaseCommand
from mybe.models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    CustomerList,
    SalesRepresentative,
    Transaction,
)

class Command(BaseCommand):
    help = 'Populate initial data into the database'

    def handle(self, *args, **options):
        self.populate_data()

    def populate_data(self):
        # Connect to SQLite database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        equipment_type_data = [
            {"type_id": 1, "type_name": "Trucks"},
            {"type_id": 2, "type_name": "Big Rigs"},
            {"type_id": 3, "type_name": "Trackhoes"},
            {"type_id": 4, "type_name": "Backhoes"},
            {"type_id": 5, "type_name": "Excavators"},
            {"type_id": 6, "type_name": "Bulldozers"},
            {"type_id": 7, "type_name": "Dump Trucks"},
            {"type_id": 8, "type_name": "Cranes"},
        ]

        for data in equipment_type_data:
            cursor.execute("INSERT INTO mybe_equipmenttype (type_id, type_name) VALUES (?, ?)", (data['type_id'], data['type_name']))

        equipment_listing_data = [
            {"listing_id": 1, "type_id": 1, "make": "Volvo", "model": "VNL64T780", "year": 2018, "price": 80000},
            {"listing_id": 2, "type_id": 2, "make": "Freightliner", "model": "Cascadia", "year": 2016, "price": 70000},
            {"listing_id": 3, "type_id": 3, "make": "Peterbilt", "model": "389", "year": 2015, "price": 120000},
            {"listing_id": 4, "type_id": 4, "make": "Caterpillar", "model": "320D", "year": 2019, "price": 150000},
            {"listing_id": 5, "type_id": 5, "make": "John Deere", "model": "310SL", "year": 2017, "price": 60000},
            {"listing_id": 6, "type_id": 6, "make": "Komatsu", "model": "PC200-8", "year": 2015, "price": 90000},
            {"listing_id": 7, "type_id": 7, "make": "Caterpillar", "model": "D6T", "year": 2016, "price": 130000},
            {"listing_id": 8, "type_id": 8, "make": "Volvo", "model": "VHD64B200", "year": 2017, "price": 100000},
        ]

        for data in equipment_listing_data:
            cursor.execute("INSERT INTO mybe_equipmentlisting (listing_id, type_id, make, model, year, price) VALUES (?, ?, ?, ?, ?, ?)", 
                           (data['listing_id'], data['type_id'], data['make'], data['model'], data['year'], data['price']))

        customer_order_data = [
            {"order_id": 1, "listing_id": 1, "customer": "ABC Construction", "quantity": 2, "total_price": 160000},
            {"order_id": 2, "listing_id": 4, "customer": "XYZ Excavation", "quantity": 1, "total_price": 150000},
            {"order_id": 3, "listing_id": 5, "customer": "DEF Contractors", "quantity": 3, "total_price": 180000},
            {"order_id": 4, "listing_id": 7, "customer": "GHI Construction", "quantity": 2, "total_price": 260000},
            {"order_id": 5, "listing_id": 8, "customer": "JKL Builders", "quantity": 1, "total_price": 100000},
            {"order_id": 6, "listing_id": 9, "customer": "MNO Contractors", "quantity": 1, "total_price": 800000},
        ]

        for data in customer_order_data:
            cursor.execute("INSERT INTO mybe_customerorder (order_id, listing_id, customer, quantity, total_price) VALUES (?, ?, ?, ?, ?)", 
                           (data['order_id'], data['listing_id'], data['customer'], data['quantity'], data['total_price']))

        customer_list_data = [
            {"customer_id": 1, "name": "ABC Construction", "contact": "John Smith", "email": "john@abcconstruction.com", "phone": "+1 (555) 123-4567"},
            {"customer_id": 2, "name": "XYZ Excavation", "contact": "Jane Doe", "email": "jane@xyzexcavation.com", "phone": "+1 (555) 987-6543"},
            {"customer_id": 3, "name": "DEF Contractors", "contact": "Mike Johnson", "email": "mike@defcontractors.com", "phone": "+1 (555) 789-0123"},
            {"customer_id": 4, "name": "GHI Construction", "contact": "Sarah Johnson", "email": "sarah@ghiconstruction.com", "phone": "+1 (555) 111-2222"},
            {"customer_id": 5, "name": "JKL Builders", "contact": "Tom Smith", "email": "tom@jklbuilders.com", "phone": "+1 (555) 333-4444"},
            {"customer_id": 6, "name": "MNO Contractors", "contact": "Emily Brown", "email": "emily@mnocontractors.com", "phone": "+1 (555) 555-6666"},
        ]

        for data in customer_list_data:
            cursor.execute("INSERT INTO mybe_customer (customer_id, name, contact, email, phone) VALUES (?, ?, ?, ?, ?)", 
                           (data['customer_id'], data['name'], data['contact'], data['email'], data['phone']))

        sales_representative_data = [
            {
                "rep_id": 1,
                "name": "Alice Brown",
                "email": "alice@company.com",
                "phone": "+1 (555) 111-2222",
            },
            {
                "rep_id": 2,
                "name": "Bob White",
                "email": "bob@company.com",
                "phone": "+1 (555) 333-4444",
            },
            {
                "rep_id": 3,
                "name": "Carol Green",
                "email": "carol@company.com",
                "phone": "+1 (555) 555-6666",
            },
            {
                "rep_id": 4,
                "name": "David Lee",
                "email": "david@company.com",
                "phone": "+1 (555) 777-8888",
            },
            {
                "rep_id": 5,
                "name": "Rachel Wong",
                "email": "rachel@company.com",
                "phone": "+1 (555) 999-0000",
            },
            {
                "rep_id": 6,
                "name": "Michael Chen",
                "email": "michael@company.com",
                "phone": "+1 (555) 123-4567",
            },
        ]

        for data in sales_representative_data:
            cursor.execute(
                "INSERT INTO mybe_salesrepresentative (rep_id, name, email, phone) VALUES (?, ?, ?, ?)",
                (data["rep_id"], data["name"], data["email"], data["phone"]),
            )

        transaction_data = [
            {
                "transaction_id": 1,
                "order_id": 1,
                "payment_method": "Credit Card",
                "amount": 160000,
                "status": "Paid",
            },
            {
                "transaction_id": 2,
                "order_id": 2,
                "payment_method": "Wire Transfer",
                "amount": 150000,
                "status": "Paid",
            },
            {
                "transaction_id": 3,
                "order_id": 3,
                "payment_method": "Check",
                "amount": 180000,
                "status": "Pending",
            },
            {
                "transaction_id": 4,
                "order_id": 4,
                "payment_method": "Check",
                "amount": 260000,
                "status": "Paid",
            },
            {
                "transaction_id": 5,
                "order_id": 5,
                "payment_method": "Wire Transfer",
                "amount": 100000,
                "status": "Unpaid",
            },
            {
                "transaction_id": 6,
                "order_id": 6,
                "payment_method": "Credit Card",
                "amount": 800000,
                "status": "Pending",
            },
        ]

        for data in transaction_data:
            cursor.execute(
                "INSERT INTO mybe_transaction (transaction_id, order_id, payment_method, amount, status) VALUES (?, ?, ?, ?, ?)",
                (
                    data["transaction_id"],
                    data["order_id"],
                    data["payment_method"],
                    data["amount"],
                    data["status"],
                ),
            )

        # Commit changes and close connection
        conn.commit()
        conn.close()

### Explanation of Django Data Population Script:

#### Technical Perspective:

#  **Database Interaction:**
#    - The script interacts with a SQLite database using the `sqlite3` module to populate initial data into tables.

# **Data Preparation:**
#    - Data for various models like `EquipmentType`, `EquipmentListing`, `CustomerOrder`, etc., is prepared as dictionaries.

# **Data Insertion:**
#    - Iterating through the prepared data, SQL queries are executed to insert records into corresponding tables using cursor.execute().

# **Commit and Close:**
#    - After inserting all data, changes are committed to the database using `conn.commit()` and the database connection is closed.

# #### Non-Technical Perspective:

#  **Populating Initial Data:**
#    - This script fills the SQLite database with initial data required for the CRM application to function.
   
#.**Data Preparation:**
#    - Information about equipment types, equipment listings, customer orders, sales representatives, and transactions is prepared in structured formats.
   
# **Adding Data to Database:**
#    - The script goes through each data set and adds it to the database tables using SQL queries, ensuring that the database contains relevant information for the application to work correctly.
   
#  **Finalizing Changes:**
#    - Once all data is added, the changes are saved to the database, and the script closes the connection.

# The initial data required for the CRM application is prepared and inserted into the database, ensuring that the application has the necessary information to operate effectively in this file.
