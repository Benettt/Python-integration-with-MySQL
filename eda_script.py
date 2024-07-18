
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Display the first few rows of the dataset
    print("First 5 rows of the dataset:")
    display(df.head())

    # Display summary statistics
    print("\nSummary statistics:")
    display(df.describe())

    # Display information about the dataset
    print("\nDataset information:")
    display(df.info())

    # Check for missing values
    print("\nMissing values in each column:")
    display(df.isnull().sum())

    # Visualize the distribution of each numerical feature
    numerical_features = df.select_dtypes(include=[np.number]).columns
    for feature in numerical_features:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.show()

    # Visualize the correlation matrix
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

    # Visualize the count of each categorical feature
    categorical_features = df.select_dtypes(include=[object]).columns
    for feature in categorical_features:
        plt.figure(figsize=(10, 6))
        sns.countplot(y=df[feature], order=df[feature].value_counts().index)
        plt.title(f'Count of {feature}')
        plt.xlabel('Count')
        plt.ylabel(feature)
        plt.show()
