"""
Algoritmo responsavel pelo controle das questões e uso das funções criadas

"""

import DataHora
import CPF
import Nome 
import NumeroReal
import senha
import Email
import telefone

import casalTipo1 
import casalTipo2
import casalTipo3
import casalTipo4 
import casalTipo5 
import casalTipo6 
import casalTipo7 

dec = int(input('Informe a questão desejada ( 1 -> 1º Questão | 2 -> 2º Questão ): '))

if dec == 1 or dec == 2:

    if dec == 1:

        print('''

            Funções da primeira questão:

            Escolha algum dos valores que representa a questão desejada:

            1 -> Nome, nome do meio e Sobrenome
            2 -> E-mail
            3 -> Senha
            4 -> CPF
            5 -> Telefone
            6 -> Data e horário
            7 -> Número real ou com sinal
         
        ''')

        while True: 
            valQuest = int(input('Digite o valor da questão desejada:'))
            
            if valQuest > 0 and valQuest < 8:

                if valQuest == 1: #Nome
                    Nome.validaTestes()

                elif valQuest == 2: #Email
                    Email .validaTestesSenha()

                elif valQuest == 3: #Senha
                    senha.validaTestesSenha()

                elif valQuest == 4: #CPF
                    CPF.validaTestesCPF()

                elif valQuest == 5: #Telefone
                    telefone.validaTestesTelefone()

                elif valQuest == 6: #Data e Hora
                    DataHora.validaTestesDataHora()

                elif valQuest == 7: #Numero real 
                    NumeroReal.validaTestesNumReal()

                break
            else:
                print('Valor Invalido, Tente novamente.')
        
    else:
        print('''

            Funções da segunda questão:

            Escolha algum dos valores que representa a questão desejada:

            1 -> Casal tipo 1
            2 -> Casal tipo 2
            3 -> Casal tipo 3
            4 -> Casal tipo 4
            5 -> Casal tipo 5
            6 -> Casal tipo 6
            7 -> Casal tipo 7
         
        ''')

        while True: 
            valQuest = int(input('Digite o valor da questão desejada:'))
            
            if valQuest > 0 and valQuest < 8:

                if valQuest == 1: #Casal Tipo 1
                    casalTipo1.geraFamiliaTesteTipo1()

                elif valQuest == 2: #Casal Tipo 1
                    casalTipo2.geraFamiliaTesteTipo2()

                elif valQuest == 3: #Casal Tipo 2
                    casalTipo3.geraFamiliaTesteTipo3()

                elif valQuest == 4: #Casal Tipo 3
                    casalTipo4.geraFamiliaTesteTipo4()

                elif valQuest == 5: #Casal Tipo 4
                    casalTipo5.geraFamiliaTesteTipo5()

                elif valQuest == 6: #Casal Tipo 6
                    casalTipo6.geraFamiliaTesteTipo6()

                elif valQuest == 7: #Casal Tipo 7
                    casalTipo7.geraSentenca()

                break
            else:
                print('Valor Invalido, Tente novamente.')
else:
    print('Valor Invalido, Tente Novamente')