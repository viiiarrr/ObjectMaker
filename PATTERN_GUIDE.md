# 🎯 Artboard1 Pattern Generator - Panduan Lengkap

## ✨ Konsep Utama

Program ini akan **membaca gambar Artboard1.png** dan **membuat sphere-sphere yang membentuk pola/bentuk sesuai gambar tersebut**. Ini seperti "pixel art" menggunakan sphere yang bergerak!

## 🎮 Kontrol Utama

### **⭐ PATTERN GENERATION (Fitur Utama):**
- **G** = Generate sphere pattern dari Artboard1.png 
- **1** = Pattern kecil (50 spheres)
- **2** = Pattern sedang (100 spheres) 
- **3** = Pattern besar (200 spheres)
- **P** = Toggle physics ON/OFF

### **🎨 MANUAL CONTROLS:**
- **Left Click** = Tambah sphere manual
- **Right Click** = Tambah sphere warna
- **SPACE** = Toggle trail mode
- **C** = Clear semua sphere
- **ESC** = Keluar

## 🎯 Cara Menggunakan

### **Langkah 1: Pastikan Artboard1.png Ada**
File harus ada di: `assets/images/Artboard1.png`

### **Langkah 2: Jalankan Program**
```bash
python sphere_drawings.py
```

### **Langkah 3: Generate Pattern**
- Tekan **G** untuk membuat sphere pattern dari gambar Anda
- Atau tekan **1**, **2**, atau **3** untuk ukuran berbeda

### **Langkah 4: Kontrol Physics**
- Tekan **P** untuk mematikan physics = sphere tetap di posisi pattern
- Tekan **P** lagi untuk menghidupkan physics = sphere bergerak

## 🔧 Cara Kerja

1. **Analisis Gambar**: Program membaca pixel Artboard1.png
2. **Deteksi Bentuk**: Mencari pixel yang bukan background (putih)
3. **Generate Posisi**: Membuat koordinat sphere sesuai bentuk gambar
4. **Render Sphere**: Menempatkan sphere di posisi yang tepat
5. **Physics Simulation**: Sphere bisa bergerak atau tetap diam

## 🎨 Tips untuk Gambar Artboard1.png

### ✅ **Gambar yang Bagus:**
- **Background putih** atau transparan
- **Bentuk dengan kontras tinggi** (hitam, warna gelap)
- **Resolusi cukup** (200x200 hingga 800x800)
- **Bentuk simple** dengan garis tegas

### ❌ **Hindari:**
- Gambar dengan detail terlalu halus
- Background dengan warna gelap
- Gradasi atau blur yang berlebihan

## 🎭 Mode Visualisasi

### **Physics OFF (P):**
- Sphere tetap membentuk pattern gambar
- Tidak ada gerakan atau physics
- Perfect untuk melihat bentuk asli

### **Physics ON (P):**
- Sphere bergerak dengan gravity & physics
- Menciptakan animasi artistik
- Pattern berubah menjadi art dinamis

### **Trail Mode (SPACE):**
- **ON**: Trail persisten, menciptakan efek lukisan
- **OFF**: Clear screen setiap frame

## 🎯 Workflow Recommended

1. **Generate Pattern**: Tekan **G** 
2. **Lihat Bentuk**: Physics OFF dengan **P**
3. **Mulai Animasi**: Physics ON dengan **P**
4. **Artistic Mode**: Toggle trail dengan **SPACE**
5. **Reset**: Tekan **C** untuk mulai lagi

## 💡 Ideas Kreatif

- **Logo Animation**: Gunakan logo sebagai Artboard1
- **Text Pattern**: Buat teks besar di Artboard1  
- **Symbol Art**: Gunakan simbol atau icon
- **Character Outline**: Gambar karakter simple
- **Geometric Shapes**: Bentuk-bentuk geometris

## 🐛 Troubleshooting

**Pattern tidak muncul?**
- ✅ Pastikan Artboard1.png ada di assets/images/
- ✅ Cek background gambar putih/transparan
- ✅ Gunakan kontras tinggi untuk bentuk utama

**Sphere terlalu sedikit?**
- ✅ Tekan **3** untuk pattern besar
- ✅ Cek apakah gambar punya area hitam/warna cukup

**Pattern tidak sesuai bentuk?**
- ✅ Simplify gambar Anda
- ✅ Gunakan bentuk yang lebih tegas
- ✅ Increase kontras warna

**Selamat menciptakan seni digital dengan pola gambar Anda! 🎨✨**
