import streamlit as st
import streamlit.components.v1 as stc 


about = """

#### O que é diabetes?
Diabetes é uma doença causada pela produção insuficiente ou má absorção de insulina, hormônio que regula a glicose no sangue e garante energia para o organismo.
A insulina é um hormônio que tem a função de quebrar as moléculas de glicose(açúcar) transformando-a em energia para manutenção das células do nosso organismo.
O diabetes pode causar o aumento da glicemia e as altas taxas podem levar a complicações no coração, nas artérias, nos olhos, nos rins e nos nervos. Em casos mais graves, o diabetes pode levar à morte.
De acordo com a Sociedade Brasileira de Diabetes, existem atualmente, no Brasil, mais de 13 milhões de pessoas vivendo com a doença, o que representa 6,9% da população nacional.
A melhor forma de prevenir é praticando atividades físicas regularmente, mantendo uma alimentação saudável e evitando consumo de álcool, tabaco e outras drogas.
Comportamentos saudáveis evitam não apenas o diabetes, mas outras doenças crônicas, como o câncer.
A causa do tipo de diabetes ainda é desconhecida e a melhor forma de preveni-la é com práticas de vida saudáveis (alimentação, atividades físicas e evitando álcool, tabaco e outras drogas).

#### Quais os tipos mais comuns de diabetes?
O diabetes mellitus pode se apresentar de diversas formas e possui diversos tipos diferentes. Independente do tipo de diabetes, com aparecimento de qualquer sintoma é fundamental que o paciente procure com urgência o atendimento médico especializado para dar início ao tratamento.

#### O que é diabetes tipo 1?
Sabe-se que, via de regra, é uma doença crônica não transmissível, hereditária, que concentra entre 5% e 10% do total de diabéticos no Brasil. Cerca de 90% dos pacientes diabéticos no Brasil têm esse tipo. Ele se manifesta mais frequentemente em adultos, mas crianças também podem apresentar. 
O diabetes tipo 1 aparece geralmente na infância ou adolescência, mas pode ser diagnosticado em adultos também. Pessoas com parentes próximos que têm ou tiveram a doença devem fazer exames regularmente para acompanhar a glicose no sangue.
O tratamento exige o uso diário de insulina e/ou outros medicamentos para controlar a glicose no sangue.
A causa do diabetes tipo 1 ainda é desconhecida e a melhor forma de preveni-la é com práticas de vida saudáveis (alimentação, atividades físicas e evitando álcool, tabaco e outras drogas).

#### O que é diabetes tipo 2?
O diabetes tipo 2 ocorre quando o corpo não aproveita adequadamente a insulina produzida. A causa do diabetes tipo 2 está diretamente relacionado ao sobrepeso, sedentarismo, triglicerídeos elevados, hipertensão.e hábitos alimentares inadequados.
Por isso, é essencial manter acompanhamento médico para tratar, também, dessas outras doenças, que podem aparecer junto com o diabetes. 
Diabetes Latente Autoimune do Adulto (LADA):  Atinge basicamente os adultos e representa um agravamento do diabetes tipo 2. 
Caracteriza-se, basicamente, no desenvolvimento de um processo autoimune do organismo, que começa a atacar as células do pâncreas.  

#### O que é o pré-diabetes?
Pré-diabetes é quando os níveis de glicose no sangue estão mais altos do que o normal, mas ainda não estão elevados o suficiente para caracterizar um Diabetes Tipo 1 ou Tipo 2. É um sinal de alerta do corpo, que normalmente aparece em obesos, hipertensos e/ou pessoas com alterações nos lipídios. 
Esse alerta do corpo é importante por ser a única etapa do diabetes que ainda pode ser revertida, prevenindo a evolução da doença e o aparecimento de complicações, incluindo o infarto.
No entanto, 50% dos pacientes que têm o diagnóstico de pré-diabetes, mesmo com as devidas orientações médicas, desenvolvem a doença.
A mudança de hábito alimentar e a prática de exercícios são os principais fatores de sucesso para o controle.

#### O que é diabetes gestacional?
Ocorre temporariamente durante a gravidez. As taxas de açúcar no sangue ficam acima do normal, mas ainda abaixo do valor para ser classificada como diabetes tipo 2. 
Toda gestante deve fazer o exame de diabetes, regularmente, durante o pré-natal. Mulheres com a doença têm maior risco de complicações durante a gravidez e o parto. 
Esse tipo de diabetes afeta entre 2 e 4% de todas as gestantes e implica risco aumentado do desenvolvimento posterior de diabetes para a mãe e o bebê.   

#### Sintomas do diabetes tipo 1:
- Fome frequente;
- Sede constante;
- Vontade de urinar diversas vezes ao dia;
- Perda de peso;
- Fraqueza;
- Fadiga;
- Mudanças de humor;
- Náusea e vômito.
 
#### Sintomas do diabetes tipo 2:
- Fome frequente;
- Sede constante;
- Formigamento nos pés e mãos;
- Vontade de urinar diversas vezes;
- Infecções frequentes na bexiga, rins, pele e infecções de pele;
- Feridas que demoram para cicatrizar;
- Visão embaçada.


	"""

def run_about_app():
	st.subheader("Sobre a Diabetes")
	st.markdown(about)