from django.db import models
from jsonfield import JSONField

class EquipmentType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_id}: {self.type_name}"


class EquipmentListing(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return f"{self.listing_id}: {self.make} {self.model} ({self.year}) - ${self.price}"


class CustomerOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    listing_id = models.IntegerField()
    customer = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
        return f"{self.order_id}- {self.listing_id}-{self.customer} - {self.quantity} - ${self.total_price}"

class CustomerList(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def phone(self):
        return "-".join([self.phone[:3], self.phone[3:6], self.phone[6:]])

    def __str__(self):
        return f"{self.customer_id}: {self.name} - {self.contact} ({self.email})"


class SalesRepresentative(models.Model):
    rep_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.rep_id}: {self.name} - {self.email} ({self.phone})"

class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Order ID: {self.order_id}, Status: {self.status}"

    def formatted_amount(self):
        return "${:,.2f}".format(self.amount)


# Creates models = O.R.M. Object relational mapping
# can create diffrent db models
# & have it automattically creates your schema in
# in diffrent langs like sqllite3, sql, mongo or what every you choose
# Next go to admin.py in this folder
