#!/usr/bin/env python
# coding: utf-8

# # Y.Music

# <div style="border:solid black 2px; padding: 20px"><h1 style="color:green; margin-bottom:20px">Reviewer's comment v1</h1>
# Halo Joy!
# 
# Perkenalkan saya Naufal, disini saya akan mereview tugas Joy ya.
# 
# Saya akan memberikan beberapa komen seperti dibawah ini, tolong jangan dipindah, dirubah, maupun dihapus ya.
# 
# Komen yang saya berikan akan muncul dalam warna hijau, kuning, atau pun merah seperti ini:
# 
# <div class="alert alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Bagus, semua berjalan lancar.
# 
# </div>
# 
# <div class="alert alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Terdapat beberapa catatan.
# 
# </div>
# 
# <div class="alert alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Perlu beberapa perbaikan
# 
# </div>
# 
# Dan tentu saja Joy dapat menjawab saya dengan menggunakan ini
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# </div>

# <div style="border:solid black 2px; padding: 20px">
# <b>Reviewer's comment v1:</b>
#     
# <b>Overall Feedback</b> 
#     
# - Secara keseluruhan ini adalah hasil yang sangat bagus! Semoga konsisten kedepanya.
# - Namun terdapat beberapa poin dimana perlu perbaikan namun saya rasa bukan lah hal yang sulit seperti terdapat beberapa pengulangan yang kurang efektif baik dalam perumusan fungsi maupun penulisan koding.
#     
# Untuk perbaikan nya ditunggu ya!
# </div>
# 
#         

# <div style="border:solid black 2px; padding: 20px">
# <b>Reviewer's comment v2:</b>
#     
# <b>Overall Feedback</b> 
#     
# Selamat! project ini saya setujui dan bisa melanjutkan ke tahap selanjutnya. Ini merupakan kerja yang sangat bagus dan efisien. Dalam satu iterasi semua catatan dan perbaikan sudah dilakukan dengan baik. Namun tetap terdapat catatan yang mungkin akan membantu di masa depan. Semoga berhasil kedepanya!. 
# </div>
# 
#         

# # Konten <a id='back'></a>
# 
# * [Pendahuluan](#intro)
# * [Tahap 1. Ikhtisar Data](#data_review)
#     * [Kesimpulan](#data_review_conclusions)
# * [Tahap 2. Pra-pemrosesan Data](#data_preprocessing)
#     * [2.1 Gaya penulisan judul](#header_style)
#     * [2.2 Nilai-nilai yang hilang](#missing_values)
#     * [2.3 Duplikat](#duplicates)
#     * [2.4 Kesimpulan](#data_preprocessing_conclusions)
# * [Tahap 3. Menguji Hipotesis](#hypotheses)
#     * [3.1 Hipotesis 1: aktivitas pengguna di dua kota](#activity)
#     * [3.2 Hipotesis 2: preferensi musik pada hari Senin dan Jumat](#week)
#     * [3.3 Hipotesis 3: preferensi genre di kota Springfield dan Shelbyville](#genre)
# * [Temuan](#end)

# ## Pendahuluan <a id='intro'></a>
# Setiap kali kita melakukan penelitian, kita perlu merumuskan hipotesis yang kemudian dapat kita uji. Terkadang kita menerima hipotesis ini; tetapi terkadang kita juga menolaknya. Untuk membuat keputusan yang tepat, sebuah bisnis harus dapat memahami apakah asumsi yang dibuatnya benar atau tidak.
# 
# Dalam proyek kali ini, Anda akan membandingkan preferensi musik kota Springfield dan Shelbyville. Anda akan mempelajari data Y.Music yang sebenarnya untuk menguji hipotesis di bawah ini dan membandingkan perilaku pengguna di kedua kota ini.
# 
# ### Tujuan: 
# Menguji tiga hipotesis:
# 1. Aktivitas pengguna berbeda-beda tergantung pada hari dan kotanya.
# 2. Pada senin pagi, penduduk Springfield dan Shelbyville mendengarkan genre yang berbeda. Hal ini juga ini juga berlaku untuk Jumat malam.
# 3. Pendengar di Springfield dan Shelbyville memiliki preferensi yang berbeda. Di Springfield, mereka lebih suka musik pop, sementara Shelbyville, musik rap memiliki lebih banyak penggemar.
# 
# ### Tahapan
# Data tentang perilaku pengguna disimpan dalam berkas `/datasets/music_project_en.csv`. Tidak ada informasi tentang kualitas data, jadi Anda perlu memeriksanya lebih dahulu sebelum menguji hipotesis.
# 
# Pertama, Anda akan mengevaluasi kualitas data dan melihat apakah masalahnya signifikan. Kemudian, selama pra-pemrosesan data, Anda akan mencoba memperhitungkan masalah yang paling serius.
#  
# Proyek ini akan terdiri dari tiga tahap:
#  1. Ikhtisar Data
#  2. Pra-pemrosesan Data
#  3. Menguji Hipotesis
# 
#  
# [Kembali ke Daftar Isi](#back)

