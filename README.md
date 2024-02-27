# PDF Template Testing Tools

### Requirements:
- Python 3.8+

### Parameters:
  `json_file`     - Path to the JSON file

  `template_path` - Path to the template file (e.g., transactions.html)

  `style_path`    - Path to the style file (e.g., base.css)

  `date_from`     - Date from (e.g., 2020-03-04)

  `date_to`       - Date to (e.g., 2020-03-04)

### Usage:
```
1. Create virtual environment
2. Install requirements.txt with ```pip install -r requirements.txt```
3. Run main.py (with parameters)

Shell commands for MacOS:
- ``
```

#### FLTK Order Report
```shell
python main.py data/fltk_orders.json fltk_order_report.html
```

#### Onramp Offramp Report
```shell
python main.py data/onramp_offramp_report.json onramp_offramp_report.html
```

#### Crypto Transactions Report
```shell
python main.py data/crypto_transactions_report.json crypto_transactions_report.html
```

### Example with defined date range:
```shell
python main.py data/onramp_offramp_report.json onramp_offramp_report.html --date_from=2021-01-01 --date_to=2023-01-01
```

### Example with defined date range and style:
```shell
python main.py data/onramp_offramp_report.json onramp_offramp_report.html --date_from=2021-01-01 --date_to=2023-01-01 --style_path=style.css
```

### Example with added account summary to template:
```shell
python main.py data/crypto_transactions_report.json crypto_transactions_report.html --summary
```