import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

def load_data():
    """Loads the Bank Marketing dataset from UCI. Downloads if not already saved."""
    # Ensure absolute path to the data directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    data_dir = os.path.join(project_root, "src/uplift_bank_marketing/data")
    os.makedirs(data_dir, exist_ok=True)  # Always ensure the directory exists

    X_path = os.path.join(data_dir, "X_bank_marketing.csv")
    y_path = os.path.join(data_dir, "y_bank_marketing.csv")
    metadata_path = os.path.join(data_dir, "metadata.txt")
    variables_path = os.path.join(data_dir, "variables.txt")

    # Check if data already exists
    if os.path.exists(X_path) and os.path.exists(y_path):
        print("Loading data from saved files...")
        X = pd.read_csv(X_path)
        y = pd.read_csv(y_path)
        print("Data loaded successfully.")
        return X, y

    # If not, download from UCI and save
    print("Downloading data from UCI Machine Learning Repository...")
    bank_marketing = fetch_ucirepo(id=222)

    # Save features and target
    X = bank_marketing.data.features
    y = bank_marketing.data.targets

    X.to_csv(X_path, index=False)
    y.to_csv(y_path, index=False)

    # Save metadata and variables as text files
    with open(metadata_path, "w") as meta_file:
        meta_file.write(str(bank_marketing.metadata))
    
    with open(variables_path, "w") as var_file:
        var_file.write(str(bank_marketing.variables))
    
    print("Data downloaded and saved successfully.")
    return X, y