# ## Tahap 1. Ikhtisar Data <a id='data_review'></a>
# 
# Buka data di Y.Music lalu jelajahi data yang ada di sana.

# Anda akan membutuhkan `Pandas`, jadi Anda harus mengimpornya.

# In[2]:


# mengimpor Pandas
import pandas as pd


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Bagus! `pandas` terimpor dengan benar, bahkan beserta singkatan yang umum dipakai.
# 
# </div>

# Baca file `music_project_en.csv` dari folder `/datasets/` lalu simpan di variabel `df`:

# In[3]:


# membaca berkas dan menyimpannya ke df
df = pd.read_csv('/datasets/music_project_en.csv')
df.describe()


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Penulisan direktori sudah benar dengan mencantumkan folder `/datasets/` serta penggunaan `describe()` untuk melihan informasi data secara cepat.
# 
# </div>

# Tampilkan 10 baris tabel pertama:

# In[4]:


# memperoleh 10 baris pertama dari tabel df
df.head(10)


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# `print()` sudah tidak diperlukan disini karena memang sudah merupakan baris terakhir d sel tersebut sehingga auto menampilkan outpunya.
# 
# </div>

# Memperoleh informasi umum tentang tabel dengan satu perintah:

# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Sepertinya ini seharusnya sebagai komen.
# 
# </div>

# In[5]:


# memperoleh informasi umum tentang data di df
df.info()


# <div class="alert alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Pilihan yang tepat menggunakan `info()` untuk menampilkan banyak informasi dari dataframe dengan efisien.
# 
# </div>

# Tabel ini berisi tujuh kolom. Semuanya menyimpan tipe data yang sama, yaitu: `objek`.
# 
# Berdasarkan dokumentasi:
# - `'userID'` — pengenal pengguna
# - `'Track'` — judul trek
# - `'artist'` — nama artis
# - `'genre'`
# - `'City'` — kota tempat pengguna berada
# - `'time'` — lama waktu lagu tersebut dimainkan
# - `'Day'` — nama hari
# 
# Kita dapat melihat tiga masalah dengan gaya penulisan nama kolom:
# 1. Beberapa nama huruf besar, beberapa huruf kecil.
# 2. Ada penggunaan spasi pada beberapa nama.
# 3. Kolom artist diawali dengan huruf kapital
# 
# Jumlah nilai kolom berbeda. Ini berarti data mengandung nilai yang hilang.
# 

# ### Kesimpulan <a id='data_review_conclusions'></a> 
# 
# Setiap baris dalam tabel menyimpan data pada lagu yang dimainkan. Beberapa kolom menggambarkan lagu itu sendiri: judul, artis, dan genre. Sisanya menyampaikan informasi tentang pengguna: kota asal mereka, waktu mereka memutar lagu.
# 
# Jelas bahwa data tersebut cukup untuk menguji hipotesis. Namun, ada nilai-nilai yang hilang.
# 
# Selanjutnya, kita perlu melakukan pra-pemrosesan data terlebih dahulu.

# [Kembali ke Daftar Isi](#back)

# ## Tahap 2. Pra-pemrosesan Data <a id='data_preprocessing'></a>
# Perbaiki format pada judul kolom dan atasi nilai yang hilang. Kemudian, periksa apakah ada duplikat dalam data.

# ### Gaya Penulisan Judul <a id='header_style'></a>
# Tampilkan judul kolom:
# 

# In[6]:


# daftar nama kolom di tabel df
df.columns


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Pengulangan dari sebelumnya bahwa `print()` sudah tidak diperlukan disini karena memang sudah merupakan baris terakhir d sel tersebut sehingga auto menampilkan outpunya.
# 
# </div>

# Ubah nama kolom sesuai dengan aturan gaya penulisan yang baik:
# * Jika nama memiliki beberapa kata, gunakan snake_case
# * Semua karakter harus menggunakan huruf kecil
# * Hapus spasi

# In[7]:


