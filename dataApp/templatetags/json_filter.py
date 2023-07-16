import json
from django import template

register = template.Library()

@register.filter
def format_json(value):
    try:
        parsed_value = json.loads(value)
        return json.dumps(parsed_value, indent=4)
    except ValueError:
        return value
