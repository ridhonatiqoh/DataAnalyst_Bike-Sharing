# Import seluruh libraries yang digunakan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from PIL import Image

# Generate load dataset
day_df = pd.read_csv('https://github.com/ridhonatiqoh/DataAnalyst_Bike-Sharing/blob/main/Dataset/day.csv')
hour_df = pd.read_csv('https://github.com/ridhonatiqoh/DataAnalyst_Bike-Sharing/blob/main/Dataset/hour.csv')

# Membuat sidebar dan tittle dashboar
# Menambahkan logo perusahaan
with st.sidebar:
    st.image('C:/Users/A S U S/Desktop/SEMESTER V - ASSIGN/MACHINE LEARNING/SUBMISSION DICODING/bikeshare.png')
    st.write("**TRUSTED BIKE SHARE COMPANY**")
    st.sidebar.title("Navigasi Web")
    page = st.sidebar.selectbox("Pilih halaman yang ingin ditampilkan", ["Halaman Utama","Halaman Analisis Data"])

#Jika user memilih pilihan halaman utama
if page == "Halaman Utama":
    st.header("Welcome to Bike Share Company Dashboard")
    image1= Image.open('C:/Users/A S U S/Desktop/SEMESTER V - ASSIGN/MACHINE LEARNING/SUBMISSION DICODING/bikeshare.png')
    st.image(image1, caption="Bike Share Company")
    st.subheader("Tentang Perusahaan")
    st.write("""
             **Bike Share System** merupakan generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian 
             kembali telah menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan mengembalikannya 
             kembali ke posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari 
             lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena peran pentingnya dalam lalu lintas, 
             masalah lingkungan dan kesehatan.""") 
    st.subheader("Visi Perusahaan")
    st.write("""
             Menjadi perusahaan terdepan dalam solusi mobilitas berkelanjutan melalui sistem berbagi sepeda yang inovatif, aman, dan ramah lingkungan, 
             serta memberikan kontribusi nyata dalam mengurangi kemacetan lalu lintas, polusi lingkungan, dan meningkatkan kesehatan masyarakat.""")
    st.subheader("Misi Perusahaan")
    st.write("""
             1. Memberikan sistem penyewaan sepeda yang mudah diakses dan efesien, dengan teknologi otomatis yang memudahkan keanggotaan, penyewaan dan pengembalian sepeda di berbagai lokasi
             2. Berkontribusi dalam menciptakan kota-kota yang lebih hijau dan ramah lingkungan dengan mengurangi emisi karbon serta mengurangi ketergantungan pada kendaraan bermotor.
             3. Mengembangkan inovasi berkelanjutan yang terus memperbaiki pengalaman pengguna serta memperluas aksesibilitas bagi semua kalangan masyarakat.""")
    st.subheader("")

