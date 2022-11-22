import zipfile

def extract_file(zfile, password):
    try:
        zfile.extractall(pwd = bytes(password, 'utf-8'))
        return password
    except:
        print('Wrong password!')
        return

def main():
    zfile = zipfile.ZipFile('test2.zip')
    passfile = open('passlist.txt')
    for line in passfile.readlines():
        password = line.strip('\n')
        guess = extract_file(zfile, password)
        if guess:
            print('Password = ' + password)
            break

if __name__ == '__main__':
    main()