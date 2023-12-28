import argparse
import os
import uuid
from datetime import datetime

from helpers import load_data_from_json, generate_pdf, save_file, create_directory, format_date


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate PDF from JSON data and template.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    parser.add_argument('template_path', type=str, help='Path to the template file (e.g., transactions.html)')
    parser.add_argument('--style_path', type=str, nargs='?', default='base.css',
                        help='Path to the style file (e.g., base.css)')
    parser.add_argument('--date_from', type=str, nargs='?', default='2020-03-04', help='Date from (e.g., 2020-03-04)')
    parser.add_argument('--date_to', type=str, nargs='?', default='2022-04-04', help='Date to (e.g., 2020-03-04)')
    parser.add_argument('--summary', default=False, action='store_true',
                        help='Relevant only for Crypto Rransaction Report')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    records = load_data_from_json(args.json_file)
    summary = load_data_from_json('data/summary.json')

    content = {
        'header': True,
        'footer': True,
        'date_from': args.date_from,
        'date_to': args.date_to,
        'records': records,
        'summary': summary if args.summary else None,
        'fiat_currency': 'EUR',
        'created_at': format_date(datetime.now())
    }
    pdf = generate_pdf(args.template_path, args.style_path, content)
    create_directory('out')
    filename = f'out/{uuid.uuid4()}.pdf'
    save_file(filename, pdf)
    print('PDF generated successfully.')
    os.system(f'open {filename}')
