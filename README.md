# UAS Teknik Optimasi 2026

## Data Mahasiswa
- **Nama**: Hidayat Lossen
- **NIM**: 2300018116
- **Kelas**: A
- **Mata Kuliah**: Teknik Optimasi 2026
- **Tanggal UAS**: 28 Januari 2026

---

## Soal UAS

Diberikan dua algoritma optimasi berbasis populasi yaitu Ant Colony Optimization (ACO) dan Genetic Algorithm (GA).

### Soal 1: Genetic Algorithm (GA) - Optimasi Paket Parcel Lebaran
Selesaikanlah permasalahan penentuan paket parcel lebaran menggunakan Genetic Algorithm dengan objektif selisih kembalian terkecil.

**Parameter yang digunakan:**
- Jumlah kromosom = 25
- Crossover rate = 0.23
- Mutation rate = 0.1
- Max generation = 55
- Budget = Rp. 125.000

**Penyelesaian harus memuat:**
- a. Output nilai minimum yang dihasilkan di tiap iterasi dalam bentuk tabel dengan dua kolom yaitu iterasi dan nilai minimum
- b. Nilai minimum global/akhir yang diperoleh

### Soal 2: Ant Colony Optimization (ACO) - Rute Ziarah Wali Songo
Selesaikanlah permasalahan rute terpendek ziarah wali songo menggunakan ACO. Titik berangkat dan akhir adalah dari rumah/kos.

**Parameter yang digunakan:**
- Q = 100
- ρ = 0.05
- antSize = 17
- t_max = 35

**Penyelesaian harus memuat:**
- a. Output nilai minimum yang dihasilkan di tiap iterasi dalam bentuk tabel dengan dua kolom yaitu iterasi dan nilai minimum
- b. Nilai minimum global/akhir yang diperoleh

---

## Hasil Output

### Soal 1: Algoritma Genetika (Genetic Algorithm)

```
============================================================
GENETIC ALGORITHM - OPTIMASI PAKET PARCEL
============================================================
Budget           : Rp 125,000
Jumlah Kromosom  : 25
Crossover Rate   : 0.23
Mutation Rate    : 0.1
Max Generation   : 55
Jumlah Produk    : 18
============================================================

Generation-1 -> Nilai Optimasi: 0.001427, Total: Rp 124,300, Kembalian: Rp 700
Generation-2 -> Nilai Optimasi: 0.001664, Total: Rp 124,400, Kembalian: Rp 600
Generation-3 -> Nilai Optimasi: 0.002849, Total: Rp 124,650, Kembalian: Rp 350
Generation-4 -> Nilai Optimasi: 0.002849, Total: Rp 124,650, Kembalian: Rp 350
Generation-5 -> Nilai Optimasi: 0.006623, Total: Rp 124,850, Kembalian: Rp 150
Generation-6 -> Nilai Optimasi: 0.000714, Total: Rp 123,600, Kembalian: Rp 1,400
Generation-7 -> Nilai Optimasi: 0.009901, Total: Rp 124,900, Kembalian: Rp 100
Generation-8 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-9 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-10 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-11 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-12 -> Nilai Optimasi: 0.001248, Total: Rp 124,200, Kembalian: Rp 800
Generation-13 -> Nilai Optimasi: 0.002849, Total: Rp 124,650, Kembalian: Rp 350
Generation-14 -> Nilai Optimasi: 0.000526, Total: Rp 123,100, Kembalian: Rp 1,900
Generation-15 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-16 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-17 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-18 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-19 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-20 -> Nilai Optimasi: 0.001248, Total: Rp 124,200, Kembalian: Rp 800
Generation-21 -> Nilai Optimasi: 0.001248, Total: Rp 124,200, Kembalian: Rp 800
Generation-22 -> Nilai Optimasi: 0.000625, Total: Rp 123,400, Kembalian: Rp 1,600
Generation-23 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-24 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-25 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-26 -> Nilai Optimasi: 0.003322, Total: Rp 124,700, Kembalian: Rp 300
Generation-27 -> Nilai Optimasi: 0.000588, Total: Rp 123,300, Kembalian: Rp 1,700
Generation-28 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-29 -> Nilai Optimasi: 0.000833, Total: Rp 123,800, Kembalian: Rp 1,200
Generation-30 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-31 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-32 -> Nilai Optimasi: 0.002849, Total: Rp 124,650, Kembalian: Rp 350
Generation-33 -> Nilai Optimasi: 0.009901, Total: Rp 124,900, Kembalian: Rp 100
Generation-34 -> Nilai Optimasi: 0.009901, Total: Rp 124,900, Kembalian: Rp 100
Generation-35 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-36 -> Nilai Optimasi: 0.000999, Total: Rp 124,000, Kembalian: Rp 1,000
Generation-37 -> Nilai Optimasi: 0.000999, Total: Rp 124,000, Kembalian: Rp 1,000
Generation-38 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-39 -> Nilai Optimasi: 0.006623, Total: Rp 124,850, Kembalian: Rp 150
Generation-40 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-41 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-42 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-43 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-44 -> Nilai Optimasi: 0.000833, Total: Rp 123,800, Kembalian: Rp 1,200
Generation-45 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-46 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-47 -> Nilai Optimasi: 0.009901, Total: Rp 124,900, Kembalian: Rp 100
Generation-48 -> Nilai Optimasi: 0.002494, Total: Rp 124,600, Kembalian: Rp 400
Generation-49 -> Nilai Optimasi: 0.000951, Total: Rp 123,950, Kembalian: Rp 1,050
Generation-50 -> Nilai Optimasi: 0.001248, Total: Rp 124,200, Kembalian: Rp 800
Generation-51 -> Nilai Optimasi: 0.001248, Total: Rp 124,200, Kembalian: Rp 800
Generation-52 -> Nilai Optimasi: 0.001248, Total: Rp 124,200, Kembalian: Rp 800
Generation-53 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-54 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200
Generation-55 -> Nilai Optimasi: 0.004975, Total: Rp 124,800, Kembalian: Rp 200

============================================================
Soal 1a. TABEL NILAI MINIMUM (KEMBALIAN) PER GENERASI
============================================================
Generasi        Kembalian (Rp)
-----------------------------------
1               700.00
2               600.00
3               350.00
4               350.00
5               150.00
6               1,400.00
7               100.00
8               400.00
9               400.00
10              400.00
11              400.00
12              800.00
13              350.00
14              1,900.00
15              300.00
16              400.00
17              200.00
18              300.00
19              300.00
20              800.00
21              800.00
22              1,600.00
23              300.00
24              300.00
25              300.00
26              300.00
27              1,700.00
28              400.00
29              1,200.00
30              400.00
31              400.00
32              350.00
33              100.00
34              100.00
35              400.00
36              1,000.00
37              1,000.00
38              400.00
39              150.00
40              200.00
41              200.00
42              200.00
43              200.00
44              1,200.00
45              400.00
46              400.00
47              100.00
48              400.00
49              1,050.00
50              800.00
51              800.00
52              800.00
53              200.00
54              200.00
55              200.00
============================================================

============================================================
Soal 1b. HASIL AKHIR OPTIMASI
============================================================
Nilai Optimasi  : 0.004975
Total Belanja   : Rp 124,800
Budget          : Rp 125,000
Kembalian       : Rp 200
Ditemukan pada Generasi ke-7
============================================================

============================================================
DETAIL PAKET PARCEL TERPILIH:
============================================================
VIDORAN Xmart 1+ Madu 125g          x4 = Rp     43,600
INDOMIE Nyemek Jogja Rendang        x4 = Rp     13,800
RICHEESE Wafer                      x2 = Rp     10,000
SO FRESH M. Angin Citrus            x3 = Rp     37,500
BEBEK Pembersih Kloset              x1 = Rp     19,900
------------------------------------------------------------
TOTAL BELANJA                            = Rp    124,800
BUDGET                                   = Rp    125,000
KEMBALIAN                                = Rp        200
============================================================

=== Data Mahasiswa ===
Nama : Hidayat Lossen
NIM  : 2300018116
UAS  : Teknik Optimasi 2026 - A
```

