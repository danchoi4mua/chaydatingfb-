import time
import uiautomator2 as u2
import os
from xacthuc import layma2fa



#d dai dien cho devices

def loi_khong_mo_dc(d,tk=None,mk=None,tentep=None):
    d.app_stop("com.facebook.katana")
    d.app_clear('com.facebook.katana')
    if tk != None :
        f = open(tentep, mode="a+")
        f.write(tk + " " + mk + "\n")
        f.close()

def tat_mo_fb(d):
    d.app_stop("com.facebook.katana")
    d.app_start("com.facebook.katana", use_monkey=True)

def thay_ip():
    os.system("rasdial/disconnect")
    time.sleep(10)
    os.system(r"%windir%\system32\rasdial viettel")
    time.sleep(10)



        #def xac_minh(tai_khoan_va_devices):
"""def xac_minh_us(d):
    d.app_start("com.facebook.katana", use_monkey=True)


    while True:
        try:

            d(text="Phone or email").click()   #test
            d.send_keys("100029047173326")
                #d.send_keys(tai_khoan_va_devices[0][0])
            d(text="Password").click()
            d.send_keys("qtjduywk6731")
            d.xpath("//*[@content-desc='Log In']").click()

            if d(text="You can't log in right now").exists(timeout=30) or d.xpath("//*[@text='Sorry, unable to login. Please check your internet connection.']").exists or d.xpath().exists:
                thay_ip()
                loi_khong_mo_dc(d)
                continue


            if d(text="Login Code Required").exists(timeout=30):

                d(text="OK").click()
                ma2fa = layma2fa("JAV7SZI5KEAXWZUQKVQ33NVVHEKSUCP5")
                d.send_keys(ma2fa)
                d.xpath("//*[@content-desc='Continue']").click()
                while True:
                    time.sleep(2)
                    if d.xpath("//*[@content-desc='Search Facebook']").exists:
                        d.xpath("//*[@content-desc='Search Facebook']").click()
                        d.send_keys("Dating")
                        time.sleep(3)
                        d(className="androidx.recyclerview.widget.RecyclerView") \
                            .child(className="android.view.ViewGroup")[1] \
                            .click()
                        if d.xpath("//*[@bounds='[0,123][540,202]']").exists:
                            d.xpath("//*[@bounds='[0,123][540,202]']").click(timeout=10)
                            break
                        elif d.xpath("//*[@text='Find love through what you like']").exists or d(text="Find love through what you like").exists(timeout=30):  #ham nay chay reset lai cho toi khi dating xuat hien
                            break
                        elif d.xpath("//*[@content-desc='Profile']").exists or d.xpath(
                                "//*[@content-desc='Dating profile']").exists:
                            break
                        elif d.xpath("//*[@content-desc='Dating']").exists or d(text="Dating").exists(timeout=10):
                            tat_mo_fb(d)
                        else:
                            break
                    elif d.xpath("//*[@ content-desc='Allow']").exists:
                        d.xpath("//*[@ content-desc='Allow']").click()
                        d.xpath("// *[@text='ALLOW']").click()
                    else:
                        tat_mo_fb(d)

                if d.xpath("//*[@content-desc='Profile']").exists or d.xpath("//*[@content-desc='Dating profile']").exists:
                    loi_khong_mo_dc(d, "100044168651865", "ifegmqqn3212", "acc_da_mo_dating.txt")
                    break

                elif d.xpath("//*[@id='gemstone_onboarding_next_button_test_key']").exists:
                    while True:
                        if d.xpath("//*[@id='gemstone_enable_location_services_button_test_key']").exists:
                            d.xpath("//*[@id='gemstone_enable_location_services_button_test_key']").click()
                            continue
                        elif d.xpath("//*[@text='Something went wrong. Please try again.']").exists:
                            lap_tim_dia_chi=0
                            for _ in range(5):

                                d.xpath("//*[@text='Something went wrong. Please try again.']").click()
                                if d.xpath("//*[@content-desc='Update Location']").exists or d.xpath("//*[@content-desc='C???p Nh???t V??? Tr??']").exists:

                                    break
                                else:
                                    lap_tim_dia_chi+=1
                                    if lap_tim_dia_chi==5:
                                        d.xpath("//*[@text='Someqwdqwdonqwdqddddwqsacasaain.']").click()   #cai nay bo vo cho no loi de thoat ra lap lai tu dau

                        elif d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").exists:
                            d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").click()
                            d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
                            continue

                        elif d.xpath("//*[@ content-desc='Allow']").exists:
                            d.xpath("//*[@ content-desc='Allow']").click()
                            d.xpath("// *[@text='ALLOW']").click()
                            continue

                        elif d.xpath("//*[@content-desc='Skip']").exists:
                            d.xpath("//*[@content-desc='Skip']").click()
                            continue
                        elif  d.xpath("//*[@id='gemstone_onboarding_next_button_test_key']").exists:
                            d.xpath("//*[@id='gemstone_onboarding_next_button_test_key']").click()
                            continue
                        elif d.xpath("//*[@content-desc='Profile']").exists or d.xpath("//*[@content-desc='Dating profile']").exists:
                            loi_khong_mo_dc(d, "100044168651865", "ifegmqqn3212", "acc_mo_thanh_cong.txt")

                        else:
                            time.sleep(300)
                            break
                else:
                    loi_khong_mo_dc(d, "100044168651865", "ifegmqqn3212", "acc_khong_co_dating.txt")

            if d(text="Wrong Credentials").exists(timeout=30) or d.xpath("//*[@text='Invalid username or password']").exists :
                loi_khong_mo_dc(d, "100044168651865", "ifegmqqn3212", "acc_sai_mk.txt")
                break

            else :
                loi_khong_mo_dc(d,"100044168651865", "ifegmqqn3212","acc_loi.txt")
                break
        except:
            loi_khong_mo_dc(d)"""
