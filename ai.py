import pandas as pd

data = pd.read_csv(
    'data/contributions-AIConsult2020.csv',
    encoding='latin-1',
    sep=';',          # EU portal CSVs often use semicolons
    on_bad_lines='skip'  # skip malformed rows for now
)


# Step 1: understand the respondents
print(data['User type'].value_counts())
print(data['Country'].value_counts().head(20))
print(data['Organisation size'].value_counts())

# Step 2: isolate the columns you care about
metadata_cols = ['Reference', 'User type', 'Organisation name', 'Country', 'Scope', 'Transparency register number']
likert_cols = [c for c in data.columns if '1-5' in c]
text_cols = [c for c in data.columns if c not in metadata_cols + likert_cols]

print(f"\n{len(likert_cols)} Likert columns, {len(text_cols)} text columns")

pdf_col = 'You can upload a document here:\n\n'

has_pdf = data[pdf_col].notna()
print(f"Responses with PDF: {has_pdf.sum()}")
print(f"Responses without PDF: {(~has_pdf).sum()}")

# breakdown by actor type
print(data.groupby('User type')[pdf_col].apply(lambda x: x.notna().sum()).sort_values(ascending=False))