# Generated by Django 2.1.1 on 2018-09-14 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance_borrow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='borrow',
            new_name='borrower',
        ),
    ]