---

### Soal 2: Algoritma Koloni Semut (Ant Colony Optimization)

```
============================================================
ANT COLONY OPTIMIZATION - RUTE ZIARAH WALI SONGO
============================================================
Parameter:
- Q (Pheromone Constant)  : 100
- ρ (Evaporation Rate)    : 0.05
- Ant Size                : 17
- Max Iteration (t_max)   : 35
- Titik Awal & Akhir      : Kos
============================================================

============================================================
Soal 2a. TABEL NILAI MINIMUM PER ITERASI
============================================================
Iterasi    Nilai Minimum (km)  
------------------------------
1          1345.70
2          1289.40
3          1361.30
4          1414.40
5          1297.30
6          1382.60
7          1390.20
8          1318.40
9          1295.50
10         1344.50
11         1382.40
12         1318.20
13         1425.50
14         1321.20
15         1313.30
16         1374.40
17         1289.60
18         1337.80
19         1350.20
20         1318.20
21         1409.10
22         1361.40
23         1313.30
24         1368.60
25         1325.70
26         1367.00
27         1316.40
28         1366.80
29         1432.40
30         1316.40
31         1322.60
32         1297.30
33         1385.00
34         1345.10
35         1345.10
============================================================

============================================================
Soal 2b. NILAI MINIMUM GLOBAL/AKHIR
============================================================
Jarak Terpendek: 1289.40 km
Ditemukan pada iterasi ke-2

=== Rute Terpendek Ziarah Makam Wali Songo ===
Kos
Sunan Ampel (Surabaya)
Sunan Giri (Gresik)
Sunan Gresik
Sunan Drajat (Lamongan)
Sunan Bonang (Tuban)
Sunan Muria (Kudus)
Sunan Kudus
Sunan Kalijaga (Demak)
Sunan Gunung Jati (Cirebon)
Kos
Total : 1289.4 kilometer

=== Data Mahasiswa ===
Nama : Hidayat Lossen
NIM  : 2300018116
UAS  : Teknik Optimasi 2026 - A
```

---

## Kesimpulan

### Soal 1: Genetic Algorithm
- **Kembalian Terkecil**: Rp 100 (ditemukan di generasi ke-7, 33, 34, 47)
- **Solusi Akhir (Generasi 55)**: Kembalian Rp 200
- **Total Produk Terpilih**: 5 jenis produk (14 item)
- **Efisiensi Budget**: 99.84% (Rp 124,800 dari Rp 125,000)

### Soal 2: Ant Colony Optimization
- **Jarak Terpendek**: 1289.40 km
- **Ditemukan pada**: Iterasi ke-2
- **Jumlah Makam Dikunjungi**: 9 makam Wali Songo
- **Total Kota**: 10 (termasuk Kos sebagai start & finish)

---

## File Program
- `soal1_ga_parcel.py` - Program Genetic Algorithm untuk optimasi paket parcel
- `soal2_aco_walisongo.py` - Program Ant Colony Optimization untuk rute ziarah Wali Songo

---

*Dibuat untuk memenuhi UAS Teknik Optimasi 2026 - Kelas A*