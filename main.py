from database import Database
from modelo import Maquinario, Operador

db_maq = Database(database="projeto", collection="maquinarios")
db_op = Database(database="projeto", collection="operadores")
maquinario = Maquinario(db=db_maq)
operador = Operador(db=db_op)

def create_maq():
    print("Um maquinário será criado!")
    marca = input("Qual a marca do maquinário? ")
    modelo = input("Qual é o modelo do maquinário? ")
    ano = int(input("Qual o ano de fabricação do maquinário? "))
    status = input("Qual o status do maquinário? ")
    maquinario.create_maq(marca, modelo, ano, status)
    print("Maquinário criado!")

def read_maq_by_id():
    maq_id = input("Entre com o ID do maquinário que deseja buscar: ")
    maquinario.read_maq_by_id(maq_id)

def update_maq():
    print("Um maquinário será atualizado!")
    maq_id = input("Qual o ID do maquinário que você deseja atualizar? ")
    marca = input("Qual a nova marca do maquinário? ")
    modelo = input("Qual é o novo modelo do maquinário? ")
    ano = int(input("Qual o novo ano de fabricação do maquinário? "))
    status = input("Qual o novo status do maquinário? ")
    maquinario.update_maq(maq_id, marca, modelo, ano, status)
    print("Atualização feita com sucesso!")

def delete_maq():
    maq_id = input("Qual o ID do maquinário que você deseja deletar? ")
    maquinario.delete_maq(maq_id)

def create_op():
    name = input("Entre com o nome do operador: ")
    operador.create_op(name)

def read_op():
    name = input("Entre com o nome do operador: ")
    operador.read_op(name)

def update_op():
    name = input("Entre com o nome do operador: ")
    new_maq = input("Entre com o ID do novo maquinário: ")
    operador.update_op(name, new_maq)

def delete_op():
    name = input("Entre com o nome do operador: ")
    operador.delete_op(name)

def add_op_to_maq():
    maq_id = input("Entre com o ID do maquinário: ")
    op_id = input("Entre com o ID do operador: ")
    maquinario.add_operator(maq_id, op_id)

def remove_op_from_maq():
    maq_id = input("Entre com o ID do maquinário: ")
    maquinario.remove_operator(maq_id)

def main_menu():
    while True:
        print("\nEntre com uma opção:")
        print("1. Criar maquinário")
        print("2. Buscar maquinário pelo ID")
        print("3. Atualizar maquinário")
        print("4. Apagar maquinário")
        print("5. Criar operador")
        print("6. Buscar operador pelo nome")
        print("7. Atualizar operador")
        print("8. Apagar operador")
        print("9. Adicionar operador a um maquinário")
        print("10. Remover operador de um maquinário")
        print("11. Sair")

        op = input("\nDigite o número referente à opção escolhida: ")

        if op == '1':
            create_maq()
        elif op == '2':
            read_maq_by_id()
        elif op == '3':
            update_maq()
        elif op == '4':
            delete_maq()
        elif op == '5':
            create_op()
        elif op == '6':
            read_op()
        elif op == '7':
            update_op()
        elif op == '8':
            delete_op()
        elif op == '9':
            add_op_to_maq()
        elif op == '10':
            remove_op_from_maq()
        elif op == '11':
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main_menu()
