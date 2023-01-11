##################################### Shodan-like Scanner ################################################
""""
Script em Python que captura banners de comunicacção TCP.
Python script that captures TCP communication banners.
"""
##################################### Change Log #########################################################
#Change_log:


###################################### News #############################################################
#News: 

#########################################################################################################



######################### Variáveis Globais/ Global Variables #########################################
import socket 

#Substitua pelo IP desejado. IP local por padrão/ Give an IP. Localhost IP by default. 
ip = "127.0.0.1"

#Informe as Portas/ Give the ports you want to scan
ports = []

######################################################################################################

###################################### Funções #######################################################

#######################################################################################################


###################################### Execução ######################################################
# criamos um novo objeto socket para executarmos algumas funções/ Create a new socket
 

#realiza a conexão ao IP e porta

for port in ports:

	print("Esse é o banner da porta/ This is the banner for the port:")
	print(port)
	
	s = socket.socket() 
	s.connect((ip , port))  

	# lê  1024 bytes de dados do socket e armazena na variável resposta/ Capture a banner 
	resp = s.recv(1024)  

	print(resp)

#termina a conexão/close connection
s.close() 

######################################################################################################





