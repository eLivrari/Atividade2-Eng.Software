# Exemplo de uso do sistema (sem digitar nada no terminal)
from monitoria import SistemaMonitoria

sistema = SistemaMonitoria()

# o monitor cadastra os horarios
sistema.cadastrar_horario(1, "Cálculo", "Ana", 1, "Segunda", "14:00")
sistema.cadastrar_horario(2, "Cálculo", "Ana", 1, "Segunda", "14:30")
sistema.cadastrar_horario(3, "POO", "Carlos", 1, "Terça", "10:00")

print("Horários livres de Cálculo:")
for h in sistema.listar_horarios_livres("Cálculo"):
    print(" -", h.id_horario, h.dia, h.hora, "monitor:", h.monitor)

# o aluno faz a reserva
sistema.reservar_horario(1, "12345", "Derivadas")
print("Reserva feita no horário 1")

# outro aluno tenta pegar o mesmo horario
try:
    sistema.reservar_horario(1, "99999", "Integrais")
except ValueError as erro:
    print("Erro:", erro)

print("Horários livres de Cálculo depois da reserva:")
for h in sistema.listar_horarios_livres("Cálculo"):
    print(" -", h.id_horario, h.dia, h.hora, "monitor:", h.monitor)
