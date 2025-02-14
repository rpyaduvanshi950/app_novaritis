import numpy as np
import pandas as pd
import os

# Check if the file exists:
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "content", "filedata.xlsx")
if os.path.exists(file_path):
    print(f"File found at: {file_path}")
else:
    print(f"Error: File not found at: {file_path}")
    # Handle the error (e.g., ask the user to provide a different path)

# Try reading the file with openpyxl:
try:
    data = pd.read_excel(file_path, engine='openpyxl')
    data1 = data.copy()
except OSError as e:
    print(f"Error reading file: {e}")
    # Handle the error (e.g., display a more user-friendly message)

# Step 1: Split combined categories into lists
data1['Phases_split'] = data1['Phases'].str.split('|')

# Step 2: Explode the lists into separate rows
data1_exploded = data1.explode('Phases_split')

# Step 3: Add binary columns for each unique category
data1_exploded['Phase1'] = (data1_exploded['Phases_split'] == 'PHASE1').astype(int)
data1_exploded['Phase2'] = (data1_exploded['Phases_split'] == 'PHASE2').astype(int)
data1_exploded['Phase3'] = (data1_exploded['Phases_split'] == 'PHASE3').astype(int)

# Step 4: Aggregate the binary columns back to the original structure
binary_columns = ['Phase1', 'Phase2', 'Phase3']
data1_binary = data1_exploded.groupby(level=0)[binary_columns].max()

# Step 5: Merge the binary columns back into the original dataset
data1 = data1.merge(data1_binary, left_index=True, right_index=True)

# Step 6: Drop intermediate columns if necessary
data1 = data1.drop(columns=['Phases_split'])

# Display the updated dataset
data1.head(3)
data1.drop(['Phases'],axis='columns',inplace=True)
data1.columns
# Step 1: Split combined categories into lists and remove any leading/trailing spaces
data1['Age_split'] = data1['Age'].str.split(',').apply(lambda x: [item.strip() for item in x])

# Step 2: Explode the lists into separate rows
data1_exploded = data1.explode('Age_split')

# Step 3: Add binary columns for each unique category
data1_exploded['Age_CHILD'] = (data1_exploded['Age_split'] == 'CHILD').astype(int)
data1_exploded['Age_ADULT'] = (data1_exploded['Age_split'] == 'ADULT').astype(int)
data1_exploded['Age_OLDER_ADULT'] = (data1_exploded['Age_split'] == 'OLDER_ADULT').astype(int)

# Step 4: Aggregate the binary columns back to the original structure
binary_columns = ['Age_CHILD', 'Age_ADULT', 'Age_OLDER_ADULT']
data1_binary = data1_exploded.groupby(level=0)[binary_columns].max()

# Step 5: Merge the binary columns back into the original dataset
data1 = data1.merge(data1_binary, left_index=True, right_index=True)

# Step 6: Drop intermediate columns if necessary
data1 = data1.drop(columns=['Age_split'])

# Display the updated dataset
data1.head(3)
data1=data1.drop(['Study Type','Last Update Posted','Results First Posted','First Posted','Funder Type'],axis='columns')
import matplotlib.pyplot as plt
import seaborn as sns
# Split the 'System Design' column into multiple components using | as a separator
split_columns = data1['Study Design'].str.split('|', expand=True)

# Extract the keys (e.g., "Allocation", "Intervention Model") and their values
for col in split_columns.columns:
    key_value = split_columns[col].str.split(':', expand=True)
    key = key_value[0].str.strip()  # Extract the key and strip any whitespace
    value = key_value[1].str.strip()  # Extract the value and strip any whitespace
    data1[key[0]] = value

# Drop the original 'System Design' column after splitting
data1 = data1.drop(columns=['Study Design'])
# Convert 'Study Results' column to binary (1 for YES, 0 for NO)
data1['Study Results'] = data1['Study Results'].map({'YES': 1, 'NO': 0})

