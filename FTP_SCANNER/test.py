import ftplib

def anonymous_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostname) + 'FTP Anonymous login succeded')
        ftp.quit()
        return True
    except:
        print('\n [-] ' + str(hostname) + 'FTP Anonymous login failed')
        return False

if __name__ == '__main__':
    anonymous_login('142.251.39.46')