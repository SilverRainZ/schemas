from textwrap import dedent
from sphinxnotes.any import Schema, Field

Project = Schema('project',
                 name=Field(unique=True, referenceable=True, required=True, form=Field.Form.LINES),
                 attrs={
                     'github': Field(),
                 },
                 content=Field(),
                 reference_template='🧰{{ title }}',
                 description_template=dedent('''
                {% if github %}
                .. |{{ github }}-badge| image:: https://img.shields.io/github/stars/{{ github }}.svg?style=social&label=Star&maxAge=2592000
                |{{ github }}-badge|
                {% endif %}

                {% if content %}{{ content }}{% endif %}
                 '''))
