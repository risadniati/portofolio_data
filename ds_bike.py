# 1. Mempersiapkan DataFrame yang telah diproses menggunakan Google Colab

## Import seluruh library yang diperlukan 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st

## Load berkas sebagai dataframe
day_df = pd.read_csv('day_rev.csv')
hour_df = pd.read_csv('hour_rev.csv')

# 2. Membuat konten pada sidebar
with st.sidebar:
    # Menambahkan gambar
    st.image('https://i.pinimg.com/736x/31/ac/0b/31ac0b04fb4101fe551a464521b6298b.jpg')

    # Menuliskan identitas
    st.markdown('Dashboard dibuat oleh')
    st.markdown('Maria Goretti Risadniati M. \n [Risa\'s LinkedIn](https://www.linkedin.com/in/maria-goretti-r-madsun-601752218/)')

# 3. Melengkapi Dashboard dengan Visualisasi Data
st.header('Bike Sharing Dashboard')

# Visualisasi data 1
st.subheader("Tren Penyewaan Sepeda pada Tahun 2011-2012")
tren_per_bulan_tahun = day_df.groupby(by=['mnth', 'yr']).cnt.sum()
tren_per_bulan_tahun = tren_per_bulan_tahun.unstack()
fig, ax = plt.subplots(figsize=(10, 6))
tren_per_bulan_tahun.plot(kind='line', stacked=True, marker='o', ax=ax)

ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah')
ax.legend(title='Tahun', loc='upper left')
st.pyplot(fig)

# Visualisasi Data 2 dan 3
st.subheader('Tren Penyewaan Sepeda Setiap Tahun')
tab1, tab2 = st.tabs(["Tahun 2011", "Tahun 2012"])
 
with tab1:
    st.write("Tren Penyewaan Sepeda Tertinggi - Terendah pada 2011")
    day_df_2011 = day_df[day_df['yr'] == 2011]

    monthly_counts = day_df_2011.groupby(by='mnth').cnt.sum().reset_index()
    monthly_counts = monthly_counts.sort_values(by='cnt', ascending=False)

    colors = ['blue'] + ['lightgrey'] * (len(monthly_counts) - 1)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='mnth', y='cnt', data=monthly_counts, palette=colors, order=monthly_counts['mnth'], ax=ax)

    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

with tab2:
    st.write("Tren Penyewaan Sepeda Tertinggi - Terendah pada 2012")
    day_df_2012 = day_df[day_df['yr'] == 2012]

    monthly_counts = day_df_2012.groupby(by='mnth').cnt.sum().reset_index()
    monthly_counts = monthly_counts.sort_values(by='cnt', ascending=False)

    colors = ['blue'] + ['lightgrey'] * (len(monthly_counts) - 1)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='mnth', y='cnt', data=monthly_counts, palette=colors, order=monthly_counts['mnth'], ax=ax)

    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

# Visualisasi Data 4 dan 5  
st.subheader('Tren Penyewaan Sepeda Berdasarkan Berbagai Faktor')
tab1, tab2 = st.tabs(["Faktor Waktu Operasional", "Faktor Musim"])
with tab1:
    st.write('Tren Peminjaman Sepeda Berdasarkan Waktu Operasional')
    tren_per_jam = hour_df.groupby(by=['hr']).cnt.sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    tren_per_jam.plot(kind='line', marker='o', ax=ax)

    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah')

    ax.set_xticks(ticks=tren_per_jam.index)
    ax.set_xticklabels(tren_per_jam.index)
    st.pyplot(fig)

with tab2:
    st.write('Proporsi Penyewaan Sepeda Berdasarkan Musim')
    season_counts = day_df.groupby(by='season_').cnt.sum().sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(figsize=(4, 4), dpi=30)

    ax.pie(season_counts['cnt'], labels=season_counts['season_'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'])
    st.pyplot(fig)







