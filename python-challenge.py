# 

## level 1
print(2**38) #274877906944


## level 2
# given a Caesar cipher of K -> M and a ciphertext:
# capture the ciphertext string in a variable
txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# create the map table to replace the characters in the ciphertext
x = "abcdefghijklmnopqrstuvwxyz"
y = "cdefghijklmnopqrstuvwxyzab"

# put it all together
trans = txt.maketrans(x, y)
print (txt.translate(trans))

# then do the same thing on the URL to get to the next level:
url = "map"
newLink = url.maketrans(x, y)
print (url.translate(newLink))