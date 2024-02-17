import requests
import pandas as pd

def download_csv(covered_recipient_profile_id, year, payment_type):
    base_url = "https://openpaymentsdata.cms.gov/api/1/datastore/query/"
    
   # Dictionary mapping years to their respective identifiers for both research and general payments
    year_identifiers = {
        2016: {
            "general": "755e8737-e4b9-5ed0-bfcf-a91aa3a24da1",
            "research": "9d794b04-97e4-5ac9-9a73-65ac533e3c69"
        },
        2017: {
            "general": "fd7e68cb-8e96-516d-817a-ab42c022ffd3",
            "research": "1ed9f7d9-b1bb-5cd1-9432-7f4f7a1da2aa"
        },
        2018: {
            "general": "90afa48e-f943-5ba0-aade-55f83c094487",
            "research": "d84bef70-5e72-55ab-b7a7-310f1a1a1a0b"
        },
        2019: {
            "general": "f6f151f2-a3fe-5667-b1cd-cd054f88d992",
            "research": "67d7ab83-7eaa-5342-87d3-ac5a48ae9772"
        },
        2020: {
            "general": "4da03195-f672-5972-a640-e3f9289ceaca",
            "research": "70d8687e-9bc4-51a1-a243-0af8b7df328c"
        },
        2021: {
            "general": "f7a64d65-e552-5cea-8849-a01d76064208",
            "research": "9bd627e2-f038-5ac3-bfcf-e1d370a33746"
        },
        2022: {
            "general": "66dfcf9a-2a9e-54b7-a0fe-cae3e42f3e8f",
            "research": "845be348-202e-59e1-a75d-584fa061d2c7"
        },
    }
    
    identifier = year_identifiers.get(year, {}).get(payment_type.lower())
    if not identifier:
        print(f"Error: Identifier not found for year {year} and payment type {payment_type}.")
        return
    
    url = f"{base_url}{identifier}/download?conditions[0][property]=covered_recipient_profile_id&conditions[0][value]={covered_recipient_profile_id}&conditions[0][operator]==&format=csv"

    response = requests.get(url)

    if response.status_code == 200:
        filename = f"{payment_type.lower()}_payment_{year}_{covered_recipient_profile_id}.csv"
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"{payment_type.capitalize()} payment CSV for {year} downloaded successfully.")
        return filename
    else:
        print(f"Failed to download {payment_type.lower()} payment CSV for {year}. Status code: {response.status_code}")
        return None

# Example usage:
covered_recipient_profile_id = "444210"
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
payment_types = ["research", "general"]

# Lists to store downloaded file paths
research_files = []
general_files = []

for year in years:
    for payment_type in payment_types:
        downloaded_file = download_csv(covered_recipient_profile_id, year, payment_type)
        if downloaded_file:
            if payment_type == "research":
                research_files.append(downloaded_file)
            elif payment_type == "general":
                general_files.append(downloaded_file)

# Merge all general payments into one CSV file
general_dataframes = [pd.read_csv(file) for file in general_files]
general_merged = pd.concat(general_dataframes, ignore_index=True)
general_merged.to_csv("Yelena Janjigian_general_payments.csv", index=False)
print("Merged all general payments into 'all_general_payments.csv'.")

# Merge all research payments into one CSV file
research_dataframes = [pd.read_csv(file) for file in research_files]
research_merged = pd.concat(research_dataframes, ignore_index=True)
research_merged.to_csv("Yelena Janjigian_research_payments.csv", index=False)
print("Merged all research payments into 'Sumithira Vasu_research_payments.csv'.")


##############################Associated Payment#####################################




import pandas as pd
import requests
import io
def download_csv(api_url, filename):
    response = requests.get(api_url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"CSV downloaded successfully. Saved as {filename}")
    else:
        print(f"Failed to download CSV. Status code: {response.status_code}")


def merge_csv_files(output_filename, *input_filenames):
    dfs = [pd.read_csv(filename) for filename in input_filenames]
    result = pd.concat(dfs, ignore_index=True)
    result.to_csv(output_filename, index=False)
    print(f"All CSV files merged successfully. Saved as {output_filename}")


covered_recipient_profile_id = "444210"
years = [2016, 2017, 2018, 2019, 2020, 2021,2022]
payment_types = ["Associated research"]

merged_filename = "Yelena Janjigian_Associated_data.csv"


for year in years:
    for payment_type in payment_types:
        base_url = "https://openpaymentsdata.cms.gov/api/1/datastore/query/"

        year_identifiers = {
            2016: "9d794b04-97e4-5ac9-9a73-65ac533e3c69",
            2017: "1ed9f7d9-b1bb-5cd1-9432-7f4f7a1da2aa",
            2018: "d84bef70-5e72-55ab-b7a7-310f1a1a1a0b",
            2019: "67d7ab83-7eaa-5342-87d3-ac5a48ae9772",
            2020: "70d8687e-9bc4-51a1-a243-0af8b7df328c",
            2021: "9bd627e2-f038-5ac3-bfcf-e1d370a33746",
            2022: "845be348-202e-59e1-a75d-584fa061d2c7",
            
        }

        identifier = year_identifiers.get(year)
        if not identifier:
            print(f"Error: Identifier not found for year {year}.")
            continue

        url = f"{base_url}{identifier}/download?conditions[0][property]=covered_recipient_profile_id&conditions[0][value]={covered_recipient_profile_id}&conditions[0][operator]=%3C%3E&conditions[1][groupOperator]=or&conditions[1][conditions][0][property]=principal_investigator_1_profile_id&conditions[1][conditions][0][value]={covered_recipient_profile_id}&conditions[1][conditions][0][operator]==&conditions[1][conditions][1][property]=principal_investigator_2_profile_id&conditions[1][conditions][1][value]={covered_recipient_profile_id}&conditions[1][conditions][1][operator]==&conditions[1][conditions][2][property]=principal_investigator_3_profile_id&conditions[1][conditions][2][value]={covered_recipient_profile_id}&conditions[1][conditions][2][operator]==&conditions[1][conditions][3][property]=principal_investigator_4_profile_id&conditions[1][conditions][3][value]={covered_recipient_profile_id}&conditions[1][conditions][3][operator]==&conditions[1][conditions][4][property]=principal_investigator_5_profile_id&conditions[1][conditions][4][value]={covered_recipient_profile_id}&conditions[1][conditions][4][operator]==&format=csv"
        filename = f"{payment_type.lower()}_payment_{year}_{covered_recipient_profile_id}.csv"
        download_csv(url, filename)

# Merging all downloaded CSV files into one
merge_csv_files(merged_filename, *[f"{payment_type.lower()}_payment_{year}_{covered_recipient_profile_id}.csv" for year in years for payment_type in payment_types])

        