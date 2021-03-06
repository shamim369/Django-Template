# Generated by Django 3.2.11 on 2022-02-17 05:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('psf_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Address')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('image', models.ImageField(max_length=255, upload_to=None)),
                ('document', models.FileField(max_length=255, upload_to=None)),
                ('youtube_link', models.URLField(max_length=255, verbose_name='Youtube Link')),
                ('num_stars', models.IntegerField()),
                ('publish_date', models.DateField(verbose_name='Publish Date')),
                ('publish_time', models.TimeField(verbose_name='Publish Time')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_active', models.BooleanField(default=False)),
                ('binary_data', models.BinaryField(blank=True, null=True, verbose_name='Binary')),
                ('duration_data', models.DurationField(blank=True, null=True, verbose_name='Duration')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psf_app.author')),
                ('tag', models.ManyToManyField(to='psf_app.Tag')),
                ('track', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psf_app.track')),
            ],
        ),
    ]
