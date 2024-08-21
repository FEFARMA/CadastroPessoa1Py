# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2 - Lista Pessoa Fisica / 3 - Sair
# 1 - Cadastrar Pessoa Juridica/ 2 - Lista Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input("Escolha um opcao: 1 - Pessoa Fisica / 2 - Pessoa Juridica /3 - Remover CPF da lista - 4 - Atualizar item da lista - 0 - Sair"))
        if opcao == 1:
            while True:
                opcaopf =int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Voltar ao menu anterior"))

                # Cadastrar uma Pessoa Fisica
                if opcaopf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica")
                    novapf.cpf = input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros):"))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ") # Solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue # Retornar ao inicio do loop

                    # Cadastro de Endereco
                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o numero")
                    end_comercial = input("Este endereco e comercial? S/N ")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso !!")

                # Listar Pessoa Fisica
                elif opcaopf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome} ")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%y')}")
                            print(f"Imposto a ser pago: R$: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista vazia")

                elif opcaopf == 3:
                    cpf_para_remover = input("Digite o cpf da pessoa fisica que deseja remover: ")


                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_remover:
                         lista_pf.remove(cada_pf)
                         pessoa_encontrada = True
                         print(" Pessoa fisica removida! ")

                         break

                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada ")

                # Atualizar Lista Pessoa Fisica
                elif opcaopf == 4:
                    cpf_para_atualizar = input("Digite o CPF que deseja atualizar ")
                    pessoa_encontrada = False

                    for cada_cpf in lista_pf:
                        if cada_pf.cpf == cpf_para_atualizar:
                            pessoa_encontrada = True

                            print("Escolha qual dado deseja atualizar ")
                            print("N - Nome ")
                            print("R - Rendimento ")
                            print("L - Logradouro ")
                            print("M - Numero do Endereco ")

                            escolha = input("Digite a inicial do atributo que deseja alterar ").strip().upper()

                            if escolha == 'N':
                                novo_nome = input(f"O nome atual e  {cada_pf.nome}. Digite o novo nome para atualizar ")
                                cada_pf.nome = novo_nome
                            elif escolha  == 'R':
                                novo_rendimento = input(f"O rendimento atual e {cada_pf.rendimento}. Digite o novo valor de rendimento ")
                                cada_pf.rendimento = novo_rendimento
                            elif escolha == 'L':
                                novo_logradouro = input(f"O logradouro atual e {cada_pf.logradouro}. Digite o novo logradouro ")
                                cada_pf.logradouro = novo_logradouro
                            elif escolha == 'M':
                                novo_numero = input(f"O numero do endereco atual e {cada_pf.numero}. Digite um novo numero para atualizar ")
                                cada_pf.numero = novo_numero
                            else:
                                print("Opcao invalida ")

                                       
                 # SAIR DO MENU ATUAL
                elif opcaopf == 0:
                    print("Voltando ao menu anterior ")
                    break
                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas ")

        elif opcao == 2:
           
            while True:
                opcaopj = opcaopj =int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Remover Pessoa Juridia - 4 - Atulizar item da lista - 0 - Voltar ao menu anterior "))
            # Repetir o menu
            # Opcao _pj == 1 / opcao_pj == 2
                
                if opcaopj == 1:
                        novapj = PessoaJuridica()
                        novo_end_pj = Endereco()

                        novapj.nome = input("Digite o nome da empresa ")
                        novapj.cnpj = input("Digite o CNPJ da empresa ")
                        novapj.rendimento = float(input("Digite o rendimento da empresa (Digite somente numeros): "))

                        # Cadastro de Endereco
                        novo_end_pj.logradouro = input("Digite o endereco: ")
                        novo_end_pj.numero = input("Digite o numero: ")
                        end_comercial = input("Este endereco e comercial? S/N ")
                        novo_end_pj.endereco_Comercial = end_comercial.strip().upper() == 'S'

                        novapj.endereco = novo_end_pj

                        lista_pj.append(novapj)
                        print("Cadastro realizado com sucesso !! ")

                # Listar Pessoa Juridica
                elif opcaopj == 2:
                    if lista_pj:
                        if lista_pj:
                            for cada_pj in lista_pj:
                                print(f"Nome: {cada_pj.nome} ")
                                print(f"CNPJ: {cada_pj.cnpj} ")
                                print(f"Endereco: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero} ")
                                print(f"Imposto a ser pago: R$: {cada_pj.calcular_imposto(cada_pj.rendimento)} ")
                                print("Digite 0 para voltar ao menu ")
                                input()

                
                # Remover o Cadastro
                elif opcaopj == 3:
                    cnpj_para_remover = input("Digite o CNPJ da pessoa empresa que deseja remover: ")

                    empresa_encontrada = False

                    for cada_pj in lista_pj:
                        
                        if cada_pj.cnpj == cnpj_para_remover:
                            lista_pj.remove(cada_pj)
                            empresa_encontrada = True
                            print(" Cadastro de pessoa juridica excluido com sucesso! ")
                            break

                    if not pessoa_encontrada:
                        print("Nenhuma pessoa com o CNPJ informado foi encontrado! ")
                
                
                              
                # Atualizar Lista Pessoa Fisica
                elif opcaopj == 4:
                    atualizar_item = int(input("Escolha um item para atualizar: 1 - Nome - 2 - CNPJ - 3 - Endereco - 5 - Rendimento "))
                   
                    if atualizar_item == 1:
                        novo_nome = input("Digite o novo nomeç ")
                        novapj.nome = novo_nome

                    elif atualizar_item == 2:
                        nova_cnpj = input("Digite o CNPJ: ")
                        novapf.cnpj = nova_cnpj

                    elif atualizar_item == 3:
                        novo_endereco = input("Digite o novo endereco: ")
                        novapj.endereco = novo_endereco
                        
                    elif atualizar_item == 5:
                        novo_rendimento = float(input("Digite o rendimento mensal (Digite somente numeros):"))

                    
                else:
                    print("Opcao invalida ")
                              
        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema! Valeu! ")
        else:
            print("Opcao invalida, por favor digite uma das opcoes validas! ")
        
if __name__== "__main__":
    main() # Chama a funcao principal
        
    
