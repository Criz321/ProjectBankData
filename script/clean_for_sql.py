from pathlib import Path
import pandas as pd

RAW = Path("raw")
CLEAN = Path("cleaned")
CLEAN.mkdir(exist_ok=True)

money_columns = {
    "users_data.csv": [
        "per_capita_income",
        "yearly_income",
        "total_debt"
    ],
    "cards_data.csv": [
        "credit_limit"
    ]
}

for file_name, columns in money_columns.items():

    df = pd.read_csv(RAW / file_name)

    for col in columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float)
        )

    df.to_csv(CLEAN / file_name, index=False)

print("Archivos limpios correctamente.")