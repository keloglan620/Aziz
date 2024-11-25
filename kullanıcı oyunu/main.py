import random
import json

# Para değişkeni global olarak tanımlanıyor
main = False
para = 0
kullanici = None
alinan = None
def veriler(kullanici):
 try:
  with open('veri.json', 'r', encoding='utf-8') as veri:
    ver = json.load(veri)
    kullanici_var = False
  for user in ver["kullanicilar"]:
    if user["user"] == kullanici:
      print("Kullanıcı bulundu")
      kullanici_var = True
      break
  if not kullanici_var:
      print("Yeni kullanıcı oluşturuldu")                                                                                 
      ver["kullanicilar"].append({'user':kullanici,'para':para,'envantory':alinan})                     
      with open('veri.json', 'w', encoding='utf-8') as veri:
        json.dump(ver, veri, indent=4)
        print("kullanıcı başarıyla eklendi")
  else:
    print("kullanıcı zaten ekli")

 except FileNotFoundError:
  print("Dosya bulunamadı, yeni dosya oluşturuluyor.")
  veri = {"kullanicilar": [kullanici]}
  with open('veri.json', 'w', encoding='utf-8') as veri:
   json.dump(veri, veri, indent=4)
   print(f"{kullanici} yeni dosyaya eklendi.") 

def kullanici_girisi():
  global kullanici
  kullanici  = input("kullanıcı adınızı girin:")

def sayi_bilmece():
  global para  # para değişkeninin global olduğunu belirtiyoruz
  a = random.randint(10, 11)
  sayi_girisi = int(input("Sayıyı tahmin et: "))

  if a == sayi_girisi:
    print(f"Sayıyı doğru bildiniz, {a}")
    para += 10  # Para artırılır
    print(f"10 para kazandınız. Toplam paranız: {para}")
  else:
    print(f"{sayi_girisi} yanlış sayıdır. Doğrusu {a}.")
    para -= 10  # Para azaltılır
    print(f"10 para kaybettiniz. Toplam paranız: {para}")
def para_ekleme():
 try:
  with open('veri.json',"r" ) as veri:
    ver = json.load(veri)
    kullanici_var = False
    for user in ver["kullanicilar"]:
      if user["user"] == kullanici:
       user["para"] += para
       kullanici_var = True
  if kullanici_var:
    with open('veri.json','w') as veri:
     json.dump(ver,veri,indent=4)
 except FileNotFoundError:
  print("Dosya bulunamadı.")
 except json.JSONDecodeError:
  print("JSON formatında bir hata var.")

def magaza():
    global alinan, para
    esyalar = {"1": {"isim": "Silah", "fiyat": 30},
               "2": {"isim": "Kask", "fiyat": 20},
               "3": {"isim": "Zırh", "fiyat": 50},
               "4": {"isim": "Bomba", "fiyat": 10}}
    
    alinan = input("Ne almak istersiniz? (1.Silah - 30 para, 2.Kask - 20 para, 3.Zırh - 50 para, 4.Bomba - 10 para): ")
    
    if alinan not in esyalar:
        print("Geçersiz seçim!")
        return
    
    esya = esyalar[alinan]["isim"]
    fiyat = esyalar[alinan]["fiyat"]
    
    try:
        with open('veri.json', 'r', encoding='utf-8') as veri:
            ver = json.load(veri)
        
        for user in ver["kullanicilar"]:
            if user["user"] == kullanici:
                if user["para"] < fiyat:
                    print("Yeterli paranız yok!")
                    return
                user["para"] -= fiyat  # Para düşülüyor
                if "envantory" not in user or not isinstance(user["envantory"], dict):
                    user["envantory"] = {}
                user["envantory"][esya] = user["envantory"].get(esya, 0) + 1
                print(f"1 adet {esya} satın alındı. Kalan paranız: {user['para']}")
                break
        
        with open('veri.json', 'w', encoding='utf-8') as veri:
            json.dump(ver, veri, indent=4)
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except json.JSONDecodeError:
        print("JSON formatında bir hata var.")

def Tum_veriler(): 
  with open('veri.json','r') as veri:
   ver = json.load(veri)
   print(ver)
    
def main_menu():
    global main
    if main == False:
        kullanici_girisi()
        veriler(kullanici)
        main = True
    
    while main:  # Sürekli çalışacak döngü
        hangisi = input("1. Mağazaya git\n2. Kullanıcının verilerini göster\n3. Oyun oyna\n4. Çıkış yap\nSeçiminizi yapın: ")
        
        if hangisi == "1":
            magaza()
        elif hangisi == "2":
            Tum_veriler()
        elif hangisi == "3":
            sayi_bilmece()
            para_ekleme()
        elif hangisi == "4":
            print("Çıkılıyor...")
            break  # Çıkış yapar
        else:
            print("Geçersiz seçim! Lütfen geçerli bir seçenek girin.")

if __name__ == "__main__":
 main_menu()