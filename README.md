# IntroJson
Introdução ao json + python

JSON

Foi criado para salvar ou transportar dados (Dicionário do python)

Como criar?
	Cria uma pasta
	No vscode cria um arquivo dentro dessa pasta .json
	Cria outro arquivo na mesma pasta .py

Podemos ter 6 tipos de dados:
	boolean (true e false)
	numero
	null
	"string"
	[array]
	{Objeto}

Exemplo de json:
	[
		{"name": "Luiz", "lastName": "Miranda"}, # name = chave (As chaves precisam ter nomes diferentes), luiz = valor
		{"name": "Maria", "lastName": "Miranda"},
   		{"name": "Helena", "lastName": "Miranda"}
	]

O exemplo acima é um array com 3 objetos

Podemos aninhar diversos tipos de dados

Nas chaves é obrigatório colocar aspas duplas, assim como em strings

E como podemos criar um json utilizando python?

	Para usar o json com python é necessário importar algumas bibliotecas:
		import json
		import os
	
	Abaixo está o código utlizado para criar um json que possui uma chave e um valor (Login e senha):

from os.path import dirname, realpath, isfile # Importamos o dirname, realpath e isfile da biblioteca os. O realpath Pega o path atual do arquivo, o isfile verifica se o arquivo ja existe
from json import dump # Importamos o dump da biblioteca json. O dump é para escrever


class JsonManager: # Classe utilizada para a criação do json

    def __init__(self): # Construtor
        self.path = dirname(realpath(__file__))  + '/' # Esse __file__ é o proprio arquivo, ou seja, estamos pegando o path atual desse arquivo. O dirname extrai o caminho do diretório, mas remove o último componente do caminho
        
    def create_json(self, file): #Método para criar o arquivo json
        data = {"username": "", "password": ""}  #Informa a estrutura do arquivo json (Quando o json estiver pronto vai mostrar essa estrutura)
        path_data_json = self.path + file 

        if not isfile(path_data_json): # Se esse arquivo não existir:
            with open(path_data_json, 'w') as f: #O w significa escrever
                dump(data, f) #Passa as informações do data para o f e escreve
            return True
        else:
            return False
        
if __name__ == '__main__':
    jmanager = JsonManager()
    jmanager.create_json('data/data.json') #Criando o arquivo dentro da pasta data

A partir desse arquivo criado em python, é gerado um json dentro da pasta data com o nome "data.json":

	{"username": "", "password": ""} --> Conteúdo do arquivo

Podemos também indentar esse arquivo, para melhor visualização, modificando o código:

	dump(data, f, indent=2) # O 2 é modificável e indica o espaço da indentação


Ao modificar o código, precisamos excluir o arquivo json que foi criado para modificá-lo

Após as modificações o arquivo "data.json" ficou da seguinte forma:

	{
  		"username": "",
  		"password": ""
	}

