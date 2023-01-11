#Caesar Cipher

import string


wordList=[]

def build_coder(shift):

    ## Gera uma chave de criptografia de acordo com um número de espaço

    assert shift in range(-52,53)

    codigo ={}

    lowercase_and_space = string.ascii_lowercase + ' '
    uppercase_and_space = string.ascii_uppercase + ' '

    shifted_lowercase_and_space = lowercase_and_space[shift:] + lowercase_and_space[:shift]
    shifted_uppercase_and_space = uppercase_and_space[shift:] + uppercase_and_space[:shift]

    for i in range(len(uppercase_and_space)):
        codigo[uppercase_and_space[i]] = shifted_uppercase_and_space[i]

    for i in range(len(lowercase_and_space)):
        codigo[lowercase_and_space[i]] = shifted_lowercase_and_space[i]

    return codigo

print(build_coder(10))

def best_guess(wordList,text):

    ## tenta descobrir qual o numero de shifts foram dados em uma mensagem criptografada

    max_num_real_words = 0
    best_guess= 0

    for shift in range(53):

        shifted_text = app_shift(text,shift)

        potencial_words = shifted_text.split()
        num_real_words=0

        for word in potencial_words:


            if word in wordList:

                num_real_words+=1

            if num_real_words > max_num_real_words:

                max_num_real_words = num_real_words
                best_shift = shift

    return best_shift



def app_cod(texto,codigo):

    #Aplica a tabela de conversão, tanto para criptografar quanto para descriptografar

    cod_text = ''   

    for letra in str(texto):
       

        if letra in codigo:

            cod_text += codigo[letra]


        else:

            cod_text+= letra

    return cod_text

         
text1=['O mundo é tudo que é o caso']   


def app_shift(text, shift):

    return app_cod(text, build_coder(shift))

def app_decrypt(crypt):

    best_shift = best_guess(wordList, crypt)

    return app_shift(crypt, best_shift)

print(app_shift('O mundo é tudo que é o caso',24))

crypt = app_shift('O mundo é tudo que é o caso',24)

best = best_guess(wordList, crypt)

print(app_decrypt(crypt))


def app_multi_shift(text,nuplas):

    cod_tex = text
    
    i=0

    for par in nuplas:

        n_1 = nuplas[i][0]
        n_2 = nuplas[i][1]

        cod_tex = cod_tex[:n_1] + app_shift(cod_tex[n_1:],n_2)

        i+=1

    return cod_tex

print(app_multi_shift("O mundo e tudo que e o caso", [(0,6), (3, 18),
(12, 16)]))

a = app_multi_shift("O mundo e tudo que e o caso", [(0,6), (3, 18),
(12, 16)])
b = app_decrypt(a)
print(b)





