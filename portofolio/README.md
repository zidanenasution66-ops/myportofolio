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