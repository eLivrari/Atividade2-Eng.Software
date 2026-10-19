# Projeto Inicial - História 1: Reserva de horário de monitoria

O projeto vai implementar apenas a História 1, que tem prioridade Alta. Toda a lógica será feita em classes e métodos chamados direto pelos testes, sem usar leitura de dados pelo terminal.

## Classes e Responsabilidades

**Classe Horario**
Guarda as informações de cada horário de 30 minutos da monitoria: id do horário, disciplina, nome do monitor, semana, dia e hora, se o atendimento é individual ou em grupo e o status atual, que começa como livre e muda para ocupado após a reserva. Também armazena o RA do aluno e o assunto da dúvida quando o agendamento é feito.

**Classe SistemaMonitoria**
Gerencia a lista de horários cadastrados no sistema e faz as validações da reserva através de três métodos principais:

- cadastrar_horario: adiciona um novo horário de 30 minutos na lista do sistema como livre, verificando antes se a matéria informada faz parte das ofertadas pelo curso: Cálculo, Física, POO ou Estruturas de Dados.
- listar_horarios_livres: recebe o nome de uma disciplina e retorna todos os horários dela que estão com status livre no momento.
- reservar_horario: recebe o id do horário, o RA do aluno e o assunto da dúvida para fechar o agendamento. Antes de confirmar, o método checa se nenhum dado veio em branco, se o horário realmente existe e está livre para não dar conflito em atendimento individual, e se o aluno já não atingiu o limite de 2 reservas naquela mesma matéria e semana. Se passar por tudo, muda o status do horário para ocupado e salva os dados do aluno. Se cair em algum impedimento, cancela a operação e levanta uma exceção informando o erro correspondente.

## Testes de Aceitação

Os testes serão feitos na classe TestReservaMonitoria usando a biblioteca unittest, ligando cada critério de aceitação da História 1 aos seguintes métodos de teste:

- Critério 1 - Reserva de horário livre em disciplina válida:
  Será verificado pelo teste test_reservar_horario_livre_sucesso, que cadastra um horário livre em uma matéria válida, faz a reserva com RA e dúvida preenchidos e confere se o status mudou para ocupado.

- Critério 2 - Bloqueio de conflito em horário individual ocupado:
  Será verificado pelo teste test_erro_horario_individual_ja_ocupado, que tenta reservar um horário individual que já foi pego por outro aluno e confere se o sistema barra a operação retornando erro de horário indisponível.

- Critério 3 - Limite de 2 horários por semana na mesma matéria:
  Será verificado pelos testes test_erro_limite_semanal_atingido, que faz duas reservas para o mesmo aluno na mesma matéria e semana e verifica se a terceira tentativa é bloqueada, e test_permitir_reserva_outra_materia_mesma_semana, que garante que o bloqueio não afeta matérias diferentes.

- Critério 4 - Recusa de disciplina inexistente ou dados em branco:
  Será verificado pelos testes test_erro_disciplina_invalida, que tenta usar uma matéria fora das quatro ofertadas, e test_erro_dados_em_branco, que tenta reservar passando o RA ou o assunto vazios, conferindo se ambos retornam erro de dados inválidos.