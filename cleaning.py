import pandas as pd
import numpy as np

# Load the messy data
df = pd.read_csv('marketing_campaign_data_messy.csv')

# Clean column names: strip whitespace, lowercase, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Remove duplicate columns (keeping the first occurrence)
df = df.loc[:, ~df.columns.duplicated()]

# Clean 'spend' column: remove any character that isn't a digit, comma, or hyphen
df['spend'] = df['spend'].astype(str).str.replace(r'[^\d,-]', '', regex=True)

# Convert 'spend' to numeric (invalid entries become NaN)
df['spend'] = pd.to_numeric(df['spend'], errors='coerce')

# Standardize channel names using a mapping dictionary
channel_cleanup_map = {
    'Facebok': 'Facebook',
    'Insta_grams': 'Instagram',
    'Gogle': 'Google Ads',
    'Tik_Tok': 'TikTok',
    'E-mail': 'Email',
    'N/A': np.nan,
}
df['channel'] = df['channel'].replace(channel_cleanup_map)

# Convert 'active' column to boolean using a mapping of yes/no values
boolean_cleanup_map = {
    'Yes': True,
    'Y': True,
    '1': True,
    'No': False,
    'N': False,
    '0': False,
}
df['active'] = df['active'].map(boolean_cleanup_map).fillna(False).astype(bool)

# Parse date columns, handling different date formats
df['start_date'] = pd.to_datetime(df['start_date'], format='mixed').dt.strftime('%Y-%m-%d')
df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
df['end_date'] = pd.to_datetime(df['end_date'], dayfirst=True, errors='coerce')

# Fix "time travel" rows where end_date is earlier than start_date
# (Replace end_date with start_date + 30 days)
time_travel_mask = df['end_date'] < df['start_date']
df.loc[time_travel_mask, 'end_date'] = df.loc[time_travel_mask, 'start_date'] + pd.Timedelta(days=30)

# Cap outliers in 'spend' using the IQR rule (values above Q3 + 3*IQR are set to that upper limit)
Q1 = df['spend'].quantile(0.25)
Q3 = df['spend'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 3 * IQR
outlier_mask = df['spend'] > upper_limit
df.loc[outlier_mask, 'spend'] = upper_limit

# Extract season from campaign_name (pattern: Q1_Spring_2024 → 'Spring')
df['season'] = df['campaign_name'].str.extract(r'Q\d_([^_]+)_')

# Saving cleaned data into a new CSV file
df.to_csv('cleaned_marketing_campaign_data.csv')