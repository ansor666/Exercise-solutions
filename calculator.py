#Here I made a calculator that you can test through the console

import sys

def main():
    if len(sys.argv)!=4:
        print(f"Error!!\nUsage: py {sys.argv[0]} <Operation> <a> <b>\nExample: py {sys.argv[0]} + 1 2 ---> 3")
        sys.exit()
    op,a,b = sys.argv[1:]
    if op == "+":
        val = float(a)+float(b)
    elif op == '-':
        val = float(a)-float(b)
    elif op == '*':
        val = float(a)*float(b)
    elif op == '/':
        val = float(a)/float(b)
    elif op=="%":
        val = int(a)%int(b)
    elif op == '//':
        val = float(a)//float(b)
    else:
        val = f"Error: unrecongnized {op}!!"
    print(val)
    


#####################################################
if __name__ == "__main__":
    main()