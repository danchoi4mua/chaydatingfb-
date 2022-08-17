

import xacthuc
import time
import uiautomator2 as u2
import os
import subprocess
from adbutils import adb
import  multiprocessing
from xac_minh import chay_acc
def tat_mo_fb(d):
    d.app_stop("com.facebook.katana")
    d.app_start("com.facebook.katana", use_monkey=True)
"""def xoa_pop_up(d):
  bien_lap = 0
  while bien_lap == 0:
    try :
      d.xpath("//*[@content-desc='Search Facebook']").click()
      bien_lap += 1
    except :
      d.app_stop("com.facebook.katana")
      d.app_start("com.facebook.katana", use_monkey=True)"""

"""nixpath=//*[@content-desc='Liked You 0']
nixpath=//*[@contentDescription='Liked You 0']
nixpath=//*[@id='dating_home_interested_tab_nav_button']"""


def mofile():
    f = open("acccanmo.txt", mode='r', encoding='utf-8')
    tai_khoan = []
    for tk in f:
        tk = tk.rstrip().split()
        tk[2] = "".join(tk[2:])
        del tk[3:]
        tai_khoan.append(tk)
    f.close()
    return tai_khoan


def lay_info_devices():
    dia_chi_nox = []
    for d in adb.device_list():
        dia_chi_nox.append(d.serial)  # print device serial
    return dia_chi_nox
#day la cai test lan dau
def taochuoichaydaluong(taikhoan,devices):

    mangchay=[]
    bo_dem_acc = 0
    bo_dem_nox = 0
    for _ in range(0,len(tai_khoan)):
        if bo_dem_nox == len(devices):
            bo_dem_nox = 0
        mangchay.append(list((taikhoan[bo_dem_acc], devices[bo_dem_nox])))
        bo_dem_nox += 1
        bo_dem_acc += 1
    mangchay = np.array_split(mangchay,round(( len(mangchay)/len(devices) +0.49) ))


    return mangchay
#day la cai sau khi chinh xong
def taochuoichaydaluong(taikhoan, devices):
    mangchay = []
    mang_xu_ly=[]
    mang_cuoi=[]
    bo_dem_acc = 0
    bo_dem_nox = 0
    for _ in range(0, len(tai_khoan)):
        if bo_dem_nox == len(devices):
            bo_dem_nox = 0
        mangchay.append(list((taikhoan[bo_dem_acc], devices[bo_dem_nox])))
        bo_dem_nox += 1
        bo_dem_acc += 1

    #so_lan_chay = round((len(mangchay) / len(devices) + 0.49))
    #mangchay = np.array_split(mangchay, round((len(mangchay) / len(devices) + 0.49)))
    bien_dem=0
    for so_thu_tu_de_chia in range(len(mangchay)):
        mang_xu_ly.append(mangchay[so_thu_tu_de_chia])
        bien_dem += 1
        if bien_dem % len(devices) == 0 or so_thu_tu_de_chia == len(mangchay):
            mang_cuoi.append(mang_xu_ly)
            mang_xu_ly = []
    return mang_cuoi





def hihi(a):
    print(a)

if __name__ == '__main__':

    tai_khoan=mofile()
    devices = lay_info_devices()
    luong=[]
    bo_hang_vao_choi_thoi = taochuoichaydaluong(tai_khoan,devices)
    print(bo_hang_vao_choi_thoi)
    #lap nay chay vao lap list lan 1 vi list no boc list
    for a in range(len(bo_hang_vao_choi_thoi)):
        #vong lap nay chay vong trong list lap  1  lan
        for b in bo_hang_vao_choi_thoi[a]:
            chay = multiprocessing.Process(target=chay_acc, args=[b])
            chay.start()
            luong.append(chay)
        for hetluong in luong:
            hetluong.join()

"""while True:
    time.sleep(2)
    if d.xpath("//*[@content-desc='Tìm kiếm Facebook']").exists or d(
            text="//*[@content-desc='Tìm kiếm Facebook']").exists(timeout=30):
        d.xpath("//*[@content-desc='Tìm kiếm Facebook']").click()
        d.send_keys("Dating")
        time.sleep(3)
        d(className="androidx.recyclerview.widget.RecyclerView") \
            .child(className="android.view.ViewGroup")[1] \
            .click()
        if d.xpath("//*[@text='Find love through what you like']").exists or d(
                text="Find love through what you like").exists(timeout=5):
            break
        if d.xpath("//*[@content-desc='Trang cá nhân']").exists or d.xpath(
                "//*[@content-desc='Gợi ý ghép đôi']").exists:
            break
        if d.xpath("//*[@content-desc='Dating']").exists or d(text="Dating").exists(timeout=5):
            tat_mo_fb(d)
        else:
            break
    elif d.xpath("//*[@content-desc='Cho phép']").exists:
        d.xpath("//*[@content-desc='Cho phép']").click()
        d.xpath("// *[@text='CHO PHÉP']").click()

    else:
        tat_mo_fb(d)"""
"""if d.xpath("//*[@content-desc='Cho phép']").exists:
        d.xpath("//*[@content-desc='Cho phép']").click()
        d.xpath("// *[@text='CHO PHÉP']").click()"""

