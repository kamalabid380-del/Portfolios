from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pinterest',
            field=models.URLField(blank=True),
        ),
    ]