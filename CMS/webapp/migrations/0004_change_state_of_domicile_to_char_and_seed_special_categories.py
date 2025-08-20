from django.db import migrations, models


def seed_special_categories(apps, schema_editor):
    SpecialCategory = apps.get_model('webapp', 'SpecialCategory')
    options = [
        'None',
        'NCC Quota',
        'Army Quota',
        'Ward of College/University Permanent Staff',
        'Ward of transferable Central / State Govt. Employee (eg. Rly, Bank, etc)',
        'Sport Quota',
        'NSS Quota',
        'Fine Arts Quota',
    ]
    for name in options:
        SpecialCategory.objects.get_or_create(name=name, defaults={'is_active': True})


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0004_alter_studentbasicinfo_place_of_residence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbasicinfo',
            name='state_of_domicile',
            field=models.CharField(max_length=100),
        ),
        migrations.RunPython(seed_special_categories, migrations.RunPython.noop),
    ]


