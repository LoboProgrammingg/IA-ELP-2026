# Estrutura dados IA - Riscos_Operacionais_2024

## UNIDADE: [R.ASSCOM.01]

### Indicador

**Descrição Do Risco:** Material jornalístico ou publicitário divulgado na mídia (imprensa e redes sociais) que possa prejudicar a reputação da instituição, seus diretores, gestores e colaboradores.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Revisão de todas matérias para publicação
**Quem:** Unidade de Comunicação e Marketing  / Diretoria
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para criar bom relacionamento com a imprensa e mitigar possíveis danos a imagem institucional
**Como:** 1 – Monitoramento dos principais veículos de imprensa de Mato Grosso;
2 – Rotina de envio de releases e oferecimento de pautas sobre as ações da MTI à imprensa;
3 – Realizar Midia Training com os principais porta-vozes da instituição;
4 – Monitoramento dos riscos de crise institucional junto a Direx ou Comitê de Crise;

**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** ASSCOM
**Situação Geral:** 100,00%
**Número De Ações:** 2.0
**Quantidade De Eventos De Riscos:** 2.0

## UNIDADE: [R.ASSCOM.02]

### Indicador

**Descrição Do Risco:** Agir em desconformidade com a Lei Geral de Proteção de Dados (LGPD) e expor dados sensíveis ou sofrer com possíveis vazamentos de dados.
**Categoria Do Risco:** CONFORMIDADE
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** SIM
**O Que:**    Transparência
**Quem:** Unidade de Comunicação e Marketing / Unidade Jurídica
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para que as informações disponibilizadas estejam conforme os padrões
**Como:** 1 – Monitoramento dos sites institucionais, redes sociais e veículos de comunicação ligados a MTI;
2 – Participar de Capacitação junto a CGE, Ouvidoria e Unidade Jurídica da MTI;
3 – Submeter à Unidade Jurídica da MTI qualquer solicitação que possa ferir a LGPD;

**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** ASSCOM

## UNIDADE: [R.DTIC.01]

### Indicador

**Descrição Do Risco:** Indisponibilidade do MT LOGIN
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** O MT LOGIN deve estar disponível 24x7 com uma disponibilidade superior a 99%
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** GCP
**Por Que:** Garantir maior disponibilidade e estabilidade na aplicação
**Como:** Migrando para Nuvem GCP
**Início:** 01/06/2024
**Fim:** 01/09/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 20,00%
**Observações:** Ações e Resultados

Criar monitoramento 24x7 da aplicação com equipe dedicada - Painel diário com Relatório semanal [contrato rw3]
DNS em nuvem (gcp)
Redundância Total de ambiente para alta disponibilidade
Atualização do Keycloack
Refatoração do ambiente para dev, homol, integração e prod
Atualização conceitual para deixar focado em autenticar usuário
Migração de base de dados para Postgres com cobertura contratual da RW3
Migrar notamt para utilizar o mt login da forma correta
Criar plano de ação para ajustar aplicações do governo digital que estão em produção e novas
Recriar indicadores e medidores próprios, incluindo disponibilidade de status na plataforma de clientes
Monitoramento de segurança e painel diário com relatório mensal de incidentes de segurança
Esteira de Código Seguro
Esteira de Testes (unitário, e2e, integração)
Atendimento nível 1 para o usuário do MT Login (mapear ambientes de integração e produção)
**Ug:** DTIC
**Situação Geral:** 17,50%
**Número De Ações:** 5.0
**Quantidade De Eventos De Riscos:** 5.0

## UNIDADE: [R.DTIC.02]

### Indicador

**Descrição Do Risco:** Indisponibilidade do MT ID
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** O MT ID deve estar disponível 24x7 com uma disponibilidade superior a 99%
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** OPENSHIFT
**Por Que:** Garantir maior disponibilidade e estabilidade na aplicação
**Como:** Atualizando ambiente openshift
Atualizando aplicação, estruturando documentação, criando time dedicado, ajustando contrato de sustentação
**Início:** 01/06/2024
**Fim:** 30/12/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 20,00%
**Observações:** Ações e Resultados


Redundância total de ambiente para alta disponibilidade
Criar monitoramento da aplicação 24x7 com equipe dedicada - Painel diário com relatório mensal [contrato da rw3]
Criar plano de ação para permitir a integração com sistemas do governo de forma facilitada [Instrução normativa??]
Repositório de documentação (principalmente legal) atualizada (ferramental)
Site público para integração de todos os sistemas, explicando como que isso é feito
Recriar indicadores e medidores próprios, incluindo disponibilidade de status na plataforma de clientes
Monitoramento de segurança e painel diário com relatório mensal de incidentes de segurança
Atendimento nível 1 para o usuário do MT ID (mapear ambientes de integração e produção)
Esteira de Código Seguro
**Ug:** DTIC

## UNIDADE: [R.DTIC.03]

### Indicador

**Descrição Do Risco:** Indisponibilidade do Portal de Serviços de MT
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** O Portal de Serviços de MT deve estar disponível 24x7 com uma disponibilidade superior a 99%
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** GCP
**Por Que:** Garantir maior disponibilidade e estabilidade na aplicação
**Início:** 01/06/2024
**Fim:** 01/06/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 20,00%
**Observações:** Ações e Resultados

Redundância total de ambiente para alta disponibilidade
Load Balance (gcp) e demais componentes  -- estudar diferentes regiões geográficas incluindo datacenter cuiaba
Criar monitoramento da aplicação 24x7 com equipe dedicada - Painel diário com relatório mensal
Recriar indicadores e medidores próprios, incluindo disponibilidade de status na plataforma de clientes
Monitoramento de segurança e painel diário com relatório mensal de incidentes de segurança
Nova versão ---- mais robusta e segura do portal
Esteira de Código Seguro
**Ug:** DTIC

## UNIDADE: [R.DTIC.04]

### Indicador

**Descrição Do Risco:** Indisponibilidade dos Portais de Comunicação de MT
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Os portais de comunicação do Estado de MT devem estar disponíveis 24x7 com uma disponibilidade superior a 99%
**Quem:** UGSDG
**Início:** 01/04/2025
**Fim:** 30/12/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 10,00%
**Observações:** Ações e Resultados

Redundância total de ambiente para alta disponibilidade
Criar monitoramento da aplicação 24x7 com equipe dedicada - Painel diário com relatório mensal
-- Criar plano de ação para deixar o ambiente em nuvem com alta disponibilidade
-- Criar plano de ação para nuvem liferay 
-- Criar plano de ação outra alternativa tecnologica para substituição
Recriar indicadores e medidores próprios, incluindo disponibilidade de status na plataforma de clientes
Monitoramento de segurança e painel diário com relatório mensal de incidentes de segurança
Esteira de Código Seguro
**Ug:** DTIC

## UNIDADE: [R.DTIC.05]

### Indicador

**Descrição Do Risco:** Indisponibilidade do Aplicativo MT Cidadão
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** A aplicação nativa do MT Cidadão, logando, navegando no home do app, navegando na parte não logada, entre outras funcionalidades exclusivas do aplicativo devem estar disponíveis 24x7 com disponibilidade superior a 99% -- aplicativo não quebrar de forma alguma -- (microserviços da plataforma, devem estar bem identificados quando estiverem indisponiveis)
**Quem:** UGGDI
**Início:** 01/03/2024
**Fim:** 30/12/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 25,00%
**Observações:** Ações e Resultados

[contrato da rw3]

Testes integrados, e2e, unitário, fluxo de desenvolvimento de alta qualidade com esteira automatizada
Esteira de Código seguro
Testes de cobertura para ios e android, com maior cobertura de so e versão
Criar monitoramento da aplicação 24x7 com equipe dedicada - Painel diário com relatório mensal
Recriar indicadores e medidores próprios, incluindo disponibilidade de status na plataforma de clientes
Monitoramento de segurança e painel diário com relatório mensal de incidentes de segurança
Central de atendimento nível 1 e nível 2 de atendimento
**Ug:** DTIC

## UNIDADE: [R.GADP.01]

### Indicador

**Descrição Do Risco:** Não priorização pelo governo quanto às soluções a serem entregues pela MTI
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**O Que:** Alinhamento com a área estratégica do governo
**Como:** - Elaboração e aprovação do PTA;
- A partir da consolidação do PTA, apresentar e argumentar as necessidades junto ao órgão central do orçamento.
- Priorização das atividades a serem realizadas, a partir do teto disponibilizado;
- Viabilizar agendas peiódicas com o Governador, para priorização;
- Pautar, nas agendas ordinárias do Conselho de Administração, o monitoramento dos projetos estratégicos.
**Início:** 02/01/2023
**Fim:** 29/12/2023
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 20,00%
**Observações:** - Verificar orçamento 2023 com ideraldo
**Ug:** GADP
**Situação Geral:** 20,00%
**Número De Ações:** 3.0
**Quantidade De Eventos De Riscos:** 3.0

## UNIDADE: [R.GADP.02]

### Indicador

**Descrição Do Risco:** Não contratação da MTI em tempo hábil
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**O Que:** Aperfeiçoar o modelo de contratação dos serviços
**Como:** - Alinhamaento com a PGE e COTEC para criação de um modelo de contratação corporativa da MTI.
**Início:** 02/01/2023
**Fim:** 29/12/2023
**Quanto:** R$ 0,00
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 20,00%
**Ug:** GADP

## UNIDADE: [R.GADP.03]

### Indicador

**Descrição Do Risco:** Vencimento do contrato de temporários 
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**O Que:** Solução para continuidade dos negócios sob responsabilidade dos temporários
**Como:** - Verificação com a UNIJUR das soluções jurídicas; 
- Análise da UGPES;
- Verificação de soluções com a DTIC.
**Ug:** GADP

## UNIDADE: [R.OUVIDORIA.01]

### Indicador

**Descrição Do Risco:** A -  Descumprimento das normas e prazos de Ouvidoria
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Cumprir normas e prazos de Ouvidoria
**Quem:** Mara e Maria
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para cumprimento das normas,  fortalecimento da imagem institucional e satisfação dos usuários
**Como:** 1. Capacitação/atualização da equipe de Ouvidoria;
2. Cumprimento das normativas de Ouvidoria e Transparência;
3. Monitormento dos resultados (relatório de gestão da Ouvidoria);
4. Disseminação das Normas de Ouvidoria e Transparência.

**Início:** 04/03/2024
**Fim:** 20/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1. Maria - 14 cursos e eventos / Mara - 13 cursos e eventos / Jennifer - 06 cursos e eventos / Gabrielle - 11
2. jan-dez- 275demandas respondidas no prazo legal.
3. 04 relatórios publicados
4. 14 disseminações
**Ug:** OUVIDORIA
**Situação Geral:** 100,00%
**Número De Ações:** 3.0
**Quantidade De Eventos De Riscos:** 3.0

## UNIDADE: [R.OUVIDORIA.02]

### Indicador

**Descrição Do Risco:** C - Não cumprir a meta na avaliação de satisfação com a Ouvidoria
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Cumprir Meta
**Quem:** Mara e Maria
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Fortalecimento da imagem institucional e satisfação dos usuários
**Como:** 1. Capacitação/atualização da equipe de Ouvidoria;
2. Cumprimento das normativas de Ouvidoria e Transparência;
3. Monitormento dos resultados (relatório de gestão da Ouvidoria);
4. Disseminação das Normas de Ouvidoria e Transparência.

**Início:** 04/03/2024
**Fim:** 21/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1. Maria - 14 cursos e eventos / Mara - 13 cursos e eventos / Jennifer - 06 cursos e eventos /  Gabrielle - 11
2. 111 avaliações recebidas, 100% positivas
3. 04 relatórios publicados
4. 14 disseminações
**Ug:** OUVIDORIA

## UNIDADE: [R.OUVIDORIA.03]

### Indicador

**Descrição Do Risco:** D - Descumprimento das normas e prazos da LAI no que se refere as demandas de SIC; 
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Cumprir normas e prazos do SIC
**Quem:** Mara e Maria
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para cumprimento da LAI,  fortalecimento da imagem institucional e satisfação dos usuários
**Como:** 1. Capacitação/atualização da equipe de Ouvidoria;
2. Cumprimento das normativas de Ouvidoria e Transparência;
3. Monitormento dos resultados (relatório de gestão da Ouvidoria);
4. Disseminação das Normas de Ouvidoria e Transparência.

**Início:** 04/03/2024
**Fim:** 22/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1. Maria - 14 cursos e eventos / Mara - 13 cursos e eventos / Jennifer - 06 cursos e eventos /  Gabrielle - 11
2. jan-dez - 04 pedidos de informações respondido no prazo legal
3. 04 relatórios publicados
4. 14 disseminações
**Ug:** OUVIDORIA

## UNIDADE: [R.UGACO.01]

### Indicador

**Descrição Do Risco:** Atraso nos prazos previstos para a conclusão das aquisições
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Instrução correta dos processos
**Quem:** GCTO E GAQS
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para que os processos não retorne por diversas vezes as unidades demandantes para correção
**Como:** 1 - Elaboração do Check List dos documentos necessários para instrução e mapeamento do processo                                                                                   
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Ug:** UGACO
**Situação Geral:** 100,00%
**Número De Ações:** 7.0
**Quantidade De Eventos De Riscos:** 8.0

## UNIDADE: [R.UGACO.02]

### Indicador