# mengganti nama kolom
df = df.rename(
    columns={
        '  userID': 'user_id',
        'Track': 'track',
       '  City  ': 'city',
        'Day': 'day' 
    }
)


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Semua berjalan dengan lancar.
# 
# </div>

# Periksa hasilnya. Tampilkan nama kolom sekali lagi:

# In[8]:


# hasil pengecekan: daftar nama kolom
df.columns


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# `print()` sudah tidak diperlukan disini karena memang sudah merupakan baris terakhir d sel tersebut sehingga auto menampilkan outpunya.
# 
# </div>

# [Kembali ke Daftar Isi](#back)

# ### Nilai-Nilai yang Hilang <a id='missing_values'></a>
# Pertama, temukan jumlah nilai yang hilang dalam tabel. Untuk melakukannya, gunakan dua metode `Pandas`:

# In[9]:


# menghitung nilai yang hilang
df.isna().sum()


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Sama dengan sebelumnya `print()` sudah tidak diperlukan disini karena memang sudah merupakan baris terakhir d sel tersebut sehingga auto menampilkan outpunya.
# 
# </div>

# Tidak semua nilai yang hilang berpengaruh terhadap penelitian. Misalnya, nilai yang hilang dalam `track` dan `artist` tidak begitu penting. Anda cukup menggantinya dengan tanda yang jelas.
# 
# Namun nilai yang hilang dalam `'genre'` dapat memengaruhi perbandingan preferensi musik di Springfield dan Shelbyville. Dalam kehidupan nyata, ini akan berguna untuk mempelajari alasan mengapa data tersebut hilang dan mencoba memperbaikinya. Tetapi kita tidak memiliki kesempatan itu dalam proyek ini. Jadi Anda harus:
# * Isi nilai yang hilang ini dengan sebuah tanda
# * Evaluasi seberapa besar nilai yang hilang dapat memengaruhi perhitungan Anda

# Ganti nilai yang hilang pada `'track'`, `'artist'`, dan `'genre'` dengan string `'unknown'`. Untuk melakukannya, buat list `columns_to_replace`, lakukan *loop* dengan `for`, dan ganti nilai yang hilang di setiap kolom:

# In[10]:


# loop nama kolom dan ganti nilai yang hilang dengan 'unknown'
columns_to_replace = ['track', 'artist', 'genre']

for row in df:
        df[columns_to_replace] = df[columns_to_replace].fillna('unknown') 
        
print(df)


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Looping berjalan dengan lancar, penggantian nilai berjalan tanpa masalah. Sebagai pengingat lagi bahwa `print()` tidak diperlukan.
# 
# </div>

# Pastikan tidak ada tabel lagi yang berisi nilai yang hilang. Hitung kembali nilai yang hilang.

# In[11]:


# menghitung nilai yang hilang
df.isna().sum()


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# `print()` sudah tidak diperlukan disini karena memang sudah merupakan baris terakhir d sel tersebut sehingga auto menampilkan outpunya.
# 
# </div>

# [Kembali ke Daftar Isi](#back)

# ### Duplikat <a id='duplicates'></a>
# Temukan jumlah duplikat yang jelas dalam tabel menggunakan satu perintah:

# In[12]:


# menghitung duplikat yang jelas
df.duplicated().sum()


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Perhitungan duplikat sudah dilakukan secara benar dan efisien. Dan lagi `print()` tidak perlu digunakan.
# 
# </div>

# Panggil metode `Pandas` untuk menghapus duplikat yang jelas:

# In[13]:


# menghapus duplikat yang jelas
df = df.drop_duplicates() 


# Hitung duplikat yang jelas sekali lagi untuk memastikan Anda telah menghapus semuanya:

# In[14]:


# memeriksa duplikat
df.duplicated().sum()


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# `print()` sudah tidak diperlukan disini karena memang sudah merupakan baris terakhir d sel tersebut sehingga auto menampilkan outpunya.
# 
# </div>

# Sekarang hapus duplikat implisit di kolom `genre`. Misalnya, nama genre dapat ditulis dengan cara yang berbeda. Kesalahan seperti ini juga akan memengaruhi hasil.

# Tampilkan daftar nama genre yang unik, urutkan berdasarkan abjad. Untuk melakukannya:
# * Ambil kolom DataFrame yang dimaksud
# * Terapkan metode pengurutan untuk itu
# * Untuk kolom yang diurutkan, panggil metode yang akan menghasilkan semua nilai kolom yang unik

# In[15]:


# melihat nama genre yang unik
df['genre'].sort_values().unique()


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Masih terdapat nilai yang duplikat atau tidak unik.
# 
# </div>

