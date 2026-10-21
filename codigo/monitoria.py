# Sistema de reserva de horarios de monitoria

DISCIPLINAS = ["Cálculo", "Física", "POO", "Estruturas de Dados"]
LIMITE_POR_SEMANA = 2


class Horario:
    def __init__(self, id_horario, disciplina, monitor, semana, dia, hora, individual):
        self.id_horario = id_horario
        self.disciplina = disciplina
        self.monitor = monitor
        self.semana = semana
        self.dia = dia
        self.hora = hora
        self.individual = individual  # True = individual, False= em grupo
        self.status = "livre"
        # listas com os alunos que reservaram (no grupo pode ter mais de um)
        self.alunos = []
        self.assuntos = []


class SistemaMonitoria:
    def __init__(self):
        self.horarios = []

    def cadastrar_horario(self, id_horario, disciplina, monitor, semana, dia, hora, individual=True):
        if disciplina not in DISCIPLINAS:
            raise ValueError("Dados inválidos: disciplina não existe")

        horario = Horario(id_horario, disciplina, monitor, semana, dia, hora, individual)
        self.horarios.append(horario)
        return horario

    def buscar_horario(self, id_horario):
        for horario in self.horarios:
            if horario.id_horario == id_horario:
                return horario
        return None

    def listar_horarios_livres(self, disciplina):
        if disciplina not in DISCIPLINAS:
            raise ValueError("Dados inválidos: disciplina não existe")

        livres = []
        for horario in self.horarios:
            if horario.disciplina == disciplina and horario.status == "livre":
                livres.append(horario)
        return livres

    def contar_reservas(self, ra, disciplina, semana):
        total = 0
        for horario in self.horarios:
            if horario.disciplina == disciplina and horario.semana == semana:
                if ra in horario.alunos:
                    total = total + 1
        return total

    def reservar_horario(self, id_horario, ra, assunto):
        # 1. nenhum dado pode vir em branco
        if not id_horario or not ra or not assunto:
            raise ValueError("Dados inválidos: preencha todos os campos")

        # 2. o horario precisa existir
        horario = self.buscar_horario(id_horario)
        if horario is None:
            raise ValueError("Dados inválidos: horário não existe")

        # 3. horario individual ja ocupado nao pode ser reservado de novo
        if horario.individual and horario.status == "ocupado":
            raise ValueError("Horário indisponível")

        # 4. no maximo 2 reservas por semana na mesma disciplina
        if self.contar_reservas(ra, horario.disciplina, horario.semana) >= LIMITE_POR_SEMANA:
            raise ValueError("Limite semanal atingido")

        # tudo certo: faz a reserva
        horario.status = "ocupado"
        horario.alunos.append(ra)
        horario.assuntos.append(assunto)
        return horario
