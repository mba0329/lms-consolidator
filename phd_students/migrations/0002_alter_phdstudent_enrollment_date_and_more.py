# Generated by Django 5.1.3 on 2025-05-28 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phd_students", "0001_initial"),
        ("professors", "0001_initial"),
        ("research_groups", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phdstudent",
            name="enrollment_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="phdstudent",
            name="research_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="phd_students",
                to="research_groups.researchgroup",
            ),
        ),
        migrations.AlterField(
            model_name="phdstudent",
            name="supervisor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="phd_students",
                to="professors.professor",
            ),
        ),
    ]
