import unittest

from monitoria import SistemaMonitoria


class TestReservaMonitoria(unittest.TestCase):

    def setUp(self):
        # roda antes de cada teste: cria um sistema novo com alguns horarios
        self.sistema = SistemaMonitoria()
        self.sistema.cadastrar_horario(1, "Cálculo", "Ana", 1, "Segunda", "14:00")
        self.sistema.cadastrar_horario(2, "Cálculo", "Ana", 1, "Segunda", "14:30")
        self.sistema.cadastrar_horario(3, "Cálculo", "Ana", 1, "Quarta", "10:00")
        self.sistema.cadastrar_horario(4, "Física", "Bruno", 1, "Terça", "09:00")

    # Criterio 1
    def test_reservar_horario_livre_sucesso(self):
        horario = self.sistema.reservar_horario(1, "12345", "Derivadas")

        self.assertEqual(horario.status, "ocupado")
        self.assertIn("12345", horario.alunos)
        self.assertIn("Derivadas", horario.assuntos)

    # Criterio 1 - o horario reservado nao aparece mais como livre
    def test_horario_reservado_sai_da_lista_de_livres(self):
        self.assertEqual(len(self.sistema.listar_horarios_livres("Cálculo")), 3)

        self.sistema.reservar_horario(1, "12345", "Derivadas")

        self.assertEqual(len(self.sistema.listar_horarios_livres("Cálculo")), 2)

    # Criterio 2
    def test_erro_horario_individual_ja_ocupado(self):
        self.sistema.reservar_horario(1, "12345", "Derivadas")

        with self.assertRaises(ValueError) as erro:
            self.sistema.reservar_horario(1, "99999", "Integrais")

        self.assertEqual(str(erro.exception), "Horário indisponível")

    # Criterio 3
    def test_erro_limite_semanal_atingido(self):
        self.sistema.reservar_horario(1, "12345", "Derivadas")
        self.sistema.reservar_horario(2, "12345", "Limites")

        with self.assertRaises(ValueError) as erro:
            self.sistema.reservar_horario(3, "12345", "Integrais")

        self.assertEqual(str(erro.exception), "Limite semanal atingido")

    # Criterio 3
    def test_permitir_reserva_outra_materia_mesma_semana(self):
        self.sistema.reservar_horario(1, "12345", "Derivadas")
        self.sistema.reservar_horario(2, "12345", "Limites")

        horario = self.sistema.reservar_horario(4, "12345", "Cinemática")

        self.assertEqual(horario.status, "ocupado")

    # Criterio 4
    def test_erro_disciplina_invalida(self):
        with self.assertRaises(ValueError) as erro:
            self.sistema.cadastrar_horario(5, "Química", "Carlos", 1, "Sexta", "08:00")
        self.assertIn("Dados inválidos", str(erro.exception))

        with self.assertRaises(ValueError) as erro:
            self.sistema.listar_horarios_livres("Química")
        self.assertIn("Dados inválidos", str(erro.exception))

    # Criterio 4
    def test_erro_dados_em_branco(self):
        with self.assertRaises(ValueError) as erro:
            self.sistema.reservar_horario(1, "", "Derivadas")
        self.assertIn("Dados inválidos", str(erro.exception))

        with self.assertRaises(ValueError) as erro:
            self.sistema.reservar_horario(1, "12345", "")
        self.assertIn("Dados inválidos", str(erro.exception))

        with self.assertRaises(ValueError) as erro:
            self.sistema.reservar_horario(None, "12345", "Derivadas")
        self.assertIn("Dados inválidos", str(erro.exception))

        # o horario continua livre porque nenhuma reserva foi feita
        self.assertEqual(self.sistema.buscar_horario(1).status, "livre")


if __name__ == "__main__":
    unittest.main()
