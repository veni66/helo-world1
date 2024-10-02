import streamlit as st

# Judul aplikasi
st.title("🎈 Masukkan Nama Lengkap")

# Input untuk nama depan
first_name = st.text_input("Nama Depan:")

# Input untuk nama belakang
last_name = st.text_input("Nama Belakang:")

# Pilihan untuk jenis kelamin
gender = st.selectbox("Jenis Kelamin:", ["Pilih", "Pria", "Wanita"])

# Tombol untuk mengirimkan
if st.button("Sapa!"):
    if first_name and last_name and gender != "Pilih":
        greeting = f'Halo, {first_name} {last_name}! Selamat datang!'
        st.write(greeting)
    else:
        st.write("Silakan lengkapi semua kolom!")
