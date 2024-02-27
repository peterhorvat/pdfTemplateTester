from datetime import datetime
from pathlib import Path
import os
import json

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

import filters

font_config = FontConfiguration()


def save_file(out_file: str, content: bytes):
    Path(out_file).write_bytes(content)


def load_data_from_json(json_file: str) -> object:
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


def build_html_template(template_path: str, content: dict) -> str:
    # jinja_env = Environment(loader=PackageLoader('pdf', 'templates'),
    #                         autoescape=select_autoescape(['html']))

    jinja_env = Environment(loader=FileSystemLoader("templates/"))
    for name in dir(filters):
        if callable(getattr(filters, name)):
            jinja_env.filters[name] = getattr(filters, name)
    template = jinja_env.get_template(template_path)
    return template.render(content)


def generate_pdf(template_path: str, style_path: str, content: dict) -> bytes:
    html = build_html_template(template_path, content)
    pdf_html = HTML(string=html, base_url='.')
    pdf_css = CSS(f'templates/styles/{style_path}', font_config=font_config)
    pdf_content = pdf_html.write_pdf(stylesheets=[pdf_css], presentational_hints=True, font_config=font_config)
    # pdf_render = pdf_html.render(stylesheets=[pdf_css])
    return pdf_content


def create_directory(directory_path: str):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def format_date(date: datetime) -> str:
    return datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y %H:%M:%S')
