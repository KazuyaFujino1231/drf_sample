from rest_framework import serializers

from sample.model.models.user import User


def my_validator(attrs):
    print("Userモデルの作成と更新時に共通でおこなうバリデーションです。")
    return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "birthday", "email", "phone_number")


class UserCreateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        validators = [my_validator]

    def validate_phone_number(self, value):
        print("create時に発生するphone_numberのバリデーションです。")
        return value

    def validate(self, attrs):
        print("create時に発生するフィールド全体に対するバリデーションです。")
        return attrs

    def save(self, **kwargs):
        print("create時に発生するsaveメソッドです。")
        return super().save(**kwargs)


class UserUpdateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        validators = [my_validator]

    def validate_phone_number(self, value):
        print("update時に発生するphone_numberのバリデーションです。")
        return value

    def validate(self, attrs):
        print("update時に発生するフィールド全体に対するバリデーションです。")
        return attrs

    def update(self, **kwargs):
        print("update時に発生するupdateメソッドです。")
        return super().update(**kwargs)