# <div class="alert alert-success">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Masalah sudah teratasi dengan baik.
# 
# </div>

# Lihat melalui *list* untuk menemukan duplikat implisit dari genre `hiphop`. Ini bisa berupa nama yang ditulis secara salah atau nama alternatif dari genre yang sama.
# 
# Anda akan melihat duplikat implisit berikut:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Untuk menghapusnya, gunakan fungsi `replace_wrong_genres()` dengan dua parameter:
# * `wrong_genres=` — daftar duplikat
# * `correct_genre=` — string dengan nilai yang benar
# 
# Fungsi harus mengoreksi nama dalam kolom `'genre'` dari tabel `df`, yaitu mengganti setiap nilai dari daftar `wrong_genres` dengan nilai dalam `correct_genre`.

# In[16]:


# fungsi untuk mengganti duplikat implisit
def replace_wrong_genre(wrong_genres, correct_genre): 
    for wrong_genre in wrong_genres: 
        df['genre'] = df['genre'].replace(wrong_genres, correct_genre)


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Fungsi terdefinisi dengan benar.
# 
# </div>

# Panggil `replace_wrong_genres()` dan berikan argumennya sehingga menghapus duplikat implisit (`hip`, `hop`, dan `hip-hop`) dan menggantinya dengan `hiphop`:

# In[17]:


# menghapus duplikat implisit
duplicates = ['hip', 'hop', 'hip-hop']
right_genre = 'hiphop'
replace_wrong_genre(duplicates, right_genre)


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Tidak ada error. Sepertinya drop_duplicate tidak diperlukan lagi
# 
# </div>

# Pastikan nama duplikat telah dihapus. Tampilkan daftar nilai unik dari kolom `'genre'`:

# In[18]:


# memeriksa duplikat implisit
df['genre'].sort_values().unique()


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Sama halnya dengan bagian sebelumnya, `print()` tidak diperlukan dan daftar genre yang unik dan berurutan sudah didapatkan. Namun alangkah lebih baiknya untuk mengurutkan nilai di dataframe menggunakan metode `sort_values()` sehingga seperti ini `df['genre'].sort_values().unique()`.
# 
# </div>

# [Kembali ke Daftar Isi](#back)

# ### Kesimpulan <a id='data_preprocessing_conclusions'></a>
# Kita mendeteksi tiga masalah dengan data:
# 
# - Gaya penulisan judul yang salah
# - Nilai-nilai yang hilang
# - Duplikat yang jelas dan implisit
# 
# Judul telah dibersihkan untuk mempermudah pemrosesan tabel.
# 
# Semua nilai yang hilang telah diganti dengan `'unknown'`. Tapi kita masih harus melihat apakah nilai yang hilang dalam `'genre'` akan memengaruhi perhitungan kita.
# 
# Tidak adanya duplikat akan membuat hasil lebih tepat dan lebih mudah dipahami.
# 
# Sekarang kita dapat melanjutkan ke pengujian hipotesis.

# [Kembali ke Daftar Isi](#back)

# ## Tahap 3. Menguji Hipotesis <a id='hypotheses'></a>

# ### Hipotesis 1: Membandingkan Perilaku Pengguna di Dua Kota <a id='activity'></a>

# Menurut hipotesis pertama, pengguna dari Springfield dan Shelbyville memiliki perbedaan dalam mendengarkan musik. Pengujian ini menggunakan data pada hari: Senin, Rabu, dan Jumat.
# 
# * Pisahkan pengguna ke dalam kelompok berdasarkan kota.
# * Bandingkan berapa banyak lagu yang dimainkan setiap kelompok pada hari Senin, Rabu, dan Jumat.

# Untuk latihan, lakukan setiap perhitungan secara terpisah.
# 
# Evaluasi aktivitas pengguna di setiap kota. Kelompokkan data berdasarkan kota dan temukan jumlah lagu yang diputar di setiap kelompok.
# 
# 

# In[19]:


# Menghitung lagu yang diputar di setiap kota
group_city = df.groupby('city')['user_id'].count()
group_city


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Hanya diperlukan satu kolom saja yang digunakan dalam pengelompokkan agar informasi terkait aktivitas pengguna di setiap kota diatas lebih mudah dipahami.
# 
# </div>

# <div class="alert alert-warning">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# `print()` tidak diperlukan disini.
# 
# </div>

