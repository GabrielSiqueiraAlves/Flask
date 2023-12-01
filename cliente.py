from flask_restful import Resource, reqparse

clientes = [
            {
             'cliente_id': '1',
             'nome': 'Gabriel',
             'Email': 'galvesiqueira@outlook.com',
             'Senha': 'camposhumana',
             'Cidade': 'São José dos Campos',
             'Estado': 'São Paulo'
            },
            {
             'cliente_id': '2',
             'nome': 'Fernanda',
             'Email': 'fernada@outlook.com',
             'Senha': 'camposhumana2222',
             'Cidade': 'Rio de Janeiro',
             'Estado': 'Rio de Janeiro'
            },
]

class ClientesModel:
    def __init__(self, cliente_id, nome, Email, Senha, Cidade, Estado):
         self.cliente_id = cliente_id,
         self.nome = nome,
         self.Email = Email
         self.Senha = Senha
         self.Cidade = Cidade
         self.Estado = Estado

    def json(self):
         return {
              'cliente_id': self.cliente_id,
              'nome': self.nome,
              'Email': self.Email,
              'Senha': self.Senha,
              'Cidade': self.Cidade,
              'Estado': self.Estado
         }



class Clientes(Resource):
    def get(self):
        return {'clientes': clientes}


class Cliente(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('Email')
    argumentos.add_argument('Senha')
    argumentos.add_argument('Cidade')
    argumentos.add_argument('Estado')

    def find_clientes(cliente_id):
        for cliente in clientes:
                if cliente['cliente_id'] == cliente_id:
                    return cliente
        return None
   

    def get(self, cliente_id):
            cliente = Cliente.find_clientes(cliente_id)
            if cliente:
                return clientes
            return{'message': 'Cliente not found.'}, 404  
      

    def post(self, cliente_id):
            dados = Cliente.argumentos.parse_args()
            cliente_objeto = ClientesModel(cliente_id, **dados)
            novo_cliente = cliente_objeto.json()
            clientes.append(novo_cliente)
            return novo_cliente, 201 #criado
    
    def put(self, cliente_id):
 
            dados = Cliente.argumentos.parse_args()

            cliente_objeto = ClientesModel(cliente_id, **dados)

            novo_cliente = cliente_objeto.json()   

            cliente = Cliente.find_clientes(cliente_id)

            if cliente:
                cliente.update(novo_cliente)
                return cliente, 200
            else:
                clientes.append(novo_cliente)    
                return novo_cliente, 201 # criado
                 
    def delete(self, cliente_id):
        global clientes
        clientes = [cliente for cliente in clientes if cliente['cliente_id'] != cliente_id]
        return{'message': 'Cliente Deletado'}
