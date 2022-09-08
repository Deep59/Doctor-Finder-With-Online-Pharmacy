# Generated by Django 2.0 on 2021-04-08 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_status', models.BooleanField(default=False)),
                ('appointment_bookdate', models.DateField()),
                ('appotime', models.TimeField(default=False)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail_date', models.DateField()),
                ('mstart_time', models.TimeField()),
                ('mend_time', models.TimeField()),
                ('estart_time', models.TimeField()),
                ('eend_time', models.TimeField()),
                ('status', models.BooleanField(default=False)),
                ('morningday', models.CharField(max_length=500)),
                ('eveningday', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField(default=10)),
                ('Address', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('disease', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Keywords', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='img/')),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('Contact', models.BigIntegerField(default=122)),
                ('Year_of_experience', models.IntegerField(default=2)),
                ('Clinic_name', models.CharField(max_length=50)),
                ('Specialazion', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('Gender', models.CharField(default='', max_length=10)),
                ('birthdate', models.DateField(blank=True, default='2021-12-12')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('about_doc', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(default='', max_length=20)),
                ('profile_pic', models.FileField(default='doc_male.png', upload_to='img/')),
                ('discriptions', models.TextField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=200)),
                ('Answer', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=50)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField(default=0)),
                ('Description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('Contact', models.BigIntegerField()),
                ('Ordername', models.CharField(max_length=50)),
                ('Total', models.BigIntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.BigIntegerField()),
                ('Price', models.BigIntegerField()),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField(default=10)),
                ('Address', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('birthdate', models.DateField(blank=True, default='2021-12-12')),
                ('blood_group', models.CharField(blank=True, max_length=10)),
                ('blood_presure', models.CharField(blank=True, max_length=10)),
                ('sugar', models.CharField(blank=True, max_length=10)),
                ('Haemoglobin', models.CharField(blank=True, max_length=10)),
                ('profile_pic', models.FileField(default='patient_icon.png', upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PharmaName', models.CharField(max_length=50)),
                ('FullName', models.CharField(max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('InstitutionTrainning', models.CharField(blank=True, max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('Countrycode', models.CharField(blank=True, max_length=30)),
                ('Shopname', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField(default=10)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(default='doc_male.png', upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_file', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Case')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productname', models.CharField(max_length=50)),
                ('ProductDescription', models.CharField(max_length=50)),
                ('Price', models.BigIntegerField()),
                ('Expirydate', models.DateField(max_length=50)),
                ('Mfgdate', models.DateField(max_length=50)),
                ('Details', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='img/')),
                ('status', models.BooleanField(default=False)),
                ('Category', models.CharField(max_length=50)),
                ('Quantity', models.BigIntegerField(default=5)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
                ('pharmacy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productname', models.CharField(max_length=200)),
                ('Quantity', models.BigIntegerField()),
                ('Price', models.BigIntegerField()),
                ('Total', models.BigIntegerField()),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
                ('Cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=50)),
                ('Otp', models.CharField(max_length=50)),
                ('is_create', models.DateTimeField(auto_now_add=True)),
                ('is_update', models.DateTimeField(auto_now_add=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='order_product',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient'),
        ),
        migrations.AddField(
            model_name='order',
            name='pharmacy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pharmacy'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AddField(
            model_name='faq',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='case',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Doctor'),
        ),
        migrations.AddField(
            model_name='case',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient'),
        ),
        migrations.AddField(
            model_name='availability',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='availability_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.availability'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Patient'),
        ),
    ]
