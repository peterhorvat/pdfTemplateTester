def format_date(value):
    # If value is a string, convert it to a datetime object first
    if isinstance(value, str):
        from datetime import datetime
        value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")

    # Return the formatted date string
    return value.strftime('%d.%m.%Y')


def shorten_with_dots(value):
    # First check if the value is None
    if value is None:
        return ""  # Return an empty string or some default value indicating a missing value

    if len(value) > 8:  # Check if the string is longer than the sum of characters to be shown
        return f"{value[:4]}...{value[-4:]}"

    return value  # Return the original string if it's not long enough


def format_amount_no_symbol(value, decimals=2, allow_three_decimals=False):
    if value is None:
        return ""

    # Convert string to float if necessary
    try:
        numeric_value = float(value)
    except ValueError:
        # Return the original value or some error indication if conversion fails
        return value

    # Adjust decimal places based on the input and the allow_three_decimals flag
    if allow_three_decimals:
        # Convert to string to check the number of decimal places
        value_str = f"{value}"
        decimal_places = len(value_str.split('.')[-1]) if '.' in value_str else 0
        decimals = min(3, decimal_places)  # Use actual decimal places up to a maximum of 3

    # Format the number with the desired number of decimal places.
    formatted_number = f"{numeric_value:,.{decimals}f}"

    # Manually replace the thousands separator and decimal point for European formatting
    formatted_number = formatted_number.replace(",", "X").replace(".", ",").replace("X", ".")

    return formatted_number


def format_crypto_amount(value):
    if value is None:
        return ""

    try:
        numeric_value = float(value)
    except ValueError:
        return value

    # Determine if the value is an integer or a float and format accordingly
    if numeric_value.is_integer():
        return f"{int(numeric_value):,}".replace(",", ".")  # Use dot as thousands separator
    else:
        # Format with up to 8 decimals without rounding up
        temp_formatted = f"{numeric_value:.9f}"
        formatted_number = temp_formatted[:temp_formatted.rfind(".") + 9]
        formatted_number = formatted_number.rstrip('0').rstrip('.')

        # Split into parts to handle thousands separator
        parts = formatted_number.split('.')
        parts[0] = parts[0].replace(",", ".")  # Replace commas temporarily to avoid conflict
        parts[0] = f"{int(parts[0]):,}".replace(",", ".")  # Format thousands and replace separator

        # Join integer and decimal parts, ensuring comma is used as decimal separator
        formatted_number = ','.join(parts) if len(parts) > 1 else parts[0]

        return formatted_number


def capitalize_first_letter(value):
    if not value or not isinstance(value, str):
        return ""
    return value[0].upper() + value[1:].lower()