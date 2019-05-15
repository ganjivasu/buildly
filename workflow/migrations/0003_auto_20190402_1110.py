# Generated by Django 2.0.7 on 2019-04-02 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0002_auto_20190401_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='coregroup',
            name='is_global',
            field=models.BooleanField(default=False, verbose_name='Is global group'),
        ),
        migrations.AddField(
            model_name='coregroup',
            name='is_org_level',
            field=models.BooleanField(default=False, verbose_name='Is organization level group'),
        ),
        migrations.AddField(
            model_name='coregroup',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
    ]