# Springfield memiliki lebih banyak lagu yang dimainkan daripada Shelbyville. Namun bukan berarti warga Springfield lebih sering mendengarkan musik. Kota ini lebih besar, dan memiliki lebih banyak pengguna.
# 
# Sekarang kelompokkan data menurut hari dan temukan jumlah lagu yang diputar pada hari Senin, Rabu, dan Jumat.

# In[20]:


# Menghitung trek yang diputar pada masing-masing hari
group_day = df.groupby('day')['user_id'].count()
group_day


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Sama seperti sebelumnya hanya diperlukan satu kolom saja yang digunakan dalam pengelompokkan agar informasi terkait aktivitas pengguna di setiap kota diatas lebih mudah dipahami.
# 
# </div>

# <div class="alert alert-warning">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# `print()` tidak diperlukan untuk menampilkan output apabila sudah berada di baris terakhir di sebuah sel.
# 
# </div>

# Rabu adalah hari paling tenang secara keseluruhan. Tetapi jika kita mempertimbangkan kedua kota secara terpisah, kita mungkin akan memiliki kesimpulan yang berbeda.

# Anda telah melihat cara kerja pengelompokan berdasarkan kota atau hari. Sekarang tulis fungsi yang akan dikelompokkan berdasarkan keduanya.
# 
# Buat fungsi `number_tracks()` untuk menghitung jumlah lagu yang diputar untuk hari dan kota tertentu. Ini akan membutuhkan dua parameter:
# * nama hari
# * nama kota
# 
# Dalam fungsi, gunakan variabel untuk menyimpan baris dari tabel asli, di mana:
#   *  Nilai kolom `'day'` sama dengan parameter `day`
#   * Nilai kolom `'city'` sama dengan parameter `city`
# 
# Terapkan pemfilteran berurutan dengan pengindeksan logis.
# 
# Kemudian hitung nilai kolom `'user_id'` pada tabel yang dihasilkan. Simpan hasilnya ke variabel baru. Kembalikan variabel ini dari fungsi.

# In[23]:


# <membuat fungsi number_tracks()>
# Kita akan mendeklarasikan sebuah fungsi dengan dua parameter: day=, city=.
# Biarkan variabel track_list menyimpan baris df di mana
# nilai di kolom 'day' sama dengan parameter day= dan, pada saat yang sama,
# nilai pada kolom 'city' sama dengan parameter city= (terapkan pemfilteran berurutan
# dengan pengindeksan logis).
# Biarkan variabel track_list_count menyimpan jumlah nilai kolom 'user_id' pada track_list
# (temukan dengan metode count()).
# Biarkan fungsi menghasilkan jumlah: nilai track_list_count.

# Fungsi menghitung lagu yang diputar untuk kota dan hari tertentu.
# Pertama-tama ini akan mengambil baris dengan hari yang diinginkan dari tabel,
# kemudian memfilter baris hasilnya dengan kota yang dimaksud,
# kemudian temukan jumlah nilai 'user_id' pada tabel yang difilter,
# kemudian menghasilkan jumlah tersebut.
# Untuk melihat apa yang dihasilkan, kemas pemanggilan fungsi pada print().


def number_tracks(data, day, city):
        track_list = data.loc[(data['day'] == day) & (data['city'] == city)]
        track_list_count = track_list['user_id'].count()
        print(track_list_count)


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Tahap melakukan filter berdasarkan `day` dan `city` masih belum terdefinisi.
# 
# </div>

# <div class="alert alert-success">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# OK!
# 
# </div>

# Panggil `number_tracks()` enam kali dan ubahlah nilai parameternya, sehingga Anda bisa mengambil data di kedua kota untuk masing-masing hari tersebut.

# In[24]:


# jumlah lagu yang diputar di Springfield pada hari Senin
number_tracks(data=df, day='Monday', city='Springfield')


# In[25]:


# jumlah lagu yang diputar di Shelbyville pada hari Senin
number_tracks(data=df, day='Monday', city='Shelbyville')


# In[26]:


#  jumlah lagu yang diputar di Springfield pada hari Rabu
number_tracks(data=df, day='Wednesday', city='Springfield')


# In[27]:


#  jumlah lagu yang diputar di Shelbyville pada hari Rabu
number_tracks(data=df, day='Wednesday', city='Shelbyville')


# In[28]:


# jumlah lagu yang diputar di Springfield pada hari Jumat
number_tracks(data=df, day='Friday', city='Springfield')


# In[29]:


# jumlah lagu yang diputar di Shelbyville pada hari Jumat
number_tracks(data=df, day='Friday', city='Shelbyville')


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Masih terdapat sel yang kosong
# </div>