**Descrição Do Risco:** processos iniciados sem previsão orcamentária (PTA)
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Cumprimento das Legislações (LRF, Decreto 1.525/2022/, RLC...
**Quem:** UGACO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A unidade demandante deve saber se o produto ou o serviço a ser adquirido foi incluido no PTA e se existe orçamento para a aquisição
**Como:** 1 - Disparar CI com a informação e encaminhar às areas
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGACO

## UNIDADE: [R.UGACO.03]

### Indicador

**Descrição Do Risco:** Prorrogações contratuais realizadas com o prazo exíguo ou correndo risco de perder o prazo para prorrogação
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Evitar a perda do contrato por desídia
**Quem:** UGACO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Perda das prorrogações dos contratos geram demandas novas com custos elevados e tempo para conclusão
**Como:** 1 -  A GCTO comunicará mensalmente (12 meses antes de vencer )  as areas demandantes sobre os vencimentos dos contratos e o check list com os documentos necessários para as  prorrogações, via SIGADOC.                                                                           2. 06 Meses antes do vencimento dos contratos , a GCTO intensifica o contato com area para alertar sobre os vencimentos dos contratos, via SIGADOC e  caso não seja respondidoo prazo máximo de 60dias do vencimento , então realiza o item 3.                                                                                 .                       3 Cobranças semanais das Unidades com cópia para os Chefes imediatos e Presidência para o cumprimento da demanda no prazo, realizadas por e-mail ou CI
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGACO

## UNIDADE: [R.UGACO.04]

### Indicador

**Descrição Do Risco:** Realizar contratações emergenciais
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Evitar a perda dos contratos que devem ser prorrogados e planejar as aquisições em tempo hábil
**Quem:** UGACO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Contratos emergenciais devem ser realizados somente em casos estritamente necessários e com justificativa plausível
**Como:** 1 - Demandar CI para as Unidades com as recomendações.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGACO

## UNIDADE: [R.UGACO.05]

### Indicador

**Descrição Do Risco:** Fiscalização contratal ineficiente
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**O Que:** Evitar que os contratos sejam mal fiscalizados
**Quem:** GCTO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** As contratações devem ser monitoradas e acompanhadas, visando a entrega de um excelente serviço ou produto
**Como:** 1 - Curso de Capacitação em fiscalização de contratos (encaminhado e-mail para os responsáveis para arealização do curso que foi disponibilizado gratuitamente)                                                                                                            2 - Elaborar cartilha juntamente a UNISECI m para orientações.                                                                                                                                                                                                                                                                                                                                                                                      3.Portaria com após a publicação do novo RLC. 
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGACO

## UNIDADE: [R.UGACO.06]

### Indicador

**Descrição Do Risco:** Receber, para si ou para outrem, vantagem(econômica ou não), direta ou indireta, por ação ou omissão decorrente das atribuições do Agente Público
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Receber vantagens financeiras
**Quem:** UGACO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Evitar qualquer Infração Penal prevista em lei, com sanções administrativas e Penais.
**Como:** 1 - Atuar conforme principios da Legalidade, Imparcialidade, Moralidade, Publicidade e Ética
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGACO

## UNIDADE: [R.UGACO.07]

### Indicador

**Descrição Do Risco:** Baixo engajamento das equipes internas
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**O Que:** Demora na Analise de processos, conclusão e finalização
**Quem:** UGACO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Ausencia de politicas que incentivem a produtividade
**Como:** 1 - Estrutura o setor com pessoa com perfil pertinente a UGACO .                                                                                                      2. Capacitação da equipe .                                                                                                           3. Reconhecer e incentivar colaboradores a atingirem suas metas e obrigações diarias.                                                                                                                                                                                 
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGACO

## UNIDADE: [R.UGACO.08]

### Indicador

**Descrição Do Risco:** Indisponibilidade dos serviços de TIC
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** CRÍTICO
**O Que:** Aperfeiçoar o plano anual de contratação (com prioridades para assuntos críticos de continuidade de negócio)
**Quem:** UGACO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI 
**Por Que:** Melhorar a consciência dos elaboradores das áreas demandante, para que o plano anual seja elaborado e executado com maior qualidade, planejamento, tempestividade e interesse na concretização de contratações, buscando assim priorizar e mitigar os assuntos críticos.
**Como:** 1. Através de reuniões trimestrais com as áreas demandantes, orientar e estimular a melhoria na elaboração e execução no plano anual de aquisições. 
2. Acompanhar a execução do plano anual de contratação vigente, realizando ajustes caso necessário. 

**Início:** 02/02/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%

## UNIDADE: [R.UGADM.01]

### Indicador

**Descrição Do Risco:** Não coordenar a gestão do arquivo permanente
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**O Que:** Coordenar efetivamente a gestão do arquivo permanente
**Quem:** Marcela 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Gestão de documentos em cumprimento aos Decretos Estaduais nº 1.654/97, de 29 de agosto de 1997 e 1.509/2008, de 12 de agosto de 2008, a Secretaria de Estado de Gestão, através do Arquivo Público de Mato Grosso, tem a atribuição de orientar os órgãos públicos do Estado de Mato Grosso sobre a implantação ou implementação da Política de Gestão de Documentos
**Como:** Treinamento SEPLAG
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1° Ciclo - até 30/04/2024 - Foi enviado para avaliação  para Coordenadoria do Arquivo Publico 

2° Ciclo - até 31/07/2024 -  Foi enviado para avaliação  para Coordenadoria do Arquivo Publico 

3° Ciclo - até 31/10/2024 -  Foi enviado para avaliação  para Coordenadoria do Arquivo Publico 
**Ug:** UGADM
**Situação Geral:** 100,00%
**Número De Ações:** 6.0
**Quantidade De Eventos De Riscos:** 6.0

## UNIDADE: [R.UGADM.02]

### Indicador

**Descrição Do Risco:** Falta de gestão dos documentos da empresa
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Coordenar a gestão de documentos 
**Quem:** Marcela 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI 
**Por Que:** Manter a gestão de documentos 
**Como:** Treinamento SEPLAG/ Arquivo Publico 
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Realizado através da Portaria de eliminação de documentos 
**Ug:** UGADM

## UNIDADE: [R.UGADM.03]

### Indicador

**Descrição Do Risco:** Falta de planejamento e distribuição dos materiais de consumo
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**O Que:** Implantação do Módulo Almoxarifado no Protheus 
**Quem:** Marcelo 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI 
**Por Que:** Utilizar o Sistema já utulizado pela MTI 
**Como:** Realizar a contabilidade dos materiais no sistema e parametrizar as regras no Protheus juntamente com o Gestor do Sistema 
**Início:** 03/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGADM

## UNIDADE: [R.UGADM.04]

### Indicador

**Descrição Do Risco:** Não realizar manutenção predial 
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Formalizar o processo de Manutenção Predial 
**Quem:** Olívia 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI 
**Por Que:** Dar suporte a equipe GETS nas demandas solicitadas.
**Como:** Realizar a contratação com a empresa 
**Início:** 04/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Ug:** UGADM

## UNIDADE: [R.UGADM.05]

### Indicador

**Descrição Do Risco:** Falta de controle dos materiais permanentes 
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**O Que:** Implantação do Módulo Patrimonio no Protheus 
**Quem:** Marcelo 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Utilizar o Sistema já utulizado pela MTI 
**Como:** Realizar a contabilidade dos materiais no sistema e parametrizar as regras no Protheus juntamente com o Gestor do Sistema 
**Início:** 05/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGADM

## UNIDADE: [R.UGADM.06]

### Indicador

**Descrição Do Risco:** Falta de realização de inventário (Bens permanentes, consumo, imobiliário e intangíveis)
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Implantação do Módulo Patrimonio no Protheus 
**Quem:** Marcelo 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI 
**Por Que:** Encerramento do Exercício que prevê prazos e limites para providências quanto ao Inventário de Bens e demais ações.
**Como:** Alimentar com todas as informações a comissão de inventário 
**Início:** 06/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGADM

## UNIDADE: [R.UGARQ.01]

### Indicador

**Descrição Do Risco:** Indisponibilidade da Plataforma de Simplificação 
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** - Manter redundância dos ativos  e monitorar a saúde do ambiente
- Quanto ao risco contratual, apenas aceitar, pois é uma tecnologia proprietária e não tem como ter uma alterativa. Em caso de ocorrer a quebra de contrato, as aplicações precisam ser refeitas para não utilizar essa tecnologia.
**Quem:** William Chitto
**Qual Ativo Crítico Afetado Pelo Risco:** GIAP
**Por Que:** Mitigar a chance de indisponibilidade
**Como:** Monitorar o ambiente pelo Zabbix, e manter servidores redundantes rodando em paralelo
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Ug:** UGARQ
**Situação Geral:** 50,00%
**Número De Ações:** 4.0
**Quantidade De Eventos De Riscos:** 4.0

## UNIDADE: [R.UGARQ.02]

### Indicador

**Descrição Do Risco:** Indisponibilidade do servidor seguro e central da MTI no Xvia
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** - Evoluir o xVia para ser entregue em formato de docker, assim fica mais fácil para provisionar outros ambientes em caso de falha
- Manter redundância dos servidores
**Quem:** George Oliveira
**Qual Ativo Crítico Afetado Pelo Risco:** GASI
**Por Que:** Mitigar a chance de indisponibilidade
**Como:** Compliar o xVia na versão nova e manter uma imagem de fácil deploy. 
Instalar várias instâncias dos servidores seguros para mitigar chance de indisponibilidade.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 95,00%
**Observações:** Foi feito o deploy do SS da MTI no GKE, ainda resolvendo problema de IPs no kubernetes local para fazer deploy de outros servidores seguros
**Ug:** UGARQ

## UNIDADE: [R.UGARQ.03]

### Indicador

**Descrição Do Risco:** Indisponibilidade do servidor seguro dos órgãos no Xvia
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** PEQUENO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** - Prover suporte para as equipes dos clientes
- Evoluir o xVia para ser entregue em formato de docker, assim fica mais fácil para provisionar outros ambientes em caso de falha
**Quem:** George Oliveira
**Qual Ativo Crítico Afetado Pelo Risco:** GASI
**Por Que:** Mitigar a chance de indisponibilidade
**Como:** Fornecer nova versão do xVia aos clientes
**Início:** 01/06/2024
**Fim:** 31/12/2024
**Situação:** NÃO INICIADA
**Percetual De Execução:** 0,00%
**Observações:** Aguardando finalizar o item R.UGARQ.02
**Ug:** UGARQ

## UNIDADE: [R.UGARQ.04]

### Indicador

**Descrição Do Risco:** Indisponibilidade do GCP
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** - Manter redundância das aplicações em ambiente local
**Quem:** Fernando Tonon 
**Qual Ativo Crítico Afetado Pelo Risco:** UGARQ
**Por Que:** Evitar a indisponibilidade das aplicações quando não houver mais contrato com o GCP
**Como:** Recomendar aos responsáveis das aplicações a aplicação de uma arquitetura em que as aplicações sejam disponibilizadas em paralelo no ambiente da MTI
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 5,00%
**Observações:** Necessário preparar os ambientes e configurar as esteiras de desenvolvimento e aplicações
**Ug:** UGARQ

## UNIDADE: [R.UGCOF.01]

### Indicador

**Descrição Do Risco:** B - Descumprimento de prazos para envio de informações relativas à Conciliação Bancaria pelo setor Financeiro em detrimento do processo de compatibilização de informações entre os sistemas de gestão Publico e Privado.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Cumprimento de prazos
**Quem:** Alcindo / Gustavo / Marcio
**Qual Ativo Crítico Afetado Pelo Risco:** UGOFF/UGCOF/GICF
**Por Que:** Ações a serem realizadas para mitigação de riscos de atrasos nos fechamentos contabeis mensais, oriundos de ausencias de informações internas. 
**Como:** Com a realização da conciliação bancaria em ritmo diario ou semanal, com intuito de otimizar a data de fechamento mensal e posterior entrega à UGCOF para as devidas validações.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** As entregas dos balancetes mensais foram realizadas no prazo para a Sefaz e Conselho Fiscal.
**Ug:** UGCOF
**Situação Geral:** 100,00%
**Número De Ações:** 5.0
**Quantidade De Eventos De Riscos:** 5.0

## UNIDADE: [R.UGCOF.02]

### Indicador

**Descrição Do Risco:** C - Descumprimento de prazos para envio de informações relativas ao Faturamento Mensal pela GFAC em detrimento do processo de compatibilização de informações entre os sistemas de gestão Publico e Privado.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Cumprimento de prazos
**Quem:** Alcindo / Gustavo / Marcio
**Qual Ativo Crítico Afetado Pelo Risco:** UGOFF/UGCOF/GICF
**Por Que:** Ações a serem realizadas para mitigação de riscos de atrasos nos fechamentos contabeis mensais, oriundos de ausencias de informações internas. 
**Como:** Com o fechamento das informações relativas aos faturamentos do mês corrente em prazo hábil e a conferencia dos cancelamentos de documentos de competencias anteriores que servirão de creditos tributarios nas apurações tributarias do mês avaliado. 
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** A validação do faturamento está ocorrendo até o segundo dia util do mês subsequente, dentro do prazo.
**Ug:** UGCOF

## UNIDADE: [R.UGCOF.03]

### Indicador

**Descrição Do Risco:** D - Analise de documento fiscal em descumprimento as normas de retenção ou creditos tributarios.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Legislação Tributaria
**Quem:** Alcindo / Gustavo
**Qual Ativo Crítico Afetado Pelo Risco:** UGCOF/GICF
**Por Que:** Análises necessarias para liberação de um documento de entrada/saida, considerando que os mesmos interferem diretamente no montante de tributos apurado mensalmente.
**Como:** Com observação a legislação tributaria, realização de atualizações constantes sobre o assunto e tratamento de erros na validação dos documentos.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Realizadas melhorias no sentido de verificar caso a caso as devidas retenções e aproveitamentos de crédito tributario.
**Ug:** UGCOF

## UNIDADE: [R.UGCOF.04]

### Indicador

**Descrição Do Risco:** G - Preço dos produtos/serviços não competitivos com o mercado
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Atualização do plano de gestão de custos
**Quem:** Alcindo / Naianne
**Qual Ativo Crítico Afetado Pelo Risco:** UGCOF/GCCP
**Por Que:** Necessidade de revisão dos custos dos serviços prestados, considerando folha, insumos e tributos para melhoria e adequação da apropriação dos custos e preços de venda
**Como:** Com a observação nas melhores praticas de gestão de custos,realização de capacitação do pessoal responsavel e implantação de ferramentas necessarias. 
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Iniciado o Pré projeto para realização do custeio de uma unidade piloto e apresentação do modelo à diretoria.
**Ug:** UGCOF

## UNIDADE: [R.UGCOF.05]

### Indicador

**Descrição Do Risco:** H - Descumprimento dos prazos de entrega dos Inventarios de Bens móveis, imóveis e de Consumo
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Gestão patrimonial
**Quem:** Alcindo / Olivia
**Qual Ativo Crítico Afetado Pelo Risco:** UGCOF/UGADM
**Por Que:** Necessidade do registro e classificação dos bens e suas alterações/cessões tempestivamente.
**Como:** Com a correta utilização da ferramenta de gestão de ativos, realização de ações  que mitiguem o risco de perda, dano ou extravio dos bens da empresa.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Nomeação de novo gerente de patrimonio. Levantamento de informações dos bens da empresa (por empregado).
**Ug:** UGCOF

## UNIDADE: [R.UGENP.01]

### Indicador

**Descrição Do Risco:** Não haver captação de novas ideias
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Criar um sistema estruturado para a coleta, avaliação e implementação de novas ideias.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Um sistema de gestão de ideias ajuda a organizar o processo de captação e seleção das melhores ideias.
**Como:** Divulgar o programa nos canais da Empresa
Divulgar nos eventos realizados pela MTI
Incluir os colaboradoradores no Sistema de Gestão de gamificação
**Início:** 01/06/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 95,00%
**Observações:** Sistema MTIGen em fase final de homologação. Testes em Produção com PILOTO com a UGPES.
**Ug:** UGENP
**Situação Geral:** 99,55%
**Número De Ações:** 13.0
**Quantidade De Eventos De Riscos:** 14.0

## UNIDADE: [R.UGENP.02]

### Indicador

**Descrição Do Risco:** Não cumprir o planejamento da demanda
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Realizar planejamento e monitorar as priorizações da camada estratégica da MTI 
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para otimizar a força de trabalho alinhado ao interesse estratégico da MTI 
**Como:** Realizar reuniões e monitoramento das ações da DIRC
Alinhar sobre as priorizações da MTI



**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Reuniões semanais com o Diretor DIRC
**Ug:** UGENP

## UNIDADE: [R.UGENP.03]

### Indicador

**Descrição Do Risco:** Falta de recursos para eventos planejados
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Estabelecer um processo claro de gestão de recursos que permita o acompanhamento e a alocação adequada dos recursos para os eventos.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Uma gestão eficiente dos recursos ajuda a evitar desperdícios e a garantir que os recursos estejam disponíveis quando necessários.
**Como:** Utilizar ferramentas de gestão de projetos, definir responsabilidades claras, monitorar o uso de recursos e fazer ajustes conforme necessário.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CANCELADA
**Ug:** UGENP

## UNIDADE: [R.UGENP.04]

### Indicador

**Descrição Do Risco:** Deficiência na entrega de demanda priorizada innovation day
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Engajar e envolver as equipes responsáveis pela entrega das demandas priorizadas, garantindo que estejam comprometidas com os objetivos do Innovation Day.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** O engajamento das equipes é fundamental para garantir a colaboração e o foco na entrega das demandas prioritárias.
**Como:** Realizar sessões de brainstorming, incentivar a comunicação aberta e criar um ambiente de trabalho colaborativo para motivar as equipes.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Conversas diárias com membros da equipe, sobre aspectos pessoais/emocionais e profissionais.
**Ug:** UGENP

## UNIDADE: [R.UGENP.05]

### Indicador

**Descrição Do Risco:** Não haver participação de trabalhos em congressos 
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Conscientizar os colaboradores sobre os benefícios e oportunidades de participar em congressos, como networking, aprendizado e visibilidade.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A participação em congressos contribui para o desenvolvimento profissional dos colaboradores e para a disseminação do conhecimento da empresa.
**Como:** Realizar palestras internas, compartilhar casos de sucesso e incentivar a participação ativa dos colaboradores na busca por oportunidades de apresentação em congressos.                                                                                   Apoiar Financeiramente e Logisticamente os Colaboradores
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CANCELADA
**Ug:** UGENP

## UNIDADE: [R.UGENP.06]

### Indicador

**Descrição Do Risco:** Não oferecer soluções inovadoras de acordo com o mercado
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Acompanhar de perto as tendências e as mudanças no mercado de Tecnologia da Informação para identificar oportunidades de inovação.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Estar atento às demandas e preferências dos clientes permite antecipar as necessidades do mercado e desenvolver soluções inovadoras.
**Como:** Realizar análises de mercado, participar de eventos do setor, e manter contato com clientes e parceiros para obter feedback sobre tendências emergentes.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Participação em evento de TI, agendas com parceiros sobre tendências e oportunidades. 
**Ug:** UGENP

## UNIDADE: [R.UGENP.07]

### Indicador

**Descrição Do Risco:** Não haver participação de colaboradores nos eventos internos e externos
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Personalizar a comunicação e a programação dos eventos de acordo com os interesses e necessidades dos colaboradores.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Eventos relevantes e alinhados com as expectativas dos colaboradores aumentam o engajamento e a participação.
**Como:** Realizar pesquisas de interesse, segmentar a programação dos eventos, e oferecer opções variadas que atendam às preferências da equipe.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Busca com outras áreas sobre tema e palestrantes para as agendas do Café Tech e Tech Talk
**Ug:** UGENP

## UNIDADE: [R.UGENP.08]

### Indicador

**Descrição Do Risco:** Não evolução de contratações dos produtos disponibilizados através de parcerias da MTI
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Estabelecer métricas de desempenho e monitorar regularmente a aceitação e o uso dos produtos disponibilizados por meio das parcerias.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Parcerias sólidas e transparentes são essenciais para a evolução contínua dos produtos e para a manutenção de uma rede de colaboração eficaz.
**Como:** Monitorar possibilidades de novos parceiros para poderem eventualmente possibilitar a continuidade de negócios.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 20 Empresas Entrevistadas: Positivo Tecnologia; Italtel Brasil; Norden IT; Pentágono TI; MTM Tecnologia; EVO; BA Group e Teltec; Palo Alto;  Positivo; Thales; PPN Tecnologia; Autodesk; LanLink; Pars/Adobe; Bricon It Solution; Invillia; Energy Telecom; Chip Cia/DELL; 9NET/AWS; VALID
**Ug:** UGENP

## UNIDADE: [R.UGENP.09]

### Indicador

**Descrição Do Risco:** Vazamento de dados sigilosos referentes ao processo de parcerias e ideias de inovação
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Participar de treinamentos regulares sobre segurança da informação e a importância da proteção de dados sigilosos.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** conscientização dos colaboradores é essencial para prevenir erros humanos, phishing e outras ameaças internas.
**Como:** Participar de campanhas de conscientização, simulações de phishing, e orientar os colaboradores sobre boas práticas de segurança.                                                                                       Fomentar políticas de acesso baseadas em funções, criptografar dados sensíveis e monitorar as atividades de acesso e uso dos dados.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Worshop sobre LGPD;                                                  Participação nos fóruns de LGPD;                          Participação em pesquisa;                             Revisão do compartilhamento de pastas e arquivos da UG, dos processos de parceria estratégica.      
**Ug:** UGENP

## UNIDADE: [R.UGENP.10]

### Indicador

**Descrição Do Risco:** Direcionamento de um processo de parceria ou chamamento público
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Assegurar que o processo de seleção seja conduzido de forma imparcial, sem favorecimentos ou direcionamentos indevidos.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A transparência fortalece a credibilidade da empresa, demonstra a lisura do processo e permite a prestação de contas à sociedade.
**Como:** Participar de comissão ou equipe responsável pela avaliação, evitar conflitos de interesse e garantir a transparência em todas as etapas do processo.                                                                                                                    Dar publicidade de informações sobre o processo, disponibilizar relatórios de avaliação, e responder a questionamentos e solicitações de esclarecimento de forma aberta.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Participação de comitê de inovação e Transformação Digital MT;                                                  Grupo de Trabalho da Politica de IA para Poder Executivo de Mato Grosso
**Ug:** UGENP

## UNIDADE: [R.UGENP.11]

### Indicador

**Descrição Do Risco:** Baixo engajamento das equipes internas
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Criar oportunidades para que os colaboradores participem ativamente, contribuam com ideias e sugestões, e se envolvam em projetos e iniciativas da empresa.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** O envolvimento dos colaboradores aumenta a motivação, a criatividade e a produtividade, além de fortalecer o senso de pertencimento e a cultura de colaboração.
**Como:** Sensibilização/motivação das equipes
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Liberação para participação em palestras de tecnologia e inovação;                                Participação de Evento externo do Gartner; Participação em Eventos 
**Ug:** UGENP

## UNIDADE: [R.UGENP.12]

### Indicador

**Descrição Do Risco:** Baixa capacidade para operacionalizar as parcerias estratégicas
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Elaborar um plano estratégico que defina objetivos claros, metas mensuráveis e ações específicas para operacionalizar as parcerias estratégicas.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Um plano de gestão estruturado orienta as atividades, alinha os esforços da equipe e facilita a execução eficaz das parcerias.
**Como:** Aperfeiçoar o modelo de parcerias estratégicas a. monitorar a execução de todo o processo das parcerias estratégicas em conjuto com os parceiros.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Aprovação des instrumentos do Regulamento de Parceria MIPP / TAP / Compliance
**Ug:** UGENP

## UNIDADE: [R.UGENP.13]

### Indicador

**Descrição Do Risco:** Risco a oportunidade de negócios ou comprometimento da continuidade de negócios de produtos de parceria da MTI
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Identificar e avaliar os riscos que podem impactar as oportunidades de negócios e a continuidade das operações da empresa.
**Quem:** Aílton Machado
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A análise de riscos permite antecipar ameaças potenciais, tomar medidas preventivas e mitigar os impactos negativos nos negócios.
**Como:** Realizar avaliações regulares de riscos, envolver as partes interessadas, priorizar os riscos identificados e desenvolver planos de ação para gerenciá-los.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Revisitação no Plano de Riscos, inerentes a UGENP
**Ug:** UGENP

## UNIDADE: [R.UGENP.14]

### Indicador

**Categoria Do Risco:** ESTRATÉGICO

## UNIDADE: [R.UGEPV..04]

### Indicador

**Descrição Do Risco:** Falta de suporte pós-venda adequado.
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** canais de relacionamento
**Quem:** UGEPV
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A equipe de pós venda deve estar sempre em contato com o cliente, sanando dúvidas, ouvindo as dificuldades que ele venda a ter, anseios dos clientes, identificando os pontos de atenção e buscar sanar ou mitigar juntos os gestores.
**Como:** Criar e manter canais de relacionamento com o cliente.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Aumentamos o numero de visitas aos clientes com o intuito de ouvi-los tanto em relação a necessidades do dia a dia, quanto nas necessidades futuras, a expectativa é que essas interações traga ao cliente mais confiança em nossos consultores e principalmente os tenham como um ponto focal para relatos de problemas e novas oportunidades
**Ug:** UGEPV

## UNIDADE: [R.UGEPV.01]

### Indicador

**Descrição Do Risco:** Insatisfação do cliente com o serviço adquirido.
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** 1. Entrega deficitária
2. Entrega fora do prazo acordado;
3. Falta de atendimento em tempo hábil
**Quem:** todas as equipes 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** O acordo entabulado com o cliente deve ser rigorosamente cumprido emtodos os seus termos
**Como:** Acompanhar o cliente em todo processo desde a compra até a entrega do produto, cada equipe seguindo seu processo na cadeia comercial, proporcionando ao cliente a segurança e satisfação pretendida. 
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Aumentamos o numero de visitas aos clientes com o intuito de ouvi-los tanto em relação a necessidades do dia a dia, quanto nas necessidades futuras, a expectativa é que essas interações traga ao cliente mais confiança em nossos consultores e principalmente os tenham como um ponto focal para relatos de problemas e novas oportunidades
**Ug:** UGEPV
**Situação Geral:** 100,00%
**Número De Ações:** 7.0
**Quantidade De Eventos De Riscos:** 7.0

## UNIDADE: [R.UGEPV.02]

### Indicador

**Descrição Do Risco:** Atrasos na entrega de serviços .
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** cumprimento de prazos
**Quem:** todas as equipes 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A pontualidade é um fator primordial que vai ser o grande divisor entre atrair ou afastar o cliente.
**Como:** Identificar onde estão os pontos que acarretam nos atrasos das entregas e sanar ou miticar tais pontos 
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Para essa atividade estamos estreitando a comunicação entre a equipe de Fabrica, projetos e comercial, desta forma conseguiremos estar junto "just in time" na entregas e conforme reuniões semanais o andamento das entregas visando assim uma entrega a contento para o cliente.
**Ug:** UGEPV

## UNIDADE: [R.UGEPV.03]

### Indicador

**Descrição Do Risco:** Dificuldades na utilização do produto/serviços por parte do cliente.
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Orientação, treinamento, informação.
**Quem:** todas as equipes 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** se o Cliente não sabe ou não consegue utilizar o produto adquirido na sua totalidade e/ou da forma correta esse produto se torna sem valor.
**Como:** Orientar o cliente quanto a  eventuais dificuldades que o cliente possa ter na utilização adequada do produto.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Estamos entendendo os processos, bem como os produtos, para dessa forma consguirmos ajudar nossos clientes em suas necessidades/duvidas, contudo apesar de não dominarmos em sua totalidade as ferramentas, sempre conseguimos alinhar com os parceiros capacitações / overview's para sanarem duvidas existentes.
**Ug:** UGEPV

## UNIDADE: [R.UGEPV.05]

### Indicador

**Descrição Do Risco:** Dificuldades na resolução de problemas ou reclamações dos clientes.
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Suporte dos Gestores Diretores
**Quem:** todas as equipes
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** O cliente é o centro do negócio, sem ele, a empresa não tem razão de existir, de modo que, a prioridade é que o cliente utilize nossos produtos sem qualquer intercorrência, e quando houver que seja sanado no menor tempo possível.
**Como:** Oferecer suporte para apoiar o cliente direcionando para o atendimento adequado, no entanto, quando não for possível essa resolução, é de suma importância acionar os Gestores Diretores para dirimir demandas de alçada maior.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Hoje os clientes utilizam a plataforma service now, ainda estamos em fase inicial contudo, pela relação que estamos construindo com os clientes os mesmos nos acionam quando necessario visando celeridade em um ponto ou outro que precisam de maior agilidade;
**Ug:** UGEPV

## UNIDADE: [R.UGEPV.06]

### Indicador

**Descrição Do Risco:** Falta de comunicação e acompanhamento eficaz com o cliente após a venda.
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Acompanhamento dos projetos
**Quem:** todas as equipes
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** è importante que o cliente tenha plena transparencia dos produtos adquiridos e entregues
**Como:** Acompanhar de forma macro a entrega dos produtos.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Estamos antenados com os acompanhamentos dos projetos e em sua grande maioria acompanhamos as reuniões semanais de entrega juntamente com o cliente, a idéia é que dentro dessa iteração consigamos entender se o que foi entregue esta a contento.
**Ug:** UGEPV

## UNIDADE: [R.UGEPV.07]

### Indicador

**Descrição Do Risco:** "O turnover"
Baixo engajamento da equipe
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** valorização dos colaboradores
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A valorização dos colaboradores é de suma importância para o crescimento de uma empresa.
**Como:** Cultura Organizacional Forte, Comunicação Clara e Aberta, Desenvolvimento Profissional, Conscienticação/ Equilíbrio entre Vida Profissional e Pessoal;Feedback e Desenvolvimento Individual:
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Uma cultura positiva e inclusiva pode ajudar os funcionários a se sentirem valorizados e conectados à missão da empresa, 
Manter os canais de comunicação abertos para que os colaboradores se sintam ouvidos e compreendidos, ofereçemos hoje oportunidades de desenvolvimento profissional, como treinamentos, workshops e programas de mentoria.
Ainda é necessario conseguirmos mais ferramentas para engajamento e conexão individual da equipe, estamos trabalhando para um curso/imersão visão construção de equipe.
**Ug:** UGEPV

## UNIDADE: [R.UGGDC.01]

### Indicador

**Descrição Do Risco:** Indisponibilidade do Ambiente do Data Lake
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Regularizar licenciamento e suporte técnico das plataformas de BigData "Cloudera"
**Quem:** Helder Ramos
**Qual Ativo Crítico Afetado Pelo Risco:** GEGD
**Por Que:** Para garantir ambiente tecnológico adequado para o desenvolvimento de soluções de BI e BigData Lake Coorportivo
**Como:** 1 -Elaborar TR para renovação de licença e suporte técnico (Clodera) de todos os produtos que contempla o Projeto de BigData


**Início:** 17/01/2024
**Fim:** 20/12/2024
**Quanto:** R$ 15.142.815,95
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 99%
**Observações:** Processo Autorizado para Licitação -  MTI-PRO-2023/02416
**Ug:** UGGDC
**Situação Geral:** 50,00%
**Número De Ações:** 3.0
**Quantidade De Eventos De Riscos:** 3.0

## UNIDADE: [R.UGGDC.02]

### Indicador

**Descrição Do Risco:** Indisponibilidade do Ambiente de GeoProcessamento
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Elaborar Termo de Referência ou desenvolver Parceria Estratégica de Soluções de GeoProcessamento
**Quem:** Helder Ramos
**Qual Ativo Crítico Afetado Pelo Risco:** GEGD
**Por Que:** Possibilitar a atualização tecnológica de GeoProcessamento e mão de obra especializada
**Como:** 1 - Elaborar ETP e TR para aquisição
2 - Prospecção de Parceria Estratégica de GeoProcessamento

**Início:** 02/03/2024
**Fim:** 21/12/2024
**Situação:** CANCELADA
**Percetual De Execução:** 0,00%
**Observações:** Acordado junto a UGEN que será feito a atualização com a renovação tecnológica já existente.
**Ug:** UGGDC

## UNIDADE: [R.UGGDC.03]

### Indicador

**Descrição Do Risco:** Ataques cibernéticos 
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Elaborar Projeto para Implementação de CSIRT - Centro de Tratamento de Incidêntes com objetivo de tratar todos e qualquer incidente Cibernético
**Quem:** Hercules
**Qual Ativo Crítico Afetado Pelo Risco:** GEDC
**Por Que:** Para garantir o tratamento adequado de Ataques Cibernéticos
**Como:** 1 - Capacitar a Equipe Técnica 
2 - Elaboração do Projeto de CSIRT 
3 - Contratação de Soluções de CiberSegurança  
4 - Implementação das Soluções 
5 - Monitoramento

**Início:** 03/03/2024
**Fim:** 22/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 51%
**Observações:** Planejamento do Projeto Elaborado, porém passará por uma revisão, para começar as fases de execução. Projeto sendo acompanhando no ServiceNow
**Ug:** UGGDC

## UNIDADE: [R.UGGDI.01]

### Indicador

**Descrição Do Risco:** A. Não priorizar a continuidade de negócio dos produtos de Identificação Digital do Cidadão da Plataforma de Governo Digital
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Priorização da continuidade de negócio dos produtos de Identificação Digital do Cidadão da Plataforma de Governo Digital
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** UGGDI
**Por Que:** Por se tratar de produtos altamente estratégicos, diretamente ligados à agenda estratégica de Governo Digital, os mesmos devem ser priorizados e estruturados para sua continuidade
**Como:** 1. Preparando uma ou mais pessoas de carreira da MTI que esteja engajada e comprometida e que tenha conhecimento técnico e habilidade conduzir a continuidade dos produtos

2. Monitorando a continuidade da parceria
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 20,00%
**Observações:** PONTO DE ATENÇÃO: MT.id sendo mantido pelo time Mandaloriano, é necessário mudar para o time Digital ID. Após a correção do problema na validação da assinatura do mt.id pela SIGADOC, será realizado o planejamento para separação do mt.id do backend do MT Cidadão e repasse de conhecimento para o time Digital Id.
Foi criada ug de arquitetura que está apoiando da evolução e continuidade dos produtos
Esmael está coordenando os produtos: MT Login, MTI Valida
Dedé está atuando no Prova de Vida, MT Login e MTI Valida
Foi iniciada a transferência de conhecimento do ambiente de infra do MTI valida para a equipe da MTI
Implementado monitoramento da VMs do MTI Valida no Zabbix. Foi solicitado a implementação do monitoramento dos pods openshift do MTI Valida no Kuma.
Está sendo negociado com a SEPLAG um contrato de sustentação da plataforma de governo digital
**Ug:** UGGDI
**Situação Geral:** 19,50%
**Número De Ações:** 4.0
**Quantidade De Eventos De Riscos:** 4.0

## UNIDADE: [R.UGGDI.02]

### Indicador

**Descrição Do Risco:** B. Não priorizar a continuidade de negócio dos produtos dos Canais de Atendimento Digitais da Plataforma de Governo Digital
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Priorização da continuidade de negócio dos produtos de dos produtos dos Canais de Atendimento Digitais da Plataforma de Governo Digital
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** UGGDI
**Por Que:** Por se tratar de produtos altamente estratégicos, diretamente ligados à agenda estratégica de Governo Digital, os mesmos devem ser priorizados e estruturados para sua continuidade
**Como:** 1. Preparando uma ou mais pessoas de carreira da MTI que esteja engajada e comprometida e que tenha conhecimento técnico e habilidade conduzir a continuidade dos produtos

2. Monitorando a continuidade da parceria
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 16,00%
**Observações:** PONTO DE ATENÇÃO: O PO do MT Cidadão é o Adauto da RW3
Novo canal de atendimento ao cidadão: Chatbot e Whatsapp. Está sendo acompanhado pelo analista temporário Marcelo Mialho.
Está sendo negociado com a SEPLAG um contrato de sustentação da plataforma de governo digital
**Ug:** UGGDI

## UNIDADE: [R.UGGDI.03]

### Indicador

**Descrição Do Risco:** C. Indisponibilidade dos produtos de Identificação Digital do Cidadão da Plataforma de Governo Digital
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Melhorar a disponibilidade dos produtos de Identificação Digital do Cidadão da Plataforma de Governo Digital
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** UGGDI
**Por Que:** Por se tratar de produtos altamente estratégicos, diretamente ligados à agenda estratégica de Governo Digital, os mesmos devem estar disponíveis 24x7
**Como:** 1. Preparando uma ou mais pessoas de carreira da MTI que esteja engajada e comprometida e que tenha conhecimento técnico e habilidade conduzir a continuidade dos produtos
2. Monitoramento 24x7 (contrato de consumo interno parceria TD)
3. Redundancia do ambiente tecnológico
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Quanto:** Valor do contrato consumo: R$ 4.778.935,20
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 19,00%
**Observações:** Projeto de atualização e migração do MT Login em fase de homologação (PRJ0010450). Previsão para migração em produção: 15/12/2024
Monitoramento das VMS do MTI Valida já implementado
Os relatórios de disponibilidade do MT Login são gerados mensalmente para composição do indicador estratégico
**Ug:** UGGDI

## UNIDADE: [R.UGGDI.04]

### Indicador

**Descrição Do Risco:** D. Indisponibilidade dos produtos dos Canais de Atendimento Digital da Plataforma de Governo Digital
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Melhorar a disponibilidade dos produtos dos Canais de Atendimento Digital da Plataforma de Governo Digital
**Quem:** UGGDI
**Qual Ativo Crítico Afetado Pelo Risco:** UGGDI
**Por Que:** Por se tratar de produtos altamente estratégicos, diretamente ligados à agenda estratégica de Governo Digital, os mesmos devem estar disponíveis 24x7
**Como:** 1. Preparando uma ou mais pessoas de carreira da MTI que esteja engajada e comprometida e que tenha conhecimento técnico e habilidade conduzir a continuidade dos produtos
2. Monitoramento 24x7 (contrato de consumo interno parceria TD)
3. Redundancia do ambiente tecnológico
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Quanto:** Valor do contrato consumo: R$ 4.778.935,20
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 23,00%
**Observações:** Monitoramento do Portal e MT Cidadão sendo realizado e acompanhado mensalmente e são utilizados na composição do indicador estratégico
Novo canal de atendimento ao cidadão: Chatbot e Whatsapp. Necessário implementar monitoramento do Chatbot e Whatsapp.
**Ug:** UGGDI

## UNIDADE: [R.UGGOV.01]

### Indicador

**Descrição Do Risco:** Execução parcial do plano estratégico
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** a) Divulgar mensalmente os resultados no painel de Indicadores da MTI (12,5%/12) = 1,0417
b) Acompanhar evento mensal da DIREX (50%/12) = 4,167
c) Publicar os resultados na intranet - bimestralmente  (12,5%/6) = 2,0833
d) Disseminar cartaz de gestão à vista (12,5%) = 12,5
e) Publicar 2 matérias para os colaboradores (em conjunto com a asscom) (12,5%/2) = 6,25

