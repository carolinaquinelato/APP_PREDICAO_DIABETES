import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import seaborn as sns
import plotly.express as px

# Carregar o DataSet
@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_eda_app():
	st.subheader("Análise Exploratória dos Dados ")
	# df = pd.read_csv("C:/Users/carol/Documents/GitHub/Diabetes/data/diabetes_data_upload.csv")
	df = load_data("C:/Users/carol/Documents/GitHub/Diabetes/data/diabetes_data_upload.csv")
	freq_df = load_data("C:/Users/carol/Documents/GitHub/Diabetes/data/freqdist_of_age_data.csv")
	df_encoded = load_data("C:/Users/carol/Documents/GitHub/Diabetes/data/diabetes_data_upload_clean.csv")

	submenu = st.sidebar.selectbox("EDA", ["Descritivo", "Gráficos"])
	if submenu == "Descritivo":
		st.write("Análise descritiva")
		st.dataframe(df)

		with st.expander("Descrição das Idades"):
			st.dataframe(df.describe())

		with st.expander("Distribuição dos Gêneros"):
			st.write("Quantos dos dados são do sexo feminino e masculino")
			st.dataframe(df['Gender'].value_counts())

		with st.expander("Distribuição dos Dados"):
			st.write("Quantos dos dados são positivos ou negativos para diabetes")
			st.dataframe(df['class'].value_counts())



	elif submenu == "Gráficos":
		st.write("Análise visual")

		#Layout
		col1, col2 = st.columns([1,1])

		with col1:
			#Gênero
			gen_df = df['Gender'].value_counts().to_frame()
			gen_df = gen_df.reset_index()
			gen_df.columns= ["Gênero", "Contagem"]

			with st.expander("Distribuição de Gênero"):
				st.dataframe(gen_df)

			with st.expander("Gráfico de Distribuição de Gênero"):

				p = px.bar(gen_df, x='Gênero', y='Contagem')
				st.plotly_chart(p, use_container_width=True)

				p1 = px.pie(gen_df, names='Gênero', values='Contagem')
				st.plotly_chart(p1, use_container_width=True)
			
		with col2:
			#Diabetes
			class_df = df['class'].value_counts().to_frame()
			class_df = class_df.reset_index()
			class_df.columns= ["Classificação", "Contagem"]

			with st.expander("Distribuição de Classificação"):
				st.dataframe(class_df)

			with st.expander("Gráfico de Distribuição de Classificação"):
				
				p2 = px.bar(class_df, x='Classificação', y='Contagem')
				st.plotly_chart(p, use_container_width=True)

				p3 = px.pie(class_df, names='Classificação', values='Contagem')
				st.plotly_chart(p3, use_container_width=True)


		#Idade
		with st.expander("Frequência de Distribuição de Idade"):
			p4 = px.bar(freq_df, x='Idade', y='Contagem')
			st.plotly_chart(p4, use_container_width=True)

		#Outlier
		with st.expander("Detecção de Outliers"):
			p5 = px.box(df, x='Age', color='Gender')
			st.plotly_chart(p5, use_container_width=True)

		#Correlação
		with st.expander("Matriz de Correlação"):
			corr_matrix = df_encoded.corr()
			fig = plt.figure(figsize=(15,10))
			sns.heatmap(corr_matrix, annot=True)
			st.pyplot(fig)

			st.write("Somente as correlações maiores do que 0.30")
			corr_matrix = df_encoded.corr()
			highest_corr = corr_matrix[corr_matrix>=.3]
			fig = plt.figure(figsize=(15,10))
			sns.heatmap(highest_corr, annot=True)
			st.pyplot(fig)