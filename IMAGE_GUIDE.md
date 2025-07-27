# Progressive Dot Art Generator

## Konsep Utama

Program ini membaca gambar **Artboard1.png** dan menciptakan **dot art** dimana ribuan dots kecil muncul **satu per satu** membentuk gambar tersebut.

## File yang Dibutuhkan

**Letakkan gambar Anda:**
```
e:\! UGM\!! GAMAFORCE\ObjectMaker\assets\images\Artboard1.png
```

## Format Gambar yang Didukung

✅ **PNG** (Paling direkomendasikan)
✅ **JPG/JPEG** 
✅ **GIF**
✅ **BMP**

## Tips Gambar Artboard1.png

### ✅ **Gambar Ideal:**
- **Background putih** atau transparan
- **Kontras tinggi** (objek gelap, background terang)
- **Bentuk yang jelas** dengan garis tegas
- **Resolusi cukup** (300x300 hingga 800x800 pixel)

### ❌ **Hindari:**
- Gradasi atau blur yang berlebihan
- Background dengan warna gelap
- Detail terlalu halus atau rumit
- Warna yang terlalu mirip antara objek dan background

## Struktur Folder
```
ObjectMaker/
├── assets/
│   └── images/
│       └── Artboard1.png  ← Gambar utama Anda
├── sphere_drawings.py
└── README.md
```

## Cara Kerja

1. **Program scan** setiap 8 pixel dari gambar Artboard1.png
2. **Deteksi warna** dan skip area putih/background
3. **Generate koordinat** untuk setiap dot
4. **Progressive creation** - dots muncul satu per satu
5. **Membentuk gambar** sesuai pola asli

## Hasil yang Diharapkan

- ✅ Ribuan dots kecil berwarna
- ✅ Muncul satu per satu secara bertahap  
- ✅ Membentuk gambar Artboard1.png dengan presisi
- ✅ Efek seperti time-lapse pointillism painting

**Siapkan gambar Artboard1.png Anda dan lihat magic happen! 🎨✨**
