# Yoldaş

Bu proje, basit bir **pa manager** uygulamasının başlangıç sürümünü içerir. `pa manager`, yerel bir JSON dosyasında paketleri yönetmeye yarayan küçük bir komut satırı aracıdır.

## Kurulum

Bu depoda yalnızca `pa_manager.py` ve gerekli README bulunmaktadır. Gerekli Python sürümü: 3.8+

## Kullanım

```bash
# Veri dosyasını oluştur
python pa_manager.py init

# Paket ekle
python pa_manager.py add paket_adi

# Paketleri listele
python pa_manager.py list

# Paket sil
python pa_manager.py remove paket_adi
```

`packages.json` dosyası scriptin bulunduğu dizinde saklanır ve eklenen paketleri burada tutar.

## Katkı

Pull request'lere açıktır. Hataları veya geliştirme önerilerinizi iletebilirsiniz.
