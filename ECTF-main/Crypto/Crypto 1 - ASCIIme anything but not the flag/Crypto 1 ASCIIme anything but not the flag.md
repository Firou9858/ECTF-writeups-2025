# Crypto 1 : ASCIIme anything but not the flag

There is an encrypted flag, good luck with that I encrypted it well !

`108 100 111 109 123 85 99 49 122 95 106 53 95 79 111 51 95 88 52 116 95 48 109 95 51 111 88 121 90 107 97 106 48 105 125 10 10 69 98 111 98 32 102 112 32 118 108 114 111 32 104 98 118 44 32 100 108 108 97 32 105 114 122 104 32 58 32 72 66 86 72 66 86 10 10 87 101 108 108 32 100 111 110 101 44 32 98 117 116 32 110 111 119 32 100 111 32 121 111 117 32 107 110 111 119 32 97 98 111 117 116 32 116 104 101 32 103 117 121 32 119 104 111 32 103 111 116 32 115 116 97 98 98 101 100 32 50 51 32 116 105 109 101 115 32 63`

\Author - Antoine

#### Points :
`150`

## Solution
The tools i used are https://www.dcode.fr/ and https://www.cachesleuth.com/multidecoder/.  
Note : Cachesleuth is good to multiple decode when you don't know what is the encryption.
 
### Step 1 :
ASCII Encoding: 
```
ldom{Uc1z_j5_Oo3_X4t_0m_3oXyZkaj0i}

Ebob fp vlro hbv, dlla irzh : HBVHBV

Well done, but now do you know about the guy who got stabbed 23 times ?
```
### Step 2 :
Caesar Cipher (Shift 23):
```
ogrp{Xf1c_m5_Rr3_A4w_0p_3rAbCndm0l}

Here is your key, good luck : KEYKEY
```
### Step 3 :
Vigenère Cipher (Key: KEYKEY):
```
ectf{Th1s_i5_Th3_W4y_0f_3nCrYpti0n}
```
