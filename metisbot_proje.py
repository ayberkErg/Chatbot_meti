# Ayberk ERGÜÇ 25.08.2022

import random as rd
import time
 

saat = time.asctime()
#print(saat)
saat = saat.split(' ')
now_time = saat[3]

nowTimeL = list(now_time)
tm = nowTimeL[0:2]
nowTimeL = ''.join(tm)
hitap = ""


list_tanışma1 = ["Merhabalar" , "Selamlar", "Merhabalar nasılsınız" ]
list_ayrılma1_sabah = ["Günaydın" , "İyi sabahlar" , "Gününüz güzel geçsin"]
list_ayrılma1_ogle = ["İyi günler dilerim" , "Keyifli günler" , "Gününüz güzel geçsin"]
list_nasılsın_cevap = ["iyiyim teşekkür ederim, size nasıl yaardımcı olabilirim ?", "bomba gibiyim, size nasıl yardımcı olabilirim ?" , "Haaariiikaaayıım !!!, size nasıl yardımcı olablirim ?"]
list_ayrılma1_aksam = ["İyi akşamlar dilerim" , "Görüşmek üzere" , "İyi akşamlar"]
list_sirket_hakkında_bilgi = ["1996 yılında yola çıktığımızda amacımız farklı yazılım seçenekleri ile işletmelerin sorunlarına akıllı çözümler geliştirmekti. Yaklaşık 25 yıldır birçok farklı sektör için bu yöntemle geliştirdiğimiz uygulamalar sadece sorunları çözmekle kalmamış aynı zamanda operasyonları daha verimli hale getirmiştir. Uzun yıllara dayanan tecrübemiz ve yapay zeka teknolojisinin gelişimi ile endüstriyel uygulama platformu Heliks Framework'ü geliştirdik. Endüstri 4.0 geçişinin temelinde yer alan bu platform ile yapay zeka ve makine öğrenimi bileşenlerini içeren çözüm ve Ar-Ge projelerimiz Entropi Elektronik ve Teknoloji A.Ş.'ye devredildi. altında birleştirilmiştir."]
list_teşekkür = ["Biz teşekkür ederiz" , "Rica ederiz"]
list_urun_bilgi = ["Metisbot Akıllı ve aynı zamanda kıvrak zekaya sahib bir asistandır." , "Müşterinizle sizin adınıza iletişim kurabilen, onları anlayabilen ve ihtiyaçlarını karşılayan, geri bildirim toplayan ve sürekli kendini geliştiren Metisbot, sizin için bir yardımcı !!!"]
list_bitirme = ["Tamamdır Öyleyse İyi günler dilerim. Sağlıcakla kalın.", "Tamamdır Öyleyse İyi akşamlar dilerim. Sağlıcakla kalın."]
list_bot_ekleme = ["Bu konuda size en iyi Hakan Güngör bey yardımcı olacaktır. Biraz bekleteceğim hemen yönlendiriyorum."]
list_bot_cesit = ["- Metis Sigorta \n - Metis Belediye \n - Metis Ürün Desteği \n - Metis İnsan Kaynakları"]
list_bot_iletisim =["Telefon: +90 532 799 75 37 \n Adres:İstanbul Ofis: Merkez mah. Ayazmayolu Cad. Papirus Plaza No:37 kat:6/10 Ofis:5-FP Kağıthane \n Edirne Ofis: Şükrüpaşa Mah. Zübeyde Hanım Cad. Trakya Üniversitesi Teknopark Yerleşkesi No:3/56\n E-Mail: bilgi@metisbot.net "]
list_teknik_problem = ["Sayfayı yeniden başlatabilirsiniz" , "Chatbou kapatıp tekrar açabilirsiniz" , "Bu konuda size en iyi Burak Dikici bey yardımcı olacaktır. Biraz bekleteceğim hemen yönlendiriyorum."] 
isim = input("Merhabalar ben meti, isminizi öğrenebilir miyim ? " ).strip().capitalize()
print()
#print(f'Teşekkür ederim {isim} şimdi görüşmemize başlıyoruz. \n Size Nasıl Yardımcı Olabilirim ')

f = open("isimler.txt" , "r" , encoding="utf-8")

def foo():
    for satır in f:
        ad = satır[2::]
        ad = ad[:-8]
        cinsiyet = satır[:-3]
        cinsiyet = cinsiyet[-1]
        
        if isim == ad:
           # print("buldum")
            #print(ad)
    
            if cinsiyet == "E":
                hitap = "Bey"
                #print(hitap)
                continue
            elif cinsiyet == "K":
                hitap = "Hanım"
                #print(hitap)
                continue
            elif cinsiyet == "U":
                hitap = "Hanım/Bey"
                #print(hitap)
                continue
            continue
                
    print(f'Teşekkür ederim {isim} {hitap} şimdi görüşmemize başlıyoruz. \nSize Nasıl Yardımcı Olabilirim. \n' )
    
foo()  