"""
while True:

    if d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").exists:
        d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").click()
        continue
    elif d.xpath("//*[@text='Something went wrong. Please try again.']").exists :
        for _ in range(5):
            d.xpath("//*[@text='Something went wrong. Please try again.']").click()
            if d.xpath("//*[@content-desc='Update Location']").exists or d.xpath("//*[@content-desc='Cập Nhật Vị Trí']").exists :
                break

    elif d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").exists:
        d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").click()
        d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
        continue    
    elif d.xpath("//*[@content-desc='Cho phép']").exists:
        d.xpath("//*[@content-desc='Cho phép']").click()
        d.xpath("// *[@text='CHO PHÉP']").click()
        continue
    elif d.xpath("//*[@content-desc='Bỏ qua']").exists:
        d.xpath("//*[@content-desc='Bỏ qua']").click()
        continue
    elif d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").exists  :
        d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
        continue
    elif d.xpath("//*[@content-desc='Trang cá nhân']").exists() or d.xpath("//*[@content-desc='Gợi ý ghép đôi']").exists:
        loi_khong_mo_dc(d, "100044168651865", "ifegmqqn3212", "acc_da_mo_dating.txt")
        break
    else:
        time.sleep(300)
        break
"""
"""
xpath=//*[@content-desc='Tìm kiếm Facebook']
while True:
    if d.xpath("//*[@content-desc='Update Location']").exists:
        break
    else:
        d.xpath("//*[@index='8']").click()
        bien_dem += 1
        if bien_dem == 15:
            subprocess.run("adb -s {} reboot".format("emulator-5554"))
            break
while d.xpath("//*[@content-desc='Skip']").exists:
    d.xpath("//*[@content-desc='Skip']").click()
    if d.xpath("//*[@content-desc='Everyone, Unselected']").exists:
        break
"""

"""d(className="android.widget.Button") \
    .child(className="android.widget.Button")[8] \
    .click()
"""
"""
if d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").exists:
    print("hihi")
    while d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").exists:
        d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
        if d.xpath("//*[@content-desc='Everyone, Unselected']").exists:
            break
    d.xpath("//*[@content-desc='Everyone, Unselected']").click()
    d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
    if d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").exists:
        d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").click()
    if d.xpath("//*[@content-desc='Allow']").exists:
        d.xpath("//*[@content-desc='Allow']").click()
        d(text="ALLOW").click()
    bien_dem=0
    while True:
        if d.xpath("//*[@content-desc='Update Location']").exists:
            break
        else:
            d.xpath("//*[@index='8']").click()
            bien_dem+=1

    while d.xpath("//*[@content-desc='Skip']").exists:
        d.xpath("//*[@content-desc='Skip']").click()
        if d.xpath("//*[@content-desc='Everyone, Unselected']").exists:
            break"""








"""if d.xpath("//*[@contentDescription='Liked You 0']").exists:
    print("gigi")
if d.xpath("//*[@content-desc='Liked You 0']").exists:
    print("exists")"""
"""
def xoa_pop_up_va_tim_dating(d):
    bien_lap = 0
    while bien_lap == 0:
        
        if d.xpath("//*[@content-desc='Search Facebook']").exists:
            d.xpath("//*[@content-desc='Search Facebook']").click()
            d.send_keys("Dating")
            d(className="androidx.recyclerview.widget.RecyclerView") \
            .child(className="android.view.ViewGroup")[1] \
            .click()
            time.sleep(10)
            if d.xpath("//*[@content-desc='Profile']").exists:
            
                print("hhihi co dating roi")
            elif d.xpath("//*[@id ='gemstone_onboarding_next_button_test_key']").exists:
                print("hhihi chua co  dating ne ")
            else:
                print("khong co dating")
            bien_lap += 1
        else:
            d.app_stop("com.facebook.katana")
            d.app_start("com.facebook.katana", use_monkey=True)

xoa_pop_up_va_tim_dating(d)"""
#d.xpath("//*[@contentDescription='Liked You 0'").click()


#resource-id=gemstone_onboarding_next_button_test_keyz



"""if d.xpath("//*[@content-desc='Liked You 0'").exists(timeout=10):
    print("hihi")"""
#d(text="Dating").down(text="Dating")

"""d(text="Search']").click()
d.send_keys("Dating")
d().down()"""
#d(text="Search Facebook").click()
""""d.xpath("//*[@content-desc='Search Facebook']").click()
d.send_keys("Dating")
d(className="androidx.recyclerview.widget.RecyclerView") \
  .child(className="android.view.ViewGroup")[1] \
  .click()"""
"""bien_lap=0
while bien_lap == 0:
  d.xpath("//*[@content-desc='Search Facebook']").click()
  bien_lap += 1
  if bien_lap==0:
    d.app_stop("com.facebook.katana")
    d.app_start("com.facebook.katana", use_monkey=True)"""

#nixpath=(//*[@class='androidx.recyclerview.widget.RecyclerView']/*[@class='android.view.ViewGroup' and @height>0])[2]
#d.xpath("//*[@class='androidx.recyclerview.widget.RecyclerView']/*[@class='android.view.ViewGroup' and @height>0])[2]").click()"""




"""
d.app_stop("com.facebook.katana")
d.app_start("com.facebook.katana", use_monkey=True)
nixpath=//*[@text='Sai mật khẩu']
d.xpath("//*[@text='Sai mật khẩu']").click()
d.send_keys("Dating")

d(className="androidx.recyclerview.widget.RecyclerView") \
  .child(className="android.view.ViewGroup")[1] \
  .click()
try:
  d(text="duc").click()
  print("hihi")
except:
  loi_khong_mo_dc(d)"""





"""    d.xpath("//*[@content-desc='Search Facebook']").click()
    d.send_keys("Dating")
    d(className="androidx.recyclerview.widget.RecyclerView") \
        .child(className="android.view.ViewGroup")[1] \
        .click()"""
"""  try:
        d(text="duc").click(timeout=20)
        print("hihi")
    except:
        loi_khong_mo_dc(d)"""