#jika user memilih pilihan halaman analisis data
else:
    st.header("Selamat Datang Di Halaman Analisis Data")
    st.write("""
            Dashboard interaktif ini dibuat untuk menjelaskan pertanyaan business berikut:
            - **Pertanyaan 1:** Bagaimana korelasi pengaruh musim dan cuaca terhadap jumlah penyewaan sepeda?
            - **Pertanyaan 2:** Bagaimana distribusi volume penyewaan sepeda setiap jam dalam satu hari? """)

    st.write("Pertanyaan tersebut terjawab oleh analisis data company yang disajikan pada tab-tab berikut:")
    tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

    with tab1:
        st.subheader("Bar Chart Korelasi Musim dan Cuaca Terhadap Jumlah Penyewaan Sepeda")
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
        colors_1 = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
        season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
        average_usage_season = day_df.groupby('season')['cnt'].mean()


        average_usage_season = average_usage_season.sort_values(ascending=False)

    # Membuat plot dengan nama musim, bukan angka
        season_labels = [season_mapping[season] for season in average_usage_season.index]

        sns.barplot(y=season_labels, x=average_usage_season.values, palette=colors_1, ax=ax[0])
        ax[0].set_title('Rata-rata Penyewaan Sepeda per Musim', loc='center', fontsize=10)
        ax[0].set_ylabel(None)
        ax[0].set_xlabel(None)
        ax[0].tick_params(axis='y', labelsize=10)


        colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
        weather_mapping = {1: "Clear", 2: "Mist + cloudy", 3: "Light snow", 4: "Heavy rain"}
        average_usage_weather = day_df.groupby('weathersit')['cnt'].mean()

    # Menambahkan kategori cuaca 4 dengan nilai 0 jika tidak ada dalam data
        if 4 not in average_usage_weather.index:
            average_usage_weather.loc[4] = 0
            average_usage_weather = average_usage_weather.sort_index()

    # Membuat plot dengan nama cuaca, termasuk kategori cuaca 4 dengan nilai 0
        weather_labels = [weather_mapping[weather] for weather in average_usage_weather.index]

        sns.barplot(y=weather_labels, x=average_usage_weather.values, palette=colors, ax=ax[1])
        ax[1].set_title('Rata-rata Penyewaan Sepeda per Cuaca', loc='center', fontsize=10)
        ax[1].set_ylabel(None)
        ax[1].set_xlabel(None)
        ax[1].tick_params(axis='y', labelsize=10)

    # Sup title untuk kedua plot
        plt.tight_layout()
        plt.suptitle('Korelasi Musim dan Cuaca terhadap Traffic Penyewaan Sepeda', fontsize=13, y=1.04)
        st.pyplot(fig)
        with st.expander("Lihat Kesimpulan"):
            st.write("""Pada bar chart diatas menunjukkan jumlah penyewaan sepeda pada **musim gugur (fall)** lebih tinggi daripada musim lainnya, 
                     hal ini disebabkan oleh musim gugur menjadi musim yang cocok untuk keluar dan bersepeda sehingga perusahaan mesti menskemakan persediaan 
                     sepeda agar mencukupi kebutuhan pengguna. Terlihat pada tabel juga cuaca **cerah** menjadikan traffic penyewaan tinggi sebab cuaca 
                     tersebut mendukung untuk beraktivitas di luar ruangan. """)

    # Menghitung rata-rata penyewaan sepeda untuk setiap jam dalam sehari
    avg_hourly_rentals = hour_df.groupby('hr')['cnt'].mean()

    # Menampilkan hasil pada tab kedua
    with tab2:
        st.subheader("Line Chart Grafik Rata-Rata Penyewaan Sepeda per Jam")

        # Membuat figure untuk grafik
        fig, ax = plt.subplots(figsize=(12, 6))

        # Menampilkan pola penggunaan sepeda per jam dalam satu hari menggunakan grafik garis
        sns.lineplot(x=avg_hourly_rentals.index, y=avg_hourly_rentals.values, marker='o')
        ax.set_title('Rata-Rata Penyewaan Sepeda per Jam\n')
        ax.set_xlabel('Jam')
        ax.set_ylabel('Rata-Rata Penyewaan Sepeda')
        ax.set_xticks(range(0, 24))  # Membuat range jam 00.00 - 24.00 (1 hari)
        ax.grid(True)  # Menampilkan garis-garis untuk memudahkan membaca line chart

        # Menampilkan grafik di Streamlit
        st.pyplot(plt)

        # Menentukan jam dengan jumlah penyewaan sepeda paling tinggi
        busiest_hour = avg_hourly_rentals.idxmax()

        # Menampilkan hasil di Streamlit
        with st.expander("Lihat Kesimpulan"):
            st.write("""Pada grafik line chart di atas merepresentasikan traffic penyewaan sepeda dalam hitungan per jam dalam waktu sehari
                     , grafik menunjukkan data fluktuatif dan terlihat terdapat dua titik puncak yang cukup menarik. Puncak tersebut
                     merepresentasikan traffic penyewaan sangat tinggi yakni sekitar pukul 8 AM dan 5 PM, waktu tersebut merupakan waktu
                     pergi dan pulang kerja kebanyakan orang sehingga menyebabkan di jam-jam tersebut angka jumlah penyewaan sepeda tinggi. """)

    