# Display the updated column
print(data1['Study Results'].head())
# Define the mapping for Study Status
status_mapping = {
    "UNKNOWN": 0,
    "NOT_YET_RECRUITING": 1,
    "ACTIVE_NOT_RECRUITING": 2,
    "ENROLLING_BY_INVITATION": 3,
    "RECRUITING": 4,
    "SUSPENDED": 5,
    "TERMINATED": 6,
    "COMPLETED": 7

}

# Apply the mapping to the 'Study Status' column
data1['Study Status'] = data1['Study Status'].map(status_mapping)
import re

# Define the cleaning function
def clean_text_for_biobert(text):
    # Remove numeric values
    text = re.sub(r'\b\d+\b', '', text)
    # Remove special characters like "â„¢"
    text = re.sub(r'[^\w\s]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Convert to lowercase
    text = text.lower().strip()
    return text

# Step 1: Apply the cleaning function to each column
data1['Primary Outcome filtered'] = data1['Primary Outcome Measures'].apply(clean_text_for_biobert)
import pandas as pd
import re

# Define the cleaning function
def clean_text_for_biobert(text):
    if pd.isna(text):  # Check if the value is NaN
        return ""
    # Remove numeric values
    text = re.sub(r'\b\d+\b', '', str(text))  # Ensure the value is a string
    # Remove special characters like "â„¢"
    text = re.sub(r'[^\w\s]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Convert to lowercase
    text = text.lower().strip()
    return text

# Apply the cleaning function to each column
data1['Secondary Outcome filtered'] = data1['Secondary Outcome Measures'].apply(clean_text_for_biobert)
# Define a function for conditional merging
def merge_outcomes(secondary, primary):
    if secondary and primary:  # Both columns have non-blank values
        return f"{secondary} || {primary}"
    elif secondary:  # Only the secondary column has a value
        return secondary
    elif primary:  # Only the primary column has a value
        return primary
    else:  # Both are blank
        return ""

# Apply the function to create the merged column
data1['Merged Outcome'] = data1.apply(
    lambda row: merge_outcomes(row['Secondary Outcome filtered'], row['Primary Outcome filtered']),
    axis=1
)
data1.drop(['Primary Outcome filtered','Secondary Outcome filtered'],axis='columns',inplace=True)
# Replace NaN values with "Not Applicable"
data1[['Allocation', 'Intervention Model', 'Masking']] = data1[['Allocation', 'Intervention Model', 'Masking']].fillna('Not Applicable')

# Replace blank values with "Unknown"
data1[['Allocation', 'Intervention Model', 'Masking']] = data1[['Allocation', 'Intervention Model', 'Masking']].replace(r'^\s*$', 'Unknown', regex=True)
# Drop the specified columns
data1 = data1.drop(columns=['Primary Outcome Measures', 'Secondary Outcome Measures'])
# Drop rows where the column 'Sex' has missing values
data1 = data1.dropna(subset=['Sex'])
data1.drop(['Completion Date'],axis='columns',inplace=True)

# Calculate the mean of the column
mean_value = data1["Primary Completion Duration of Trial"].mean()

# Filling the NaN values with that mean
data1["Primary Completion Duration of Trial"] = data1["Primary Completion Duration of Trial"].fillna(mean_value)
# Separate columns into numeric, categorical, and textual based on data types and unique value analysis
numeric_columns = []
categorical_columns = []
textual_columns = []

for column in data1.columns:
    dtype = data1[column].dtype
    unique_values = data1[column].nunique()

    # Check if the dtype is a pandas CategoricalDtype or a NumPy numeric type
    if pd.api.types.is_categorical_dtype(dtype) or np.issubdtype(dtype, np.number):
        if unique_values < 10:  # Heuristic: less than 10 unique values likely indicates categorical
            categorical_columns.append(column)
        else:  # If it's numeric and has many unique values, treat it as numeric
            numeric_columns.append(column)
    else:
        textual_columns.append(column)

print("Numeric Columns:")
print(numeric_columns)
print("\nCategorical Columns:")
print(categorical_columns)
print("\nTextual Columns:")
print(textual_columns)
X_test=data1
# Declare textual and numerical columns
textual_cols = [
    'Study Title', 'Brief Summary', 'Conditions', 'Interventions',
    'Allocation', 'Intervention Model', 'Masking', 'Primary Purpose', 'Merged Outcome'
]

numerical_cols = [
    'Enrollment', 'Duration of Trial', 'Primary Completion Duration of Trial',
    'Phase1', 'Phase2', 'Phase3', 'Age_CHILD', 'Age_ADULT',
    'Age_OLDER_ADULT', 'Study Status', 'Study Results'
]
# Combine textual columns into a single string for each row
X_test['combined_text'] = X_test[textual_cols].fillna('').agg(' '.join, axis=1)
# Load BioBERT tokenizer and model
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
import gc

tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
biobert_model = AutoModel.from_pretrained("dmis-lab/biobert-v1.1")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
biobert_model.to(device)

# Function to generate embeddings in batches
def generate_embeddings_in_batches(text_data, batch_size=32):
    embeddings = []
    for i in range(0, len(text_data), batch_size):
        batch = text_data[i:i + batch_size]
        tokens = tokenizer(
            list(batch), padding=True, truncation=True, max_length=512, return_tensors="pt"
        )
        tokens = {key: val.to(device) for key, val in tokens.items()}
        with torch.no_grad():
            outputs = biobert_model(**tokens)
        batch_embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
        embeddings.append(batch_embeddings)
        del tokens, outputs
        gc.collect()
        torch.cuda.empty_cache()
    return np.vstack(embeddings)

# Generate embeddings for training and testing sets
X_test_embeddings = generate_embeddings_in_batches(X_test['combined_text'].values, batch_size=32)

np.save('X_test_data_embeddings.npy', X_test_embeddings)
# Declare textual and numerical columns
textual_cols = [
    'Study Title', 'Brief Summary', 'Conditions', 'Interventions',
    'Allocation', 'Intervention Model', 'Masking', 'Primary Purpose', 'Merged Outcome'
]

numerical_cols = [
    'Enrollment', 'Duration of Trial', 'Primary Completion Duration of Trial',
    'Phase1', 'Phase2', 'Phase3', 'Age_CHILD', 'Age_ADULT',
    'Age_OLDER_ADULT', 'Study Status', 'Study Results'
]
# Assuming X_train and X_test are the training and testing datasets

# Extract the normalized numerical features
X_test_data_numerical = X_test[numerical_cols].values

# Verify the shapes
print("X_test_numerical shape:", X_test_data_numerical.shape)

X_test_embeddings=np.load('/content/X_test_data_embeddings.npy')
# Combine BioBERT embeddings with numerical features
X_test_data_combined = np.hstack([X_test_embeddings, X_test_data_numerical])

# Save combined features
np.save('X_test_data_combined.npy', X_test_data_combined)

from sklearn.preprocessing import StandardScaler
import joblib

# Define the feature columns and the target variable
numerical_cols = [
    'Enrollment', 'Duration of Trial', 'Primary Completion Duration of Trial',
    'Phase1', 'Phase2', 'Phase3', 'Age_CHILD', 'Age_ADULT',
    'Age_OLDER_ADULT', 'Study Status', 'Study Results'
]

# Initialize scalers
feature_scaler = StandardScaler()

# Standardize the features
X_test_data_combined = feature_scaler.fit_transform(X_test_data_combined)

import pickle
import pandas as pd

# Load the trained model
model_path = "/content/gbm_model_log.pkl"
with open(model_path, 'rb') as file:
    gbm_model = pickle.load(file)

# Make predictions on the test dataset
y_pred_log = gbm_model.predict(X_test_data_combined)

# If your target variable was log-transformed, inverse the transformation
y_pred_rescaled = np.expm1(y_pred_log)  # Use np.expm1 to reverse log(1+x)

# Create a DataFrame with the predictions
predictions_df = pd.DataFrame({
    'Predicted Recruitment Rate': y_pred_rescaled.flatten()
})

# Save predictions to an Excel file
output_file = "predictions.xlsx"
predictions_df.to_excel(output_file, index=False)

print(f"Predictions saved to {output_file}")
nct_id = data['NCT Number']

final_data = pd.DataFrame({
    'NCT Number': nct_id,
    'Predicted Recruitment Rate': y_pred_rescaled.flatten()
})