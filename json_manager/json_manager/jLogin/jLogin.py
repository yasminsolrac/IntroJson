from os.path import dirname, realpath, join 
from utils.lib import JsonManager #Importanto a classe JsonManager da biblioteca lib que criamos
from getpass import getpass
from crypt import crypt # Biblioteca para fazer a criptografia da senha

class JLogin(JsonManager): #Herdamdo a classe JsonManager da lib

    def __init__(self): #Já que tiramos o construtor da outra classe, precisamos colocar nessa, para utilizar o realpath
        self.path = dirname(realpath(__file__))
        self.path_data = join(self.path, 'data/data.json') #Pegar o path da pasta data, o join faz a junção do realpath com o arquivo data

    def sign_in(self):
        # data = JsonManager().read_json(self.path_data) #Para fazer a leitura pegamos a função de leitura da lib (Não vamos utilizar para o método de criação)
        print('#### Sign in ####')
        username = input("Digite seu usuário:")
        password = getpass("Digite sua senha") #Utiliza o getpass pra pegar a senha
        password_verify = getpass("Digite a senha novamente") #Verificar a senha digitada

        while password != password_verify:
            print("As senhas não coincidem")
            password_verify = getpass("Digite a senha novamente")

        JsonManager().create_json(self.path_data, username, crypt(password_verify)) # Caso a senha esteja correta, cria o json (chamando a função), o crypt vai criptografar a senha
        print('Registro completo!')

        def main(self): #Método onde será feito os testes
            self.sign_in() #Chamando o método


        #Área de testes:

        if __name__ == '__main__':
            jL = JLogin() #Instância da classe
            jL.main() #Chamando o método main