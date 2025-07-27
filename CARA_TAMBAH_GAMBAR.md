# Panduan Menambahkan Gambar Sendiri

## 📁 Lokasi File Gambar

**Letakkan semua gambar Anda di folder:**
```
e:\! UGM\!! GAMAFORCE\ObjectMaker\assets\images\
```

## 📋 Format Gambar yang Didukung

✅ **PNG** (Paling direkomendasikan - mendukung transparansi)
✅ **JPG/JPEG** (Bagus untuk foto)
✅ **GIF** (Mendukung animasi sederhana)
✅ **BMP** (Format Windows)

## 🎨 Tips Memilih Gambar

### 1. **Ukuran Optimal**
- **Ukuran ideal**: 64x64 hingga 128x128 pixel
- **Maksimal**: 256x256 pixel (untuk performa terbaik)
- Gambar akan otomatis di-resize sesuai ukuran sphere

### 2. **Background Transparan (PNG)**
```
✅ BAGUS: PNG dengan background transparan
❌ KURANG BAGUS: JPG dengan background putih/warna solid
```

### 3. **Kontras Tinggi**
- Gunakan warna-warna cerah dan kontras
- Hindari gambar dengan detail terlalu halus
- Gambar simple lebih terlihat jelas

### 4. **Contoh Gambar yang Cocok**
- 😀 Emoji/emoticon
- ⭐ Icon simple
- 🎮 Logo game
- 🔵 Bentuk geometris
- 🦄 Karakter kartun sederhana
- ⚡ Simbol/tanda

## 📂 Cara Menambahkan Gambar

### Langkah 1: Siapkan Gambar
1. Pilih gambar yang ingin digunakan
2. Edit gambar jika perlu (crop, resize, background removal)
3. Simpan dalam format PNG untuk hasil terbaik

### Langkah 2: Copy ke Folder
1. Buka folder: `e:\! UGM\!! GAMAFORCE\ObjectMaker\assets\images\`
2. Copy/paste file gambar Anda ke folder ini
3. Berikan nama yang mudah diingat (contoh: `my_logo.png`, `cute_cat.png`)

### Langkah 3: Jalankan Program
```bash
python sphere_drawings.py
```

### Langkah 4: Gunakan Gambar
- **Right Click**: Tambah sphere dengan gambar di posisi mouse
- **Tekan I**: Tambah sphere gambar random di posisi random
- **Left Click**: Tetap menambah sphere warna biasa

## 🔧 Kontrol Lengkap

| Input | Fungsi |
|-------|--------|
| **Left Click** | Tambah sphere warna biasa |
| **Right Click** | Tambah sphere dengan gambar |
| **I** | Tambah sphere gambar random |
| **R** | Tambah sphere warna random |
| **SPACE** | Toggle mode trail |
| **C** | Clear & reset |
| **ESC** | Keluar |

## 🐛 Troubleshooting

### Gambar Tidak Muncul?
1. ✅ Cek apakah file ada di `assets/images/`
2. ✅ Pastikan format file didukung (.png, .jpg, .gif, .bmp)
3. ✅ Cek nama file tidak mengandung karakter khusus
4. ✅ Restart program setelah menambah gambar baru

### Gambar Terlalu Buram?
1. ✅ Gunakan gambar dengan resolusi lebih tinggi
2. ✅ Hindari gambar dengan detail terlalu halus
3. ✅ Gunakan kontras warna yang tinggi

### Performance Lambat?
1. ✅ Kurangi ukuran file gambar
2. ✅ Gunakan format PNG yang sudah dioptimasi
3. ✅ Batasi jumlah sphere di layar

## 🎯 Contoh Workflow

1. **Download/buat gambar** (contoh: logo tim, avatar, icon)
2. **Edit di software image editor** (Photoshop, GIMP, Paint.NET)
   - Crop ke bentuk persegi
   - Resize ke 64x64 atau 128x128
   - Remove background (PNG)
3. **Simpan sebagai PNG** dengan nama simple
4. **Copy ke folder** `assets/images/`
5. **Jalankan program** dan test dengan Right Click

## 💡 Ideas Kreatif

- **Personal Avatar**: Foto profil Anda
- **Team Logo**: Logo tim/grup
- **Game Characters**: Karakter game favorit
- **Memes**: Gambar meme lucu
- **Symbols**: Simbol matematika, musik, dll
- **Animals**: Icon hewan-hewan cute

Selamat bereksperimen dengan gambar Anda sendiri! 🎨