**Quem:** Carlos
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Promover a transparência e responsabilização das partes a fim de melhorar o nível de execução / alcance das metas estratégicas
**Como:** Atuando de acordo com os cronogramas internos da UGGOV
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Dos 6 indicadores estratégicos:
03 indicadores atigiram a meta(Nível de satisfação do cliente com as soluções de TIC entregues, Índice de satisfação e imagem, Percentual de pessoas com 100% de seu PDI executado)
02 indicadores com tendência de atingir a meta(Índice de disponibilidade das soluções de TIC e, Valor do Faturamento)
01 indicador resultado abaixo da média (Grau de maturidade de governança e gestão)
**Ug:** UGGOV
**Situação Geral:** 66,67%
**Número De Ações:** 3.0
**Quantidade De Eventos De Riscos:** 3.0

## UNIDADE: [R.UGGOV.02]

### Indicador

**Descrição Do Risco:** Baixo índice de conclusão das oportunidades de melhoria priorizadas pela equipe gerencial
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** a) Divulgar mensalmente os resultados no painel de avaliação da gestão da MTI (5%/12) = 0,4167
b)Promover capacitação da equipe gerencial (5%) = 5,0
c)Acompanhar evento semestral  da DIREX (20%)/2 = 10,0
d) Acompanhar evento semestral no Comitê (20%)/2 = 10,0
e) Apoiar na elaboração dos planos de ação (5%) = 5,0
f) Monitorar mensalmente as OM´S (40%)/12 = 3,33
g) Atuar em conjunto com Asscom na criação de informes   semestral (comunicação de equipe) (5%/2) = 2,5 


