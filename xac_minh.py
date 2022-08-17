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
                                if d.xpath("//*[@content-desc='Update Location']").exists or d.xpath("//*[@content-desc='Cập Nhật Vị Trí']").exists:

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
            if d.xpath("//*[@content-desc='Cho phép']").exists:
                d.xpath("//*[@content-desc='Cho phép']").click()
                d.xpath("// *[@text='CHO PHÉP']").click()
            d(text="Số điện thoại hoặc email").click()   #test
            print(tk_mk_2fa[0])
            d.send_keys(tk_mk_2fa[0])
                #d.send_keys(tai_khoan_va_devices[0][0])
            d(text="Mật khẩu").click()
            d.send_keys(tk_mk_2fa[1])
            d.xpath("//*[@content-desc='Đăng nhập']").click()
            time.sleep(15)


            if d(text="Bạn hiện không thể đăng nhập").exists or d.xpath("//*[@text='Rất tiếc, không thể đăng nhập. Vui lòng kiểm tra kết nối Internet.']").exists or d.xpath("// *[ @ text = 'Chúng tôi đã tạm \
            thời khóa tài khoản của bạn để đảm bảo an toàn. Trước khi bạn thử đăng nhập lại, hãy kiểm tra thông tin \
            đăng nhập và chắc chắn là bạn đang sử dụng thiết bị thường dùng trên mạng an toàn.']").exists:
                thay_ip()
                loi_khong_mo_dc(d)
                d.app_start("com.facebook.katana", use_monkey=True)
                continue


            if d(text="Cần có mã đăng nhập").exists:
                print("dang nhap")
                d(text="OK").click()
                ma2fa = layma2fa(tk_mk_2fa[2])
                d.send_keys(ma2fa)
                if d.xpath("//*[@content-desc='Tiếp tục']").exists:
                    d.xpath("//*[@content-desc='Tiếp tục']").click(timeout=30)
                time.sleep(15)

                #tim da ting
                while True:
                    while True:
                        if d.xpath("// *[@text='Bỏ qua']").exists:
                            d.xpath("// *[@text='Bỏ qua']").click()
                        if d.xpath("// *[@text='BỎ QUA']").exists:
                            d.xpath("// *[@text='BỎ QUA']").click()
                        if d.xpath("// *[@text='Lúc khác']").exists:
                            d.xpath("// *[@text='Lúc khác']").click()
                        if d.xpath("//*[@content-desc='Tìm kiếm Facebook']").exists:
                            break
                        elif d.xpath("//*[@content-desc='Cho phép']").exists:
                            break
                    print("tim dating")
                    print("dung lai doi ")
                    time.sleep(10)
                    if d.xpath("//*[@content-desc='Tìm kiếm Facebook']").exists:
                        d.xpath("//*[@content-desc='Tìm kiếm Facebook']").click()
                        d.set_fastinput_ime(False)
                        d.send_keys("Dating")
                        time.sleep(3)
                        d(className="androidx.recyclerview.widget.RecyclerView") \
                            .child(className="android.view.ViewGroup")[1] \
                            .click()
                        time.sleep(3)
                        if d.xpath("//*[@bounds='[0,123][540,204]']").exists:
                            d.xpath("//*[@bounds='[0,123][540,204]']").click(timeout=10)
                        if d.xpath("//*[@text='Tìm nửa kia qua những điều bạn thích']").exists or d(text="Chúng tôi sẽ không gợi ý bạn bè hiện tại trên Facebook trong phần Hẹn hò hoặc không cho họ biết rằng bạn đã tham gia. Bạn sẵn sàng tìm một nửa xứng đôi chưa nào?").exists :
                            break
                        if d.xpath("//*[@content-desc='Trang cá nhân']").exists or d.xpath("//*[@content-desc='Gợi ý ghép đôi']").exists:
                            break
                        elif d.xpath("//*[@content-desc='Dating']").exists or d(text="Dating").exists or d(text="Hẹn hò").exists:
                            time.sleep(20)
                            tat_mo_fb(d)
                        else:
                            break

                    elif d.xpath("//*[@content-desc='Cho phép']").exists:
                        time.sleep(2)
                        d.xpath("//*[@content-desc='Cho phép']").click()
                        d.xpath("// *[@text='CHO PHÉP']").click()
                    else:
                        print("timdating nhung chua dc mo lai ")
                        tat_mo_fb(d)
                if d.xpath("//*[@content-desc='Trang cá nhân']").exists or d.xpath("//*[@content-desc='Gợi ý ghép đôi']").exists:
                    print("xac minh la acc da co dating")
                    loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_da_mo_dating.txt")
                    break

                elif d.xpath("//*[@text='Tìm nửa kia qua những điều bạn thích']").exists or d(text="Chúng tôi sẽ không gợi ý bạn bè hiện tại trên Facebook trong phần Hẹn hò hoặc không cho họ biết rằng bạn đã tham gia. Bạn sẵn sàng tìm một nửa xứng đôi chưa nào?").exists :
                    print("chay acc dating")
                    while True:
                        if d.xpath("//*[@content-desc='Cho phép']").exists:
                            time.sleep(2)
                            d.xpath("//*[@content-desc='Cho phép']").click()
                            d.xpath("// *[@text='CHO PHÉP']").click()
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
                                if d.xpath("//*[@content-desc='Update Location']").exists or d.xpath("//*[@content-desc='Cập Nhật Vị Trí']").exists:
                                    break
                                else:
                                    lap_tim_dia_chi += 1
                                    if lap_tim_dia_chi == 5:
                                        d.xpath("//*[@text='Someqwdqwdonqwdqddddwqsacasaain.']").click()  # cai nay bo vo cho no loi de thoat ra lap lai tu dau

                        if d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").exists:

                            d.xpath("//*[@resource-id='gemstone_onboarding_other_ANYONE_test_key']").click()
                            d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
                            continue



                        if d.xpath("//*[@content-desc='Bỏ qua']").exists:

                            d.xpath("//*[@content-desc='Bỏ qua']").click()
                            continue
                        if d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").exists:

                            d.xpath("//*[@resource-id='gemstone_onboarding_next_button_test_key']").click()
                            continue
                        if d.xpath("//*[@content-desc='Trang cá nhân']").exists or d.xpath("//*[@content-desc='Gợi ý ghép đôi']").exists:
                            print("lay tien")
                            loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_mo_thang_cong.txt")
                            break


                else:
                    loi_khong_mo_dc(d,tk_mk_2fa[0],tk_mk_2fa[1], "acc_khong_co_dating.txt")
                    print("acc khong co dating")
                    break

            if d(text="Sai mật khẩu").exists or d.xpath("//*[@text='Sai mật khẩu']").exists:
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





