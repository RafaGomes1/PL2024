import csv
import re
import ply.lex as lex

def main():
    tokens = [
        'LISTAR',
        'SAIR',
        'SALDO',
        'MOEDA',
        'SELECIONAR',
    ]
    
    # A regular expression rule with some action code
    def t_LISTAR(t):
        r'LISTAR'
        for row in t.lexer.products:
            print(f"{row[0]}----->{row[1]}----->{row[2]}")
        return t
    
    def t_SAIR(t):
        r'SAIR'
        print(f"Change: {t.lexer.balance}")
        t.lexer.exit_flag = True
        return t
    
    def t_SALDO(t):
        r'SALDO'
        print(f"Available balance: {int(t.lexer.balance / 100)}e {t.lexer.balance % 100}c")
        return t

    def t_MOEDA(t):
        r'MOEDA((\s(5|10|20|50)c)|\s(1|2)e)+'
        values = re.findall(r'\d{1,2}', t.value)
        denominations = re.findall(r'[ec]', t.value)
        pairs = list(zip(values, denominations)) 
        for amount, unit in pairs:
            if unit == 'c':
                t.lexer.balance += int(amount)
            else:
                t.lexer.balance += int(amount) * 100
        return t

    def t_SELECIONAR(t):
        r'SELECIONAR\s\d+'
        product_index = int(re.findall(r'\d+', t.value)[0])
        if 0 <= product_index < len(t.lexer.products):
            price_str = t.lexer.products[product_index][2]
            price_parts = price_str.split(" ")

            total_price = 0
            for part in price_parts:
                if part.endswith('e'):
                    total_price += int(part[:-1]) * 100
                else:
                    total_price += int(part[:-1])
            
            if total_price <= t.lexer.balance:
                t.lexer.balance -= total_price
                print("Product purchased")
            else:
                print("Insufficient balance")
        else:
            print("Product unavailable")
        return t
    
    # Characters to ignore (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(t):
        t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()

    # Read the file
    with open("products.csv", 'r') as file:
        products = list(csv.reader(file, delimiter=';'))
    lexer.products = products

    lexer.exit_flag = False
    lexer.balance = 0
    while not lexer.exit_flag:
        user_input = input("Enter command: ")
        lexer.input(user_input)
        tok = lexer.token()
        if not tok:
            print("Invalid operation")

if __name__ == "__main__":
    main()
