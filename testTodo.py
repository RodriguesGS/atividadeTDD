import unittest
from todoList import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_adicionar_tarefa(self):
        self.todo.adicionar("Estudar", "Estudar TDD em Python")
        self.assertEqual(len(self.todo.tarefas), 1)
        self.assertEqual(self.todo.tarefas[0]["nome"], "Estudar")
        self.assertEqual(self.todo.tarefas[0]["descricao"], "Estudar TDD em Python")
        self.assertEqual(self.todo.tarefas[0]["status"], "pendente")

    def test_marcar_como_concluida(self):
        self.todo.adicionar("Ler", "Ler um livro")
        self.todo.alterar_status(0, "concluída")
        self.assertEqual(self.todo.tarefas[0]["status"], "concluída")

    def test_marcar_como_andamento(self):
        self.todo.adicionar("Treinar", "Ir para academia")
        self.todo.alterar_status(0, "em andamento")
        self.assertEqual(self.todo.tarefas[0]["status"], "em andamento")

    def test_editar_tarefa(self):
        self.todo.adicionar("Dormir", "Dormir cedo")
        self.todo.editar(0, "Dormir muito", "Dormir cedo e bem")
        self.assertEqual(self.todo.tarefas[0]["nome"], "Dormir muito")
        self.assertEqual(self.todo.tarefas[0]["descricao"], "Dormir cedo e bem")

    def test_excluir_tarefa(self):
        self.todo.adicionar("Jogar", "Jogar videogame")
        self.todo.excluir(0)
        self.assertEqual(len(self.todo.tarefas), 0)

    def test_listar_tarefas_vazia(self):
        self.assertEqual(len(self.todo.tarefas), 0)

    def test_adicionar_tarefas_lista(self):
        self.todo.adicionar("Estudar", "Estudar programação")
        self.todo.adicionar("Treinar", "Treinar musculação")
        self.assertEqual(len(self.todo.tarefas), 2)
        self.assertEqual(self.todo.tarefas[0]["nome"], "Estudar")
        self.assertEqual(self.todo.tarefas[1]["nome"], "Treinar")

if __name__ == "__main__":
    unittest.main()
