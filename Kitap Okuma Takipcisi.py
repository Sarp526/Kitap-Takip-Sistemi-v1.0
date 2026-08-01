print("""
=== Kitap Takip Sistemi ===
1. Kitap ekle.
2. Kitapları listele.
3. Okunan sayfaları güncelle.
4. Çıkış yap.
""")

kitaplar = []

while True: 
    secim = "yok"
    secim = input(">> ")

    if secim == "1": 
        kitap_ismi = input("Kitabın adını giriniz: ")
        sayfa_sayisi = input("Sayfa sayısını giriniz: ")
        yeni_kitap = {"İsim": kitap_ismi, "Sayfa Sayısı": sayfa_sayisi}
        kitaplar.append(yeni_kitap)

    elif secim == "2": 
        for kitap in kitaplar:
            print(f"{kitaplar.index(kitap) + 1}. Kitap adı: {kitap.get("İsim")}, {kitap.get("Sayfa Sayısı")} sayfa")

    elif secim == "3":
        kitap_no = int(input("Kitabınızı kaydettiğiniz sıra numarasını giriniz: "))
        incelenecek_kitap = kitaplar[kitap_no - 1]
        okunan_sayfa = int(input("Bulunduğunuz sayfa numarasını giriniz: "))
        tamamlanma_yuzdesi = round(okunan_sayfa / int(incelenecek_kitap.get("Sayfa Sayısı")) * 100, 1)
        print(f"Kitabınızı %{tamamlanma_yuzdesi} oranda tamamladınız.")

    elif secim == "4":
        print("Uygulamadan çıkıldı.")
        break
    
    else:
        print("Lütfen geçerli bir seçim numarası giriniz!")