**Quem:** Carlos
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir que as OM´S priorizadas de fato sejam implementadas  
**Como:** Atuando de acordo com os cronogramas internos da UGGOV
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 05.06. Ações em andamento / modelo de gestão-governança foi alterado - afetando também o cronograma e métrica. De todo modo, ações de diagnóstico e planos de ação serão elaboradas com novos cronogramas - quando definidos, faremos a atualização aqui.
**Ug:** UGGOV

## UNIDADE: [R.UGGOV.03]

### Indicador

**Descrição Do Risco:** Processos críticos não mapeados ou não atualizados
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** a) Identificar os processos críticos (15%)
b) Definir um plano de ação para cada processo identificado (5%)
c) Atuar no mapeamento/desenho do processo (40%)
d) Orientar gestores para execução, monitoramento e avaliação dos processos (40%)
**Quem:** Bruno
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para melhorar a performance gerencial e os resultados da organização
**Como:** a) Verificando junto controle interno e UNICRS e posteriormente junto ao Diretor respectivo. A gestão de riscos e segurança da informação poderá fornecer insumos relevantes para determinação dos processos críticos, juntamente com o Diretor. 
b) Elaborando plano de ação para atuação dos processos críticos identificados
c) Orientando conforme metodologia de gestão de processos
d) Orientando gestores para a efetiva execução, monitoramento e avaliação
**Início:** 18/03/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CANCELADA
**Percetual De Execução:** 0,00%
**Observações:** Em planejamento / atualização de prioridades considerando as demandas na uggov

Início em atraso devido demandas do governo não previstas em planejamento anual - afetando as atividades na equipe

Nova análise: 05/06/24. Em análise quanto a real capacidade da equipe em absorver esta ação.
Análise 02/07: Equipe com alta demanda e sem condições no momento de atuar nesta atividade / Poucas pessoas para atuação com o volume de competências na uggov.

Análise de risco 24/07: Em consideração às exposições anteriores e considerando IMGG, informamos que a questão será mitigada através de um PMGG - plano de melhoria de governança e gestão - IMGG para 2025, portanto, solicito o CANCELAMENTO
**Ug:** UGGOV

## UNIDADE: [R.UGITI.01]

### Indicador

**Descrição Do Risco:** Baixa performance nos equipamentos de processamento de dados;
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Substituir Parque Computacional obsoleto
**Quem:** GPAC
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a integridade dos dados e disponiblidade dos serviços de TI
**Como:** 3 Cenários possíveis:
* Aguardar a aquisição de HCI através do PROFISCO II, conforme projeto da MTI já reportado à SEFAZ;
* Realizar a Migração dos workloads de clientes/serviços dedicados para infraestrutura do Parceiro ZADARA, sendo necessário readequação contratual;
* Realizar a aquisição de mais nós de HCI que suporte a demanda, e definir estratégia de ciclo de investimentos contínuos
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 51,00%
**Observações:** Necessário discutir possibilidades e definir estratégia.

* Parte será viabilizado pela ARP RedHat,para construção de ambiente dedicado;
* Aguardando agenda com a presidência para encaminhamento quanto a ARP RedHat;
* Aguardando retorno do CONDES;
Pregão agendado para 09/12
**Ug:** UGITI
**Situação Geral:** 73,00%
**Número De Ações:** 8.0
**Quantidade De Eventos De Riscos:** 8.0

## UNIDADE: [R.UGITI.02]

### Indicador

**Descrição Do Risco:** Indisponibilidade do ambiente de hospedagem (colocation)
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Executar Retrofit do Espaço Físcio do DC
**Quem:** GPAC
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a integridade dos dados e disponiblidade dos serviços de TI
**Como:** Realizar a contratação de serviços de engenharia para elaboração de Projetos de Retrofi do DC, que compreendam as necessidade de Refrigeração, Elétrica, Combate e prevenção de incêndio, Monitoramento e automação (DCIM);
Após projetos disponíveis realizar a priorização, para contratação das execuções 
**Início:** 01/02/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 98%
**Observações:** Processo de contratação de engenheiro em fase de assinatura de Contrato, logo após segue para emissão de OS e início das atividades.
* Projetos em fase de validação;
* Realizada apresentação das especificações de alteração do DC para Diretoria que irá levar a Presidência para aprovação;
Aguardando finalização da documentação do projeto básico 
**Ug:** UGITI

## UNIDADE: [R.UGITI.08]

### Indicador

**Descrição Do Risco:** Indisponibilidade no Ambiente de Virtualização;
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Substituir Parque Computacional obsoleto
**Quem:** GPAC
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a integridade dos dados e disponiblidade dos serviços de TI
**Como:** 3 Cenários possíveis:
* Aguardar a aquisição de HCI através do PROFISCO II, conforme projeto da MTI já reportado à SEFAZ;
* Realizar a Migração dos workloads de clientes/serviços dedicados para infraestrutura do Parceiro ZADARA, sendo necessário readequação contratual;
* Realizar a aquisição de mais nós de HCI que suporte a demanda, e definir estratégia de ciclo de investimentos contínuos
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 50,00%
**Observações:** Processo MTI-CIN-2022/00205; Contrato assinado em 17/05/2022;


* Parte será viabilizado pela ARP RedHat,para construção de ambiente dedicado;
* Aguardando agenda com a presidência para encaminhamento quanto a ARP RedHat;
* Aguardando retorno do CONDES;
Pregão agendado para 09/12
**Ug:** UGITI

## UNIDADE: [R.UGITI.11]

### Indicador

**Descrição Do Risco:** Indisponibilidade dos serviços de internet
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** PEQUENO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Ampliar a capacidade dos links de internet do AS
**Quem:** GRCO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a continuidade dos processos de negócio do Estado de Mato Grosso
**Como:** Adtivo contratual com os provedores de Internet do AS para aumento da capacidade do LINK de internet
**Início:** 01/12/2023
**Fim:** 15/04/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Observações:** Novos contratos assinados com as empresas Claro e Titânia.
Aguardando ativação ;
Mesmo Status
**Ug:** UGITI

## UNIDADE: [R.UGITI.16]

### Indicador

**Descrição Do Risco:** Indisponibilidade de comunicação na rede Infovia
e rede Core (incluindo rede de acesso - Datacenter)
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Subustituição de todo o parque de Ativos de Rede CORE
**Quem:** GRCO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a continuidade dos serviços de conectividade  do Datacenter e da Rede Infovia
**Como:** Executar o Projeto de Implantação da Rede Core SDN (Spine/Leaf) licitada em 2023
**Início:** 05/12/2023
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 74,00%
**Observações:** Contrato assinado, emitido OS. Está em fase de planejamento, enquanto aguarda chegada dos equipamentos;
Equipamentos Entregues (Agosto/2024), iniciada fase de instalação e ativação;
* Instalação realizada, iniciado planejamento lógico e de migração;
Finalizando implantação, para início das migrações.
* De acordo com cronograma atualizado (encerramento previsto para 05/12)
**Ug:** UGITI

## UNIDADE: [R.UGITI.23]

### Indicador

**Descrição Do Risco:** Indisponibilidade do Ambiente de Balanceamento
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Finalizar projeto de migração dos Virtual Servers (VS) do ambiente legado para novo
**Quem:** GABD
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a disponibilidade e segurança das aplicações mantidas pela MTI
**Como:** Emitir OS para o contratado realizar as ações de configuração e finalização do projeto de migração, consequentemente desativar ambiente legado
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 87,00%
**Observações:** Contrato 016/2022
**Ug:** UGITI

## UNIDADE: [R.UGITI.33]

### Indicador

**Descrição Do Risco:** Baixa performance no uso das aplicações
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** ampliar uso da ferramenta de monitoramento de performance de aplicações (APM)
**Quem:** GABD
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a disponibilidade e segurança das aplicações mantidas pela MTI
**Como:** Avaliar possiblidade de adesão a ARP de subscrições e serviços Dynatrace para ampliar utilização da solução de monitoramento
**Início:** 10/05/2024
**Fim:** 31/12/2024
**Situação:** NÃO INICIADA
**Observações:** Iniciada análise de mercado e elaboração do Termo de Referência após a aprovação do recurso e repriorização dessa ação.

Aberto o processo MTI-PRO-2022/00154 para contratação;

Aguardando Homologação do Pregão realizado;
Contrato assinado;
Solução Implantada;
Iniciado configuração de aplicações a serem monitoradas;

* Aguardando definições quanto a cenários possíveis de contratação.
- Ação ficará para 2025, devido necessitar finalizar contratação
**Ug:** UGITI

## UNIDADE: [R.UGITI.37]

### Indicador

**Descrição Do Risco:** Indisponibilidade da Plataforma de
 Container - RedHat Openshift.
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Manter equipe capacitada na operacionalização da solução de containers
**Quem:** GABD
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Garantir a disponibilidade das aplicações mantidas pela MTI
**Como:** * Realizar Licitação de ARP de soluções Red Hat para prover subscrições e serviços que atendam a plataforma e sua expansão;
Avaliar lote de appliance que suporte ambiente dedicado
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 51,00%
**Observações:** Aguardando licitação
* Aguardando retorno do CONDES quanto ao processo em andamento;
Pregão agendado para 09/12
**Ug:** UGITI

## UNIDADE: [R.UGOFF.01]

### Indicador

**Descrição Do Risco:** D - Pagamentos por Indenização
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Pagamentos de despesas sem cobertura contratual.
**Quem:** Todas as áreas demandantes
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Morosidade nos trâmites processuais para a renovação ou contratação de serviços contínuos. Falta de planejamento por parte do Gestor e Fiscal do Contrato, considerando que o Setor de Contratos envia e-mails orientativos informando o vencimento dos Contratos com até 6 (seis) meses de antecedência
**Como:** O Gestor e o Fiscal do Contrato deverão fazer o acompanhamento da vigência do Contrato que é de sua responsabilidade, tomando as devidas providências quanto a sua renovação ou nova contratação, em tempo hábil, evitando pagamentos indenizatórios e abertura de Processo Administrativo - PAD.
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CANCELADA
**Percetual De Execução:** 0%
**Observações:** Não houve pagamento por indenização no período de janeiro à junho de 2024. Este Indicador será revisto, haja vista que a UGOFF, não tem gerência sobre processos de indenizações.
**Ug:** UGOFF
**Situação Geral:** -
**Número De Ações:** 6.0
**Quantidade De Eventos De Riscos:** 6.0

## UNIDADE: [R.UGOFF.02]

### Indicador

**Descrição Do Risco:** H - Morosidade na liberação do Pedido de Venda via INFOCENTER.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**O Que:** Atraso na emissão e entrega das notas fiscais para o cliente.
**Quem:** UGENE
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Morosidade na liberação do pedido de venda através do INFOCENTER.
**Como:** A UGENE deverá liberar o pedido de venda através do INFOCENTER/PROTHEUS, validando todos os valores e serviços prestados para o cliente até o dia 05 domês subsequente ao serviços prestado pela MTI. GFAC - Gerar a nota fiscal, o  DAR - Documento de Arrecadação se necessário e envia o processo via SIGADOC para o cliente até o dia 10.
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 506,00
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 50,46%
**Observações:** De janeiro à outubro foram realizados 747 faturamentos, sendo que 50,46% que equivale a 316 notas fiscais foram enviadas dentro do prazo de até o dia 10 do mês subsquente aos serviços prestados pela MTI.
**Ug:** UGOFF

## UNIDADE: [R.UGOFF.03]

### Indicador

