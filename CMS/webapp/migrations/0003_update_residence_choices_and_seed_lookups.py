from django.db import migrations


def seed_lookup_data(apps, schema_editor):
    GenderOption = apps.get_model('webapp', 'GenderOption')
    CasteCategory = apps.get_model('webapp', 'CasteCategory')
    Nationality = apps.get_model('webapp', 'Nationality')
    BloodGroup = apps.get_model('webapp', 'BloodGroup')
    Religion = apps.get_model('webapp', 'Religion')

    genders = ['Male', 'Female', 'Transgender']
    castes = ['General', 'SC', 'ST', 'BC - I', 'BC - II']
    nationalities = ['Indian', 'Other']
    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    religions = ['Hindu', 'Muslim', 'Christian', 'Parsi']

    for name in genders:
        GenderOption.objects.get_or_create(name=name, defaults={'is_active': True})

    for name in castes:
        CasteCategory.objects.get_or_create(name=name, defaults={'is_active': True})

    for name in nationalities:
        Nationality.objects.get_or_create(name=name, defaults={'is_active': True})

    for name in blood_groups:
        BloodGroup.objects.get_or_create(name=name, defaults={'is_active': True})

    for name in religions:
        Religion.objects.get_or_create(name=name, defaults={'is_active': True})


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0002_bloodgroup_castecategory_genderoption_nationality_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_lookup_data, migrations.RunPython.noop),
    ]


