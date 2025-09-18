from rest_framework import serializers

from sample.model.models.user import User


def my_validator(attrs):
    print("3, Userモデルの作成と更新時に共通でおこなうバリデーションです。")
    print("\tattrs:", attrs)
    return attrs


class UserSerializer(serializers.ModelSerializer):
    # CreateとUpdateでバリデーションが共通であればシリアライザを分ける必要はない
    class Meta:
        model = User
        fields = ("id", "name", "birthday", "email")


class UserCreateSerializer(UserSerializer):
    # Create時のバリデーションと、Update時のバリデーションが違う場合はこのようにシリアライザを分けるのが良い
    class Meta(UserSerializer.Meta):
        validators = [my_validator]
    
    def run_validation(self, data=...):
        print("-- バリデーションの入り口です --")
        print("0, run_validation()は以下の順序で処理されます。")
        print("1, to_internal_value()の呼び出し")
        print("2, Meta.validatorsの呼び出し")
        print("3, validate()の呼び出し")
        return super().run_validation(data)

    def to_internal_value(self, data):
        try:
            print("1-1, run_validation()からto_internal_value()が呼ばれ、モデルフィールドに基づくバリデーション処理が行われます。")
            print("\tdata:", data)
            return super().to_internal_value(data)
        except serializers.ValidationError as exc:
            # ここでexc.detailを書き換えてカスタムメッセージにできる
            if "email" in exc.detail:
                exc.detail["email"] = ["このメールアドレスは既に使われています。"]
            raise exc

    def validate_name(self, value):
        print("1-2, モデルフィールドに基づくバリデーション処理が問題なければ、validate_xxxメソッドが呼ばれます。")
        print("\tvalue:", value)
        return value
    
    def run_validators(self, value):
        print("2, to_internal_value()が問題なければrun_validators()によりMetaのvalidatorsが呼ばれます。")
        print("\tvalue:", value)
        return super().run_validators(value)

    def validate(self, attrs):
        print("3, run_validators()が問題なければフィールド全体に対するバリデーションです。")
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