Podemos utilizar também o parâmetro "separators" que faz a separação baseado em caracteres, exemplo:

	dump(data, f, indent=2, separators=(',',': ') #Faz a separação do arquivo a partir dos caracteres "," e ":"

Agora que já sabemos como criar um arquivo json, vamos criar um método para ler esse arquivo

Para isso, adicionamos informações no arquivo json, para podermos lê-las

Agora modificamos o código anterior, adicionando algumas informações para pode fazer a leitura:

def read_json(self, file): # Método para ler um arquivo json
        if isfile(self.path + file):
            with open(self.path + file, 'r') as f: # Não é necessário colocar esse r, pois por padrão o arquivo já abre em modo de leitura
                data = load(f)
            return data
        else:
            return False

#Essa parte é para fazer o teste da criação        
if __name__ == '__main__':
    jmanager = JsonManager()
    jmanager.create_json('data/data.json') # Criando o arquivo dentro da pasta data

#Agora o teste da leitura
    print(jmanager.read_json('data/data.json')) #Com esse print irá mostras as informações do arquivo lido

Resultado das informações mostradas no terminal:

	{'username': 'Yasmin', 'password': '1234'}

Como podemos percorrer cada chave separadamente?

	 print(jmanager.read_json('data/data.json')['username']) # Escreve entre colchetes o nome da chave que queremos ler

Resultado:

	Yasmin

Agora que já sabemos como criar um json, podemos começar a utiliza-lo, para isso vamos fazer algumas modificações no código que havia sido criado anteriormente, para que possamos fazer um sistema simples de login:
	Primeiro criamos 2 novas pastas, dentro da pasta json_manager: jLogin e utils(dentro da jLogin)
	Dentro da utils está o código lib.py (antigo jsonmanager.py)
	Dentro da jLogin está a pasta data e o código jLogin.py

Abaixo está o código de lib.py com as devidas modificações:

from os.path import isfile # Importamos o dirname, realpath e isfile da biblioteca os. O realpath Pega o path atual do arquivo, o isfile verifica se o arquivo ja existe, para a lib não precisamos mais do dirname e do realpath
from json import dump, load # Importamos o dump da biblioteca json. O dump é para escrever


class JsonManager: #Classe utilizada para a criação do json

    #Não necessita de construtor nessa classe
    #def __init__(self): # Construtor
        #self.path = dirname(realpath(__file__))  + '/' # Esse __file__ é o proprio arquivo, ou seja, estamos pegando o path atual desse arquivo. O dirname extrai o caminho do diretório, mas remove o último componente do caminho
        
    def create_json(self, filepath, *args): #Método para criar o arquivo json. O filepath é o arquivo + o path. Com o *args podemos passar n argumentos em nossos métodos
        data = {"username": "", "password": ""}  #Informa a estrutura do arquivo json (Quando o json estiver pronto vai mostrar essa estrutura)

	if args: # Caso tenha args:
            data = {"username": f"{args[0]}", "password": f"{args[1]}"}

        # path_data_json = self.path + file #Remove esta linha

        # if not isfile(path_data_json): # Se esse arquivo não existir: #Remove o isfile, pois não precisa mais verificar se ele existe, já que o método será chamado
        with open(filepath, 'w') as f: # O w significa escrever, f é a variavel que vai receber os dados. Modifica o path_data_json para filepath
            dump(data, f, indent=2) # Passa as informações do data para o f e escreve, o 2 do indent é modificável e indica o espaço da indentação

    def read_json(self, filepath): # Método para ler um arquivo json, altera file para filepath também
        if isfile(filepath): # Altera self.path + file para filepath
            with open(filepath) as f: # Não é necessário colocar esse r, pois por padrão o arquivo já abre em modo de leitura
                data = load(f)
            return data
        else:
            return False
        
    def update_json(self, filepath, data): #Método para fazer updates no json
        with open(filepath, 'w') as f: 
            dump(data, f, indent=2, separators=(',',': '))


#Agora não iremos precisar dessa parte de testes
#Essa parte é para fazer o teste da criação        
#if __name__ == '__main__':
    #jmanager = JsonManager()
    #jmanager.create_json('data/data.json') # Criando o arquivo dentro da pasta data

#Agora o teste da leitura
    #print(jmanager.read_json('data/data.json')['username']) #Com esse print irá mostras as informações do arquivo lido

Agora nós vamos começar a trabalhar no arquivo jLogin.py, que será nosso arquivo principal, abaixo estará o código que será utilizado nele com os devidos comentários:

os.path import dirname, realpath, join 
from utils.lib import JsonManager #Importanto a classe JsonManager da biblioteca lib que criamos
from getpass import getpass

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

        JsonManager().create_json(self.path_data, username, password_verify) # Caso a senha esteja correta, cria o json
        print('Registro completo!')

Para criptografar a senha vamos utilizar a biblioteca crypt, adiciona ao código a linha:

	from crypt import crypt

Além disso, na hora de chamar a função create_json, fazemos da seguinte forma para criptografar a senha:

	JsonManager().create_json(self.path_data, username, crypt(password_verify))

Para usar a biblioteca crypt é necessário instalar um pacote
