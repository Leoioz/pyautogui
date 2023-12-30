import string
import pyautogui  #pip install pyautogui
import os
import sys
import re
import time
import getopt
import cv2 #pip install opencv-python
import numpy
import PIL #pip install pillow
from wmi import WMI #不要删

#================================huahua0.88=====================================
UAC_control_image=r'.\src\UAC_button.png'
UAC_control_code=r'C:\Windows\System32\UserAccountControlSettings.exe'

Wireless_image_1=r'.\src\Access_control_button.png'
Wireless_image_2=r'.\src\7z_install_button.png'
Wireless_image_3=r'.\src\7z_Close_button.png'
Wireless_image_4=r'.\src\Wireless_install_finsh.png'
Wireless_code_1=r'C:\Users\%USERNAME%\Desktop\7z2201-x64.exe'
Wireless_code_2=r'''cd 'C:\Program Files\7-Zip\''''
Wireless_code_3=r".\7z.exe x C:\Users\$env:UserName\Desktop\Release_27.6.1.zip -oC:\Users\$env:UserName\Desktop\Release_27.6.1"
Wireless_code_4=r'cd C:\Users\$env:UserName\Desktop\Release_27.6.1'
Wireless_code_5=r'.\Autorun.exe'
set_20_code_1=r'''\\10.11.1.20'''


#==============================huahua1.88========================================
#==============================office========================================
Mount_iso_code=r'''Mount-DiskImage -ImagePath "C:\Users\$env:UserName\Desktop\cn_office_professional_plus_2019_x86_x64_dvd_5e5be643.iso"'''
diskpart_iso_code=r'''diskpart'''
liskvolume_iso_code=r'''list volume'''
select_disk_iso_code=r'''select volume 0'''
assign_letter_iso_code=r'''assign letter=n'''
exit_n_iso_code=r'''exit'''
cd_n_iso_code=r'''cd n:'''
dir_n_iso_code=r'''dir'''
Office_setup_code=r'.\Setup.exe'
DisMount_iso_code=r'Dismount-DiskImage -ImagePath "C:\Users\$env:UserName\Desktop\cn_office_professional_plus_2019_x86_x64_dvd_5e5be643.iso"'


#===================================enpower====================================
cell_code=r'''cd C:\Users\$env:UserName\Desktop\cell'''
ENPowerActiveX86_code=r'.\ENPowerActiveX86.msi'
cell_component_code=r'''.\cell5380620.exe'''
cell_plug_code=r'''.\cell2008121321664295.exe'''

#=================================Adobe========================================
adobe_cd_7z=r'''cd 'C:\Program Files\7-Zip\''''
adobe_unzip=r'''.\7z.exe x C:\Users\$env:UserName\Desktop\adobeacrobatXpro_setup.rar -oC:\Users\$env:UserName\Desktop\adobeacrobatXpro_setup'''
adobe_code=r'''cd C:\Users\$env:UserName\Desktop\adobeacrobatXpro_setup\adobeacrobatXpro_setup'''
root_code=r'''cd .\ROOT'''
Adobe_setup_code=r'''.\Setup.exe'''

#=================================RTX========================================
software_code=r'''cd C:\Users\$env:UserName\Desktop'''
rtx_setup_code=r'.\rtxclient2015formal.exe'
rtx_find_serverip=r'.\src\rtx_find_serverip.png'
rtx_serverip_image=r'.\src\rtx_serverip.png'
rtx_OK_image=r'.\src\rtx_OK_image.png'
rtx_id_image=r'.\src\rtx_id_image.png'
rtx_install_finish=r'.\src\rtx_install_finish.png'

#=================================cnpe========================================
cnpe_code=r'''cd C:\Users\$env:UserName\Desktop\cnpe'''
agent_setup_code='.\agent-s.exe'

#=================================Hotkey========================================
hotkey_close='alt','f4'
hotkey_winr='win','r'
hotkey_winx='win','x'
hotkey_at='alt','tab'
hotkey_copy='ctrl','c'
hotkey_pase='ctrl','v'
hotkey_window_close='ctrl','w'
hotkey_filepath='win','e'
hotkey_up='up'
hotkey_down='down'
hotkey_left='left'
hotkey_right='right'
hotkey_enter='enter'
hotkey_backspace='backspace'
hotkey_space='space'

