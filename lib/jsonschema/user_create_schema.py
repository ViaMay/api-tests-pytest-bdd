"""
This module contains user create jsonschema
"""

user_create_schema = {
  "type": "object",
  "properties": {
    "code": {
      "type": "integer"
    },
    "type": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
  },
  "required": [
    "code",
    "type",
    "message"
  ]
}
