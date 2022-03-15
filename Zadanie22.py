import re
 
def card(string):
     
    regexVisa = "^4[0-9]{12}(?:[0-9]{3})?$";
    regexMaster = ("^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$");
    regexAmerican = ("/^3[47]\d{13,14}$/")
 
    
    p = re.compile(regexVisa);
    q = re.compile(regexMaster);
    r = re.compile(regexAmerican)
     
    # If the string is empty
    # return false
    if (string == ''):
        print("Pusty numer karty")
        return False;
         
    m = re.match(p, string);
    n = re.match(q, string);
    o = re.match(r, string);

 
    if m is None:
        print("...ups...")
        
    else:
        print("Visa")

    if n is None:
        print("...ups...")
        
    else:
        print("MasterCard")

    if o is None:
        print("...ups...")
        
    else:
        print("American Express")
        
        

def main():
    string= input("Wprowadź numer karty. >> ")
    nowyNapis = card(string=string)
main()