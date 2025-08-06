"""
Exercise:
On the attic, among the old books of your father you notice one with the following title: "Fundamentals of Programming".
Wow, he never mentioned that he learned such things… As you open the book, a yellow paper falls to your feet with a cryptic message written on it:

Bcyp Qml,

G fytc y dyrfcpjw ybtgac dmp wms:
jcypl rfc Nwrfml npmepykkgle jylesyec!

Jmtc,

Byb

On the other side of the paper you find this: "K → M, O → Q, E → G".
"""

from string import ascii_lowercase,ascii_uppercase


TEXT= """Bcyp Qml,

G fytc y dyrfcpjw ybtgac dmp wms:
jcypl rfc Nwrfml npmepykkgle jylesyec!

Jmtc,

Byb"""


def main():
    text_out = ""
    for c in TEXT:
        if c.isalpha():
            code_pnt =ord(c)+2
            if code_pnt == 123:
                code_pnt = 97
            elif code_pnt == 124:
                code_pnt = 98
            elif code_pnt == 91:
                code_pnt = 65
            elif code_pnt == 92:
                code_pnt = 66
            text_out += chr(code_pnt)
        else:
            text_out += c
    print(text_out)



def main1():
    text_out = ""
    for c in TEXT:
        if c.isalpha():
            if c.isupper():
                idx = ascii_uppercase.find(c)
                text_out += ascii_uppercase[(idx+2)%26]
            elif c.islower():
                idx = ascii_lowercase.find(c)
                text_out += ascii_lowercase[(idx+2)%26]
        else:
            text_out += c
    print(text_out)
                
#####################################################
if __name__ == "__main__":
    main1()