import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_day = pd.read_csv("Bike-sharing-dataset/day.csv", delimiter=",")

df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv", delimiter=",")

sns.set(style="whitegrid")

st.title("Bike Sharing Data Analysis Dashboard")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select Analysis", ["Pengaruh Cuaca", "Tren Hari Kerja vs Hari Libur"])

# Visualisasi 1: Pengaruh cuaca terhadap jumlah pengguna sepeda
if option == "Pengaruh Cuaca":
    st.subheader("Pengaruh Cuaca terhadap Jumlah Pengguna Sepeda")
    
    weather_effect = df_hour.groupby('weathersit')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_effect, palette="coolwarm", ax=ax)
    ax.set_title('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Cuaca')
    ax.set_xlabel('Situasi Cuaca (1: Cerah, 2: Berkabut, 3: Hujan, 4: Badai)')
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')

    st.pyplot(fig)

# Visualisasi 2: Tren penggunaan sepeda pada hari kerja vs hari libur di setiap jam
elif option == "Tren Hari Kerja vs Hari Libur":
    st.subheader("Tren Penggunaan Sepeda per Jam (Hari Kerja vs Hari Libur)")

    workingday_effect = df_hour.groupby(['workingday', 'hr'])['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', hue='workingday', data=workingday_effect, palette="Set1", ax=ax)
    ax.set_title('Penggunaan Sepeda per Jam (Hari Kerja vs Hari Libur)')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
    ax.legend(title='Hari Kerja (1) / Libur (0)')

    st.pyplot(fig)