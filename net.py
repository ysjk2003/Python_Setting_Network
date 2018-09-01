import ctypes, sys
import wmi

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#관리자 권한
if is_admin():
    # 네트워크 정보 가져오기
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # WI-FI네트워크 어댑터 정보
    nic = nic_configs[2]

    # ip, subnetmask, gateway 주소
    ip = u'10.156.146.132'
    subnetmask = u'255.255.255.0'
    gateway = u'10.156.146.1'
    dns = u'210.111.226.7'
    dns2 = u'210.111.226.8'

    # ip, subnetmask gateway설정
    nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
    nic.SetDNSServerSearchOrder([dns])
    
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)