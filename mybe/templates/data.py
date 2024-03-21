from models import (
    EquipmentType,
    EquipmentListing,
    CustomerOrder,
    Customer,
    SalesRepresentative,
    Transaction,
)

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
    EquipmentType.objects.create(**data)

equipment_listing_data = [
    {
        "listing_id": 1,
        "type_id": 1,
        "make": "Volvo",
        "model": "VNL64T780",
        "year": 2018,
        "price": 80000,
    },
    {
        "listing_id": 2,
        "type_id": 2,
        "make": "Freightliner",
        "model": "Cascadia",
        "year": 2016,
        "price": 70000,
    },
    {
        "listing_id": 3,
        "type_id": 3,
        "make": "Peterbilt",
        "model": "389",
        "year": 2015,
        "price": 120000,
    },
    {
        "listing_id": 4,
        "type_id": 4,
        "make": "Caterpillar",
        "model": "320D",
        "year": 2019,
        "price": 150000,
    },
    {
        "listing_id": 5,
        "type_id": 5,
        "make": "John Deere",
        "model": "310SL",
        "year": 2017,
        "price": 60000,
    },
    {
        "listing_id": 6,
        "type_id": 6,
        "make": "Komatsu",
        "model": "PC200-8",
        "year": 2015,
        "price": 90000,
    },
    {
        "listing_id": 7,
        "type_id": 7,
        "make": "Caterpillar",
        "model": "D6T",
        "year": 2016,
        "price": 130000,
    },
    {
        "listing_id": 8,
        "type_id": 8,
        "make": "Volvo",
        "model": "VHD64B200",
        "year": 2017,
        "price": 100000,
    },
]

for data in equipment_listing_data:
    EquipmentListing.objects.create(**data)

    customer_order_data = [
    {"order_id": 1, "listing_id": 1, "customer": "ABC Construction", "quantity": 2, "total_price": 160000},
    {"order_id": 2, "listing_id": 4, "customer": "XYZ Excavation", "quantity": 1, "total_price": 150000},
    {"order_id": 3, "listing_id": 5, "customer": "DEF Contractors", "quantity": 3, "total_price": 180000},
    {"order_id": 4, "listing_id": 7, "customer": "GHI Construction", "quantity": 2, "total_price": 260000},
    {"order_id": 5, "listing_id": 8, "customer": "JKL Builders", "quantity": 1, "total_price": 100000},
    {"order_id": 6, "listing_id": 9, "customer": "MNO Contractors", "quantity": 1, "total_price": 800000},
]

for data in customer_order_data:
    CustomerOrder.objects.create(**data)

CustomerOrder = [
    {"customer_id": 1, "name": "ABC Construction", "contact": "John Smith", "email": "john@abcconstruction.com", "phone": "+1 (555) 123-4567"},
    {"customer_id": 2, "name": "XYZ Excavation", "contact": "Jane Doe", "email": "jane@xyzexcavation.com", "phone": "+1 (555) 987-6543"},
    {"customer_id": 3, "name": "DEF Contractors", "contact": "Mike Johnson", "email": "mike@defcontractors.com", "phone": "+1 (555) 789-0123"},
    {"customer_id": 4, "name": "GHI Construction", "contact": "Sarah Johnson", "email": "sarah@ghiconstruction.com", "phone": "+1 (555) 111-2222"},
    {"customer_id": 5, "name": "JKL Builders", "contact": "Tom Smith", "email": "tom@jklbuilders.com", "phone": "+1 (555) 333-4444"},
{"customer_id": 6, "name": "MNO Contractors", "contact": "Emily Brown", "email": "emily@mnocontractors.com", "phone": "+1 (555) 555-6666"},
]
for data in CustomerOrder:
    Customer.objects.create(**data)

SalesRepresentative = [
{"rep_id": 1, "name": "Alice Brown", "email": "alice@company.com", "phone": "+1 (555) 111-2222"},
{"rep_id": 2, "name": "Bob White", "email": "bob@company.com", "phone": "+1 (555) 333-4444"},
{"rep_id": 3, "name": "Carol Green", "email": "carol@company.com", "phone": "+1 (555) 555-6666"},
{"rep_id": 4, "name": "David Lee", "email": "david@company.com", "phone": "+1 (555) 777-8888"},
{"rep_id": 5, "name": "Rachel Wong", "email": "rachel@company.com", "phone": "+1 (555) 999-0000"},
{"rep_id": 6, "name": "Michael Chen", "email": "michael@company.com", "phone": "+1 (555) 123-4567"},
]
for data in SalesRepresentative:
    SalesRepresentative.objects.create(**data)

transaction_data = [
{"transaction_id": 1, "order_id": 1, "payment_method": "Credit Card", "amount": 160000, "status": "Paid"},
{"transaction_id": 2, "order_id": 2, "payment_method": "Wire Transfer", "amount": 150000, "status": "Paid"},
{"transaction_id": 3, "order_id": 3, "payment_method": "Check", "amount": 180000, "status": "Pending"},
{"transaction_id": 4, "order_id": 4, "payment_method": "Check", "amount": 260000, "status": "Paid"},
{"transaction_id": 5, "order_id": 5, "payment_method": "Wire Transfer", "amount": 100000, "status": "Unpaid"},
{"transaction_id": 6, "order_id": 6, "payment_method": "Credit Card", "amount": 800000, "status": "Pending"},
]
for data in transaction_data:
    Transaction.objects.create(**data)
