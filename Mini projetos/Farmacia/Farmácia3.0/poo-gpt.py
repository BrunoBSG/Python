import mysql.connector
import os
import time


# ==========================
# CLASSE BANCO DE DADOS
# ==========================
class BancoDeDados:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1310",
            database="farmacia"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def buscar_todos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def atualizar_quantidade(self, id_produto, nova_quantidade):
        sql = "UPDATE produtos SET quantidade = %s WHERE id_produto = %s"
        self.cursor.execute(sql, (nova_quantidade, id_produto))
        self.conn.commit()

    def inserir_produto(self, nome, quantidade, preco):
        sql = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, quantidade, preco))
        self.conn.commit()

    def remover_produto(self, id_produto):
        sql = "DELETE FROM produtos WHERE id_produto = %s"
        self.cursor.execute(sql, (id_produto,))
        self.conn.commit()


# ==========================
# CLASSE FARMÁCIA
# ==========================
class Farmacia:
    def __init__(self, banco):
        self.banco = banco

    def listar_produtos(self):
        produtos = self.banco.buscar_todos()
        print("\nLista de Produtos\n-----------------")
        if not produtos:
            print("Nenhum produto cadastrado.")
        for p in produtos:
            print(f"{p['id_produto']} - {p['nome']} (Qtd: {p['quantidade']})")

    def pesquisar_produto(self, nome):
        produtos = self.banco.buscar_todos()
        for p in produtos:
            if nome.lower() == p["nome"].lower():
                if p["quantidade"] > 0:
                    print(f"Produto em estoque. Quantidade: {p['quantidade']}")
                else:
                    print("Produto sem estoque.")
                return
        print("Produto não encontrado.")

    def adicionar_estoque(self, id_produto, quantidade):
        produtos = self.banco.buscar_todos()
        for p in produtos:
            if p["id_produto"] == id_produto:
                nova_qtd = p["quantidade"] + quantidade
                self.banco.atualizar_quantidade(id_produto, nova_qtd)
                print("Estoque atualizado com sucesso!")
                return
        print("Produto não encontrado.")

    def remover_estoque(self, id_produto, quantidade):
        produtos = self.banco.buscar_todos()
        for p in produtos:
            if p["id_produto"] == id_produto:
                if quantidade <= p["quantidade"]:
                    nova_qtd = p["quantidade"] - quantidade
                    self.banco.atualizar_quantidade(id_produto, nova_qtd)
                    print("Estoque removido com sucesso!")
                else:
                    print("Quantidade insuficiente.")
                return
        print("Produto não encontrado.")

    def comprar(self):
        produtos = self.banco.buscar_todos()
        valor_total = 0

        while True:
            print("\n# COMPRA")
            for p in produtos:
                print(f"{p['id_produto']} - {p['nome']} (Qtd: {p['quantidade']})")

            opcao = input("Digite o ID do produto ou 's' para sair: ")

            if opcao.lower() == "s":
                break

            try:
                id_produto = int(opcao)
                quantidade = int(input("Quantidade: "))

                for p in produtos:
                    if p["id_produto"] == id_produto:
                        if quantidade <= p["quantidade"]:
                            novo_estoque = p["quantidade"] - quantidade
                            self.banco.atualizar_quantidade(id_produto, novo_estoque)
                            valor_total += p["preco"] * quantidade
                            print("Produto adicionado à compra.")
                        else:
                            print("Estoque insuficiente.")
                        break
                else:
                    print("Produto não encontrado.")

            except ValueError:
                print("Entrada inválida.")

        print(f"\nValor total da compra: R$ {valor_total:.2f}")

    def adicionar_produto(self):
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        self.banco.inserir_produto(nome, quantidade, preco)
        print("Produto cadastrado com sucesso!")

    def remover_produto(self):
        id_produto = int(input("ID do produto a remover: "))
        self.banco.remover_produto(id_produto)
        print("Produto removido com sucesso!")


# ==========================
# CLASSE SISTEMA (MENU)
# ==========================
class Sistema:
    def __init__(self):
        self.banco = BancoDeDados()
        self.farmacia = Farmacia(self.banco)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def iniciar(self):
        while True:
            self.limpar_tela()
            print("""
1 - Pesquisar Produto
2 - Ver Todos
3 - Comprar
4 - Adicionar Estoque
5 - Remover Estoque
6 - Adicionar Produto
7 - Remover Produto
8 - Sair
""")

            try:
                opcao = int(input("Escolha: "))

                match opcao:
                    case 1:
                        nome = input("Nome do produto: ")
                        self.farmacia.pesquisar_produto(nome)
                    case 2:
                        self.farmacia.listar_produtos()
                    case 3:
                        self.farmacia.comprar()
                    case 4:
                        idp = int(input("ID: "))
                        qtd = int(input("Quantidade: "))
                        self.farmacia.adicionar_estoque(idp, qtd)
                    case 5:
                        idp = int(input("ID: "))
                        qtd = int(input("Quantidade: "))
                        self.farmacia.remover_estoque(idp, qtd)
                    case 6:
                        self.farmacia.adicionar_produto()
                    case 7:
                        self.farmacia.remover_produto()
                    case 8:
                        print("Programa Finalizado")
                        time.sleep(2)
                        break
                    case _:
                        print("Opção inválida")

                input("\nPressione ENTER para continuar...")

            except ValueError:
                print("Digite apenas números.")
                time.sleep(2)


# ==========================
# EXECUÇÃO
# ==========================
if __name__ == "__main__":
    sistema = Sistema()
    sistema.iniciar()