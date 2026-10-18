# 1. Histórias de usuário

### História 1 - Reserva de horário de monitoria

- **História:** Como aluno, eu quero ver os horários livres de uma disciplina e reservar um atendimento de 30 minutos para garantir minha vaga na monitoria sem dar conflito com outros alunos.
- **Prioridade:** Alta
- **Justificativa:** É a parte principal que a coordenação pediu para acabar com a bagunça de marcar horário por mensagem. No próprio e-mail eles falam que só de a reserva funcionar já resolve o maior problema agora.
- **Trecho do e-mail:** "A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento. Cada atendimento dura 30 minutos. Não precisa resolver tudo de uma vez. Se a reserva de horários funcionar, já ajuda muito."
- **Critérios de aceitação:**
  * Se o horário de 30 minutos estiver livre em uma das disciplinas ofertadas, Cálculo, Física, POO ou Estruturas de Dados, o aluno consegue fazer a reserva informando seu RA/identificação e o assunto da dúvida, mudando o status do horário para ocupado.
  * Se o horário de atendimento individual já estiver ocupado por outro aluno, o sistema deve barrar uma nova reserva para esse mesmo horário e retornar um erro de horário indisponível.
  * O aluno só pode reservar no máximo 2 horários por semana na mesma matéria. Se tentar marcar um terceiro horário na mesma disciplina e semana, o sistema deve bloquear e avisar que o limite semanal foi atingido.
  * Se o aluno tentar reservar horário em uma disciplina que não existe no sistema ou passar os dados em branco, sem identificação ou horário, o sistema não faz o agendamento e retorna erro de dados inválidos.

---

### História 2 - Cadastro e cancelamento de horários pelo monitor

- **História:** Como monitor, eu quero cadastrar meus horários de atendimento do semestre e poder cancelar um dia específico quando eu tiver prova para que os alunos sejam avisados antes de irem até a sala à toa.
- **Prioridade:** Alta
- **Justificativa:** Sem os horários dos monitores cadastrados não tem como o aluno reservar nada, e o aviso de cancelamento resolve a reclamação recorrente dos alunos que dão viagem perdida.
- **Trecho do e-mail:** "No início do semestre, cada monitor informa os horários em que pode atender, mas às vezes precisa cancelar por causa de prova. Os alunos reclamam que só descobrem o cancelamento quando chegam na sala."
- **Critérios de aceitação:**
  * O monitor consegue cadastrar seus horários de 30 minutos informando dia, hora, matéria e se o atendimento é individual ou em grupo, deixando o horário com status livre.
  * Quando o monitor cancela um horário que já estava cadastrado, mesmo que já tenha aluno marcado, o status daquele horário muda para cancelado e o sistema registra um aviso para o aluno que tinha reservado.
  * Horários marcados como cancelados pelo monitor não podem aparecer como disponíveis e devem recusar novas tentativas de reserva pelos alunos.

---

### História 3 - Relatório mensal de horas dos monitores

- **História:** Como membro da coordenação, eu quero gerar um relatório mensal com o total de horas que cada monitor trabalhou para fazer o controle do pagamento das bolsas.
- **Prioridade:** Média
- **Justificativa:** É necessário para a coordenação fechar o pagamento do mês, mas depende que os atendimentos já estejam acontecendo no sistema para ter o que somar.
- **Trecho do e-mail:** "A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo."
- **Critérios de aceitação:**
  * Ao informar o mês desejado, o sistema soma todos os atendimentos de 30 minutos realizados por cada monitor naquele período e mostra o total em horas.
  * Apenas usuários do tipo coordenação podem gerar esse relatório. Se um aluno ou monitor tentar acessar essa função, o sistema bloqueia e retorna erro de permissão.
  * Horários que o monitor cancelou ou em que o aluno levou falta não entram na conta de horas trabalhadas do relatório.

---

### História 4 - Consulta de assuntos com mais dúvidas

- **História:** Como professor, eu quero ver quais conteúdos tiveram mais agendamentos de monitoria na minha matéria para saber o que a turma está tendo mais dificuldade e revisar em aula.
- **Prioridade:** Baixa
- **Justificativa:** Ajuda o professor a planejar as aulas, mas não é urgente para o funcionamento básico dos agendamentos e só faz sentido depois que vários alunos já tiverem usado o sistema.
- **Trecho do e-mail:** "Os professores das disciplinas gostariam de saber quais conteúdos geram mais dúvidas, para reforçar em aula."
- **Critérios de aceitação:**
  * Quando o professor consulta sua matéria, o sistema retorna uma lista dos assuntos preenchidos pelos alunos nas reservas, ordenada do tema mais repetido para o menos repetido.
  * A busca deve filtrar apenas os registros da disciplina escolhida pelo professor, sem misturar dúvidas de outras matérias.
  * Se a matéria ainda não tiver nenhuma reserva feita, o sistema retorna uma lista vazia informando que ainda não há registros.

---

### História 5 - Registro de presença e faltas dos alunos

- **História:** Como monitor, eu quero marcar se o aluno apareceu ou faltou na monitoria agendada para ter controle de quem reserva horário e não vai.
- **Prioridade:** Baixa
- **Justificativa:** Ajuda a controlar os horários perdidos, mas como os próprios monitores ainda não decidiram se vão bloquear quem falta ou não, fica com prioridade menor que o agendamento em si.
- **Trecho do e-mail:** "Também tem o problema das faltas. Quando o aluno reserva e não aparece, o horário fica perdido. Alguns monitores sugeriram bloquear quem falta muito, mas outros acham isso exagerado."
- **Critérios de aceitação:**
  * O monitor consegue marcar "presente" ou "falta" em um atendimento agendado, e o sistema soma +1 no histórico de faltas do aluno caso ele não tenha ido.
  * Se o aluno acumular 3 faltas no semestre, o sistema mostra um aviso de histórico de faltas para o monitor quando esse aluno fizer uma nova reserva, mas sem bloquear o agendamento por enquanto.
  * O sistema não deixa lançar presença ou falta em horários que estavam livres, sem ninguém marcado, ou que foram cancelados pelo monitor.