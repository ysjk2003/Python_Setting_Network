import ctypes, sys
import wmi

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#관리자 권한
if is_admin():
    # 어댑터 정보 가져오기
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # WI-FI 어댑터
    nic = nic_configs[2]

    # DHCP 설정과 DNS초기화
    nic.EnableDHCP()
    nic.SetDNSServerSearchOrder()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)