from mybe.models import CustomerList

customers = [
    {
        "customer_id": 2,
        "name": "XYZ Excavation",
        "contact": "Jane Doe",
        "email": "jane@xyzexcavation.com",
        "phone": "+1 (555) 987-6543",
    },
    {
        "customer_id": 3,
        "name": "DEF Contractors",
        "contact": "Mike Johnson",
        "email": "mike@defcontractors.com",
        "phone": "+1 (555) 789-0123",
    },
    {
        "customer_id": 4,
        "name": "GHI Construction",
        "contact": "Sarah Johnson",
        "email": "sarah@ghiconstruction.com",
        "phone": "+1 (555) 111-2222",
    },
    {
        "customer_id": 5,
        "name": "JKL Builders",
        "contact": "Tom Smith",
        "email": "tom@jklbuilders.com",
        "phone": "+1 (555) 333-4444",
    },
    {
        "customer_id": 6,
        "name": "MNO Contractors",
        "contact": "Emily Brown",
        "email": "emily@mnocontractors.com",
        "phone": "+1 (555) 555-6666",
    },
    {
        "customer_id": 7,
        "name": "Sara Garcia",
        "contact": "Sara",
        "email": "sara@example.com",
        "phone": "901-234-5678",
    },
    {
        "customer_id": 8,
        "name": "David Martinez",
        "contact": "David",
        "email": "david@example.com",
        "phone": "234-567-8901",
    },
    {
        "customer_id": 9,
        "name": "Laura Taylor",
        "contact": "Laura",
        "email": "laura@example.com",
        "phone": "567-890-1234",
    },
    {
        "customer_id": 10,
        "name": "Chris Rodriguez",
        "contact": "Chris",
        "email": "chris@example.com",
        "phone": "890-123-4567",
    },
]

# Save each customer object in the list
for customer_data in customers:
    customer = CustomerList(**customer_data)
    customer.save()

print("Customer data saved successfully!")

#this is how to add in data via the command line
#use python3 manage.py shell then exit() to exit