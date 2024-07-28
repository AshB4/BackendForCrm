from django.db import migrations
import json


def load_customer_list_data(apps, schema_editor):
    pass  # Temporarily disable data loading

    # CustomerList = apps.get_model("mybe", "CustomerList")
    # with open("initial_data.json", "r") as file:
    #     customer_list_data = json.load(file)
    #     for entry in customer_list_data:
    #         CustomerList.objects.create(
    #             name=entry["name"],
    #             email=entry["email"],
    #             # Add more fields as needed
    #         )


class Migration(migrations.Migration):

    dependencies = [
        (
            "mybe",
            "0003_rename_customer_customerlist",
        ),  # Replace with the previous migration name
    ]

    operations = [
        migrations.RunPython(load_customer_list_data),
    ]
