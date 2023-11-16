"""
This module contains error default jsonschema
"""

error_default_schema = {
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
  ]
}