**Descrição Do Risco:** I - Inadimplência dos Clientes da MTI
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Indíce de inadimplência dos clientes da MTI
**Quem:** Clientes 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Despesa não prevista no PTA pelos clientes; Discordância do cliente quanto aos serviços prestados; Morosidade na finalização do Termo de Referência do clientes para assinatura do contrato com a MTI; Ausência de Aditivo Contratual conforme o consumo do cliente.
**Como:**  O cliente deverá prever no PTA o valor da despesa contratada.
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 3.709.376,57
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 8,75%
**Observações:** Considerando os meses de janeiro à dezembro, consta uma inadimplência no valor de R$ 8.616.948,71, equivale a 9,73%. Insta informar que não foi considerado as notas fiscais faturadas no mês 6, uma vez que conforme clausula contratual, os clientes terão até 30 dias para realizar o pagamento considerando o atesto da nota fiscal pelo fiscal do contrato.
**Ug:** UGOFF

## UNIDADE: [R.UGOFF.04]

### Indicador

**Descrição Do Risco:** J - Solicitações de novas demandas durante a execução orçamentária, sem o devido planejamento. 
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** CRÍTICO
**O Que:** Falta de Planejamento Orçamentário e corte do valor da LOA.
**Quem:** Todas as áreas demandantes
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** 1. Falta de planejamento para novas aquisições; 
2. Dificuldades em priorizar as novas demandas; 
3. Falta de clareza nos conceitos de planejamento e execução orçamentária
**Como:**  Na elaboração do PTA cada gestor e fiscal do contrato deverá primeiramente prever o valor da despesa já contratada (vigente) e na sequência prever valores para novas aquisições que já estejam validadas pelo Diretor da área e autorizadas pelo Presidente da MTI. 
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 0,00%
**Observações:** Não houve movimentação de janeiro à dezembro
**Ug:** UGOFF

## UNIDADE: [R.UGOFF.05]

### Indicador

**Descrição Do Risco:** L - Processo de pagamento Judicial.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Processos de Execução Judicial de Sentença proferida em 48 horas
**Quem:** UNIJUR
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Curto prazo para pagamento de processos de Execução Judicial de Sentença proferida em 48 horas
**Como:** A UNIJUR encaminhar o processo de pagamento em carácter de urgência sempre comunicando a UGOFF e GEFI do curto prazo para autenticação do pagamento. Vale destacar que o sistema FIPLAN realiza pagamento até às 17h:00min e em casos de solicitação de antecipação de Float, o horário é até às 11h:00min. Pagamentos realizado sem antecipação, será creditado em até 48 horas.
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 2.347,00
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 1,23%
**Observações:** Dos 2347 pagamentos realizados  de janeiro à novembro, 1,23 % que equivale a 6 (seis) processos, foram judiciais.
**Ug:** UGOFF

## UNIDADE: [R.UGOFF.06]

### Indicador

**Descrição Do Risco:** B - Manter Atualizado o Sistema FIPLAN-GFO (Gestão Financeira de Obras e Serviços de Engenharia
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**O Que:** Manter o sistema FIPLAN-GFO atualizado
**Quem:** Gestor/Fiscal do Contrato, GCTO, GEOR, GEFI.
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Impedimento do pagamento da despesa.
**Como:** Todos os perfis envolvidos nesta demanda deverão manter os sistema FIPLAN-GFO atualizado, sendo o perfil de Operador de contratos de obras e serviços de engenharia, operador orçamentário e financeiro, fiscal de obras e serviços de engenharias, Auxiliar de fiscalização de obras e serviços de engenharia e Consulta.
**Início:** 02/01/2024
**Fim:** 31/12/2024
**Quanto:** R$ 18.050.000,00
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 49,31%
**Observações:** O Sistema FIPLAN-GFO está sendo atualizado conforme a evolução da reforma da Nova Sede da MTI através de suas medições. Vale ressaltar que a quantidade informada de R$ 18.050.000,00 é referente ao credor São Pedro Construtora LTDA.  Foi realizado pagamentos até dezembro no total de R$ 8.900.814,01 , que equivale a 49,31 % do valor contratado.
**Ug:** UGOFF

## UNIDADE: [R.UGPES.01]

### Indicador

**Descrição Do Risco:** Não propor a  implantação da Politica de Gestão
 de Pessoas, bem como a avaliação periódica da 
política e do regimento de gestão de pessoas
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Elaborar a Politica de Gestão de Pessoas
**Quem:** Silvia 
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Estabelecer Direção e Orientação Claras:
Uma política de gestão de pessoas bem elaborada fornece direção e orientação claras sobre as práticas de RH da empresa, ajudando a alinhar os objetivos organizacionais com as necessidades e expectativas dos funcionários.

Promover Consistência e Justiça:
Uma política sólida ajuda a promover consistência e justiça no tratamento dos funcionários, garantindo que todos sejam tratados de forma equitativa e que as decisões sejam tomadas de maneira transparente e imparcial.

Atrair e Reter Talentos:
Uma política de gestão de pessoas bem estruturada pode ser uma ferramenta poderosa para atrair e reter talentos, pois demonstra o compromisso da empresa com o desenvolvimento e bem-estar de seus funcionários.

Minimizar Riscos Legais e Conformidade:
Uma política abrangente pode ajudar a minimizar os riscos legais e garantir a conformidade com as leis e regulamentações trabalhistas, reduzindo assim o potencial de litígios e penalidades.
**Como:** Análise das Necessidades e Objetivos da Empresa:
Realizar uma análise das necessidades e objetivos da empresa em relação à gestão de pessoas, levando em consideração a cultura organizacional, os valores da empresa e os desafios específicos do setor de tecnologia da informação em Mato Grosso.

Envolver Diversos Stakeholders:
Envolver uma variedade de stakeholders, incluindo funcionários, gestores, líderes de equipe e representantes de RH, no processo de elaboração da política para garantir que ela seja abrangente e representativa.

Definir Diretrizes e Procedimentos Claros:
Estabelecer diretrizes e procedimentos claros em áreas-chave, como recrutamento e seleção, desenvolvimento de funcionários, avaliação de desempenho, remuneração e benefícios, gestão de talentos e resolução de conflitos.

Comunicar e Treinar:
Comunicar a política de gestão de pessoas de forma clara e acessível a todos os funcionários e fornecer treinamento adequado sobre as diretrizes e procedimentos estabelecidos.

Revisar e Atualizar Regularmente:
Revisar e atualizar a política de gestão de pessoas regularmente para garantir que ela continue relevante e eficaz em atender às necessidades em evolução da empresa e de seus funcionários.
**Início:** 1/3/2024
**Fim:** 31/12/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 50,00%
**Observações:** 
50% DE EXECUÇÃO

MINUTA DA POLITICA DE GESTÃO DE PESSOAS

Os documentos estão sendo escrito por etapas.


A mioria estão publicados na  INTRANET aba Gestão de Pessoas

INTRANET




**Ug:** UGPES
**Situação Geral:** 69,76%
**Número De Ações:** 14.0
**Quantidade De Eventos De Riscos:** 14.0

## UNIDADE: [R.UGPES.02]

### Indicador

**Descrição Do Risco:** Não propor e implantar e definir a natureza de trabalho
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Propor a  Portaria de Ponto/Assiduidade
**Quem:** Silvia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Evitar multas e ações trabalhistas, bem apontamentos dos ógãos de controle, além de ser uma forma eficaz na Unidade de Gestão de Pessoas da MTI é fundamental para promover o alinhamento organizacional, aumentar o engajamento dos funcionários e impulsionar o sucesso da organização. Ao seguir uma abordagem estruturada e envolver os funcionários no processo, a MTI pode garantir que as atividades dos funcionários estejam alinhadas com os objetivos organizacionais, promovendo um ambiente de trabalho produtivo e eficaz.
**Como:** Acompanhar a  Publicação da Portaria de Ponto
**Início:** 1/3/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 
100% CONCLUIDO

Portaria Nº 203/2024 publicada em 22 de outubro de 2024
**Ug:** UGPES

## UNIDADE: [R.UGPES.03]

### Indicador

**Descrição Do Risco:** Baixo engajamento das equipes internas
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** 1) Propor a Poltica de Gestão de Pessoas 


**Quem:** Silvia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Melhoria do Desempenho Organizacional: Funcionários engajados tendem a ser mais produtivos, criativos e comprometidos com o sucesso da organização, o que contribui para um melhor desempenho geral da empresa.

Redução da Rotatividade: O engajamento dos funcionários está fortemente relacionado à retenção de talentos. Ao aumentar o engajamento, a empresa pode reduzir a rotatividade de funcionários e os custos associados à substituição e treinamento de novos colaboradores.

Criação de uma Cultura Positiva: Um ambiente de trabalho onde os funcionários se sintam engajados, valorizados e respeitados ajuda a promover uma cultura organizacional positiva, que por sua vez atrai talentos e promove a satisfação no trabalho.

Aumento da Satisfação do Cliente: Funcionários engajados tendem a oferecer um melhor atendimento ao cliente e a demonstrar um maior comprometimento com a excelência no trabalho, o que pode resultar em uma melhor experiência do cliente e maior fidelidade à marca.
**Como:** 

Escrever Politica de Gestão de Pessoas

2) Avaliação de Engajamento:
Realizar uma avaliação abrangente do engajamento dos funcionários para identificar áreas de melhoria e entender as causas subjacentes do baixo engajamento.

Desenvolvimento de Estratégias de Engajamento:
Desenvolver estratégias específicas de engajamento que promovam uma cultura organizacional positiva, reconheçam e valorizem as contribuições dos funcionários e incentivem a colaboração e o trabalho em equipe.

Comunicação Transparente e Aberta:
Promover uma comunicação transparente e aberta entre a liderança e os funcionários, garantindo que as informações relevantes sejam compartilhadas de forma clara e oportuna.

Fomento de um Ambiente de Trabalho Positivo:
Criar um ambiente de trabalho positivo e inclusivo, onde os funcionários se sintam valorizados, apoiados e encorajados a contribuir com suas ideias e feedback.

Oferta de Programas de Desenvolvimento Profissional:
Oferecer programas de desenvolvimento profissional e oportunidades de aprendizado contínuo para os funcionários, permitindo-lhes expandir suas habilidades e avançar em suas carreiras dentro da organização.

Reconhecimento e Recompensa:
Implementar programas de reconhecimento e recompensa que reconheçam e celebrem as conquistas dos funcionários e seu comprometimento com os objetivos organizacionais.

**Início:** 1/3/2024
**Fim:** 31/12/2025
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 50,00%
**Observações:** 
50% DE EXECUÇÃO

MINUTA DA POLITICA DE GESTÃO DE PESSOAS

Os documentos estão sendo escrito por etapas.


A mioria estão publicados na  INTRANET aba Gestão de Pessoas

INTRANET




**Ug:** UGPES

## UNIDADE: [R.UGPES.04]

### Indicador

**Descrição Do Risco:** Não executar o Plano Anual de Capacitação 
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Executar o Plano de Capacitação relativo ao ano de 2024
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir o indicador estratégico  (PDI)
**Como:** Elaborar e Executar o Plano de Capacitação 2023 
**Início:** 1/3/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** "


97,93% DE EXECUÇÃO DO PLANO DE CAPACITAÇÃO APROVADO
PLANO DE CAPACITAÇÃO
O Plano de Capacitação de 2024 foi apresentado em DIREX e já foi liberado para áreas demandantes o início de sua TRs


JANEIRO
Windows Server Hybrid Administrator Associate Módulo : AZ 801

MARÇO
Gestão de Documentos na prática"

ABRIL
Foundations of Incident Management e Advanced Topics in Incident Handling,

MAIO
Governo Digital
Formação em Métricas de Fluxo
Cursos Técnicas de Negociação, Liderança e Gestão de Vendas, Liderança e Coach, Roteirização de vendas e entregas
Seminário das Estatais

JUNHO
ORATÓRIA-COMUNICAÇÃO EFICAZ com TÉCNICAS DE PNL
AUTORESPONSABILIDADE E SUCESSO-PROMOVENDO ATITUDES PROATIVAS com TEAL"

JULHO
Congresso Matogrossense de Gestão de Pessoas
NO TOUR PODER E ALTA PERFORMANCE

AGOSTO
Evento Agile Trends GOV 2024, a ser realizado entre os dias 19 e 22 de Agosto de 2024, modalidade presencial.
Curso On Demand + Exame da CTFL
Certified ScrumMaster® CSM, 10(dez) vagas - Advanced Certified Scrum Master® A-CSM, 04 (quatro) vagas - Certified Scrum Product Owner® CSPO, 10 (dez) vagas - Advanced Certified Scrum Product Owner® A-CSPO, 03 (três) vagas
ITIL V4 FOUNDATION E PRACTITIONER
7º Encontro Nacional das Estatais.

SETEMBRO
"PLANO DE CAPACITAÇÃO
97,93% DE EXECUÇÃO DO PLANO DE CAPACITAÇÃO APROVADO
O Plano de Capacitação de 2024 foi apresentado em DIREX e já foi liberado para áreas demandantes o início de sua TRs

OUTUBRO
AGILE BRAZIL 2024”
CONTRATAÇÃO DE Plataforma online de treinamentos com foco em infraestrutura de TI.
CURSO GESTÃO ESTRATÉGICA DE CUSTOS
INTELIGÊNCIA EMOCIONAL,

NOVEMBRO
COMUNICAÇÃO PLENA, "

DEZEMBRO
Curso de Oratória - Comunicação Eficaz com Técnicas de PNL





**Ug:** UGPES

## UNIDADE: [R.UGPES.05]

### Indicador

**Descrição Do Risco:** Não realizar a Avaliação de Desempenho 2024
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Realizar a avaliação de Desempenho
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir o Regulamento de Avalaição de Desempenho
**Como:** Aplicar a avaliação de Desempenho
**Início:** 1/9/2024
**Fim:** 30/9/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 
100% DA META ALCANÇADA

A Avaliação de Desempenho é realizada no Mês 09/2024

- Portaria publicada no DO e na INTRANET
**Ug:** UGPES

## UNIDADE: [R.UGPES.06]

### Indicador

**Descrição Do Risco:** Não realizar a Pesquisa de Clima
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Realizar a Pesquisa de Clima
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir o Regulamneto de Pequisa de Clima
**Como:** 1) Defnir o questionário 
2) cadastrar no sistema ELOFY 
3) Aplicar a Pequisa  
4) Apurara o resultado  
5) Publicar na Intranet
**Início:** 1/5/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** A Pequisa de Clima foi aplicada em 05/2024  e 11/2024 até 06/12/2024


**Ug:** UGPES

## UNIDADE: [R.UGPES.07]

### Indicador

**Descrição Do Risco:** Não realizar o programa de Qualidade de Vida
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Executar o programa de qualidade de vida
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir o Programa de Qualidade de Vida
**Como:** Executar as ações que estão elecandas no Programa de Qualidade de Vida
**Início:** 2/1/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 
100 % DA META ALCANÇADA ATÉ 30/11/2024

QUALIDADE DE VIDA

Janeiro: 2
Campanha do Janeiro Branco - diversos conteúdos elaborados pelo psicólogo JONATAS, divulgados pela ASSCOM sobre o tema e finalizando na última sexta do mês com uma palestra sobre o tema e ginástica laboral todos vestidos com uma peça de roupa branca
Upgrade da Saúde: Projeto vida saudável - bioimpedância
 Fevereiro – 2 
