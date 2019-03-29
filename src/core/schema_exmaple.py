from jsonschema import validate

validate([2, 3], {"maxItems": 2})

schema = {
    "type": "object",
    "properties": {
        "price": {"type": "number"},
        "name": {"type": "string"},
    },
}
validate(instance={"name": "Eggs", "price": 34.99}, schema=schema)
validate(instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema)
