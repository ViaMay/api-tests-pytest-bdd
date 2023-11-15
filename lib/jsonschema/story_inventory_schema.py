"""
This module contains story/inventory jsonschema
"""

story_inventory_schema = {
  "type": "object",
  "properties": {
    "sold": {
      "type": "integer"
    },
  },
  "required": [
    "sold",
  ]
}
