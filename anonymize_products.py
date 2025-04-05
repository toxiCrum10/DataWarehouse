import pandas as pd

# Načítanie pôvodného CSV súboru
df = pd.read_csv('datasets/Shoptet/Products_part1.csv')

# Anonymizované stĺpce
cols_to_anonymize = ['purchasePrice', 'relativeMargin', 'absoluteMargin']
for col in cols_to_anonymize:
    if col in df.columns:
        df[col] = '***'

# Oprava ceny - prevod na eurá (pre hodnoty 485 na 4.85)
df['price'] = df['price'] / 100
df['standardPrice'] = df['standardPrice'] / 100
df['purchasePrice'] = df['purchasePrice'] / 100

# Uloženie anonymizovaného a opraveného súboru
df.to_csv('datasets/Shoptet/Products_anonymized.csv', index=False)
print("Produkty anonymizované a ceny opravené a uložené do: datasets/Shoptet/Products_anonymized.csv")

