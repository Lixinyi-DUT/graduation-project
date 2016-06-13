#demo for naive LSB steganography
#------------hide process---------------------
# 1. flatten all pixels in the cover as a 1-D array with elements ranges in [0,255].
# 2. trancate the original least significant bit(LSB) of every pixel.
# 3. embed the length of secret message (binary array) as with the LSB of first several pixels
# 4. then embed the whole string as a 0-1 bytes stream into the LSB of the rest pixels
#------------reveal process---------------------
# 1. load the stego image and get LSB plane of the whole iamge
# 2. read the first several unit of LSB plane and get the length of secret message
# 3. read the corresponding length of following units and turn the binary array into string
#-------------------------------------------------

from PIL import Image
import os
import operator
import numpy as np
import string
import scipy.misc
from scipy.misc import imread


def convert_message_to_bit(string_text):
    '''convert the secret message from string to bytearray'''
    bit_string=[]
    for char in string_text:
        bit_string.extend([int(d) for d in bin(ord(char))[2:].zfill(8)])
    return np.array(bit_string)

def hide_side_information(carrier,length,pro_text_size):
    '''hide some side information(i.e. the length of secret message here) in the front of the image'''
    bit=bin(length)[2:].zfill(pro_text_size)
    length_data=np.array([int(d) for d in bit ])
    side_info=carrier[:pro_text_size]+length_data
    carrier[:pro_text_size]=side_info
    return carrier

def binary_array_to_int(arr):
    '''convert a 0-1 array into a decimal integer'''
    bit_string=''.join(arr.astype(np.str))
    return int(bit_string,2)

def hide(cover_pic,secret_text,pro_text_size):
    '''hide secret information in a given picture(cover), return a image object'''
    length=len(secret_text)
    cover=np.array(cover_pic)
    size=cover.shape
    cover_data=cover.flatten()
    carrier_data=cover_data & 0b11111110 #truncated cover without LSB plane
    l=hide_side_information(carrier_data,length,pro_text_size)
    secret_bytes=convert_message_to_bit(secret_text)
    secretbytes_length=length*8
    carrier_data[pro_text_size:pro_text_size+secretbytes_length]=carrier_data[pro_text_size:pro_text_size+secretbytes_length]+secret_bytes
    new_data=carrier_data.reshape(size)
    new_iamge=Image.fromarray(new_data)
    return new_iamge

def reveal(secret_iamge,pro_text_size):
    '''extract secret message from a given picture(stego) return a secret string'''
    im=np.array(secret_iamge).flatten()
    print(im[0:8])
    for i in range(8):
        print(im[i],[int(d) for d in bin(im[i])[2:].zfill(8)])
    lsb_plane=im & 0b00000001
    length=binary_array_to_int(lsb_plane[0:pro_text_size])
    secret_bytes=lsb_plane[pro_text_size:pro_text_size+length*8].reshape((length,8))
    secret_bit=[binary_array_to_int(x) for x in secret_bytes]
    return ''.join(chr(c) for c in secret_bit)

print(os.getcwd())
os.chdir("F:\\graduation-project\\codes")
lena=Image.open("exampleimage\\l.png") # import lena
gettysburg_address="Four score and seven years ago, our fathers brought forth upon this continent a new nation: conceived in liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war...testing whether that nation, or any nation so conceived and so dedicated. . . can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field as a final resting place for those who here gave their lives that this nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we cannot dedicate...we cannot consecrate... we cannot hallow this ground. The brave men, living and dead, who struggled here have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember, what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us...that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion... that we here highly resolve that these dead shall not have died in vain...that this nation, under God, shall have a new birth of freedom...and that government of the people, by the people, for the people, shall not perish from this earth." #import gettysburg address
hide(lena,gettysburg_address,15).save("output\\stego(gray).png")
stego=imread("output\\stego(hello_world).png")
print(bin(ord('a')))
print(reveal(stego,15))
