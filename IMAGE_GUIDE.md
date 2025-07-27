# Menambahkan Gambar ke Sphere Drawings

## Cara Menambahkan Gambar

1. **Letakkan gambar** di folder `assets/images/`
2. **Format yang didukung**: PNG, JPG, JPEG, GIF, BMP
3. **Nama file** akan menjadi nama gambar dalam program

## Struktur Folder
```
ObjectMaker/
├── assets/
│   └── images/
│       ├── ball.png
│       ├── star.jpg
│       └── emoji.png
├── sphere_drawings.py
└── README.md
```

## Kontrol Gambar Baru

- **Right Click**: Tambah sphere dengan gambar di posisi kursor
- **I**: Tambah sphere gambar random di posisi random
- **Left Click**: Tetap menambah sphere warna biasa

## Tips Gambar

1. **Ukuran optimal**: 64x64 hingga 128x128 pixel
2. **Background transparan**: Gunakan PNG dengan alpha channel untuk hasil terbaik
3. **Kontras tinggi**: Gambar dengan kontras tinggi akan terlihat lebih jelas
4. **Format ringan**: JPG untuk foto, PNG untuk grafis dengan transparansi

## Contoh Gambar yang Bagus

- Emoji atau emoticon
- Icon sederhana
- Logo atau simbol
- Bentuk geometris
- Karakter kartun sederhana

## Troubleshooting

- Jika gambar tidak muncul, cek apakah file ada di `assets/images/`
- Pastikan format file didukung
- Cek console untuk pesan error loading gambar
- Gambar akan otomatis di-scale sesuai ukuran sphere
