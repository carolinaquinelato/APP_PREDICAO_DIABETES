import streamlit as st
import streamlit.components.v1 as stc 

#importando os mini app
from eda_app import run_eda_app
from ml_app import run_ml_app
from about_app import run_about_app

st.set_page_config(
	page_title="App Predição de Diabetes",
	page_icon="🏪",
	layout="wide",
	initial_sidebar_state="expanded",
)

html_temp = """
		<div style="background-color:#1c2d5c;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Aplicativo de Predição de Diabetes em Estágio Inicial</h1>
		</div>
		"""
home = """
			Esse dataset contém sinais e sintomas de estágio inicial de pacientes diabéticos ou potencialmente diabéticos
			##### Fonte:
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			##### Conteúdo:
				- EDA: Área de análise exploratória dos dados
				- Predição: Área de predição usando o método Decision Tree de Machine Learning
				- Sobre: Área informativa sobre Diabetes

			"""


def main():
	stc.html(html_temp)

	menu = ["Página Inicial", "Sobre", "Análise Exploratória", "Predição"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Página Inicial":
		st.subheader("Página Inicial")
		st.markdown(home)
	elif choice == "Sobre":
		run_about_app()
	elif choice == "Análise Exploratória":
		run_eda_app()
	elif choice == "Predição":
		run_ml_app()
	

if __name__ == '__main__':
	main()