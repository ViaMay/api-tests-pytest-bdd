"""
This module contains story order post jsonschema
"""

story_order_post_schema = {
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "petId": {
      "type": "integer"
    },
    "quantity": {
      "quantity": "integer"
    },
    "shipDate": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "complete": {
      "type": "boolean"
    },
  },
  "required": [
    "id",
    "petId",
    "quantity",
    "shipDate",
    "status",
    "complete",
  ]
}
