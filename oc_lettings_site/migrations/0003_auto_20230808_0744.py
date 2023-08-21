# Generated by Django 3.0 on 2023-08-08 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20230808_0739'),
    ]

    operations = [
        
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Letting',      
                ),
                migrations.DeleteModel(
                    name='Address',
                ),
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="Address",
                    table="lettings_address",
                ),
                migrations.AlterModelTable(
                    name="Letting",
                    table="lettings_letting",
                ),
                migrations.AlterModelTable(
                    name="Profile",
                    table="profiles_profile",
                ),
            ]     
        )
    ]