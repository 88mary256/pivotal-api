from jsonschema import validate


class JsonValidator:

    @staticmethod
    def json_validator(instance, schema):
        validate(instance=instance, schema=schema)
        pass