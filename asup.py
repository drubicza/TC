import os, sys
print 'Masukan Username dan Password !'
username = 'Rizky'
password = 'Cungur'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('\x1b[1;92m[\x1b[1;91m+\x1b[1;92m] \x1b[1;96musername\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
    if uname == username:
        pwd = raw_input('\x1b[1;92m[\x1b[1;31m+\x1b[1;32m] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        if pwd == password:
            print 'Hello Welcome To My Tools'
            print "Don't Copy My Project !",
            sys.exit()
        else:
            print 'Password Kamu Salah!!!'
            print 'Back Login'
            restart()
    else:
        print 'Username Kamu Salah !!!'
        print 'Back Login'
        restart()

try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()
