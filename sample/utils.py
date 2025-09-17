from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None and isinstance(response.data, dict):
        for field, errors in response.data.items():
            if isinstance(errors, list):
                new_errors = []
                for err in errors:
                    if isinstance(err, dict) and "message" in err and "code" in err:
                        new_errors.append(err)
                    else:
                        code = getattr(err, "code", "invalid")
                        new_errors.append({"message": str(err), "code": code})
                response.data[field] = new_errors
    return response
