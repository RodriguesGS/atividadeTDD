class TodoList:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, nome, descricao):
        self.tarefas.append({"nome": nome, "descricao": descricao, "status": "pendente"})

    def alterar_status(self, indice, novo_status):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["status"] = novo_status
        else:
            print("Índice inválido!")

    def editar(self, indice, novo_nome, nova_descricao):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].update({"nome": novo_nome, "descricao": nova_descricao})
        else:
            print("Índice inválido!")

    def excluir(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
        else:
            print("Índice inválido!")

    def listar(self):
        if self.tarefas:
            print("\n===== LISTA DE TAREFAS =====")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i} - {tarefa['nome']} | {tarefa['descricao']} | Status: {tarefa['status']}")
        else:
            print("\nNenhuma tarefa cadastrada.")


def exibir_menu():
    menu = (
        "\n===== SISTEMA DE TAREFAS =====\n"
        "1 - Adicionar tarefa\n"
        "2 - Listar tarefas\n"
        "3 - Marcar como CONCLUÍDA\n"
        "4 - Marcar como EM ANDAMENTO\n"
        "5 - Editar tarefa\n"
        "6 - Excluir tarefa\n"
        "0 - Sair"
        "================================\n"
    )
    print(menu)
    return input("Escolha uma opção: ")


def main():
    todo = TodoList()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            todo.adicionar(nome, descricao)
            print("Tarefa adicionada!")

        elif opcao == "2":
            todo.listar()

        elif opcao in {"3", "4"}:
            todo.listar()
            status = "concluída" if opcao == "3" else "em andamento"
            indice = int(input(f"Digite o número da tarefa para marcar como {status}: "))
            todo.alterar_status(indice, status)

        elif opcao == "5":
            todo.listar()
            indice = int(input("Digite o número da tarefa para editar: "))
            novo_nome = input("Novo nome: ")
            nova_desc = input("Nova descrição: ")
            todo.editar(indice, novo_nome, nova_desc)

        elif opcao == "6":
            todo.listar()
            indice = int(input("Digite o número da tarefa para excluir: "))
            todo.excluir(indice)
            print("Tarefa excluída!")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
