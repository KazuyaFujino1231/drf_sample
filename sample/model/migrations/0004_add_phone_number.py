from django.db import migrations, models
from django.utils import timezone


def set_initial_phone_number(apps, schema_editor):
    User = apps.get_model("model", "User")
    # 例: メールアドレスがexample.comなら電話番号を"000-0000-0000"、それ以外は"999-9999-9999"
    for user in User.objects.all():
        if user.email.endswith("@example.com"):
            user.phone_number = "000-0000-0000"
        else:
            user.phone_number = "999-9999-9999"
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("model", "0003_user_phone_number"),
    ]

    operations = [
        migrations.RunPython(set_initial_phone_number),
    ]
