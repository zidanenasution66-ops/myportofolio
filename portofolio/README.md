Nama : Zidane Ahdina Putra
NPM : 2506583953
Kelas : PBP F


### Tugas 1

1. Ya, aku menggunakan elemen semantik HTML5, contohnya adalah `<header>`, `<main>`, `<section>`, dan `<footer>`. Elemen-elemen ini sangat membantu dalam menyusun static web secara terstruktur dan bersihlah menurut standar ku :).Penggunaan tag seperti `<section class="hero">`, `<section id="experience">`, `<section id="skills">`, dan `<section id="projects">` juga memudahkan pembacaan hierarki halaman di web yang aku buat, baik bagi pengembang (aku, karena kalau gaada ini yang ada aku pusing sendiri) maupun bagi mesin pencari (Search Engine Optimization/SEO) dan screen reader untuk memahami navigasi serta konten portofolio secara logis.

2. Tantangan tata letak utama yang aku temukan saat membuat tampilan responsive adalah mengatur tata letak grid pada bagian Hero (terutama antara foto profil, identitas, dan detail meta) serta cards grid agar tidak bertabrakan atau menyempit berlebihan di layar kecil. 
   
   Aku mengevaluasinya dengan pendekatan mobile-first/desktop-adaptation menggunakan `@media (max-width: 600px)`:
   * Pada layar mobile, tata letak multi-kolom CSS Grid direvisi menjadi single-column (`grid-template-columns: 1fr`) dengan mereset `grid-template-areas` agar elemen mengalir secara vertikal.
   * Ukuran teks utama (`h1`) diatur fleksibel menggunakan `clamp()`, dan batas lebar foto (`max-width: 220px`) disesuaikan agar tidak memakan seluruh ruang layar HP, sehingga teks informasi tetap menjadi prioritas utama yang mudah dibaca.

3. Batasan dari static web murni yang ku rasakan yaitu konten portofolio bersifat statis dan kaku (harus mengubah kode HTML/CSS secara manual tiap kali ada perubahan data proyek atau pengalaman), serta ngak ada interaktivitas dinamis seperti form kontak yang bisa langsung mengirim email/menyimpan pesan ke database.

   Kalau ditanya apa fungsionalitas dinamis yang ingin aku tambahkan pada iterasi selanjutnya yang kepikiran cuman Integrasi Database & Admin Panel (Django) buat mengelola data proyek, skills, dan experience secara dinamis melalui Django Admin/ORM tanpa perlu hardcode di file HTML.

Aku tidak memakai AI sih, karena tambahan yang aku masukkan ke web ku juga simple, tidak ada gimmick ataupun sistem interaksi unik yang ada. Ku cuman nambahin dikit berdasarkan tutorial yang aku temukan di internet.



### Tugas 2

1. Jadi gini, alur di Django itu kan pakai pola MVT (Model-View-Template). Pas user ngebuka halaman skills di browser, request-nya pertama kali masuk ke myportofolio/urls.py di tingkat proyek yang mengarahkan lalu lintas URL ke namespace aplikasi yang sesuai, lalu main/urls.py di tingkat aplikasi bakal mencocokkan path skills tersebut dan memanggil fungsi show_skills yang ada di views.py. Nah, fungsi di views.py ini bertugas mengatur logikanya dengan meminta data ke models.py melalui perintah Skill.objects.all(). Kelas Skill di model inilah yang menjembatani logika Python dengan database untuk mengambil seluruh data keahlian, begitu datanya dapat, views.py bakal membungkus data tersebut ke dalam context dictionary lalu menginstruksikan template skills.html untuk memprosesnya. Di dalam template, tag-tag Django Template Language bakal diolah sampai jadi dokumen HTML utuh. Terakhir, view bakal mengembalikan HTML tersebut sebagai respon ke browser kita supaya tampilannya bisa kelihatan.

2. Karena menyimpan data portofolio pakai model itu jauh lebih mending daripada tulis langsung (hardcode) di dalam template HTML, mengapa? karena dengan memakai model ku bisa memisahkan urusan tampilan UI sama urusan pengelolaan data yang dimana ini berdampak pas aku mengelola website, kalau aku mau nambah atau mengubah daftar keahlian, aku tinggal atur dari database atau Django Admin tanpa perlu mengutak-atik berkas HTML-nya lagi, karena kalau utak-atik berkas HTML lagi bakal ada risiko error sintaksis di kode tampilan. Website juga jadi jauh lebih gampang dikembangkan, soalnya data yang sudah ada di model bisa dipanggil lagi di halaman atau fitur lain dengan efisien tanpa perlu bikin kode yang sama berulang kali.

3. Nah, untuk perintah pengelolaan database, `makemigrations` sama `migrate` ini fungsinya saling melengkapi di Django. Perintah `python manage.py makemigrations` itu tugasnya memantau setiap perubahan yang dibuat di models.py, lalu menerjemahkannya jadi berkas cetak biru berupa kode Python di dalam folder `migrations/`. Perintah ini belum mengubah isi database-nya secara langsung, sedangkan perintah `python manage.py migrate` baru bertugas mengeksekusi berkas-berkas migrasi tadi untuk mengubah struktur tabel di database secara nyata. Sebagai contoh, misal mau menambah field baru `proficiency_level = models.IntegerField(default=1)` pada kelas `Skill` di `models.py`. Kita wajib menjalankan `makemigrations` dulu buat mencatat skema kolom barunya, baru habis itu jalanin `migrate` supaya kolom `proficiency_level` tersebut benar-benar dibuat di tabel database.