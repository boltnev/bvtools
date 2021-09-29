#!/usr/bin/env python
import sys
from jinja2 import Template

template = Template("""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:4
#EXT-X-MEDIA-SEQUENCE:{{media_sequence}}
{% for line in lines %}
#EXTINF:4.000000,
{{ line -}}
{% endfor %}
#EXT-X-ENDLIST
""")


lines = [l for l in sys.stdin.read().split("\n") if l]

result = template.render(
    media_sequence=len(lines)-2,
    lines=lines,
)

print(result)
