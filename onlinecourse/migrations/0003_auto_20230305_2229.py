# Generated by Django 3.1.3 on 2023-03-05 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230305_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='course',
            new_name='courses',
        ),
        migrations.RemoveField(
            model_name='question',
            name='questionGrade',
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.question'),
        ),
    ]