key = True
while key:

    girdi = input(f'{isim}: ').strip().lower()
    if girdi == "merhaba" or girdi == "selamlar" or girdi == "hello" or girdi == "selam" or girdi == "günaydın" or girdi == "merhabalar":
        index = rd.randrange(0,3)
        cıktı = list_tanışma1[index]
        print("Meti --> " , cıktı)
        continue


    if girdi == "naber" or girdi == "nasılsın" or girdi == "ne yaıyorsun" or girdi == "nasıl gidiyor" or girdi == "napıyosun":
        index = rd.randrange(0,3)
        cıktı = list_tanışma1[index]
        print("Meti --> " , cıktı)
        continue
        
    
    if girdi == "teşekkürler" or girdi == "teşekkür ederim" or girdi == "sağol" or girdi == "eyvallah" :
        index = rd.randrange(0,2)
        cıktı = list_teşekkür[index]
        print("Meti --> " , cıktı)
        print("\n\nBaşka yardımcı olabileceğim konu var mı ? \n-Şirket hakkında bilgi ver \n-Web siteme nasıl bot ekleyebilirim. \n-Metisbot çeşitleri nelerdir \n-Ürün hakkında bilgi alabilir miyim ?  \n-teknik problem yaşıyorum.")
        continue
    
    
    if girdi == "yok" or girdi == "şimdilik yok" or girdi == "şuanlık yok":
        nowTimeL1 = int(nowTimeL)
        #print(nowTimeL1, type(nowTimeL))
        if (nowTimeL1 <= 17 ):
            print("Meti --> " , list_bitirme[0])
            continue
        if (nowTimeL1 <= 24):
            print("Meti --> " , list_bitirme[1])
        continue
            
    if girdi == "var" or girdi == "evet vat" :
        print("Meti --> " ,"Yardımcı olmamı istediğiniz konuyu yazabilir misiniz ? \n\n-Şirket hakkında bilgi verebilir misin ? \n-Web siteme nasıl bot ekleyebilirim. \nMetisbot çeşitleri nelerdir ? \n-Ürün hakkında bilgi alabilir miyim ? \n-teknik problem yaşıyorum.") 
        continue
    
    if girdi == "ürün hakkında bilgi ver" or girdi == "metisbot nedir" or girdi == "metisbot ne yapar" or girdi == "metisbot ne işe yarar" or girdi == "metisbotu anlat":
        index = rd.randrange(0,2)
        cıktı = list_urun_bilgi[index]
        print("Meti --> " , cıktı)
        time.sleep(5)
        print()
        print("Meti --> " , "bilgi yeterli oldu mu ? ")
        girdi1 = input("Evet ya da Hayır yazabilirsiniz: ").strip().lower()
         
        if girdi1 == "evet":
            print("harikaa !!!")
        else:
            print("Meti --> " , "Sizi hemen Ürün Müdürümüz Fulya Terzi Balkan Hanıma Bağlıyorum...")
        continue     
    
    if girdi == "web siteme nasıl bot ekleyebilirim" or girdi == "web siteme nasıl metisbot ekleyebilirim" or girdi == "siteme nasıl metisbot ekleyebilirim" or girdi == "metisbotu nasıl kullanabilirim" :
        cıktı = list_bot_ekleme[0]
        print("Meti --> " , cıktı)
        continue
    
    if girdi == "teknik problem yaşıyorum" or girdi == "teknik sorun" or girdi =="chatbotta sorun var" or girdi == "chatbot çalışmıyor":
        index = rd.randrange(0,2)
        cıktı = list_teknik_problem[index]
        print("Meti --> " , cıktı)
        #time.sleep(2)
        girdi2 = input("problem çözüldü mü ? \nEvet ya da Hayır yazabilirsiniz.\n").strip().lower()
       
        
        if girdi2 == "evet":
            print("Harika !!!  Yardımcı olabileceğim başka bir konu var mı")
            continue
        else:
            cıktı=list_teknik_problem[2]
            print(cıktı)
            continue
        
    if girdi == "çeşit" or girdi == "bot çeşitleri" or girdi == "bot çeşitleri nelerdir" or girdi == "metisbot çeşitleri nelerdir" or girdi == "metisbot çeşitleri" or girdi == "ürün çeşitleri":
        cıktı = list_bot_cesit[0]
        time.sleep(1)
        print("Meti --> \n" , cıktı)
        continue

    if girdi == "iletişim" or girdi == "iletişim bilgileri" or girdi == "adres" or girdi == "adres bilgisi" or girdi == "mail" or girdi == "mail blgisi" or girdi == "telefon" or girdi == "telefon bilgisi":
        cıktı = list_bot_iletisim[0]
        print("Meti --> \n" , cıktı)
        continue
        
        
                
    if girdi == "şirket hakkında bilgi ver" or girdi == "bilgi ver" or girdi == "metisbot şirketi" or girdi == "metisbot firması":
        cıktı = list_sirket_hakkında_bilgi[0]
        print("Meti --> " , cıktı)
        continue
    
    if girdi == "q":
        print("Sistemden çıkılıyor, Sağlıcakla Kalın")
        key = False    
    
    else:
        print("Meti --> " , "Dediğinizi anlayamadım, Lütfen tekrar anlatır mısınız ? ")
        

        
        
