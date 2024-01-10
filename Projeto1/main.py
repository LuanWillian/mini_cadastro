from Projeto1.dados import validar
print('-'*55)
print('\033[0;33m              SEJA BEM VINDO AO SITE\033[m')
print('-'*55)

print('\033[0;33mEntrar ou cadastrar? Escolha uma das opções abaixo!\n\033[m'
      'Digite \033[0;33m1\033[m Para entrar no site\n'
      'Digite \033[0;33m2\033[m Para se cadastrar no site\n'
      'Digite \033[0;33m3\033[m para sair do site')
print('-'*55)

opcao = validar.ler_inteiro('\033[0;33mSua opção: \033[m')

if opcao == 1:
    print('-'*55)
    print('\033[0;33m              OPÇÃO "1" ENTRAR NO SITE\033[m')
    print('-'*55)
    usuario = str(input('\033[0;33mDigite seu usuario: \033[m'))
    senha = str(input('\033[0;33mDigite sua senha: \033[m'))
    validar.validar_usuario_senha(usuario, senha)

elif opcao == 2:
    print('-'*55)
    print('\033[0;33m            OPÇÃO "2" CADASTRAR NO SITE\033[m')
    print('\033[0;33mNÃO PODE CONTER CARACTERES ESPECIAS NO SEU NOME DE USUARIO!\n'
          'NÃO PODE CONTER ESPAÇOS NA SUA SENHA E NO SEU USUARIO!\n'
          'VALOR MINIMO DE CARACTERES NO NOME DE USUARIO E 5, MAXIMO 15\033[m')
    print('-'*55)
    usuario = str(input('\033[0;33mCrie um usuario(Com letras minusculas): \033[m'))
    a = validar.usuario_cadastrar(usuario)
    senha = str(input('\033[0;33mCrie uma senha(Minimo 8 caracteres Maximo 12 caracteres): \033[m'))
    b = validar.senha_cadastrar(senha)
    validar.cadastrar_usuario_senha(a, b)

elif opcao == 3:
    print('-'*55)
    print('\033[0;33m     ATE LOGO,  SAINDO DO SITE...\033[m')
    print('-'*55)