# <div class="alert alert-success">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Kerja yang bagus.
# 
# </div>

# Gunakan `pd.DataFrame` untuk membuat tabel, di mana
# * Nama kolom adalah: `['city', 'monday', 'wednesday', 'friday']`
# * Data adalah hasil yang Anda dapatkan dari `number_tracks()`

# In[111]:


# tabel dengan hasil
data_number_tracks = [
    ['Springfield', 15740, 11056, 15945],
    ['Shelbyville', 5614, 7003, 5895]
]

kolom = ['city', 'monday', 'wednesday', 'friday']

tabel_hipotesis_1 = pd.DataFrame(data = data_number_tracks, columns= kolom)

tabel_hipotesis_1


# **Kesimpulan**
# 
# Data mengungkapkan perbedaan perilaku pengguna:
# 
# - Pada Springfield, jumlah lagu yang diputar mencapai puncaknya pada hari Senin dan Jumat, sedangkan pada hari Rabu terjadi penurunan aktivitas.
# - Di Shelbyville, pengguna lebih banyak mendengarkan musik pada hari Rabu, tetapi sebaiknya pengguna di Shelbyville meningkatkan lagu yang didengar pada hari Senin dan Jumat .
# 
# Aktivitas pengguna pada hari Senin dan Jumat paling banyak.

# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Masih terdapat sel yang kosong
# </div>

# <div class="alert alert-success">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Mantab
# 
# </div>

# [Kembali ke Daftar Isi](#back)

# ### Hipotesis 2: Musik di Awal dan Akhir Minggu <a id='week'></a>

# Menurut hipotesis kedua, pada Senin pagi dan Jumat malam, warga Springfield mendengarkan genre yang berbeda dari yang dinikmati warga Shelbyville.

# Dapatkan tabel (pastikan nama tabel gabungan Anda cocok dengan DataFrame yang diberikan dalam dua blok kode di bawah):
# * Untuk Springfield — `spr_general`
# * Untuk Shelbyville — `shel_general`

# In[30]:


# mendapatkan tabel spr_general dari baris df,
# dimana nilai dari kolom 'city' adalah 'Springfield'
spr_general = df[df['city'] == 'Springfield']


# In[31]:


# mendapatkan shel_general dari baris df,
# dimana nilai dari kolom 'city' adalah 'Shelbyville'
shel_general = df[df['city'] == 'Shelbyville']


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Semua berjalan dengan lancar.
# 
# </div>

# Tulis fungsi `genre_weekday()` dengan empat parameter:
# * Sebuah tabel untuk data
# * Nama hari
# * Tanda waktu pertama, dalam format 'hh:mm'
# * Tanda waktu terakhir, dalam format 'hh: mm'
# 
# Fungsi tersebut harus menghasilkan info tentang 15 genre paling populer pada hari tertentu dalam periode diantara dua tanda waktu.

# In[33]:


# Mendeklarasikan fungsi genre_weekday() dengan parameter day=, time1=, dan time2=. Itu harus
# memberikan informasi tentang genre paling populer pada hari dan waktu tertentu:

# 1) Biarkan variabel genre_df menyimpan baris yang memenuhi beberapa ketentuan:
#    - nilai pada kolom 'day' sama dengan nilai argumen hari=
#    - nilai pada kolom 'time' lebih besar dari nilai argumen time1=
#    - nilai pada kolom 'time' lebih kecil dari nilai argumen time2=
#    Gunakan pemfilteran berurutan dengan pengindeksan logis.

# 2) Kelompokkan genre_df berdasarkan kolom 'genre', lalu ambil salah satu kolomnya,
#    dan gunakan metode count() untuk menemukan jumlah entri untuk masing-masing
#    genre yang diwakili; simpan Series yang dihasilkan ke
#    variabel genre_df_count

# 3) Urutkan genre_df_count dalam urutan menurun dan simpan hasilnya
#    ke variabel genre_df_sorted

# 4) Menghasilkan objek Series dengan nilai 15 genre_df_sorted pertama - 15 genre paling
#    populer (pada hari tertentu, dalam jangka waktu tertentu)

