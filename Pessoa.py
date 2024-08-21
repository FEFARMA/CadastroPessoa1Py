from datetime import date


class Endereco:
    from datetime import date
    def __init__(self, logradouro="", numero="", endereco_Comercial=False):
    # Inicializar os nossos atributos com valores padrao
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

# CLASSE PESSOA
class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = Endereco

    def calcular_imposto(self, rendimento):
        return rendimento
    
# CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
    # Inicializar os atributos que foram herdados e proprios atributis da classe
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
       
        # Se nehum endereco for fornecido, cria um objeto Endereco padrao
        
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
           dataNascimento = date.today()

        if super().__init__(nome, rendimento, endereco):
        
           
        # Atributos da propria classe
            self.cpf = cpf
            self.dataNascimento = dataNascimento
    
    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos ate 1500
        if rendimento <= 1500:
            return 0
        # 2% de Imposto para rendimento entre 1500 e 3500
        elif 1500 < rendimento <= 3500:
            #return(rendimento / 100) * 2
            return rendimento * 0.02
        # 3.5% de imposto para rendimento entre 3500 e 6000
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        # 5% de imposto para rendimentos acima de 6000
        else:
            return rendimento * 5
        
    
# CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    # Inicializar os atributos que foram herdados e proprios atributis da classe
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj=""):

        # Se nehum endereco for fornecido, cria um objeto Endereco padrao

        if endereco is None:
            endereco = Endereco()

        super().__init__(nome, rendimento, endereco)

        # Atributos da propria classe
        self.cnpj = cnpj
    
    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos ate 1500
        if rendimento <= 10500:
            return 0
        # 2% de Imposto para rendimento entre 1500 e 3500
        elif 10500 < rendimento <= 30500:
            #return(rendimento / 100) * 2
            return rendimento * 0.05
        # 3.5% de imposto para rendimento entre 3500 e 6000
        elif 30500 < rendimento <= 60000:
            return (rendimento / 100) * 8
        # 5% de imposto para rendimentos acima de 6000
        else:
            return rendimento * 12
            
    pass


# CLASSE ENDERECO