#==============================huahua总类========================================
class base_function():

    def function_create_menu_windows(window_text,window_title,button):
        select_value=pyautogui.confirm(text=window_text, title=window_title, buttons=button)
        print('select_value:',select_value,'\n')
        time.sleep(1)
        return select_value

    def function_create_input_windows(window_text,window_title,default):
        user_input_vlaue=pyautogui.prompt(text=window_text,title=window_title,default=default)
        print('input_value:',user_input_vlaue,'\n')
        time.sleep(1)
        return user_input_vlaue

    def function_create_waitok_window(window_text,window_title,button):
        #返回OK,string
        pyautogui.alert(text=window_text, title=window_title, button=button)
        time.sleep(1)
        pass

    def function_input_code(code):
        secs_between_keys = 0.1
        pyautogui.typewrite(code, interval=secs_between_keys)
        #pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
        pass

    def function_find_and_click(image):
        x,y,z,w=pyautogui.locateOnScreen(image)
        print(x,y,z,w)
        pyautogui.click(x+z/2,y+w/2,button='left')
        time.sleep(1)
        pass

    def function_find_and_wait_click(image):
        image_statu=pyautogui.locateCenterOnScreen(image)
        while image_statu == None:
            time.sleep(5)
            image_statu=pyautogui.locateCenterOnScreen(image)
            print(image_statu)
            pass
        x,y=image_statu
        print(x,y)
        #pyautogui.moveTo(x,y)
        pyautogui.click(x,y,button='left')
        pass

    def function_hotkey(input_hotkey):
        input_hotkey=str(input_hotkey)
        pyautogui.hotkey(input_hotkey)
        pass

    pass

class Hotkey(object):
    hotkey_close='alt','f4'
    hotkey_winr='win','r'
    hotkey_winx='win','x'
    hotkey_at='alt','tab'
    hotkey_copy='ctrl','c'
    hotkey_pase='ctrl','v'
    hotkey_window_close='ctrl','w'
    hotkey_filepath='win','e'
    hotkey_up='up'
    hotkey_down='down'
    hotkey_left='left'
    hotkey_right='right'
    hotkey_enter='enter'
    hotkey_backspace='backspace'
    hotkey_space='space'
    pass

class UAC_Wireless_driver(object):
    #===============封装===============
    def sleep(inum):
        time.sleep(inum)
        pass

    def function_input_code(code):
        secs_between_keys = 0.1
        pyautogui.typewrite(code, interval=secs_between_keys)
        #pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
        pass

    def function_find_and_click(image):
        # pyautogui.hotkey('alt','tab')
        x,y,z,w=pyautogui.locateOnScreen(image)
        print(x,y,z,w)
        # pyautogui.moveTo(x+z/2,y+w/2)
        pyautogui.click(x+z/2,y+w/2,button='left')
        time.sleep(1)
        pass

    def function_find_and_wait_click(image):
        image_statu=pyautogui.locateCenterOnScreen(image)
        while image_statu == None:
            time.sleep(5)
            image_statu=pyautogui.locateCenterOnScreen(image)
            print(image_statu)
            pass
        x,y=image_statu
        print(x,y)
        #pyautogui.moveTo(x,y)
        pyautogui.click(x,y,button='left')
        pass

    def jude(image):
        if pyautogui.locateOnScreen(image)==None:
            pyautogui.alert(text='没找到下一步的数据', title='Debug', button='滚')
            pass
        pass
    pass

class UAC_Wireless_set(object):
    def __init__(self):
        self.wmiservice = WMI()
        self.configs = self.wmiservice.Win32_NetworkAdapterConfiguration(IPEnabled=True)  # 获取到本地所有有网卡信息,list

    def get_inter(self):
        flag = 0
        # 遍历所有网卡，找到要修改的那个
        for con in self.configs:
            ip = re.findall("\d+.\d+.\d+.\d+", con.IPAddress[0])
            if len(ip) > 0:
                return 0
            else:
                flag = flag+1

    def runset(self, ip, subnetmask, interway, dns):
        adapter = self.configs[self.get_inter()]
        # 开始执行修改ip、子网掩码、网关
        ipres = adapter.EnableStatic(IPAddress=ip, SubnetMask=subnetmask)
        if ipres[0] == 0:
            print('设置IP成功')
        else:
            if ipres[0] == 1:
                print('设置IP成功，需要重启计算机！')
            else:
                print('修改IP失败')
                return False
        #修改网关
        wayres = adapter.SetGateways(DefaultIPGateway=interway, GatewayCostMetric=[1])
        if wayres[0] == 0:
            print('设置网关成功')
        else:
            print('修改网关失败')
            return False
        #修改dns
        dnsres = adapter.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
        if dnsres[0] == 0:
            print('设置DNS成功,等待3秒刷新缓存')
            time.sleep(3)
            # 刷新DNS缓存使DNS生效
            os.system('ipconfig /flushdns')
        else:
            print('修改DNS失败')
            return False
    pass


