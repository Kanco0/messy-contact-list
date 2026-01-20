import pandas as pd
import os 
import re

c_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(c_dir, 'messy_contact_list.csv')
df = pd.read_csv(file_path)
print(df)

df['Phone'].str.replace(r'\D', '', regex=True)
df['Clean_Phone'] = df['Phone'].str.replace(r'\D', '', regex=True)

print(df[['Phone', 'Clean_Phone']].head(10))

df['Name'] = df['Name'].str.strip().str.title()

print("\n--- Name Cleaning Result ---")
print(df['Name'].head(10))

df['Email_Valid'] = df['Email'].str.contains(r'[^@]+@[^@]+\.[^@]+', regex=True, na=False)

invalid_emails = df[df['Email_Valid'] == False]
print("\n--- Invalid Emails Found ---")
print(invalid_emails[['Email']].head())


df_final = df.drop_duplicates(subset=['Name', 'Email'], keep='first').copy()

clean_mask = (df_final['Email_Valid'] == True) & (df_final['Clean_Phone'].str.len().isin([10, 11]))
df_final = df_final[clean_mask]

df_final = df_final.drop(columns=['Email_Valid'])

df_final.to_csv('Clean_Contact_List.csv', index=False)

print("--- Final Cleanup Summary ---")
print(f"Total Rows Processed: {len(df)}")
print(f"Clean & Valid Rows Saved: {len(df_final)}")
print("File 'Clean_Contact_List.csv' is ready!")