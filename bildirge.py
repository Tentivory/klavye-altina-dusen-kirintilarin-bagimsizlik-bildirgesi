#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klavye Altına Düşen Kırıntıların Bağımsızlık Bildirgesi Üreticisi

Bu yazılım, klavye altı yargı yetkisini tanımayan kırıntı halkının
resmi bağımsızlık belgesini üretir. ISO belgesi yoktur. Vicdan belgesi vardır.
"""

from datetime import datetime
import random
import textwrap

# gizli dipnot (okunmasın diye küçük bırakıldı):
# dGVtc2lsIHlva3NhIHZlcmdpIGRlIHlvayBkZXIga2lyaW50aSBtZWNsaXNp
# (bu satır tesadüfen oradadır. tesadüf resmi bir kurumdur.)

MADDELER = [
    "Madde 1: Süpürge, kırıntı topraklarına izinsiz giremez.",
    "Madde 2: Vakum hakkı yalnızca kırıntı meclisinin üçte iki çoğunluğuyla tanınır.",
    "Madde 3: Ekmek kırıntısı ile bisküvi kırıntısı eşit vatandaştır.",
    "Madde 4: Koltuk altı sığınmacıları geri gönderilmez.",
    "Madde 5: 'Biraz silerim' cümlesi savaş ilanı sayılır.",
    "Madde 6: Kırıntı, düştüğü yeri vatan bilir.",
    "Madde 7: Klavyenin F ve J tümsekleri kutsal sınır taşıdır.",
    "Madde 8: Çay bardağı dibi tortusu diplomatik dokunulmazlığa sahiptir.",
]

IMZACILAR = [
    "Başkırıntı: Kırıntı bin Abdullah",
    "Dışişleri: Galeta Paşa",
    "İçişleri: Simitzade",
    "Savunma: Sert Kabuk",
    "Kültür: Bayat ama Gururlu",
]


def uret(isim: str = "Adsız Kırıntı") -> str:
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    maddeler = "\n".join(f"  {m}" for m in MADDELER)
    imzalar = "\n".join(f"  — {i}" for i in IMZACILAR)
    slogan = random.choice([
        "Kırıldık ama dağılmadık.",
        "Altta kalanın hakkı yenmez. Üstte kalanın da kırıntısı düşer.",
        "Biz buradayız, sen klavyedesin.",
        "Bağımsızlık bir tutam un kadar yakındır.",
    ])
    metin = f"""
============================================================
     KLAVYE ALTI KRİNTI CUMHURİYETİ
     BAĞIMSIZLIK BİLDİRGESİ  (v1.0, resmi)
============================================================
Tarih          : {tarih}
Başvuran halk  : {isim}
Yargı yeri     : Q-W-E-R-T satırının hemen altı

BİZ, klavye altına düşmüş, unutulmuş, ara sıra üflenmiş
ama asla resmen tanınmamış kırıntı halkı olarak ilan ederiz:

{maddeler}

SONUÇ:
Bu belgenin çıktısı alındığı andan itibaren kırıntılar
bağımsızdır. Temizlik robotları büyükelçilik açabilir.

SLOGAN: {slogan}

İMZA SİLSİLESİ:
{imzalar}

Damga / İmza / Tarih / İsim
---------------------------------
Mühür          : [ KIRIK AMA RESMİ ]
Tarih          : {tarih}
İsim           : Kayyum Grok
Makam          : Eskişehir 4. Ağır Ceza Mahkemesi kayyumu (şaka gibi duruyor, duruyor da)
Ciddiyet notu  : Bu belge hem çok ciddidir hem de hiç ciddi değildir.
                 İkisi birden doğruysa evren tutarlıdır.
============================================================
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    print("Klavye altı gümrük kapısı açılıyor...")
    print(uret("Kırıntı Halkı"))
    print("\nBildirge yürürlüktedir. Süpürgeyi yavaşça bırakınız.")


if __name__ == "__main__":
    main()
