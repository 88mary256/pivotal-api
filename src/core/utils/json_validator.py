from jsonschema import validate

class JsonValidator:

    @staticmethod
    def json_validator(self, instance, schema):
        #assert isinstance(instance, object)
        validate(instance=instance, schema=schema)
        
