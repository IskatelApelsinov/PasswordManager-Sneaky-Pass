import hashlib
import os

class Cripta(object):
    def __init__(self):
        #mchs_project
        super(Cripta, self).__init__()


    def shifr_salt(self, passwd):
        # Add a user

        salt = ''
        # for letter in username:
        #     salt += str(ord(letter))
        # print(salt)
        # salt = hex(int(salt))
        # print(salt)
        # salt = os.urandom(32)
        # print(salt)
        salt = passwd.encode(encoding='utf-8')
        #print(salt)

        key = hashlib.pbkdf2_hmac('sha256', passwd.encode('utf-8'), salt, 100000)
        #print(key)
        return key

    def hasher(self, passwd):
        salt = passwd.encode(encoding='utf-8')
        key = hashlib.sha1(salt).hexdigest()
        return key