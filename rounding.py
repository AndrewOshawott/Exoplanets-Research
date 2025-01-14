import pandas as pd
import math
from decimal import Decimal, getcontext, ROUND_HALF_UP

input_file = "multiplanet_matches.csv"
output_file = "multiplanet_matches_rounded.csv"


def format_sigfigs(num, sigfigs=6):

    if pd.isna(num):
        return num

    try:
        num_float = float(num)
    except ValueError:
        return num

    if num_float == 0:
        return '0.' + '0' * (sigfigs - 1)

    sign = '-' if num_float < 0 else ''
    num_abs = abs(num_float)

    getcontext().prec = sigfigs + 2

    exponent = int(math.floor(math.log10(num_abs)))

    decimal_places = sigfigs - exponent - 1

    d = Decimal(num_abs)

    if decimal_places >= 0:
        quantize_str = '1.' + '0' * decimal_places
    else:
        quantize_str = '1E' + str(-decimal_places)

    rounded = d.quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP)

    if decimal_places >= 0:
        fmt = f"{{0:.{decimal_places}f}}".format(rounded)
    else:
        fmt = f"{{0:.0f}}".format(rounded)

    if '.' in fmt:
        integer_part, fractional_part = fmt.split('.')
        fractional_part = fractional_part.ljust(decimal_places, '0')
        fmt = f"{integer_part}.{fractional_part}"

    sigfigs_count = len(fmt.replace('.', '').replace('-', '').lstrip('0'))

    if sigfigs_count < sigfigs:
        if '.' in fmt:
            needed = sigfigs - sigfigs_count
            fmt += '0' * needed
        else:
            fmt += '.' + '0' * (sigfigs - sigfigs_count)

    return sign + fmt


def process_csv(input_file, output_file):
    columns_to_round = ["Period_inner", "Period_outer", "Period Ratios", "delta", "Period_ttv"]

    try:
        df = pd.read_csv(input_file, dtype=str)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return
    except Exception as e:
        print(f"Error reading '{input_file}': {e}")
        return

    for col in columns_to_round:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            print(f"Warning: Column '{col}' not found in the CSV.")

    for col in columns_to_round:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: format_sigfigs(x) if pd.notnull(x) else x)

    try:
        df.to_csv(output_file, index=False)
        print(f"Processed CSV saved to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}")


process_csv(input_file, output_file)
