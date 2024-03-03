import sys
import re

def main():
    text = []
    for row in sys.stdin:
        match = re.findall(r'[oO][nN]|[oO][fF][fF]|=|\d+', row)
        text.append(match)

    b = False
    sum = 0

    for linha in text:
        for i in linha:
            if i.lower() == "on":
                b = True
            elif i.lower() == "off":
                b = False
            elif i.isdigit():
                if b:
                    sum += int(i)
            elif i == "=":
                print("Soma = " + str(sum))

if __name__ == '__main__':
    main()

