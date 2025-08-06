#Here I wrote a script that prints 2025 without using any digit in the source code.

import time

def main():
    date = time.ctime()
    print(date.split()[-1])


#####################################################
if __name__ == "__main__":
    main()