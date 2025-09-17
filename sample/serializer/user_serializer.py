from rest_framework import serializers

from sample.model.models.user import User


def my_validator(attrs):
    print("3, Userモデルの作成と更新時に共通でおこなうバリデーションです。")
    print("\tattrs:", attrs)
    return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "birthday", "email")


class UserCreateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        validators = [my_validator]

    def to_internal_value(self, data):
        try:
            print(
                "1, Userモデルの定義に基づいて、入力データを内部表現に変換します。（モデル定義に合っているか確認するためのバリデーションもここで実行されます）"
            )
            print("\tdata:", data)
            return super().to_internal_value(data)
        except serializers.ValidationError as exc:
            # exc.detailはOrderedDict。全てのエラーをラップ
            for field, errors in exc.detail.items():
                new_errors = []
                for err in errors:
                    # 既にdict形式ならそのまま、strならラップ
                    if isinstance(err, dict) and "message" in err and "code" in err:
                        new_errors.append(err)
                    else:
                        code = getattr(err, "code", "invalid")
                        new_errors.append({"message": str(err), "code": code})
                exc.detail[field] = new_errors
            raise exc

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("このメールアドレスは既に登録されています。")
        return value

    def validate_name(self, value):
        print("2, create時に発生するnameのバリデーションです。")
        print("\tvalue:", value)
        return value

    def validate(self, attrs):
        print("4, create時に発生するフィールド全体に対するバリデーションです。")
        print("\tattrs:", attrs)
        return attrs

    def save(self, **kwargs):
        print("create時に発生するsaveメソッドです。")
        return super().save(**kwargs)


class UserUpdateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        validators = [my_validator]

    def validate_name(self, value):
        print("update時に発生するnameのバリデーションです。")
        print("value:", value)
        return value

    def validate(self, attrs):
        print("update時に発生するフィールド全体に対するバリデーションです。")
        print("attrs:", attrs)
        return attrs

    def update(self, **kwargs):
        print("update時に発生するupdateメソッドです。")
        return super().update(**kwargs)