# tulis fungsi Anda di sini
def genre_weekday(df, day, time1, time2):
    # pemfilteran berturut-turut
    # genre_df hanya akan menyimpan baris df di mana day sama dengan day=
    # tulis kode program Anda di sini
    genre_df = df[df['day'] == day]
    # genre_df hanya akan menyimpan baris df di mana time lebih kecil dari time2=
    # tulis kode program Anda di sini
    genre_df = genre_df[genre_df['time'] < time2]
    # genre_df hanya akan menyimpan baris df di mana time lebih besar dari time1=
    # tulis kode program Anda di sini
    genre_df = genre_df[genre_df['time'] > time1]
    # kelompokkan DataFrame yang difilter berdasarkan kolom dengan nama genre, ambil kolom genre, dan temukan jumlah baris untuk setiap genre dengan metode count()
    # tulis kode program Anda di sini
    genre_df_grouped = genre_df.groupby('genre')['genre'].count()
    # kita akan mengurutkan hasilnya dalam urutan menurun (sehingga genre paling populer didahulukan pada objek Series
    # tulis kode program Anda di sini
    genre_df_sorted = genre_df_grouped.sort_values(ascending=False)
    # kita akan menghasilkan objek Series yang menyimpan 15 genre paling populer pada hari tertentu dalam jangka waktu tertentu
    return genre_df_sorted[:15]


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# Fungsi sudah didefinisikan dengan benar
# </div>

# Bandingkan hasil fungsi `genre_weekday()` untuk Springfield dan Shelbyville pada Senin pagi (dari pukul 07.00 hingga 11.00) dan pada Jumat malam (dari pukul 17:00 hingga 23:00):

# In[34]:


# memanggil fungsi untuk Senin pagi di Springfield (gunakan spr_general alih-alih tabel df)
genre_weekday(spr_general, 'Monday', '07:00', '11:00')


# In[116]:


# memanggil fungsi untuk Senin pagi di Shelbyville (gunakan shel_general alih-alih tabel df)
genre_weekday(shel_general, 'Monday', '07:00', '11:00')


# In[35]:


# memanggil fungsi untuk Jumat malam di Springfield
genre_weekday(spr_general, 'Friday', '17:00', '23:00')


# In[36]:


# memanggil fungsi untuk Jumat malam di Shelbyville
genre_weekday(shel_general, 'Friday', '17:00', '23:00')


# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
# 
# OK!
# 
# </div>

# **Kesimpulan**
# 
# Setelah membandingkan 15 genre teratas pada Senin pagi, kita dapat menarik kesimpulan berikut:
# 
# 1. Pengguna dari Springfield dan Shelbyville mendengarkan musik dengan genre yang sama. Lima genre teratas sama, hanya rock dan elektronik yang bertukar tempat.
# 
# 2. Di Springfield, jumlah nilai yang hilang ternyata sangat besar sehingga nilai `'unknown'` berada di urutan ke-10. Ini berarti bahwa nilai-nilai yang hilang memiliki jumlah data yang cukup besar, yang mungkin menjadi dasar untuk mempertanyakan ketepatan kesimpulan kita.
# 
# Untuk Jumat malam, situasinya serupa. Genre individu agak bervariasi, tetapi secara keseluruhan, 15 besar genre untuk kedua kota sama.
# 
# Dengan demikian, hipotesis kedua sebagian terbukti benar:
# * Pengguna mendengarkan musik yang sama di awal dan akhir minggu.
# * Tidak ada perbedaan yang mencolok antara Springfield dan Shelbyville. Pada kedua kota tersebut, pop adalah genre yang paling populer.
# 
# Namun, jumlah nilai yang hilang membuat hasil ini dipertanyakan. Di Springfield, ada begitu banyak yang memengaruhi 15 teratas kita. Jika kita tidak mengabaikan nilai-nilai ini, hasilnya mungkin akan berbeda.

# [Kembali ke Daftar Isi](#back)

# ### Hipotesis 3: Preferensi Genre di Springfield dan Shelbyville <a id='genre'></a>
# 
# Hipotesis: Shelbyville menyukai musik rap. Warga Springfield lebih menyukai pop.

# Kelompokkan tabel `spr_general` berdasarkan genre dan temukan jumlah lagu yang dimainkan untuk setiap genre dengan metode `count()`. Kemudian urutkan hasilnya dalam urutan menurun dan simpan ke `spr_genres`.

# In[21]:


# pada satu baris: kelompokkan tabel spr_general berdasarkan kolom 'genre',
# hitung nilai 'genre' dengan count() dalam pengelompokan,
# urutkan Series yang dihasilkan dalam urutan menurun, lalu simpan ke spr_genres

spr_genres = spr_general.groupby('genre')['genre'].count().sort_values(ascending=False)
spr_genres


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
#     
# Kolom `genre` tidak dipilih setelah pengelompokan sehingga terdapat perulangan informasi seperti di sel selanjutnya
# 
# </div>

