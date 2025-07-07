import time as sure
import os
os.system('pip install instaloader')

import instaloader,sys
from instaloader import Instaloader
S = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
Z1 = '\033[2;31m' 
B = '\033[2;36m'
S = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
L = '\033[1;32m' 
S = '\033[1;33m'
Y = "\033[1;91m" 
C = "\033[1;97m" 

logoo = (f"""{Y}INSTAGRAM :{C} @ilahici_tg\n{B}TELEGRAM : {C}@ilahici\n{X}\n""")

logo=(f"""{E}              ._                                            ,
               (`)..                                    ,.-')
                (',.)-..                            ,.-(..`)
                 (,.' ,.)-..                    ,.-(. `.. )
                  (,.' ..' .)-..            ,.-( `.. `.. )
                   (,.' ,.'  ..')-.     ,.-( `. `.. `.. )
                    (,.'  ,.' ,.'  )-.-('   `. `.. `.. )
                     ( ,.' ,.'    _== ==_     `.. `.. )
                      ( ,.'   _==' ~  ~  `==_    `.. )
                       \  _=='   ----..----  `==_   )
                    ,.-:    ,----___.  .___----.    -..
                ,.-'   (   _--====_  \/  _====--_   )  `-..
            ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..
        ,.-'.'   .'      (          |  |          )      `.   `.-..
    ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..
  -'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-
                              \ . _  __  _ . /
                               \ `V-'  `-V' |
                                | \ \ | /  /
                                 V \ ~| ~/V
                                  |  \  /|
                                   \~ | V  
                                    \  |
                                     VV
{logoo}
""")



print(f"{L}			Instagram detayli bilgi")

print(logo)

isim =input(str(f"\n\ninstagram kullanıcı adı :{L}"))

ism = isim.upper()
print (ism+E+" araniyor bekleyiniz...")
sure.sleep(1)

def detay():
	
	try:
		x = Instaloader()
		uname = isim
		if uname == "":
			print("\033[33mDalga'mi geciyorsun kullanici adi bos olamaz!")
			sys.exit()
	
		f = instaloader.Profile.from_username(x.context,uname)
	
		print("\033[32mKullanici ismi\033[0m :", f.username)
		sure.sleep(1)
		
		print("\033[32mID\033[0m :", f.userid)
		sure.sleep(1)
		print("\033[32misim\033[0m :", f.full_name)
		sure.sleep(1)
		print("\033[32mBiografi\033[0m :", f.biography)
		sure.sleep(1)
		print("\033[32mkategori ismi\033[0m :", f.business_category_name)
		sure.sleep(1)
		print("\033[32mURL\033[0m :", f.external_url)
		sure.sleep(1)
		print("\033[32mTakip\033[0m :", f.followees)
		sure.sleep(1)
		print("\033[32mtakipci\033[0m :", f.followers)
		sure.sleep(1)
		print("\033[32mDiminta orang\033[0m :", f.requested_by_viewer)
		
		print("\033[32mIGTV\033[0m :", f.igtvcount)
		print("\033[32mbusienss hesabi\033[0m :", f.is_business_account)
		print("\033[32mAkun pribadi\033[0m :", f.is_private)
		print("\033[32mDiverifikasi\033[0m :", f.is_verified)
		print("\033[32mPostlar\033[0m :", f.mediacount)
		print("\033[32mURL foto profil\033[0m :", f.profile_pic_url)
	
	except KeyboardInterrupt:
		print("\033[33mI bir sıkıntı oldu!")
	
	except EOFError:
		print("\033[33mbir sıkıntı oldu?")


detay()



