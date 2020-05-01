# Generated by Django 3.0.5 on 2020-04-30 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('title', models.CharField(max_length=140, null=True, verbose_name='Tittel')),
                ('place', models.CharField(blank=True, max_length=140, null=True, verbose_name='Sted')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Slutt')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Beskrivelse')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_event_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_event_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-start', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Dato påmeldt')),
                ('has_paid', models.BooleanField(default=False, verbose_name='Har betalt')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bruker')),
            ],
            options={
                'verbose_name': 'Deltaker',
                'verbose_name_plural': 'Deltakere',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='events', through='events.Participant', to=settings.AUTH_USER_MODEL, verbose_name='Påmeldte'),
        ),
    ]