Palestra Assédio Moral - entenda mais sobre o assunto e também divulgação de conteúdos sobre o tema roxo e laranja
Upgrade da Saúde: Projeto vida saudável - bioimpedância
Março
Dia internacional da mulher, entrega de bombom e mensagens para as mulheres da MTI, Campanha da Páscoa para crianças carentes com TEA.
Upgrade da Saúde: Projeto vida saudável - bioimpedância
Avaliação capilar e massagem craniana oferecida pela empresa mais cabelo
Doação de Sangue em Parceria com a Casa Civil
AbriL
Abril Verde - Informativos durante a semana sobre o tema
Conscientização sobre o autismo - Ginástica laboral com os balões verde e azul
Projeto Vida Saudável - SEPLAG - Exame de bioimpedância
Mais Cabello - Avaliação e Massagem Capilar
Maio
Alerta para doenças inflamatórias intestinais - Ginástica laboral com os balões amarelo e roxo
Projeto Vida Saudável - SEPLAG - Exame de bioimpedância
UPGRADE DA SAÚDE - Aferição de Pressão Arterial e Teste Glicêmico
Mais Cabello - Avaliação e Massagem Capilar
Comemoração do dia das Mães - coffee break e palestra - A importância da auto valorização da Mulher e Mãe
junho
almoço junino e laboral coletiva tema junino
Campanha Junho VERMELHO (doação de sangue)
Projeto Vida Saudável - SEPLAG - Exame de bioimpedância
UPGRADE DA SAÚDE - Aferição de Pressão Arterial e Teste Glicêmico
Julho
Contatos com entidades/órgãos para realização de convênios
Atualização calendário de ações de 2024
Atualização cronograma de palestrantes e realização do Momento de Espiritualidade
Realização do Upgrade da Saúde (Bioimpedância Seplag e Ginástica Laboral ( Setores e Coletiva)
Orientações Credenciamento Sesc
Encaminhamento para os colaboradores para autorização e foto Tempo de Serviço
Relação de aniversariantes de Julho (ASSCOM – DAFI – DTIC)
Relação de Tempo de Serviço Julho (ASSCOM)
Atualização Quem é Quem (ASSCOM)
Divulgação/Boas Vindas Novos colaboradores (ASSCOM)
Agosto
Contatos com novas entidades/órgãos para realização de convênios
Atualização cronograma de palestrantes e realização do Momento de Espiritualidade
Realização do Upgrade da Saúde (Bioimpedância Seplag e Ginástica Laboral ( Setores e Coletiva)
Orientações Credenciamento Sesc
Encaminhamento para os colaboradores para autorização e foto Tempo de Serviço
Relação de aniversariantes de agosto (ASSCOM – DAFI – DTIC)
Relação de Tempo de Serviço Agosto (ASSCOM)
Atualização Quem é Quem (ASSCOM)
Realização evento em comemoração ao dia dos PAIS
Participação na Elaboração do Programa de Sustentabilidade MTI - MTIGreen - 
Divulgação/Boas Vindas Novos colaboradores (ASSCOM) " 
setembro
Contatos com novas entidades/órgãos para realização de convênios Atualização cronograma de palestrantes e realização do Momento de Espiritualidade Realização do Upgrade da Saúde (Bioimpedância Seplag e Ginástica Laboral ( Setores e Coletiva) Encaminhamento para os colaboradores para autorização e foto Tempo de Serviço Relação de aniversariantes de Setembro (ASSCOM – DAFI – DTIC) Relação de Tempo de Serviço Setembro (ASSCOM) Atualização Quem é Quem (ASSCOM) Realização evento em comemoração ao dia dos PAIS Participação na Elaboração do Programa de Sustentabilidade MTI - MTIGreen - Realização da 3a. Semana da Integridade Realização da roda de conversa: Setembro amarelo: Nenhuma tempestade dura para sempre.
Outubro
Contatos com novas entidades/órgãos para realização de convênios
Atualização cronograma de palestrantes e realização do Momento de Espiritualidade
Realização do Upgrade da Saúde (Bioimpedância Seplag e Ginástica Laboral ( Setores e Coletiva)
Orientações Credenciamento Sesc
Encaminhamento para os colaboradores para autorização e foto Tempo de Serviço
Relação de aniversariantes de outubro (ASSCOM – DAFI – DTIC)
Relação de Tempo de Serviço Outubro (ASSCOM)
Atualização Quem é Quem (ASSCOM)
Realização evento Outubro Rosa - palestra sobre o tema
Participação na Elaboração do Programa de Sustentabilidade MTI - MTIGreen -
Divulgação/Boas Vindas Novos colaboradores (ASSCOM)
Participação da reunião comissão A3P
Abertura de convênio com escolas particulares
Novembro/2024
Palestra: Novembro azul - 62 participantes
UPgrade Saúde, ginástica laboral:142
Assistente Social: 01
02 Convênios: Escola Farina e Colégio Master
Momento de espiritualidade
Relação de aniversariantes de Novembro (ASSCOM – DAFI – DTI)
Atendimento psicológico: 04
Atualização Quem é Quem (ASSCOM)
Cronograma Ações/Datas Comemorativas MTI 2025
Cronograma Momento de Espiritualidade 2025
Cronograma Projeto Vida Saudável 2025 Seplag (Exame Bioimpedância)
Cronograma Posto Itinerante MT Saúde 2025

DEZEMBRO
Lançamento do projeto LUnnar - recolhimento de embalagens aerosol - sustentabilidade e apoio a proteção dos animais , Momento de espiritualidade Relação de aniversariantes de Dezembro (ASSCOM – DAFI – DTI) Atendimento psicológico: 04 Atualização Quem é Quem (ASSCOM) - Confraternização DAFI








**Ug:** UGPES

## UNIDADE: [R.UGPES.08]

### Indicador

**Descrição Do Risco:** Não gerenciar eleição da Comissão Interna de Prevenção
 de Acidentes (CIPA)
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Gerenciar a eleição da CIPA
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir a Legislação vigente
**Como:** 1 - A inscrição para o registro de candidatura dos colaboradores EFETIVOS da MTI/ 


2 - divulgar a lista dos candidatos à CIPA;
3) Emitir Ofício para informar o SINDPD sobre a eleição da CIPA na MTI, incluindo a relação dos candidatos e o cronograma da eleição;
4) Liberar o prazo para que os camdidatos realizem a campanha  CIPA, pelo meios de comunicação oficiais da empresa; 
5) Reazlizar a Eleição;
6) Divulgar o Resultado; 
7) Solcitar a Publicação no Diário Oficial

**Início:** 01/09/2024
**Fim:** 30/9/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 
100% DA META ALCANÇADA

A Eleição da CIPA é realizada no mês 09/2024

- Portaria Publicada no DO e na INTRANET
**Ug:** UGPES

## UNIDADE: [R.UGPES.09]

### Indicador

**Descrição Do Risco:** Não realizar a contratação de jovens aprendizes
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Realizar o processo seletivo
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir a Legislação vigente (cota)
**Como:** 1) Realizar cálculo  em conformidade com  a Lei (quantitativo)
2) Formar Comissão;
3) Acompanhar a  comissão  no processo seletivo
**Início:** 01/09/2024
**Fim:** 30/9/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 40,00%
**Observações:** - O processo seletivo deverá ser  realizado até 12/2024
- Publicação da Portaria desegnando os membros da Comissão
- Elaboramos o Edital que já foi envido para UNIJUR e PGE no entanto tivemos que remeter a SEPLAG . Estamos aguardando retorno 
**Ug:** UGPES

## UNIDADE: [R.UGPES.10]

### Indicador

**Descrição Do Risco:** Não contratação de apoio externo para ações de transformação cultural
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Contratar empresa para realizar as ações de transformação cultural
**Quem:** Ana Flávia
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Apoiar a transformação cultural
**Como:** Elaborar  Termos de Referencia conforme previsto  Plano de Capacitação  e da competências comportamentais identificadas no programa de Gestão por competências
**Início:** 01/04/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:**  
META 2024 70%
META ALCANÇADA ATÉ 30/11/2024 
88,30%

Do Montante de 171 Servidores avaliados no Programa Gestão Por Competências 2023/2024: 


171 Servidores com os PDIs Elaborados
150 Servidores com os PDIs concluidos de janeiro a dezembro (acumulado)
006 Servidores com os PDIs em andamento 
001 Servidores com os PDIs com iniciativas Cadastradas
014 Servidores com os PDIs incorretos sem iniciativa (criaram PDI, mas não fizeram nenhuma ação)
 
 
PDIs concluidos no mês 12/2024 = 01 colaborador


PDI - DEZEMBRO/2024
**Ug:** UGPES

## UNIDADE: [R.UGPES.11]

### Indicador

**Descrição Do Risco:** Não Gerenciar folha de Pagamento e  Encargos
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** CRÍTICO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** 1.        Implementação de Controle de Qualidade: Realizar cadastros com cautela, evitando registros de informações incorretas e garantindo conformidade com a regulamentação vigente (ACT/CLT).
2.        Capacitação da Equipe: Fornecer treinamento adequado aos funcionários responsáveis pela entrada de dados na folha de pagamento, assegurando que estejam familiarizados com os procedimentos corretos e as melhores práticas para evitar erros.
3.        Automação de Processos: Utilizar sistemas automatizados e integrados de gerenciamento de folha de pagamento, reduzindo a necessidade de inserção manual de dados e minimizando a probabilidade de erros.
4.        Implementação de Verificações Duplas: Estabelecer um processo de verificação dupla, onde um segundo membro da equipe revise os dados inseridos na folha de pagamento para identificar e corrigir possíveis erros antes da emissão dos pagamentos.
5.        Cálculo de Salários e Benefícios: Realizar os cálculos dos salários dos colaboradores, considerando horas trabalhadas, horas extras, sobreaviso e benefícios como vale-transporte e vale-alimentação, auxilio creche, PCD e outros.
6.        Descontos e Deduções: Aplicar descontos legais, como INSS, imposto de renda retido na fonte (IRRF) e contribuições sindicais, além de descontos autorizados pelos colaboradores, como plano de saúde e empréstimos consignados.
7.        Registro e Controle de Informações: Manter registros precisos e atualizados dos dados dos colaboradores, incluindo informações pessoais, contratuais, salariais e de benefícios.
8.        Conformidade Legal: Garantir o cumprimento das normas trabalhistas, previdenciárias e fiscais relacionadas à folha de pagamento, como emissão de guias de recolhimento de impostos e contribuições.
9.        Teto Constitucional: Verificar no fechamento da folha a questão do Teto Constitucional.
10.        Relacionamento com Órgãos Governamentais: Intermediar e comunicar-se com órgãos governamentais, como Ministério do Trabalho, Receita Federal e INSS, para cumprir obrigações legais e enviar informações exigidas por esses órgãos.
11.        Auditoria e Controle Interno: Realizar auditorias internas para garantir a precisão e integridade dos registros da folha de pagamento, bem como o cumprimento das políticas e procedimentos internos da empresa.

**Quem:** Rogério
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** 


1) Pagamentos incorretos aos funcionários, levando a insatisfação e possível perda de talentos.
2) Conflitos e disputas com funcionários devido a discrepâncias nos pagamentos.
3) Possíveis implicações legais e regulatórias decorrentes de não conformidade com obrigações trabalhistas e fiscais.
Impacto negativo na reputação da empresa e na confiança dos funcionários na gestão financeira da organização.

4 Evitar multas e ações trabalhistas, bem apontamentos dos ógãos de controle
**Como:** Cumpriur a legislação vigente e manter as informações no sistemas protheus atualizadas
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1) Adimila e Osmar serão responsáveis por lançar os dados na folha de pagamento, enquanto Rogério realizará a conferência da mesma.

2) Em 26/07/2024, durante uma conversa com o Diretor Administrativo, solicitei a possibilidade de conseguir um empregado público cedido para ser lotado na GPMM, com o objetivo de colaborar na execução da folha de pagamento. Em circunstâncias eventuais, como atestado médico, férias, licença assiduidade e outras, essa pessoa também poderá substituir Rogério.


3) A folha de pagamento 11/2024 passou pela auditoria da UGCOF e não houve nenhum apontamento e erros 
**Ug:** UGPES

## UNIDADE: [R.UGPES.12]

### Indicador

**Descrição Do Risco:** Não gerenciar ponto eletrônico e realizar debidos indevidos;
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Implementar Políticas Claras de Controle de Ponto: Estabelecer políticas claras e procedimentos para o registro e controle do ponto eletrônico, definindo regras específicas para horas de trabalho, intervalos e horas extras.

Automatizar o Registro de Ponto: Utilizar sistemas automatizados de registro de ponto eletrônico que garantam a precisão e integridade dos dados, minimizando a possibilidade de erros humanos.

Monitorar e Revisar Regularmente os Registros de Ponto: Realizar auditorias periódicas nos registros de ponto para identificar e corrigir possíveis discrepâncias ou irregularidades, garantindo a conformidade com as políticas estabelecidas.

Fornecer Treinamento e Conscientização: Capacitar os funcionários e gestores sobre as políticas e procedimentos de registro de ponto, destacando a importância da precisão e integridade dos registros para evitar descontos indevidos.

Implementar Controles de Aprovação: Estabelecer um processo de revisão e aprovação dos registros de ponto por parte dos gestores, garantindo que qualquer alteração ou desconto seja justificado e autorizado adequadamente.
**Quem:** Rogério
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Reduzir o descontentamento dos Funcionários: Descontos indevidos nos salários podem levar a insatisfação e desmotivação entre os funcionários, afetando o clima organizacional e a produtividade.

Riscos Legais e Trabalhistas: A realização de descontos indevidos nos salários pode resultar em processos judiciais, multas e penalidades por não conformidade com as leis trabalhistas e regulamentações vigentes.

Melhorar a Reputação da Empresa: Práticas inadequadas de gestão de ponto podem afetar negativamente a reputação da empresa, causando danos à imagem e credibilidade perante clientes, investidores e comunidade em geral.
**Como:** Realizando a Gestão de Ponto via sistemas Protheus
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 12,21%
**Observações:** PERIÓDICAMENTE: 

Osmar e Eloize
a) Monitorar diariamente os registros de ponto para identificar inconsistências ou ausências não justificadas.
b) Utilizar relatórios automatizados do sistema de ponto para facilitar a análise.
c) Cobrar dos empregados e gestores:que registrem  todas as correções de ponto de forma transparente e auditável
d) Manter uma comunicação contínua com os empregados sobre a importância do registro correto de ponto e as consequências de não cumprir as políticas.
e) Enviar lembretes periódicos sobre a política de ponto e procedimentos de correção.
f) Realizar auditorias periódicas para garantir que as práticas de registro de ponto estão sendo seguidas corretamente.
g) Verificar a conformidade com as leis trabalhistas e regulamentos internos.
h) Gerar e revisar relatórios mensais de ponto para análise de tendências, como padrões de absenteísmo e horas extras.
i) Utilizar esses relatórios para ajustes de políticas e identificação de necessidades de recursos adicionais.
j) Integrar os dados de ponto com o sistema de folha de pagamento para garantir que os cálculos de salários, horas extras e outras compensações sejam precisos.
l) Fornecer suporte contínuo para resolver problemas ou dúvidas dos empregados sobre o sistema de ponto.
m) Recolher feedback dos empregados para melhorias no processo de gestão de ponto.
n) Manter uma documentação completa e arquivar todos os registros de ponto e relatórios de auditoria, conforme exigido pela legislação.
o) Criar um manual detalhado de políticas e procedimentos de ponto.
P) Tivemos um treinamento via meet sobre a portaria de ponto e da inserção de informações no Portal RH

**Ug:** UGPES

## UNIDADE: [R.UGPES.13]

### Indicador

**Descrição Do Risco:** Não Monitorar a privacidade de dados
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Desenvolver Políticas de Privacidade de Dados Específicas: Criar políticas de privacidade de dados específicas para a Unidade de Gestão de Pessoas, abordando como os dados dos funcionários são coletados, armazenados, processados e protegidos.


Fornecer Treinamento Específico em Privacidade de Dados: Oferecer treinamento especializado em privacidade de dados para os funcionários da Unidade de Gestão de Pessoas, destacando a importância da proteção dos dados dos funcionários e os procedimentos corretos para lidar com informações confidenciais.


Implementar Controles de Acesso e Autorização: Estabelecer controles rigorosos de acesso e autorização para garantir que apenas funcionários autorizados tenham acesso aos dados pessoais dos funcionários, de acordo com as necessidades de trabalho.


Realizar Avaliações de Impacto de Privacidade de Dados: Conduzir avaliações de impacto de privacidade de dados para identificar e avaliar os riscos associados ao processamento de dados pessoais na Unidade de Gestão de Pessoas e implementar medidas de mitigação apropriadas.


Monitorar o Cumprimento da LGPD: Monitorar regularmente o cumprimento das disposições da LGPD e outras regulamentações relevantes de proteção de dados na Unidade de Gestão de Pessoas, garantindo conformidade com as leis e regulamentos aplicáveis.
**Quem:** Rogério
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Essas medidas visam criar um ambiente seguro e confiável para o tratamento dos dados pessoais dos funcionários na Unidade de Gestão de Pessoas, minimizando os riscos de violações de privacidade ou não conformidade com regulamentações de proteção de dados.
**Como:** Designar um profissional de privacidade de dados na Unidade de Gestão de Pessoas para liderar as iniciativas relacionadas à proteção de dados dos funcionários.
Estabelecer procedimentos claros para garantir a segurança e confidencialidade dos dados dos funcionários, incluindo a utilização de medidas técnicas e organizacionais apropriadas.
Manter registros detalhados das atividades de processamento de dados dos funcionários e garantir a transparência no tratamento desses dados.
Implementar políticas de retenção de dados para garantir que os dados dos funcionários sejam armazenados apenas pelo tempo necessário e de acordo com as obrigações legais e regulatórias.
Ao adotar essas medidas de mitigação, a Unidade de Gestão de Pessoas pode reduzir significativamente os riscos associados à falta de monitoramento da privacidade de dados dos funcionários e garantir a proteção adequada das informações confidenciais.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 12,21%
**Observações:** 1) As atividades estão sendo realizadas pela GPMM e GACD

