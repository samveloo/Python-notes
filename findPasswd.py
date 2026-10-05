def findPasswd(passwd):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for g in range(10):
                        for t in range(10):
                            variantPasswd = f'{i}{j}{k}{l}{g}{t}'

                            if variantPasswd == passwd:
                                return print(f'Ваш пароль найден: {variantPasswd}')

                    # print(variantPasswd)

findPasswd(input('Введите ваш пароль: '))