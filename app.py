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
        "Salário": [round(random.uniform(2000, 15000), 2) for _ in range(rows)],
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

    if option == "Gerar Dataset Fake":
        rows = st.slider("Número de linhas:", 100, 1000, 100)
        df = generate_fake_data(rows)
        st.write("### Dataset Fake Gerado ###")
        st.dataframe(df.head())
    else:
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file is not None:
            df = load_data(uploaded_file)
            st.write("### Dataset carregado ###")
            st.dataframe(df.head())

    if 'df' in locals():
        st.write("### Valores Ausentes ###")
        missing_values = check_missing_values(df)
        st.write(missing_values)

        st.write("### Valores Duplicados ###")
        duplicates = check_duplicates(df)
        st.write(f"Total de valores duplicados: {duplicates}")

        st.write("### Tipos de Dados ###")
        data_types = check_data_types(df)
        st.write(data_types)

        st.write("### Outliers ###")
        outliers = detect_outliers(df)
        st.write(outliers)

        st.write("### Distribuição das Variáveis ###")
        for column in df.select_dtypes(include=[np.number]).columns:
            fig, ax = plt.subplots()
            sns.histplot(df[column], bins=20, kde=True, ax=ax)
            st.pyplot(fig)


if __name__ == "__main__":
    main()