#==================================huahua0.88过程===================================
def UAC_set():
    pyautogui.hotkey('win', 'r')
    UAC_Wireless_driver.function_input_code(UAC_control_code)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('down')
    UAC_Wireless_driver.sleep(1)
    pyautogui.hotkey('down')
    UAC_Wireless_driver.sleep(1)
    pyautogui.hotkey('down')
    UAC_Wireless_driver.sleep(1)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(1)
    #Debug
    UAC_Wireless_driver.function_find_and_click(UAC_control_image)
    UAC_Wireless_driver.sleep(5)
    pyautogui.hotkey('enter')
    #UAC_Wireless_driver.sleep(1)
    #pyautogui.hotkey('left')
    #UAC_Wireless_driver.sleep(1)
    #pyautogui.hotkey('enter')
    pass

def Wireless_Control():
    pyautogui.hotkey('win', 'r')
    UAC_Wireless_driver.function_input_code(Wireless_code_1)
    pyautogui.hotkey('enter')
    #预留首选信任项
    #function_find_and_click(Wireless_image_1)
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(4)
    #Debug
    UAC_Wireless_driver.function_find_and_click(Wireless_image_3)
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('win', 'x')
    UAC_Wireless_driver.sleep(4)
    pyautogui.hotkey('a')
    UAC_Wireless_driver.sleep(2)
    #pyautogui.hotkey('alt','tab')
    #sleep(2)
    #pyautogui.hotkey('shift')
    #sleep(2)
    UAC_Wireless_driver.function_input_code(Wireless_code_2)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(2)
    UAC_Wireless_driver.function_input_code(Wireless_code_3)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(12)
    UAC_Wireless_driver.function_input_code(Wireless_code_4)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(2)
    UAC_Wireless_driver.function_input_code(Wireless_code_5)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('d')
    UAC_Wireless_driver.sleep(12)
    pyautogui.hotkey('n')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('a')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('n')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('enter')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('i')
    UAC_Wireless_driver.sleep(25)
    #pyautogui.hotkey('alt','tab')
    UAC_Wireless_driver.sleep(2)
    pyautogui.hotkey('f')
    UAC_Wireless_driver.sleep(2)
    pass

def Wireless_set():
    user_input_ip=pyautogui.prompt(text='愚蠢的两脚兽，IP是多少？', title='果赖的灵魂提问：' , default='')
    print('user_input_ip:',user_input_ip,'\n')

    user_input_submask=pyautogui.prompt(text='愚蠢的两脚兽，Mask是多少？', title='果赖的灵魂提问：' , default='255.255.255.0')
    print('user_input_submask:',user_input_submask,'\n')

    user_input_netgetway=pyautogui.prompt(text='愚蠢的两脚兽，Getway是多少？', title='果赖的灵魂提问：' , default='')
    print('user_input_netgetway:',user_input_netgetway,'\n')

    user_input_dns=pyautogui.prompt(text='愚蠢的两脚兽，Dns是多少？', title='果赖的灵魂提问：' , default='10.11.1.249')
    print('user_input_dns:',user_input_dns,'\n')

    UWS=UAC_Wireless_set()
    UWS.runset([user_input_ip],[user_input_submask],[user_input_netgetway],[user_input_dns])
    pass

def set_20():
    user_20_id=pyautogui.prompt(text='愚蠢的人类，账号名是多少？', title='果赖的灵魂提问：' , default='')
    print('user_input_ip:',user_20_id,'\n')
    user_20_pwd=pyautogui.prompt(text='愚蠢的人类，密码是多少？', title='果赖的灵魂提问：' , default='')
    print('user_input_ip:',user_20_pwd,'\n')
    time.sleep(2)
    pyautogui.hotkey('win', 'r')
    UAC_Wireless_driver.function_input_code(set_20_code_1)
    pyautogui.hotkey('enter')
    time.sleep(12)
    UAC_Wireless_driver.function_input_code(user_20_id)
    pyautogui.hotkey('tab')
    time.sleep(2)
    UAC_Wireless_driver.function_input_code(user_20_pwd)
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('space')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('down')
    time.sleep(1)
    pyautogui.hotkey('shift','f10')
    time.sleep(1)
    pyautogui.hotkey('m')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pass

#==================================huahua1.88过程===================================

