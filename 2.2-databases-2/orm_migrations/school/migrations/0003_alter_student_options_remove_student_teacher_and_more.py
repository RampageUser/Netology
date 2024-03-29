# Generated by Django 4.2.3 on 2023-07-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Ученика', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
