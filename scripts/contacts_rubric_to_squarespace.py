import glob
import pandas as pd
import os

path = "/mnt/c/users/aditya/Downloads/"
files = glob.glob(os.path.join(path, "*.csv"))

dfs = []

for f in files:
   try:
      df = pd.read_csv(f, usecols=["Ticket Email Address", "Full Name"])
      df[["first_name", "last_name"]] = df["Full Name"].str.split(" ", n=1, expand=True)

      df["first_name"] = df["first_name"].str.capitalize()
      df["last_name"] = df["last_name"].str.title()

      df.rename(columns={"Ticket Email Address": "email_address"}, inplace=True)
      df.drop(columns=["Full Name"], inplace=True)
      dfs.append(df)

   except Exception as e:
      print(f"Failed to process {f} due to {e}")

df_final = pd.concat(dfs, ignore_index=True)
output_path = "/mnt/c/users/aditya/Downloads/merged.xlsx"
df_final.to_excel(output_path, index=False)

print(f"Merged file saved to {output_path}")