import argparse
import os
import uuid

from helpers import load_data_from_json, generate_pdf, save_file


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate PDF from JSON data and template.')
    parser.add_argument('json_file', help='Path to the JSON file')
    parser.add_argument('template_path', help='Path to the template file (e.g., transactions.html)')
    parser.add_argument('style_path', nargs='?', default='base.css', help='Path to the style file (e.g., base.css)')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    records = load_data_from_json(args.json_file)
    content = {
        'header': True,
        'footer': True,
        'date_from': '2020-03-04',  # YYYY-MM-DD
        'date_to': '2022-04-04',  # YYYY-MM-DD
        'records': records,
    }
    pdf = generate_pdf(args.template_path, args.style_path, content)
    filename = f'out/{uuid.uuid4()}.pdf'
    save_file(filename, pdf)
    print('PDF generated successfully.')
    os.system(f'open {filename}')
