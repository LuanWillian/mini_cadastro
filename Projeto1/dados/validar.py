def ler_inteiro(mensagem):
    while True:
        valor_str = str(input(mensagem)).strip()
        if valor_str.isnumeric() and not valor_str == '':
            valor_int = int(valor_str)
            break
        else:
            print('\033[0;31mERRO! Digite apenas uma das opções acima .\033[m')
    return valor_int


def ler_arquivo(usuario, senha=''):
    file = open('usuarios_senhas', 'r')
    for c in file:
        if usuario == c.split(';')[0] and senha == c.split(';')[1]:
            return True
        elif usuario == c.split(';')[0] and senha == '':
            return True
    return False


def validar_usuario_senha(usuario, senha):
    while True:
        if ler_arquivo(usuario, senha):
            print('-'*55)
            print('\033[0;32m            LOGIN EFETUADO COM SUCESSO!\033[m')
            print('-'*55)
            break
        else:
            print('\033[0;31mERRO! Usuario ou senha não encontrado! Tente novamente.\033[m')
            usuario = str(input('\033[0;33mDigite seu usuario: \033[m')).strip()
            senha = str(input('\033[0;33mDigite sua senha: \033[m')).strip()


def procurar_caracter(usuario):
    letras = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    lista = []
    contador = 0
    for c in usuario:
        lista.append(c)
    for c in range(0, len(lista)):
        if not lista[c] in letras:
            contador += 1
    if contador == 0:
        return False
    else:
        return True


def usuario_cadastrar(usuario):
    while True:
        caracter = procurar_caracter(usuario)
        existe = ler_arquivo(usuario)
        compri = len(usuario)

        if usuario == '':
            print('\033[0;31mERRO! Esse campo não pode ficar vazio!\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        if compri > 15:
            print('\033[0;31mERRO! Voce ultrapassou o valor maximo de caracteres(Minimo 5 Maximo 15)!\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        elif compri < 5:
            print('\033[0;31mERRO! Voce não atengio o valor minimo de caracteres(Minimo 5 Maximo 15)!\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        elif usuario.islower() is False:
            print('\033[0;31mERRO! Digite apenas letras minusculas!\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        elif ' ' in usuario:
            print('\033[0;31mERRO! Não coloque espaços no seu nome de usuario!\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        elif caracter is True:
            print('\033[0;31mERRO! Não coloque caracteres especias no seu nome de usuario!\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        elif existe:
            print('\033[0;31mERRO! Usuario ja existente! Tente novamente.\033[m')
            usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m')).strip()

        else:
            return usuario


def senha_cadastrar(senha):
    while True:
        compri = len(senha)
        if senha == '':
            print('\033[0;31mERRO! Esse campo não pode ficar vazio!\033[m')
            senha = str(input('\033[0;33mCrie uma senha(Minimo 8 caracteres Maximo 12 caracteres): \033[m')).strip()

        elif compri < 8:
            print('\033[0;31mERRO! Voce não atengio o valor minimo de caracteres!\033[m')
            senha = str(input('\033[0;33mCrie uma senha(Minimo 8 caracteres Maximo 12 caracteres): \033[m')).strip()

        elif compri > 12:
            print('\033[0;31mERRO! Voce ultrapassou o valor maximo de caracteres!\033[m')
            senha = str(input('\033[0;33mCrie uma senha(Minimo 8 caracteres Maximo 12 caracteres): \033[m')).strip()

        elif ' ' in senha:
            print('\033[0;31mERRO! Não pode conter espaços na senha!\033[m')
            senha = str(input('\033[0;33mCrie uma senha(Minimo 8 caracteres Maximo 12 caracteres): \033[m')).strip()

        else:
            return senha


def cadastrar_usuario_senha(usuario, senha):
    file = open('usuarios_senhas', 'a')
    file_test = open('usuarios_senhas', 'r')
    lista_test = []
    for c in file_test:
        lista_test.append(c)
    if len(lista_test) == 0:
        file.write(f'{usuario};{senha}')
    else:
        file.write(f'\n{usuario};{senha}')
    file.close()
    print('-'*55)
    print('\033[0;32m       USUARIO E SENHA CADASTRADOS COM SUCESSO!\033[m')
    print('-'*55)
