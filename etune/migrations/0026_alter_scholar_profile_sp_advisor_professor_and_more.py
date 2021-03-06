# Generated by Django 4.0.1 on 2022-02-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0025_scholar_profile_sp_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_advisor_professor',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_bro_n_sis',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_child_in_the_patron',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_career',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_firstname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_lastname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_middlename',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_status_married',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_statuslife',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_tel_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_title',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_father_workplace',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_firstname_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_firstname_th',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_grade',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_income_source',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_lastname_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_lastname_th',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_loan',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_major',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_middlename_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_middlename_th',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_money_received_scholar',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_career',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_firstname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_lastname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_middlename',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_status_married',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_statuslife',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_tel_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_title',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_mother_workplace',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_parttime',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_parttime_income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_parttime_type',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_path_to_pdf_json',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_patron_career',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_patron_relation',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_patron_tel_no',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_patron_workplace',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_received_scholar',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_report',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_std_address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_std_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_std_tel_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_title_en',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_title_th',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='scholar_profile',
            name='sp_year_received_scholar',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
