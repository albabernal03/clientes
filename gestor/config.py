import sys
DATABASE_PATH= './CLIENTES/gestor/clientes.csv'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = './gestor/tests/clientes_tests.csv'
