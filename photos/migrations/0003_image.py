# # Generated by Django 3.0.8 on 2020-08-01 21:12

# from django.db import migrations, models
# import django.db.models.deletion


# class Migration(migrations.Migration):

#     dependencies = [
#         ('photos', '0002_category'),
#     ]

#     operations = [
#         migrations.CreateModel(
#             name='Image',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('image', models.ImageField(upload_to='images/')),
#                 ('name', models.CharField(max_length=60)),
#                 ('description', models.TextField()),
#                 ('author', models.CharField(default='admin', max_length=40)),
#                 ('date', models.DateTimeField(auto_now_add=True)),
#                 ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category')),
#                 ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location')),
#             ],
#             options={
#                 'ordering': ['date'],
#             },
#         ),
#     ]
