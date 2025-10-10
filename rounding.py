import pandas as pd
import numpy as np

# ========================
# USER SETTINGS
# ========================
INPUT_CSV  = "resonancecandidates_triples.csv"         # <-- Change this to your input file name
OUTPUT_CSV = "resonancecandidates_triples_rounded.csv"        # <-- Change this to your desired output file name
COLUMNS    = ["Period_inner",'Period_middle','Period_outer','Period Ratios_inner','Period Ratios_outer','delta_inner','delta_outer','Period_ttv_inner','Period_ttv_outer','n1','n2','n3','3 Body Equation']  # <-- Columns to format (must match CSV header)
SIGFIGS    = 6                   # <-- Number of significant figures
# ========================


def format_sigfigs(x, sigfigs=6):
    """
    Format a number to exactly `sigfigs` significant figures,
    including trailing zeros if necessary. Non-numeric values
    are returned unchanged as strings.
    """
    try:
        x = float(x)
        if x == 0:
            return f"{0:.{sigfigs - 1}f}"  # e.g. "0.00000" for sigfigs=6
        exponent = int(np.floor(np.log10(abs(x))))
        decimals = sigfigs - exponent - 1
        if decimals > 0:
            return f"{x:.{decimals}f}"  # fixed decimal with trailing zeros
        else:
            return f"{x:.{sigfigs}g}"    # scientific or integer if large
    except (ValueError, TypeError):
        return str(x)  # keep text as string


def round_csv_columns(input_csv, output_csv, columns, sigfigs=6):
    """
    Format specified columns in a CSV to exactly `sigfigs` significant figures.
    """
    # Read as strings to preserve formatting and avoid auto-conversion
    df = pd.read_csv(input_csv, dtype=str)

    for col in columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: format_sigfigs(x, sigfigs))
        else:
            print(f"⚠️ Warning: Column '{col}' not found in CSV.")

    df.to_csv(output_csv, index=False)
    print(f"✅ Rounded CSV saved to: {output_csv}")


if __name__ == "__main__":
    round_csv_columns(INPUT_CSV, OUTPUT_CSV, COLUMNS, SIGFIGS)