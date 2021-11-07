import streamlit as st

import joblib
import os

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.model_selection import train_test_split

atr_info = """
#### 
	-Idade: 10-100
	-Sexo: 1. Masculino, 2. Feminino
	-Poliúria: 1. Sim, 2. Não. (Expelir quantidades anormalmente grandes de urina)
	-Polidipsia: 1. Sim, 2. Não. (Excesso de sede)
	-Perda repentina de peso: 1.Sim, 2.Não.
	-Fraqueza: 1.Sim, 2.Não.
	-Polifagia: 1. Sim, 2. Não. (Comer em excesso devido a fome excessiva)
	-Candidíase Vaginal: 1.Sim, 2.Não.
	-Visão Embaçada: 1.Sim, 2.Não.
	-Coceira: 1. Sim, 2. Não.
	-Irritabilidade: 1. Sim, 2. Não.
	-Cicatrização demorada: 1. Sim, 2. Não.
	-Paralisia parcial: 1. Sim, 2. Não.
	-Rigidez muscular: 1. Sim, 2. Não.
	-Alopecia: 1. Sim, 2. Não. (Queda de cabelo)
	-Obesidade: 1. Sim, 2. Não.
	-Classificação: 1. Positivo, 2.Negativo.

"""
label_dict = {"Não":0,"Sim":1}
gender_map = {"Feminino":0, "Masculino":1}
target_label_map = {"Negativo":0,"Positivo":1} 

def get_fvalue(val):
	feature_dict = {"Não":0,"Sim":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 
 
def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 

# Carregar o modelo de ML
@st.cache
def load_model(modelos):
	loaded_model = joblib.load(open(os.path.join(modelos),"rb"))
	return loaded_model

def run_ml_app():
	st.subheader("Área de predição usando Machine Learning")
	log_red = load_model("C:/Users/carol/Documents/GitHub/Diabetes/modelos/logistic_regression_model_diabetes.pkl")
	dec_tree = load_model("C:/Users/carol/Documents/GitHub/Diabetes/modelos/decision_tree_model_diabetes.pkl")

	with st.expander("Informação dos Atributos"):
		st.markdown(atr_info)
	
	st.write("Escolha os atributos para realizar uma predição:")
	col1, col2 = st.columns(2)

	#Imput de dados pra prever

	with col1:

		idade = st.slider("Idade",10,100)
		genero = st.radio("Gênero",["Feminino","Masculino"])
		poliuria = st.radio("Poliuria",["Não","Sim"])
		polidipsia = st.radio("Polidipsia",["Não","Sim"]) 
		perca_de_peso_repentina = st.selectbox("Perca de peso repentina",["Não","Sim"])
		fraqueza = st.radio("Fraqueza",["Não","Sim"]) 
		polifagia  = st.radio("Polifagia",["Não","Sim"]) 
		candidiase_vaginal = st.selectbox("Candidiase vaginal",["Não","Sim"]) 

	with col2:
		visão_embaçada = st.selectbox("Visão embaçada",["Não","Sim"])
		coceira = st.radio("Coceira",["Não","Sim"]) 
		irritabilidade = st.radio("Irritabilidade",["Não","Sim"]) 
		cicatrização_demorada = st.radio("Cicatrização demorada",["Não","Sim"]) 
		paralisia_parcial = st.selectbox("Paralisia parcial",["Não","Sim"])
		rigidez_muscular = st.radio("Rigidez muscular",["Não","Sim"]) 
		queda_de_cabelo = st.radio("Queda de cabelo",["Não","Sim"]) 
		obesidade = st.radio("Obesidade",["Não","Sim"]) 

	with st.expander("Atributos Selecionados"):
		result = {
		'Idade': idade,
		'Gênero': genero,
		'Poliuria':poliuria, 
		'Polidipsia':polidipsia, 
		'Perca de peso repentina':perca_de_peso_repentina,
		'Fraqueza':fraqueza, 
		'Polifagia':polifagia, 
		'Candidiase vaginal':candidiase_vaginal, 
		'Visão embaçada':visão_embaçada,
		'Coceira':coceira,
		'Irritabilidade':irritabilidade, 
		'Cicatrização demorada':cicatrização_demorada,
		'Paralisia parcial':paralisia_parcial, 
		'Rigidez muscular':rigidez_muscular, 
		'Queda de cabelo':queda_de_cabelo, 
		'Obesidade':obesidade
		}
		st.write(result)


		#fazendo a conversão dos dados para 1 e 0
		encoded_result = []
		for i in result.values():
			if type(i) == int:
				encoded_result.append(i)
			elif i in ["Feminino","Masculino"]:
				res = get_value(i,gender_map)
				encoded_result.append(res)
			else:
				encoded_result.append(get_fvalue(i))

	if st.button("Predizer"):			
	

		st.subheader("Usando Regressão Logística")
		#transformando os dados em um array

		single_sample = np.array(encoded_result).reshape(1,-1)

		#Mandando os dados para o modelo
		prediction = log_red.predict(single_sample)

		pred_prob = log_red.predict_proba(single_sample) #probabilidade

		# st.write(prediction)
		if prediction == 1:
			st.warning("Risco Positivo para Diabetes - {}".format(prediction[0]))
			pred_probability_score = {"Chance de ser negativo":pred_prob[0][0]*100,"Chance de ser positivo":pred_prob[0][1]*100}
			st.write("Score da Probabilidade da Predição")
			st.json(pred_probability_score)
		else:
			st.success("Risco Negativo para Diabetes - {}".format(prediction[0]))
			pred_probability_score = {"Chance de ser negativo":pred_prob[0][0]*100,"Chance de ser positivo":pred_prob[0][1]*100}
			st.write("Score da Probabilidade da Predição")
			st.json(pred_probability_score)

		st.subheader("Usando Árvore de Decisão")
		prediction = dec_tree.predict(single_sample)

		pred_prob = dec_tree.predict_proba(single_sample) #probabilidade

		# st.write(prediction)
		if prediction == 1:
			st.warning("Risco Positivo para Diabetes - {}".format(prediction[0]))
			pred_probability_score = {"Chance de ser negativo":pred_prob[0][0]*100,"Chance de ser positivo":pred_prob[0][1]*100}
			st.write("Score da Probabilidade da Predição")
			st.json(pred_probability_score)
		else:
			st.success("Risco Negativo para Diabetes - {}".format(prediction[0]))
			pred_probability_score = {"Chance de ser negativo":pred_prob[0][0]*100,"Chance de ser positivo":pred_prob[0][1]*100}
			st.write("Score da Probabilidade da Predição")
			st.json(pred_probability_score)