2) Estamos em processo de mapemaneto do processos - LGPD

LGPD NOW: Mapeamento dos Processos de dados da Unidade e Resposta ao questionários de dados
 📑Atualizado dos  Contratos e Aditivos de Trabalho em conformidade com a LGPD

**Ug:** UGPES

## UNIDADE: [R.UGPES.14]

### Indicador

**Descrição Do Risco:** Não cumprir a Legislação (CLT/SST/ACT/CF-88)
**Categoria Do Risco:** CONFORMIDADE
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Manter-se Atualizada sobre a Legislação Pertinente:
Acompanhar e entender as mudanças na legislação trabalhista, de SST, ACT e CF-88 para garantir conformidade contínua.

Implementar Políticas e Procedimentos em Conformidade com a Legislação:
Desenvolver e implementar políticas e procedimentos que estejam alinhados com os requisitos legais e regulamentares aplicáveis.

Garantir a Conformidade nos Processos de Recrutamento e Seleção:
Assegurar que os processos de recrutamento e seleção respeitem os princípios da igualdade de oportunidades e não discriminação, conforme previsto na legislação.

Oferecer Treinamento sobre a Legislação Trabalhista e de SST:
Fornecer treinamento regular para funcionários e gestores sobre os requisitos da CLT, SST, ACT e CF-88, bem como sobre as políticas e procedimentos internos relacionados.

Implementar Sistemas de Monitoramento e Controle:
Estabelecer sistemas e procedimentos para monitorar e garantir o cumprimento das leis trabalhistas, de SST, ACT e CF-88 em toda a organização.
**Quem:** Rogério
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Cumprir a legislação trabalhista, de SST, ACT e CF-88 é fundamental para garantir um ambiente de trabalho justo, seguro e legalmente adequado.

O não cumprimento da legislação pode resultar em penalidades legais, multas e litígios trabalhistas, que podem ter impactos financeiros significativos na organização.

Além disso, manter a conformidade com a legislação ajuda a proteger a reputação e a credibilidade da empresa perante funcionários, clientes, acionistas e outras partes interessadas.
**Como:** Acompanhar as  publicações e alterações nas Legislação 

Designar um profissional qualificado ou equipe responsável por acompanhar e interpretar a legislação trabalhista e de SST.

Realizar auditorias internas regulares para avaliar a conformidade com a legislação e identificar áreas de não conformidade.

Estabelecer canais de comunicação eficazes para que os funcionários possam relatar preocupações relacionadas ao cumprimento da legislação.

Colaborar com departamentos jurídicos e consultores especializados, conforme necessário, para garantir que as políticas e procedimentos estejam em conformidade com a legislação aplicável.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 12,21%
**Observações:** Acompanhar as mudanças na Legislação pelos meios disponiveis (internet) e se necessário participar de cursos de aperfeiçoamento
**Ug:** UGPES

## UNIDADE: [R.UGPRO.01]

### Indicador

**Descrição Do Risco:** Ausência de acompanhamento de projetos estratégicos.
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Acompanhamento de Projetos Estratégicos
**Quem:** Gerente da UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Assegurar junto aos Times de Projetos as Entregas pactuadas junto aos Clientes.
**Como:** 1 - Acompanhamento semanal junto com Diretor de TI e Gerentes de Áreas.
2 - Implementação de Melhorias no Service Now, com intuito de garantir uma fluidez na execução de monitoramento pelos Times de Projetos.
3 - Reunião semanal de Status Report com o Presidente dos Projetos Estratégicos.
**Início:** 01/05/2024
**Fim:** 31/05/2024
**Quanto:** R$ -
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGPRO
**Situação Geral:** 57,14%
**Número De Ações:** 7.0
**Quantidade De Eventos De Riscos:** 7.0

## UNIDADE: [R.UGPRO.02]

### Indicador

**Descrição Do Risco:** Contratualização com o parceiro da ServiceNow 
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Contratação de Horas e Serviços Técnicos com Parceiro Service Now.
**Quem:** Gerente da UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para dar continuidade aos projetos do MTI
**Como:** 1 - Alinhamento com a Presidência MTI, apresentando dados e necessidades de utilização de Horas Técnicas do Parceiro no Service Now.
2 - Confecção de TR de contratação de Horas e Serviços Técnicos do Parceiro da Service Now.
3 - Planejamento na utilização de Horas e Serviços Ténicos Contratados: Implantação, Suporte e Melhorias.
**Fim:** 10/05/2024
**Quanto:** R$ -
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1. Termo de Referência encontra-se parcialmente confeccionado; Atualmente não existe orçamento previsto para contratação dos produtos e serviços, em contrapartido,a UGPRO em conjunto com a DTIC, está realizando levantamento dos contratos de TI que ainda não foram executados para utilização do Saldo Orçamentário e posteriormente apresentação de proposta a Presidência.

2. [08.07.2024] - Termo de Referência concluído e tramitado para análises e deliberações.
**Ug:** UGPRO

## UNIDADE: [R.UGPRO.03]

### Indicador

**Descrição Do Risco:** Mudanças na legislação e regulamentação
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Adequações a novas possíveis legislações 
**Quem:** Equipe da UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** As alterações nas Leis e Regulamentos Governamentais podem gerar impactos nos projetos em andamentos, exigindo ajustes nos planos e nas operações do PMO.
**Como:** 1 - Acompanhamento semanal junto com Diretor de TI e Gerentes de Áreas, levantando os potenciais problemas e riscos alinhados ao Cliente.
2- Atualização semanal do cronograma de execução física do Projeto.
**Início:** 01/05/2024
**Fim:** 31/05/2024
**Quanto:** R$ -
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGPRO

## UNIDADE: [R.UGPRO.04]

### Indicador

**Descrição Do Risco:** Mudanças nas demandas do mercado
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Solicitar mais de um fornecedor externo de tecnologia, hardware ou servidores 
**Quem:** Equipe UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para evitar falhas e riscos nos projetos 
**Como:** 1 - Sempre se atentando a mudanças no mercado.
**Quanto:** R$ -
**Situação:** CANCELADA
**Percetual De Execução:** 0,00%
**Ug:** UGPRO

## UNIDADE: [R.UGPRO.05]

### Indicador

**Descrição Do Risco:** Problemas de integração de sistemas
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Gestão de Mudança em situações de integração de Sistemas com o Service Now, que devido a ausência de especificação e/ou refinamento das necessidades, podem impactar nas automações da ferramenta.
**Quem:** Equipe da UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Impactos em rotinas de processos, utilização da ferramenta que podem chegar ao Cliente.
**Como:** 1 - Implementação de Gestão de Mudança de todas iniciativas de Melhorias no Service Now
**Quanto:** R$ -
**Situação:** CANCELADA
**Percetual De Execução:** 0,00%
**Observações:** 1. Implementação não realizando, devendo ser iniciada a partir do momento da conclusão da aquisição do Contrato de Consumo de Horas e Licenças do SN.

2. Iniciativa cancelada, em decorrência de reestruturação de nova estratégia de execução de Contrato com Parceiro da ServiceNow.
**Ug:** UGPRO

## UNIDADE: [R.UGPRO.06]

### Indicador

**Descrição Do Risco:** Riscos de fornecedores (Fábrica de Software)
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Adaptação e utilização de melhores equipamentos para comunicação
**Quem:** Equipe UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para manter a clareza e e praticidade nas reuniões 
**Como:** 1 - Solicitando sempre manutenção dos equipamentos.
**Quanto:** R$ -
**Situação:** CANCELADA
**Percetual De Execução:** 0,00%
**Ug:** UGPRO

## UNIDADE: [R.UGPRO.07]

### Indicador

**Descrição Do Risco:** Aculturamento na metodologia de gestão de projetos/ágil
**Categoria Do Risco:** ESTRATÉGICO
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Cultura engessada e sem engajamento 
a novos desafios, inovação e Gestão de 
Mudança
**Quem:** Equipe UGPRO
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** A resistência à mudança dentro da organização pode 
dificultar a implementação bem-sucedida de novas 
tecnologias ou processos, exigindo esforços extras de 
gerenciamento de mudanças.
**Como:** 1 - Promover Workshop sobre o Service Now.
2 - Comunicação nas principais Melhorias implementadas no Service Now.
3 - Implementação de Melhorias que agreguem valor aos usuários do Service Now
**Início:** 01/05/2024
**Fim:** 31/08/2024
**Quanto:** R$ -
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1. Implementação de novo Fluxo de Projetos no ServiceNow, próximos passos é a realização de capacitação, em conjunto com a DTIC, aos usuário.

2. Readequação de prazo para dia 31.08.2024.

3. Divulgados em julho o Guia de Gestão de Projeros + Painel de Dados BIP - Boletim Informativo de Projetos.

4. Elaboração de material de treinamento para disseminação da MTI.

5. Alinhamento com a VAExpert a disseminação da metodologia ágil
**Ug:** UGPRO

## UNIDADE: [R.UGSDG.01]

### Indicador

**Descrição Do Risco:** Falta de vazão na entrega dos serviços por meio de parceria
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Adequar tamanho dos pacotes de entrega confome capacidade das sprint
**Quem:** UGSDG
**Qual Ativo Crítico Afetado Pelo Risco:** UGSDG
**Por Que:** para entregar constantemente
**Como:** 1-Orientar equipe interna
2-Orientar Parceira
3-Incluir o acordo na reunião de Kick Off
3-Acompanhar tamanho dos pacotes de entrega
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 92%
**Observações:** 23/04/2024 Atualizado.
06/09/2024 Atualizado.
08/10/2024 - Atualizado
22/11/2024 - Atualizado.
**Ug:** UGSDG
**Situação Geral:** 72,22%
**Número De Ações:** 6.0
**Quantidade De Eventos De Riscos:** 6.0

## UNIDADE: [R.UGSDG.02]

### Indicador

**Descrição Do Risco:** Falta de vazão na entrega dos serviços por meio de parceria
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Automatizar processo por meio de ferramentas
**Quem:** UGSDG
**Qual Ativo Crítico Afetado Pelo Risco:** UGSDG
**Por Que:** para aumentar a fluidez do processo
**Como:** 1-Estudar Ferramentas disponiveis no mercado
2-Identificar o que pode ser automatizado no Service Now
3-Executar as adequações
4-Treinar Equipe
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 35%
**Observações:** 24/04/2024  - Atualizado.
A automatização de esteira, está sendo conduzida pela equipe UGARQ.
06/09/2024 Atualizado. Reforço recebido dos novos contatados.
08/10/2024 - Atualizado
22/11/2024 - Atualizado
**Ug:** UGSDG

## UNIDADE: [R.UGSDG.03]

### Indicador

**Descrição Do Risco:** Dificuldade para estabelecer pacotes de entrega de valor para o cliente
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Capacitar Perfil PO
**Quem:** UGSDG
**Qual Ativo Crítico Afetado Pelo Risco:** UGSDG
**Por Que:** para entregar valor para o negocio
**Como:** 1-Identificar capacitações e informar no plano de Capacitação
2-Adquirir treinamentos /certificações
3-Realizar treinamentos / certificação
**Início:** 01/03/2024
**Fim:** 31/10/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Observações:** 23/04/2024  Atualizado.
06/09/2024Atualizado. Contratações em andamento.
08/10/2024 - Atualizado
22/11/2024 - Atualizado
**Ug:** UGSDG

## UNIDADE: [R.UGSDG.04]

### Indicador

**Descrição Do Risco:** Dificuldade para estabelecer pacotes de entrega de valor para o cliente
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Avaliar a percepção do valor entregue
**Quem:** UGSDG
**Qual Ativo Crítico Afetado Pelo Risco:** UGSDG
**Por Que:** para aferir satisfação do cliente
**Como:** 1-Definir pesquisa 
2-Avaliar mensalmente
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 92%
**Observações:** 23/04/2024 -Atualizado.
06/09/2024-Atualizado.
08/10/2024 - Atualizado
22/11/2024 - Atulizado.
**Ug:** UGSDG

## UNIDADE: [R.UGSDG.05]

### Indicador

**Descrição Do Risco:** Falta de Integração dos processos (DEV, Comercial e Central)
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Integrar esteira dev e comercial
**Quem:** UGSDG
**Qual Ativo Crítico Afetado Pelo Risco:** UGSDG
**Por Que:** para desenvolver somente o que foi contratado ou autorizado comercialmente
**Como:** 1-Definir os pontos possiveis de integração das equipes
2-Implantar Fluxo de Ordem de serviço
3-Implantar Fluxo de Faturamento
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 15,00%
**Observações:** 23/04/2024 Atualizado.
06/09/2024 Atualizado.
08/10/2024 - Atualizado - Esse assunto náo andou quase nada. 
22/11/2024 - Atualizado - Esse assunto náo andou quase nada. 
**Ug:** UGSDG

## UNIDADE: [R.UGSDG.06]

### Indicador

**Descrição Do Risco:** Falta de vazão na entrega dos serviços por meio de parceria
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Solicitar contratação de Pessoas para atuarem como Líder de Celula e Tech Lead
**Quem:** UGSDG
**Qual Ativo Crítico Afetado Pelo Risco:** UGSDG
**Por Que:** para manter a capacidade de atuação, considerando o encerramento do contrato  temporário atual
**Como:** 1-Especificar perfil de Lider de Celula e Tech Lead
2-Reportar produtos /projetos impactados
**Início:** 01/03/2024
**Fim:** 30/04/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 24/04/2024 
Atualizado.
06/09/2024
Atualizado.
**Ug:** UGSDG

## UNIDADE: [R.UGSTI.01]

### Indicador

**Descrição Do Risco:** Parada de Firewall (UGGDC)
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Fazer cópias quinzenais das VMs que hospedam a ferramenta; Monitorar status de funcionamento dos firewalls gerenciados pela GSUP
**Quem:** GSUP
**Qual Ativo Crítico Afetado Pelo Risco:** Vcenter MTI
**Por Que:** Para ter como restaurar em caso de dano no ambiente original; Para acompanhar a disponibilidade dos firewalls
**Como:** Registrando chamado para a equipe que gere a Vcenter que hospeda a solução para agendar a execução do procedimento mensalmente; Através do acompanhamento de disponibilidade de funcionamento dos firewalls, gerados pela monitoria do Zabbix.

**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Processo executado, porém sem atingir a meta de contratação que era de 65 analistas temporários, sendo contratados apenas 31. "Feito o relatorio mensal sobre a disponibilidade dos Firewalls dos Clientes/Setorial na planilha
https://docs.google.com/spreadsheets/d/1YVhjTOhok5tPOz28j4gA2EaWMfX5gxq91xaeiS1un04/edit#gid=2108066493 "
**Ug:** UGSTI
**Situação Geral:** 100,00%
**Número De Ações:** 8.0
**Quantidade De Eventos De Riscos:** 8.0

## UNIDADE: [R.UGSTI.03]

### Indicador

**Descrição Do Risco:** Parada do Servidor do Antivirus (UGGDC)
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** Fazer cópias mensais das VMs que hospedam a ferramenta
**Quem:** GSUP
**Qual Ativo Crítico Afetado Pelo Risco:** Vcenter MTI
**Por Que:** Para ter como restaurar em caso de dano no ambiente original. Assegurar o bom funcionamento da ferramenta e evitar que a ferramenta fique sem analista para futuras manutenções e/ou atualizações.
**Como:** Registrando chamado para a equipe que gere a Vcenter que hospeda a solução para agendar a execução do procedimento mensalmente

**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Será feito um relatorio mensal para monitoramento e evidencias.
**Ug:** UGSTI

## UNIDADE: [R.UGSTI.05]

### Indicador

**Descrição Do Risco:** Baixa adesão Suporte do Google Workspace
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Capacitar técnicos e analistas em trilhas de conhecimento das ferramentas do Google Workspace 
**Quem:** UGSTI
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Assegurar o bom funcionamento da solução e prestar um melhor atendimento aos usuários sobre as ferramentas disponibilizadas pela solução de colaboração
**Como:** Através da realização de treinamentos e compartilhamento de conhecimento dentro das equipes  conforme o plano de capacitação da MTI e busca de auxílio por parte da parceria Google
**Início:** 01/01/2024
**Fim:** 01/07/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Está sendo realizado treinamento periódicos com a equipe.
**Ug:** UGSTI

## UNIDADE: [R.UGSTI.06]

