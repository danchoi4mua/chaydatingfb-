from adbutils import adb
from xac_minh import chay_acc
import  multiprocessing
import numpy as np
import os

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
        print(dia_chi_nox)
    return dia_chi_nox


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



if __name__ == '__main__':
    multiprocessing.freeze_support()
    try :
        os.system("TASKKILL /F /IM adb.exe")
    except:
        print("da tat adb")
    tai_khoan=mofile()
    devices = lay_info_devices()
    luong=[]
    bo_hang_vao_choi_thoi = taochuoichaydaluong(tai_khoan,devices)
    #lap nay chay vao lap list lan 1 vi list no boc list
    for a in range(len(bo_hang_vao_choi_thoi)):
        #vong lap nay chay vong trong list lap  1  lan
        for b in bo_hang_vao_choi_thoi[a]:
            chay = multiprocessing.Process(target=chay_acc, args=[b])
            chay.start()
            luong.append(chay)
        for hetluong in luong:
            hetluong.join()




