import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random


def generate_fake_data(rows=100):
    fake = Faker()
    data = {
        "ID": [fake.uuid4() for _ in range(rows)],
        "Nome": [fake.name() for _ in range(rows)],
        "Idade": [random.randint(18, 80) for _ in range(rows)],
        "Salário": [round(random.uniform(2000, 10000), 2) for _ in range(rows)],
        "Email": [fake.email() for _ in range(rows)],
        "Data_Registro": [fake.date_time_this_decade() for _ in range(rows)]
    }
    return pd.DataFrame(data)


def load_data(uploaded_file):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    else:
        return None

def check_missing_values(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_data_types(df):
    return df.dtypes

def detect_outliers(df):
    outliers = {}
    for column in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers[column] = df[(df[column] < lower_bound) | (df[column] > upper_bound)].index.tolist()
    return outliers

def main():
    st.title(":bar_chart: Data Quality")
    st.write("Faça upload de um arquivo CSV ou gere um dataset fake para analisar a qualidade dos dados.")

    option = st.radio("Escolha uma opção:", ("Upload CSV", "Gerar Dataset Fake"))