### Indicador

**Descrição Do Risco:** Parada de ativos de rede da MTI (ex: switches)
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Monitorar proativamento os status de funcionamento dos ativos de rede da MTI
**Quem:** GSUP
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para acompanhar a disponibilidade dos ativos de rede
**Como:** Através do acompanhamento de disponibilidade de funcionamento dos ativos de rede, gerados pela monitoria do Zabbix
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Realizado criação e configuração Dashboard.
**Ug:** UGSTI

## UNIDADE: [R.UGSTI.12]

### Indicador

**Descrição Do Risco:** Perda de backups Firewall´s
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Certificar junto a GPAC a realização e o armazenamento dos backups (diários, semanais e mensais dos arquivos e sistemas sensíveis).Realizar testes regulares mensais para se certificar que as cópias de segurança estão operacionais.
**Quem:** GSUP
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Assegurar disponibilidade das cópias de segurança de informações, dados e apps de utilização da UGSTI. Assegurar que as cópias de segurança realizadas estão operacionais.
**Como:** Informar sempre que necessário a equipe responsável pelo ambiente de hospedagem das soluções e ferramentas de utilização da UGSTI sobre as necessidades de cópias recorrentes e das eventuais para se evitar perda de dados ou parada de serviços. Realizar restauração sistemática amostral de backups realizados de forma a se assegurar de que os mesmos estejam operacionais.
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Está sendo realizado bkp de 15 em 15 dias pela GSUP.
**Ug:** UGSTI

## UNIDADE: [R.UGSTI.18]

### Indicador

**Descrição Do Risco:** Indisponibilidade de ativos de TI por ausência de equipamentos e peças reservas
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Assegurar a disponibilidade de equipamentos reservas e peças sobressalentes
**Quem:** UGSTI
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para que sempre se tenha equipamentos e peças de reserva para que não haja parada crítica das atividades da empresa ou de seus clientes
**Como:** 1- Confecção de novo termo de referência para aquisição de peças para manutenção;
2- Adquirir equipamentos e peças para assegurar continuidade das atividades da MTI e clientes;


**Início:** 01/01/2024
**Fim:** 30/08/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Realizada a compra de periféricos (fone de ouvidos, teclados com fio, mousescom fio, kit teclado/ mouse sem fio).
**Ug:** UGSTI

## UNIDADE: [R.UGSTI.21]

### Indicador

**Descrição Do Risco:** Prestação de serviço indevido, por falta de controle automatizado de Saldo de contas Google
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Assegurar que a planilha está atualizada para ter certeza que os clientes estão com saldo de contas
**Quem:** UGSTI
**Qual Ativo Crítico Afetado Pelo Risco:** GSUP
**Por Que:** Atualizar a planilha constantemente conforme a criação das contas para cada cliente
**Como:** 1 - Automatização do processo de atualização de contas
**Início:** 01/01/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Planilha segue sendo atualizada diariamente.
**Ug:** UGSTI

## UNIDADE: [R.UGSTI.23]

### Indicador

**Descrição Do Risco:** Baixo Engajamento das equipes internas
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Adotar ações que possibilitem o desenvolvimento das competencias e engajamento dos técnicos/analistas
**Quem:** UGSTI
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para ampliar o comprometimento e motivação em realizar suas tarefas e contribuir para os objetivos gerais da MTI. Resultando em um ambiente de trabalho colaborativo e produtivo.
**Como:** 1 - Definindo objetivos e metas de forma clara e aberta 
2 - Reconhecimento e Feedback reconhecer as realizações das equipes
3 - Desenvolvimento profissional oferencendo oportunidades

**Início:** 01/05/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UGSTI

## UNIDADE: [R.UGVEN.01]

### Indicador

**Descrição Do Risco:** Serviços prestados sem cobertura contratual pelos Clientes
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**O Que:** Existem clientes sem contrato ou com contratos deficitários em serviços e/ou quantitativos prestados X serviços contratados
**Quem:** UGVEN
**Por Que:** 1. Não prestarmos serviço sem cobertura contratual ou com quantitativos menores  
2. Não termos problemas no faturamento
3. Priorização dos projetos contratados
**Como:** - Negociar com os clientes para que seja elaborado aditivos de contrato ou novos contratos;
- Definir processos/procedimentos para cobrar e agilizar a contratação dos serviços
**Início:** 22/01/2024
**Fim:** 13/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 90,00%
**Observações:** Apenas Empaer sem contrato formal
**Ug:** UGVEN
**Situação Geral:** 65,71%
**Número De Ações:** 7.0
**Quantidade De Eventos De Riscos:** 7.0

## UNIDADE: [R.UGVEN.02]

### Indicador

**Descrição Do Risco:** Contratos não são assinados no prazo necessário
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**O Que:** Serviços prestados sem contrato
**Quem:** UGVEN
**Por Que:** Processo para contratação da MTI é lento e burocrático
**Como:** - Verificar outra forma de receber os serviços prestados pela MTI (Fundo de TI);
- Encaminhar o KIT contratação 
- Verificar parecer referencial da PGE
**Início:** 14/02/2024
**Fim:** 13/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 30,00%
**Observações:** Kits contratação em elaboração
**Ug:** UGVEN

## UNIDADE: [R.UGVEN.03]

### Indicador

**Descrição Do Risco:** Execução do serviço não compatível com a expectativa do cliente
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Acompanhar o cronograma e as entregas dos serviços contratados
**Quem:** UGVEN
**Por Que:** Fazer as adequações do projeto e/ou prazos
**Como:** Agendar reuniões sistemáticas (quinzenal ou mensal) de acompanhamento dos projetos
**Início:** 22/01/2024
**Fim:** 13/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 50,00%
**Observações:** Consultores iniciaram agendas com clientes em projetos em andamento
**Ug:** UGVEN

## UNIDADE: [R.UGVEN.04]

### Indicador

**Descrição Do Risco:** Não atualização de portfólio de serviços
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**O Que:** Revisar  Catálogo de serviços e preço dos produtos para sermos competitivos com o mercado
**Quem:** UGVEN
**Por Que:** Portfólio de serviços desatualizado
**Como:** Revisando o portfólio da MTI, mantendo os serviços atualizados e verificando os preços praticados estão adequados com os valores de mercado
**Início:** 22/01/2024
**Fim:** 13/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 80,00%
**Observações:** catálogo aprovado Direx, porém necessita de constante acompanhamento
**Ug:** UGVEN

## UNIDADE: [R.UGVEN.05]

### Indicador

**Descrição Do Risco:** Entregas dos serviços das parcerias fora do prazo acordado ou de baixa qualidade
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** MODERADO
**O Que:** Acompanhar o cronograma e as entregas dos serviços das parcerias
**Quem:** UGVEN
**Por Que:** Fazer as adequações do projeto e/ou prazos
**Como:** Agendar reuniões sistemáticas (quinzenal ou mensal) de acompanhamento dos projetos
**Início:** 22/01/2024
**Fim:** 13/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 70,00%
**Observações:** No que tange ao comercial, a equipe de vendas e pós vendas estão realizando agendas com clientes 
**Ug:** UGVEN

## UNIDADE: [R.UGVEN.06]

### Indicador

**Descrição Do Risco:** Frustração da realização das receitas previstas
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**O Que:** Celebrar novos contratos com os clientes
Celebrar contratos dos serviços/quantitativos sem cobertura contratual
**Quem:** UGVEN
**Por Que:** Aumentar a receita dos serviços
**Como:** - Identificar as oportunidades com as novas parcerias e os clientes que não tem serviços todos os serviços disponíveis.
- Celebrar novos contratos com os clientes
atualizar no Infocenter os ativos que não estão cadastrados corretamente e celebrar contratos ou aditivos dos serviços/quantitativos sem cobertura contratual
**Início:** 22/01/2024
**Fim:** 13/12/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 60,00%
**Observações:** Novas propostas e contratos oriundos de parcerias estão surgindo.
**Ug:** UGVEN

## UNIDADE: [R.UGVEN.07]

### Indicador

**Descrição Do Risco:** Baixo engajamento das equipes internas
**Categoria Do Risco:** ESTRATÉGICO
**O Que:** Baixo engajamento da equipe
**Quem:** UGVEN
**Por Que:** - Equipes internas desmotivadas
- Baixo interesse em ajudar outras equipes
- Falta de espírito colaborativo
**Como:** - Realização de treinamentos motivacionais
- Dar e receber feedback
- Reuniões com a equipe e individuais para monitoramento
**Início:** 01/03/2024
**Fim:** 29/11/2024
**Situação:** EM ANDAMENTO
**Percetual De Execução:** 80,00%
**Observações:** Reuniões com equipe e individuais
Feedback com equipe
Elaboração do PDI de todos da equipe

**Ug:** UGVEN

## UNIDADE: [R.UNICRS.01]

### Indicador

**Descrição Do Risco:** Não  elaborar e acompanhar os  indicadores do  programa de integridade da MTI.
**Categoria Do Risco:** OPERACIONAL
**Risco Inerente:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** - Criar o indicador de integridade e realizar o acompanhamento.
**Quem:** ANA BEATRIZ E IONE COSTA
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** - Evitar a ocorrência de devios de integridade; 
- Fortalecer e disseminação o programa de integridade no âmbito da MTI, incentivando uma cultura ética.
- Alcance dos objetivos estratégicos promovendo o engajamento dos colaboradores e assim a melhorando a qualidade das entregas.
**Como:** 1. Elaborar sistematica de controle no plano anual de integridade
**Início:** 01/03/2024
**Fim:** 30/04/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Ug:** UNICRS
**Situação Geral:** 100,00%
**Número De Ações:** 4.0
**Quantidade De Eventos De Riscos:** 4.0

## UNIDADE: [R.UNICRS.03]

### Indicador

**Descrição Do Risco:** Falha no acompanhamento mensal dos riscos e encaminhamento do relatório trimestral à alta direção.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** MODERADO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Acompanhamento mensal e elaboração de relatório trimestral à DIREX.
**Quem:** ANA BEATRIZ E KAMILLA
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** - Avaliar a aderência dos gerentes administrativos ao gerenciamento de riscos corporativos; 
- Acompanhar a evolução do tratamento dos riscos corporativos;
- Fornecer informações aos Diretores sobre o gerenciamento de riscos corporativos.
**Como:** 1. Realizar a atualização do mapa de gestão, mensalmente, sobre o preenchimento do plano de ação por cada UA;
2. Fazer o levantamento do andamento mensal do preenchimento por cada UA, em pasta apropriada, para subsidiar relatório trimestral;
3. Consolidar relatório trimestral e encaminhar aos Diretores, constando o andamento do tratamento dos riscos de cada UA, para deliberações internas com o UG responsável:
     1. JUNHO (mar, abr, mai)
     2. SETEMBRO (jun, jul, ago)
     3. Dezembro (set, out, nov, dez)
**Início:** 01/03/2024
**Fim:** 20/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1 - Mapa de gestão: realizada a avaliação de dezembro; 3,7% para cada mês avaliado.  

2 - Levantamento de informações para subsidiar o relatório trimestral: Foram coletadas as informações do painel de riscos em 09/01/2025, referente ao mês de outubro; 3,7% para cada mês coletado. 

3 - Relatório trimestral: em elaboração o terceiro relatório trimestral da GIRC-2024. 
**Ug:** UNICRS

## UNIDADE: [R.UNICRS.04]

### Indicador

**Descrição Do Risco:** Execução parcial do plano de segurança da informação.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** 1.Realizar as reuniões periódicas do Comitê de Segurança e Riscos;
2. Acompanhar e cobrar a execução do plano de segurança da informação para o ano vigente.
**Quem:** ANA BEATRIZ, IONE E LARISSA
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Promover conformidade com as melhores práticas de segurança da informação
**Como:** 1. Aprovação do plano anual da unidade pelo Presidente
2. Atualização dos membros do Comitê de Segurança da informação e Riscos;
3. Atualização do RI do Comitê de Segurança e Riscos;
4. Aprovação do Plano Anual da SI pelo presidente.

**Início:** 01/03/2024
**Fim:** 20/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1 - Aprovado o plano anual de SI da UNICRS. 25%

2 - Atualizado os membros do comitê de segurança da informação e riscos, portaria nº 025/2024/MTI. 25%

3 - Elaborado e validado pelos membros o Regimento Interno do Comitê de Segurança da Informação e Riscos; aprovado pela DIREX. 25%

4  - Validado o Plano Anual do CSIR. 25%
**Ug:** UNICRS

## UNIDADE: [R.UNICRS.05]

### Indicador

**Descrição Do Risco:** Falha na disseminação/treinamento de segurança da informação.
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** SIM
**O Que:** 1. Disseminar a todos os colaboradores as políticas e regulamentos instituídos sobre Segurança da Informação;
2. Promover palestras e treinamentos sobre segurança da informação aos colaboradores.
**Quem:** ANA BEATRIZ, IONE E LARISSA
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Promover conscientização dos empregados
**Como:** 1. Aprovação do plano anual da unidade pelo Presidente
2. Elaboração periódica (MENSAL) de material a ser disseminado via e-mail - projeto "tome nota"
3. Convidar palestrantes para tratar de temas relacionados a segurança da informação;
4. Realizar treinamento interno sobre políticas instituídas na MTI. 
**Início:** 01/03/2024
**Fim:** 20/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** 1 - Aprovado o plano anual da UNICRS. 

2 - foi disseminado, mensalmente, o sétimo material referente ao projeto "tome nota".  


**Ug:** UNICRS

## UNIDADE: [R.UNIJUR.01]

### Indicador

**Descrição Do Risco:** Deficiência na defesa jurídica da empresa
**Categoria Do Risco:** CONFORMIDADE
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Monitoramento de prazo judicial
**Quem:** Assessor Juridico I
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Para não perder prazos judiciais.
**Como:** 1. Por meio de planilha de registro de atividades já elaborada.
2. Emitir alertas ao assessor do prazo que está esgotando.
3. Avisar a PGE do prazo encaminhado.
4. Verificar se a PGE protocolou dentro do prazo.

**Início:** 01/03/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Observações:** Realizado diariamente
**Ug:** UNIJUR
**Situação Geral:** 97,50%
**Número De Ações:** 4.0
**Quantidade De Eventos De Riscos:** 4.0

## UNIDADE: [R.UNIJUR.02]

### Indicador

**Descrição Do Risco:** Não cumprimento da análise jurídica dentro do prazo legal de 12 dias úteis ou do prazo alinhado com a DIREX
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** CRÍTICO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Parecer jurídico no prazo
**Quem:** Assessores jurídicos
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Atender o interesse público
**Como:** 1 - Oferecer treinamento para as áreas demandantes visando disseminar o conhecimento da legislação, visando minimizar os erros.                                                                                             2 - Elaborar cartilhas de orientação para a boa instrução processual;
**Início:** 01/03/2024
**Fim:** 30/04/2024
**Situação:** ATRASADA
**Percetual De Execução:** 90%
**Observações:** Processo retornou da PGE com manifestação não conclusiva para revisão, após retornaremos a PGE para manifestação conclusiva
**Ug:** UNIJUR

## UNIDADE: [R.UNIJUR.03]

### Indicador

**Descrição Do Risco:** Não cumprimento de intimação judicial feita pelo cadastro da PGE/MT
**Categoria Do Risco:** OPERACIONAL
**Risco Residual:** ALTO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Acompanhamento semanal de todos os andamentos dos processos
**Quem:** UNIJUR
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** Não perder prazo judicial
**Como:** 1 - Divisão dos processos entre os assessores                                       2 - Conferência semanal nos sites dos Tribunais de cada processo
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Quanto:** R$ 0,00
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100%
**Observações:** Realizado diariamente
**Ug:** UNIJUR

## UNIDADE: [R.UNIJUR.04]

### Indicador

**Descrição Do Risco:**  Baixo engajamento das equipes internas
**Categoria Do Risco:** ESTRATÉGICO
**Risco Residual:** PEQUENO
**Risco De Segurança Da Informação Si:** NÃO
**O Que:** Comunicação entre a equipe
**Quem:** UNIJUR
**Qual Ativo Crítico Afetado Pelo Risco:** MTI
**Por Que:** engajar toda a equipe
**Como:** Troca de informações e atualizações diárias de todos os assuntos que ocorrem no setor com o envolvimento de toda a equipe. Participação nos eventos da empresa.
**Início:** 01/03/2024
**Fim:** 31/12/2024
**Situação:** CONCLUÍDA
**Percetual De Execução:** 100,00%
**Observações:** Realizado semanalmente
**Ug:** UNIJUR
