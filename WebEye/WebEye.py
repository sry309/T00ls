import socket
import telnetlib

def Web_Probe():
    for x in open('url.txt').readlines():
        try:
            ip = socket.gethostbyname(x.strip())

            try:
                tp = telnetlib.Telnet(ip.strip(),80)
                print(ip + '---->' + 'http://' + x)
            except Exception as E:
                pass

            try:
                ts = telnetlib.Telnet(ip.strip(),80)
                print(ip + '---->' + 'https://' + x)
            except Exception as E:
                pass

        except Exception as E:
            pass



if __name__ == '__main__':
    Web_Probe()
