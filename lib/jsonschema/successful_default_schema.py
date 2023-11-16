"""
This module contains successful default jsonschema
"""

successful_default_schema = {
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
