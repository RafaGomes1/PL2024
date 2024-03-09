import sys
import re
from ply.lex import lex

tokens = (
        'SELECT',
        'UPDATE',
        'DELETE',
        'WHERE',
        'FROM',
        'INT',
        'VAR',
        'OPERADORES'
)

t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_UPDATE = r'[Uu][Pp][Dd][Aa][Tt][Ee]'
t_DELETE = r'[Dd][Ee][Ll][Ee][Tt][Ee]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_FROM = r'[Ff][Rr][Oo][Mm]'
t_INT = r'\d+'
t_VAR =  r'\w+'
t_OPERADORES = r'>=|<=|<|>|==|='
t_ignore = ' \t'

def t_error(t):
    print("Unexpected character '%s'" % t.value[0])
    t.lexer.skip(1)

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.read()
        lexer = lex()
        lexer.input(data)
        for token in lexer:
            print(token)

if __name__ == '__main__':
    main()