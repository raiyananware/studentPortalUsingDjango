# Generated by Django 4.2.5 on 2024-02-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalApp', '0007_course_topic_subtopic_lecture_completedlecture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topicType',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]