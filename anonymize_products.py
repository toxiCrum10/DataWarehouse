import pandas as pd

df = pd.read_csv('datasets/Shoptet/Products_temp.csv')

# Anonymizované stĺpce
cols_to_anonymize = ['purchasePrice', 'relativeMargin', 'absoluteMargin']
for col in cols_to_anonymize:
    if col in df.columns:
        df[col] = '***'

df.to_csv('datasets/Shoptet/Products_anonymized.csv', index=False)
print("✅ Produkty anonymizované a uložené do: datasets/Shoptet/Products_anonymized.csv")

