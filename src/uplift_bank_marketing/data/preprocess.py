import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def process_contact_column(data_in_function):
    """
    Processes the 'contact' column:
    - Renames it to 'cellular'.
    - Encodes 'cellular' as 1 (cellular) and 0 (telephone).
    - Creates a 'cellular_missing' column if any missing values exist.
    """
    if "contact" in data_in_function.columns:
        # Create a missing flag if any values are missing
        if data_in_function['contact'].isnull().sum() > 0:
            data_in_function['cellular_missing'] = data_in_function['contact'].isnull().astype(int)
        
        # Renaming the column
        data_in_function.rename(columns={"contact": "cellular"}, inplace=True)
        
        # Encoding cellular as 1, telephone as 0
        data_in_function["cellular"] = data_in_function["cellular"].str.lower().map(
            {"cellular": 1, "telephone": 0}
        ).fillna(0).astype(int)
    
    return data_in_function

def handle_missing_values(data_in_function):
    """
    Handles missing values in the DataFrame.
    - For binary columns, creates a missing flag if needed.
    - For multi-level categorical columns, replaces with "unknown".
    """
    missing_cols = data_in_function.columns[data_in_function.isnull().sum() > 0]

    for col in missing_cols:
        if data_in_function[col].dtype == 'object':
            # Binary Columns (Two Unique Values)
            if data_in_function[col].nunique() <= 2:
                if data_in_function[col].isnull().sum() > 0:
                    missing_flag = f"{col}_missing"
                    data_in_function[missing_flag] = data_in_function[col].isnull().astype(int)
            else:
                # Multi-Level Categorical Columns
                data_in_function[col].fillna("unknown", inplace=True)
    
    return data_in_function


def encode_binary_columns(data_in_function):
    """
    Encodes binary columns as 0/1 (no/yes).
    - Applies to binary columns (two unique values).
    """
    for col in data_in_function.select_dtypes(include=['object']).columns:
        if data_in_function[col].nunique() <= 2:
            data_in_function[col] = data_in_function[col].str.lower().map(
                {"yes": 1, "no": 0, "true": 1, "false": 0, "1": 1, "0": 0}
            )
            data_in_function[col] = data_in_function[col].fillna(0).astype(int)  # Any unknown becomes 0
    
    return data_in_function


def one_hot_encode_multilevel(data_in_function):
    """
    Applies One-Hot Encoding to multi-level categorical columns.
    - Retains "unknown" and drops the second most frequent category.
    """
    categorical_cols = data_in_function.select_dtypes(include=['object']).columns

    for col in categorical_cols:
        value_counts = data_in_function[col].value_counts()
        values_to_drop = value_counts.index[1] if len(value_counts) > 1 else value_counts.index[0]
        
        if values_to_drop == "unknown":
            values_to_drop = value_counts.index[2] if len(value_counts) > 2 else None
        
        # One-Hot Encoding (0/1)
        one_hot = pd.get_dummies(data_in_function[col], prefix=col).astype(int)
        data_in_function = pd.concat([data_in_function.drop(columns=[col]), one_hot], axis=1)
        
        # Drop the chosen column if it exists and is not "unknown"
        drop_column = f"{col}_{values_to_drop}"
        if values_to_drop and drop_column in data_in_function.columns and "unknown" not in drop_column:
            data_in_function.drop(columns=[drop_column], inplace=True)
    
    return data_in_function


def process_age_column(data_in_function):
    """
    Processes the 'age' column:
    - Bins the continuous 'age' column into age groups.
    - One-Hot Encodes these age groups as 0/1, removing the reference category (18-25).
    - Drops the original 'age' column.
    """
    if "age" in data_in_function.columns:
        # Define age bins and labels
        bins = [18, 25, 35, 45, 55, 65, float("inf")]
        labels = ["18-25", "26-35", "36-45", "46-55", "56-65", "66+"]

        # Bin the 'age' column
        data_in_function["age_group"] = pd.cut(data_in_function["age"], bins=bins, labels=labels, right=False)

        # One-Hot Encode the age groups (as 0/1, not boolean)
        age_dummies = pd.get_dummies(data_in_function["age_group"], prefix="age_group", drop_first=True).astype(int)
        data_in_function = pd.concat([data_in_function.drop(columns=["age"]), age_dummies], axis=1)
    
    return data_in_function


def prepare_data(data_in_function):
    """
    Complete data preparation function combining all steps.
    - Processes 'contact' column (cellular).
    - Handles missing values.
    - Encodes binary columns.
    - One-Hot Encodes multi-level categorical columns.
    - Bins and encodes the 'age' column.
    """
    data_in_function = process_contact_column(data_in_function)
    data_in_function = handle_missing_values(data_in_function)
    data_in_function = encode_binary_columns(data_in_function)
    data_in_function = one_hot_encode_multilevel(data_in_function)
    data_in_function = process_age_column(data_in_function)
    
    return data_in_function