def xac_minh_vn(d,tk_mk_2fa):




    while True:
        print("chay tu dau")
        d.implicitly_wait(60)
        try:
            d.implicitly_wait(60)
            print("chay lai mo acc")
            if d.xpath("//*[@content-desc='Cho ph??p']").exists:
                d.xpath("//*[@content-desc='Cho ph??p']").click()
                d.xpath("// *[@text='CHO PH??P']").click()
            d(text="S??? ??i???n tho???i ho???c email").click()   #test
            print(tk_mk_2fa[0])
            d.send_keys(tk_mk_2fa[0])
                #d.send_keys(tai_khoan_va_devices[0][0])
            d(text="M???t kh???u").click()
            d.send_keys(tk_mk_2fa[1])
            d.xpath("//*[@content-desc='????ng nh???p']").click()
            time.sleep(15)


            if d(text="B???n hi???n kh??ng th??? ????ng nh???p").exists or d.xpath("//*[@text='R???t ti???c, kh??ng th??? ????ng nh???p. Vui l??ng ki???m tra k???t n???i Internet.']").exists or d.xpath("// *[ @ text = 'Ch??ng t??i ???? t???m \
            th???i kh??a t??i kho???n c???a b???n ????? ?????m b???o an to??n. Tr?????c khi b???n th??? ????ng nh???p l???i, h??y ki???m tra th??ng tin \
            ????ng nh???p v?? ch???c ch???n l?? b???n ??ang s??? d???ng thi???t b??? th?????ng d??ng tr??n m???ng an to??n.']").exists:
                thay_ip()
                loi_khong_mo_dc(d)
                d.app_start("com.facebook.katana", use_monkey=True)
                continue


            if d(text="C???n c?? m?? ????ng nh???p").exists:
                print("dang nhap")
                d(text="OK").click()
                ma2fa = layma2fa(tk_mk_2fa[2])
                d.send_keys(ma2fa)
                if d.xpath("//*[@content-desc='Ti???p t???c']").exists:
                    d.xpath("//*[@content-desc='Ti???p t???c']").click(timeout=30)
                time.sleep(15)

                #tim da ting
                while True:
                    while True:
                        if d.xpath("// *[@text='B??? qua']").exists:
                            d.xpath("// *[@text='B??? qua']").click()
                        if d.xpath("// *[@text='B??? QUA']").exists:
                            d.xpath("// *[@text='B??? QUA']").click()
                        if d.xpath("// *[@text='L??c kh??c']").exists:
                            d.xpath("// *[@text='L??c kh??c']").click()
                        if d.xpath("//*[@content-desc='T??m ki???m Facebook']").exists:
                            break
                        elif d.xpath("//*[@content-desc='Cho ph??p']").exists:
                            break
                    print("tim dating")
                    print("dung lai doi ")
                    time.sleep(10)
                    if d.xpath("//*[@content-desc='T??m ki???m Facebook']").exists:
                        d.xpath("//*[@content-desc='T??m ki???m Facebook']").click()
                        d.set_fastinput_ime(False)
                        d.send_keys("Dating")
                        time.sleep(3)
                        d(className="androidx.recyclerview.widget.RecyclerView") \
                            .child(className="android.view.ViewGroup")[1] \
                            .click()
                        time.sleep(3)
                        if d.xpath("//*[@bounds='[0,123][540,204]']").exists:
                            d.xpath("//*[@bounds='[0,123][540,204]']").click(timeout=10)
                        if d.xpath("//*[@text='T??m n???a kia qua nh???ng ??i???u b???n th??ch']").exists or d(text="Ch??ng t??i s??? kh??ng g???i ?? b???n b?? hi???n t???i tr??n Facebook trong ph???n H???n h?? ho???c kh??ng cho h??? bi???t r???ng b???n ???? tham gia. B???n s???n s??ng t??m m???t n???a x???ng ????i ch??a n??o?").exists :
                            break
                        if d.xpath("//*[@content-desc='Trang c?? nh??n']").exists or d.xpath("//*[@content-desc='G???i ?? gh??p ????i']").exists:
                            break
                        elif d.xpath("//*[@content-desc='Dating']").exists or d(text="Dating").exists or d(text="H???n h??").exists:
                            time.sleep(20)
                            tat_mo_fb(d)
                        else:
                            break

                    elif d.xpath("//*[@content-desc='Cho ph??p']").exists:
                        time.sleep(2)
                        d.xpath("//*[@content-desc='Cho ph??p']").click()
                        d.xpath("// *[@text='CHO PH??P']").click()
                    else:
                        print("timdating nhung chua dc mo lai ")
                        tat_mo_fb(d)
                if d.xpath("//*[@content-desc='Trang c?? nh??n']").exists or d.xpath("//*[@content-desc='G???i ?? gh??p ????i']").exists:
                    print("xac minh la acc da co dating")
                    loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_da_mo_dating.txt")
                    break

                elif d.xpath("//*[@text='T??m n???a kia qua nh???ng ??i???u b???n th??ch']").exists or d(text="Ch??ng t??i s??? kh??ng g???i ?? b???n b?? hi???n t???i tr??n Facebook trong ph???n H???n h?? ho???c kh??ng cho h??? bi???t r???ng b???n ???? tham gia. B???n s???n s??ng t??m m???t n???a x???ng ????i ch??a n??o?").exists :
                    print("chay acc dating")
                    while True:
                        if d.xpath("//*[@content-desc='Cho ph??p']").exists:
                            time.sleep(2)
                            d.xpath("//*[@content-desc='Cho ph??p']").click()
                            d.xpath("// *[@text='CHO PH??P']").click()
                            continue
                        if d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").exists:

                            d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").click()
                            continue

                        if  d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").exists:

                            d.xpath("//*[@resource-id='gemstone_enable_location_services_button_test_key']").click()
                            continue
                        if d.xpath("//*[@text='Something went wrong. Please try again.']").exists:

                            lap_tim_dia_chi = 0
                            for _ in range(5):

                                d.xpath("//*[@text='Something went wrong. Please try again.']").click()
                                if d.xpath("//*[@content-desc='Update Location']").exists or d.xpath("//*[@content-desc='C???p Nh???t V??? Tr??']").exists:
                                    break
                                else:
                                    lap_tim_dia_chi += 1
                                    if lap_tim_dia_chi == 5:
                                        d.xpath("//*[@text='Someqwdqwdonqwdqddddwqsacasaain.']").click()  # cai nay bo vo cho no loi de thoat ra lap lai tu dau

                        if d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").exists:

                            d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").click()
                            d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
                            continue



                        if d.xpath("//*[@content-desc='B??? qua']").exists:

                            d.xpath("//*[@content-desc='B??? qua']").click()
                            continue
                        if d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").exists:

                            d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
                            continue
                        if d.xpath("//*[@content-desc='Trang c?? nh??n']").exists or d.xpath("//*[@content-desc='G???i ?? gh??p ????i']").exists:
                            print("lay tien")
                            loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_mo_thang_cong.txt")
                            break


                else:
                    loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_khong_co_dating.txt")
                    print("acc khong co dating")
                    break

            if d(text="Sai m???t kh???u").exists or d.xpath("//*[@text='Sai m???t kh???u']").exists:
                loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_sai_mk.txt")
                break

            else :
                loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1],"acc_loi.txt")
                break
        except:
            print("loi chay lai tu dau")
            loi_khong_mo_dc(d)
            d.app_start("com.facebook.katana", use_monkey=True)


def chay_acc(du_lieu_chay_luong):


    d = u2.connect(du_lieu_chay_luong[1])         #ket noi voi adb   xoa lai tam thoi di test  #test
    d.implicitly_wait(60) #thoi gian doi cac click
    d.app_start("com.facebook.katana", use_monkey=True)
    xac_minh_vn(d, du_lieu_chay_luong[0])





