import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Membaca data dari file CSV
data = pd.read_csv('marsha.csv')

# Membuat DataFrame dari data tabel
data = {
    'Tanggal': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
    'Kendaraan': ['Mobil', 'Motor', 'Mobil', 'Motor', 'Mobil', 'Mobil', 'Motor', 'Motor', 'Mobil', 'Mobil'],
    'Merk': ['Toyota', 'Honda', 'Honda', 'Yamaha', 'Toyota', 'Honda', 'Yamaha', 'Honda', 'Toyota', 'Honda'],
    'Servis': ['Ganti Oli', 'Perbaikan Rem', 'Perbaikan Mesin', 'Ganti Oli', 'Perbaikan Rem', 'Ganti Oli', 'Perbaikan Mesin', 'Ganti Oli', 'Perbaikan Mesin', 'Perbaikan Rem'],
    'Biaya': [500000, 300000, 1500000, 200000, 600000, 450000, 1000000, 250000, 2000000, 700000]
}
# Menyimpan DataFrame ke file CSV
file_path = 'data_bengkel.csv'
df.to_csv(file_path, index=False)

print(f"Data telah disimpan ke {file_path}")

# Total pendapatan berdasarkan jenis kendaraan
total_pendapatan_kendaraan = data.groupby('Kendaraan')['Biaya'].sum()

# Merk kendaraan yang paling sering diservis
merk_tersering_diservis = data['Merk'].value_counts()

# Total pendapatan berdasarkan jenis servis
total_pendapatan_servis = data.groupby('Servis')['Biaya'].sum()

# Data untuk scatter plot (misalnya: Tanggal vs Biaya)
data['Tanggal'] = pd.to_datetime(data['Tanggal'])
data['Tanggal_ordinal'] = data['Tanggal'].map(pd.Timestamp.toordinal)

# Scatter plot: Tanggal vs Biaya
plt.figure(figsize=(10, 6))
plt.scatter(data['Tanggal_ordinal'], data['Biaya'])
plt.title('Scatter Plot: Tanggal vs Biaya')
plt.xlabel('Tanggal')
plt.ylabel('Biaya')
plt.xticks(data['Tanggal_ordinal'], data['Tanggal'].dt.strftime('%Y-%m-%d'), rotation=45)
plt.show()

# Pie chart: Total pendapatan berdasarkan jenis kendaraan
plt.figure(figsize=(8, 8))
total_pendapatan_kendaraan.plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart: Total Pendapatan Berdasarkan Jenis Kendaraan')
plt.ylabel('')  # Hilangkan label y karena redundant
plt.show()

# Bar chart: Total pendapatan berdasarkan jenis servis
plt.figure(figsize=(10, 6))
total_pendapatan_servis.plot(kind='bar')
plt.title('Bar Chart: Total Pendapatan Berdasarkan Jenis Servis')
plt.xlabel('Jenis Servis')
plt.ylabel('Total Pendapatan (Rupiah)')
plt.show()

# Diagram Venn: Perbandingan jumlah servis antara Mobil dan Motor
jumlah_servis_mobil = len(data[data['Kendaraan'] == 'Mobil'])
jumlah_servis_motor = len(data[data['Kendaraan'] == 'Motor'])

plt.figure(figsize=(8, 8))
venn2(subsets = (jumlah_servis_mobil, jumlah_servis_motor, 0), set_labels = ('Mobil', 'Motor'))
plt.title('Diagram Venn: Perbandingan Jumlah Servis antara Mobil dan Motor')
plt.show()