# <div class="alert alert-warning">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Masalah sudah teratasi dengan baik. Tetapi penggunaan `print()` sudah tidak diperlukan disini.
# 
# </div>

# Tampilkan 10 baris pertama dari `spr_genres`:

# In[130]:


# menampilkan 10 baris pertama dari spr_genres
spr_genres.head(10)


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
#     
# Tidak perlu menggunakan `print()`.
# 
# </div>

# Sekarang lakukan hal yang sama pada data di Shelbyville.
# 
# Kelompokkan tabel `shel_general` berdasarkan genre dan temukan jumlah lagu yang dimainkan untuk setiap genre. Kemudian urutkan hasilnya dalam urutan menurun dan simpan ke tabel `shel_genres`:

# In[22]:


# pada satu baris: kelompokkan tabel shel_general menurut kolom 'genre',
# hitung nilai 'genre' dalam pengelompokan menggunakan count(),
# urutkan Series yang dihasilkan dalam urutan menurun dan simpan ke shel_genres

shel_genres = shel_general.groupby('genre')['genre'].count().sort_values(ascending=False)
shel_genres


# <div class="alert alert-danger">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
#     
# Perulangan dari sebelumnya kolom `genre` tidak dipilih setelah pengelompokan sehingga terdapat perulangan informasi seperti di sel selanjutnya
# 
# </div>

# <div class="alert alert-warning">
# <b>Reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# Penggunaan `print()` sudah tidak diperlukan disini.
# 
# </div>

# Tampilkan 10 baris pertama dari `shel_genres`:

# In[131]:


# menampilkan 10 baris pertama dari shel_genres
shel_genres.head(10)


# <div class="alert alert-warning">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
#     
# Tidak perlu menggunakan `print()`.
# 
# </div>

# **Kesimpulan**

# Hipotesis terbukti benar sebagian:
# * Musik pop adalah genre paling populer di Springfield, seperti yang diharapkan.
# * Namun, musik pop ternyata sama populernya baik di Springfield maupun di Shelbyville, dan musik rap tidak berada di 5 besar untuk kedua kota tersebut.
# 

# [Kembali ke Daftar Isi](#back)

# # Temuan <a id='end'></a>

# Kita telah menguji tiga hipotesis berikut:
# 
# 1. Aktivitas pengguna berbeda-beda tergantung pada hari dan kotanya.
# 2. Pada senin pagi, penduduk Springfield dan Shelbyville mendengarkan genre yang berbeda. Hal ini juga ini juga berlaku untuk Jumat malam.
# 3. Pendengar di Springfield dan Shelbyville memiliki preferensi yang berbeda. Baik Springfield maupun di Shelbyville, mereka lebih suka musik pop.
# 
# Setelah menganalisis data, kita dapat menyimpulkan:
# 
# 1. Aktivitas pengguna di Springfield dan Shelbyville bergantung pada harinya, walaupun kotanya berbeda.
# 
# Hipotesis pertama dapat diterima sepenuhnya.
# 
# 2. Preferensi musik tidak terlalu berbeda selama seminggu di Springfield dan Shelbyville. Kita dapat melihat perbedaan kecil dalam urutan pada hari Senin, tetapi:
# * Baik di Springfield maupun di Shelbyville, orang paling banyak mendengarkan musik pop.
# 
# Jadi hipotesis ini tidak dapat kita terima. Kita juga harus ingat bahwa hasilnya bisa berbeda jika bukan karena nilai yang hilang.
# 
# 3. Ternyata preferensi musik pengguna dari Springfield dan Shelbyville sangat mirip.
# 
# Hipotesis ketiga ditolak. Jika ada perbedaan preferensi, tidak dapat dilihat dari data ini.
# 
# ### Catatan
# Dalam proyek sesungguhnya, penelitian melibatkan pengujian hipotesis statistik, yang lebih tepat dan lebih kuantitatif. Perhatikan juga bahwa Anda tidak dapat selalu menarik kesimpulan tentang seluruh kota berdasarkan data dari satu sumber saja.
# 
# Anda akan mempelajari pengujian hipotesis dalam sprint analisis data statistik.

# <div class="alert alert-success">
# <b>Reviewer's comment v1</b> <a class="tocSkip"></a>
#     
# Secara keseluruhan ini adalah hasil yang sangat bagus namun terdapat beberapa catatan yang perlu diperbaiki.
# 
# </div>

# [Kembali ke Daftar Isi](#back)
