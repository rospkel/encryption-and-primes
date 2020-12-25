import math
import numpy as np

#converts matrix entries to mod26
vector_mod26 = np.vectorize(lambda n: round(n % 26))

#change to whatever, as long as it's mod26
A = np.array([[5, 2],
              [3, 1]])
A_inv = vector_mod26(np.linalg.inv(A))
b = np.array([[6],
              [7]])

#encoding function, could be modified for more complexity
def enc(p):
    return A @ p + b

#decoding, directly related to encoding, so need a new decoding for a new encoding function
def dec(p):
    return A_inv @ p - A_inv @ b

#lettertonumber
def ltn(c):
    return ord(c)-65

#numbertoletter
def ntl(n):
    return chr((n % 26)+65)

#for polyalphabetic encoding
def messageToVectors(msg):
    vec_list = []
    while len(msg) > 1 :
        vec_list.append(np.array([[ltn(msg[0])],
                                  [ltn(msg[1])]]))
        msg = msg[2:]
    if len(msg) == 1:
        vec_list.append(np.array([[ltn(msg[0])],
                                  [0]]))
    return vec_list

#applies encoding to vector list
def appEnc(vl):
    return list(map(enc, vl))

#applies decoding to vector list
def appDec(vl):
    return list(map(dec, vl))

#in the name
def vectorsToMessage(vl):
    f = lambda v : v.tolist()
    lol = map(f, vl)
    nums = []
    for sublist in lol:
        for item in sublist:
            for realitem in item:
                nums.append(realitem)
    chars = map(ntl, nums)
    return ''.join(chars)

#actual encryption function, which takes in message
def encrypt(msg):
    print(vectorsToMessage(appEnc(messageToVectors(msg))))

#actual decryption function
def decrypt(msg):
    print(vectorsToMessage(appDec(messageToVectors(msg))))

#tests
print(A_inv)
encrypt("LISTENINGTOGOODKIDMAADCITYFORTHEFIRSTTIMERIGHTNOWITSPRETTYGOOD")
