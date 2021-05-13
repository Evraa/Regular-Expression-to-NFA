import re



def split(word):
    return list(word)

def parse_astrisk(list_of_ch):
    prev_ch = None
    new_list = []
    close_it = False
    for ch in list_of_ch:

        if ch =="*" and prev_ch != ")":
            #for sure it's a character
            new_list.insert(-1,"(")
            close_it = True

        #append the char
        if close_it:
            close_it = False
            new_list.append('*')
            new_list.append(")")
            
        else:
            new_list.append(ch)

        prev_ch = ch

    return new_list
        

def parse(txt):
    #remove spaces
    txt = txt.replace(" ","")
    list_of_ch = split(txt)
    list_of_ch = parse_astrisk(list_of_ch)
    

    print (list_of_ch)


if __name__ == "__main__":
    txt = str(input("Insert RE:\n"))
    parse(txt)