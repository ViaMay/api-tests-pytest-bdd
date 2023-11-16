"""
This module contains user get jsonschema
"""

user_get_schema = {
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "username": {
      "type": "string"
    },
    "firstName": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "password": {
      "type": "string"
    },
    "phone": {
      "type": "string"
    },
    "userStatus": {
      "type": "integer"
    },
  },
  "required": [
    "id",
    "username",
    "userStatus",
  ]
}
