---
title: 背景
---

##基于LSB的图像隐写技术

### 隐写术

隐写是指把一个文件、消息、图像或者视频隐藏到另一个文件、消息、图像或者视频的行为。与密码学不同的是，隐写术旨在隐藏消息或其他形式的信息本身的存在，不引起发送方和接收方以外的人的怀疑而完成信息的交流，而密码学则用于隐藏这些信息的内容，使得非发送方或接收方即使截获消息也无法得到所交流的信息的真实内容。隐写术的主要任务是使发生在公共信道上的秘密信息交流不被察觉，隐藏了秘密信息的图片或其他格式的载体与隐藏之前的原始数据在视觉上以及其他几个重要特征一致。

隐写术是一种秘密通信的艺术，这个术语最早在从几千年前开始，人类就着迷于密文书写，并出于多种原因和动机学习这种和研究这种技术[@Schaathun:1540219]，早期密写通常是指密码学，而随着时代发展现在密写也涵括了隐写术，两者用不同的方式实现密写的目的。无论在哪个时代，隐写术广泛应用于各个领域。早期的隐写实践是使用不可见的墨水在信件中书写消息，显而易见地，军事和政治中，在不被敌方察觉的前提下向友方传递信息的能力十分关键。在数字时代，这种思想发展为在多媒体文件中隐藏其他数字消息。现代隐写术在1985年以后随着个人计算机的推广而问世，随着计算机科学技术和数学的发展以及深入研究而迅速发展并投入更广泛的应用，例如电子通信包含了传输层内的隐写码以传送如文档文件或图片文件等多媒体数据。

与密码学相似，隐写术的使用场景决定了它必须满足以下三个要求：

- 保密性：不容易被探查到隐藏消息的存在
- 可获得性：不会出现由于修改数据的载体导致秘密消息的丢失，秘密消息可以被恢复
- 完整性： 其他人无法伪造出错误信息

隐写系统可以被视为加密系统的一个特例[@backes2005public]，在这个系统中我们要求密文与明文对于其他人来说难以区分。值得注意的是，隐写加密方必须首先合成一个与秘密消息无关的无害的文件。载体合成具有很大的挑战性，高效合成载体的隐写机制很少。对于这个问题，使用通过修改实现隐写的方法很好地避免了这个挑战。这种系统使用一个现有的与秘密消息无关的文件，也就是载体，作为隐写系统的输入的一部分，接下来秘密消息转换为以让人难以觉察的载体的修改，得到与载体极其相似的结果，即伪装（stego）。理论上，载体合成是最自由且强大的隐写方法，因为它可以不受限制地适用于任意的秘密消息。但在实践中，无害文件的合成是一个非常复杂且低效的过程，所以大多数众所周知的实用系统实用的都是修改载体的方法。当然除了合成和修改两种模式以外，载体选择[@filler2009complete]也是可行的方案，可以类比为传统密码学中使用的编码本，有多个载体或密文分别对应特定的秘密消息。然而，这种模式需要的可用载体数量太大，并不是在所有场景下都实用。所以我们在大多数情况下会选择通过修改进行隐写的模式，也就是说隐写的过程需要使用已经存在的文件作为原始的输入，而多媒体文件（如图像、音频和视频等）往往较大，包含了大规模的数据，可以找到足够的空间隐藏消息同时在不表达出可以被察觉的异常效果，是理想的载体。其中，数字图像的应用场景广泛，修改方便，且容易在互联网快速传播，成为了应用最多的载体。本文也将围绕图像隐写技术展开。

早期的隐写安全完全依赖于隐写算法，只将载体和秘密消息作为输入而不使用秘钥，被称为纯隐写系统，一旦隐写算法泄露则整个系统被破解。将秘钥引入作为输入的隐写系统则被称为秘钥隐写系统。在密码学中，加密者和解密者共享秘钥，关于算法的知识对双方区分伪装和正常消息没有帮助，这个结论即kerckhoffs原则，在隐写系统中并不总是成立[@fridrich2004searching]。符合kerckhoffs原则的系统在使用一个秘钥的实例被攻破后，使用其他秘钥的实例的安全性不受影响，与其他系统相比这样的系统具有巨大的优势，因为生成不同的秘钥恨容易，而重新设计一个算法却很困难。但事实上，基于kerckhoffs原则安全的隐写系统很难设计，同时大多数应用场景下，除了发送方和接收方外其他人对于他们的隐写系统通常一无所知，因此，不遵循kerckhoffs原则的系统也是可行的。

### LSB隐写算法

对于一个二进制整数来说，最低有效位（LSB）是最低的比特位（即第0位），决定了这个数是奇数还是偶数，这个比特位相比于其他位置的变化对于整个数值变化影响是最小的。

LSB嵌入方法是一种经典的图像隐写算法。这种方法最早被用于像素图像，在像素图像中，每个像素都是代表该点颜色强度的整数。在灰度图像中，每个点的像素值表达了该点色彩介于黑白之间的程度，而在具有三个色彩信道的RGB图像中，每个像素点由三个独立个代表红、绿、蓝三种颜色强度的值合成$\left( {R,G,B} \right)$单元，这些像素值的取值范围通常是8bit的整数值，也就是$\left[ {0,255} \right]$。在颜色强度上的微小改动被察觉的可能性很小，LSB隐写算法正是利用了像素图像的这个特性，舍弃每个像素原来的最低有效位（LSB），并替换为需要隐藏的消息。接收者得到伪装完成的图像后可以通过模2操作提取新的LSB并将之还原为完整的消息。

最基础的基于LSB的隐写系统从图像的左上角开始逐位嵌入秘密消息，推进的顺序是由发送者和编程语言决定的最自然的方向。为了方便接受者确定隐藏的消息在何处结束，我们可以将消息的大小作为头部隐藏在前$n$像素中，这里的$n$是一个双方已经约定好的整数。通过这个简单的python程序可以演示这个隐写的过程（在python中最自然的数据是逐行嵌入）：

```py
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
    lsb_plane=im & 0b00000001
    length=binary_array_to_int(lsb_plane[0:pro_text_size])
    secret_bytes=lsb_plane[pro_text_size:pro_text_size+length*8].reshape((length,8))
    secret_bit=[binary_array_to_int(x) for x in secret_bytes]
    return ''.join(chr(c) for c in secret_bit)

```
显然，这种方法使得隐藏的消息总是在同样的位置。作为最经典的图像隐写算法，LSB嵌入模式许多的变体。
