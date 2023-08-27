from random import randint
from random import choice
dictionary = {
            #You can add more symbols or change anything below, in format of "a":"b" if character a is found, it'll decode as b, and vice versa
            #make sure you add a coma every "a":"b"
            "q":"w","e":"r","t":"y","u":"i","o":"p","a":"s","d":"z","f":"g","h":"x","j":"k","l":"c","v":"b","n":"m",
            "Q": "W", "E": "R", "T": "Y", "U": "I", "O": "P","A": "S", "D": "Z", "F": "G", "H": "X", "J": "K","L": "C", "V": "B", "N": "M",
            "1":"0","2":"9","3":"8","4":"7","5":"6"," ":"&",".":"/",
            #[SUPER IMPORTANT] Do NOT add the character ! as a character here, or the code will break. it's used to determine the amount of salt in the string.

}

def split(line,ch):
    ch = str(ch)
    sring = []
    sing = ''
    for x in line:
        if x!=ch:sing=sing+x
        else:
            sring.append(sing)
            sing = ''
    if sing!='':
        sring.append(sing)
    return sring

def DecodeS(string):
    a=-1
    sring = ""
    stopAt = 0
    yes = None
    thing = split(string,"!")
    if len(thing)>1:
        yes = True
        stopAt = int(thing[1])
        string = thing[0]+thing[2]
        for x in string:
            sring=sring+x
    if yes == True:
        return sring[:len(sring)-stopAt]

def encodes(string,salt):
    encoded = ""
    ind = -1

    rand = randint(0,len(string)-1)

    for ltr in string:
        if DecodeS(string)==None:
            for enc, enc1 in dictionary.items():
                if ltr == enc:
                    encoded = encoded+enc1
                    if ind<rand:
                        ind+=1
                        if ind==rand:
                            encoded=encoded+"!"+salt+"!"
                    continue
                elif ltr == enc1:
                    encoded = encoded+enc
                    if ind<rand:
                        ind+=1
                        if ind==rand:
                            encoded=encoded+"!"+salt+"!"
                    continue
                continue

    salt = int(salt)
    while salt>0:
        salt-=1
        encoded=encoded+dictionary[choice(list(dictionary.keys()))]
    return encoded

def decode(encodited):
    decoded = ""
    encodited = DecodeS(encodited)
    if encodited!=None:
        for x in encodited:
            for enc,enc1 in dictionary.items():
                if x == enc:
                    decoded = decoded+enc1
                elif x == enc1:
                    decoded = decoded+enc
    else:
        return "Those words aren't encoded"
    return decoded

print(decode("Xrccp&yxua&ua&l!3!iaypn&rmlpzre&um&Otyxpm&nszr&vt&sentfpfsnra&pm&fuyxiv/Bgw"))
print(decode("Tpi&lsm&lpmgufier&yxr&rmlpzre&sa&nilx&sa&tpi&qpic!24!z&cujr&yiypeusc&ua&um&yxr&fuyxiv&ERSZNR/nzPbC/8Z7g6xMIXzxCscYZb9ys"))
print(" ")

saltR = None
while True:
    a = input("Random Salt Mode? Y/N :").lower()
    if a=='y':
        saltR = True
        break
    elif a=='n':
        saltR = False
        break
    
while True:
    try:a = input("Encode/Decode :")
    except EOFError:
        print("Encoder Doesn't have some of the character in that string")
        continue
    if a[:6].lower() == "encode" and len(split(a,' '))>=1:
        if saltR == False:
            try:salt = input("Amount of salt :")
            except EOFError:
                print("Please type the format correctly.")
        else:
            salt = str(randint(1,25))
        print("Encode :"+encodes(a[7::],salt))
    elif a[:6].lower() == "decode" and len(split(a,' '))>=1:
        try:print("Decode :"+decode(a[7::]))
        except EOFError:
            print("Please type the format correctly.")
    elif a == "quit":break