def function_install_office():
    pyautogui.hotkey('win','x')
    time.sleep(1)
    pyautogui.hotkey('a')
    time.sleep(3)
    base_function.function_input_code(Mount_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(diskpart_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(liskvolume_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(select_disk_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(assign_letter_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(exit_n_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(cd_n_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(dir_n_iso_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(Office_setup_code)
    time.sleep(1)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    pass

def function_install_enpower():
    pyautogui.hotkey('win','x')
    time.sleep(1)
    pyautogui.hotkey('a')
    time.sleep(3)
    base_function.function_input_code(cell_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(1)
    base_function.function_input_code(ENPowerActiveX86_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(5)
    pyautogui.hotkey('n')
    time.sleep(4)
    pyautogui.hotkey('e')
    time.sleep(4)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(8)
    pyautogui.hotkey('c')
    time.sleep(3)
    base_function.function_input_code(cell_component_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(8)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('a')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('i')
    time.sleep(8)
    pyautogui.hotkey('f')
    time.sleep(3)
    base_function.function_input_code(cell_plug_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(8)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('a')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(2)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('i')
    time.sleep(8)
    pyautogui.hotkey('f')
    time.sleep(3)
    pyautogui.hotkey('alt','f4')
    time.sleep(1)
    pass

def function_install_adobe():
    pyautogui.hotkey('win','x')
    time.sleep(1)
    pyautogui.hotkey('a')
    time.sleep(3)
    base_function.function_input_code(adobe_cd_7z)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(2)
    base_function.function_input_code(adobe_unzip)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(10)
    base_function.function_input_code(adobe_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(2)
    base_function.function_input_code(root_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(2)
    base_function.function_input_code(Adobe_setup_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(5)
    pyautogui.hotkey('i')
    time.sleep(2)
    #adobe_judge=base_function.function_create_waitok_window('adobe安装完了吗？','等待用户judge......','OK')
    base_function.function_find_and_wait_click(r'.\src\adobe_finish.png')
    #base_function.function_find_and_wait_click(r'.\src\adobe_finish1.png')
    #time.sleep(2)
    #pyautogui.hotkey('alt','f4')
    #time.sleep(2)
    #pyautogui.hotkey('alt','f4')
    pass

def function_install_rtx():
    pyautogui.hotkey('win','x')
    time.sleep(1)
    pyautogui.hotkey('a')
    time.sleep(3)
    base_function.function_input_code(software_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(2)
    base_function.function_input_code(rtx_setup_code)
    pyautogui.hotkey(str(hotkey_enter))
    time.sleep(4)
    pyautogui.hotkey('n')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('i')
    base_function.function_find_and_wait_click(rtx_install_finish)
    time.sleep(5)
    base_function.function_find_and_wait_click(rtx_find_serverip)
    time.sleep(2)
    base_function.function_find_and_wait_click(rtx_serverip_image)
    time.sleep(1)
    rtx_input_ip=base_function.function_create_input_windows('动动脑子吧！RTX服务器IP地址多少？','你的脑子被僵尸吃了','10.11.1.249')
    base_function.function_input_code(rtx_input_ip)
    time.sleep(2)
    base_function.function_find_and_wait_click(rtx_OK_image)
    time.sleep(1)
    rtx_input_id=base_function.function_create_input_windows('动动脑子吧！RTX账号多少？','你的脑子被僵尸吃了','')
    base_function.function_input_code(rtx_input_id)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('enter')
    pass

def function_install_pdf_forest():
    pyautogui.hotkey('win','x')
    time.sleep(1)
    pyautogui.hotkey('a')
    time.sleep(3)
    base_function.function_input_code(cnpe_code)
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    base_function.function_input_code(agent_setup_code)
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pass

def function(args):
    pass
#==================================huahua main===================================
def main():
    pyautogui.FAILSAFE = False
    XH=1
    while XH==1:
        menu_args='单身_uac','海王_netcard','渣男_netset','普信男_20share','绿茶_office','白莲花_enp','傻狗_adobe','小醋包_rtx','呵女人_pdf_forest','舔狗_exit'
        statu_seclet=base_function.function_create_menu_windows('选择你的款式：','愚蠢的人类，做出命运抉择吧！',menu_args)
        print(statu_seclet)
        if statu_seclet=='单身_uac':
            UAC_set()
            pass
        elif statu_seclet=='海王_netcard':
            Wireless_Control()
            pass
        elif statu_seclet=='渣男_netset':
            Wireless_set()
            pass
        elif statu_seclet=='普信男_20share':
            set_20()
            pass
        elif statu_seclet=='绿茶_office':
            function_install_office()
            pass
        elif statu_seclet=='白莲花_enp':
            function_install_enpower()
            pass
        elif statu_seclet=='傻狗_adobe':
            function_install_adobe()
            pass
        elif statu_seclet=='小醋包_rtx':
            function_install_rtx()
            pass
        elif statu_seclet=='呵女人_pdf_forest':
            function_install_pdf_forest()
            pass
        #elif statu_seclet=='test_exit':
            
        #    pass
        else:
            #base_function.function_hotkey(Hotkey.hotkey_close)
            pyautogui.hotkey('alt','f4')
            sys.exit(0)
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
