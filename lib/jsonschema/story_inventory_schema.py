"""
This module contains story/inventory jsonschema
"""

story_inventory_schema = {
  "type": "object",
  "properties": {
    "sold": {
      "type": "integer"
    },
    "On fire": {
      "type": "integer"
    },
    "string": {
      "type": "integer"
    },
    "unavailable": {
      "type": "integer"
    },
    "pending": {
      "type": "integer"
    },
    "available": {
      "type": "integer"
    },
  },
  "required": [
    "sold",
  ]
}
