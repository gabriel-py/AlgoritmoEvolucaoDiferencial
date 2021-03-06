import random
import numpy as np

tam_pop = 10
geracoes = 100
populacao = np.zeros((tam_pop,2))
f = 0.9
pc = 0.9

def fit(x):
    result = x**2+1*x+8
    return result
    
def inicializa_populacao(populacao,tam_pop):
    for i in range(tam_pop):
        for j in range(2):
            if(j==0):
                populacao[i,j] = round(random.uniform(-1000, 1000),2)
            else:
                populacao[i,j] = round(fit(populacao[i,j-1]),2)
                
    return populacao

populacao = inicializa_populacao(populacao,tam_pop)
#print(populacao)
#print("======")


def cria_nova_geracao(populacao, tam_pop):
    outros_vetores = []
    for i in range(tam_pop):
            vetor_alvo = populacao[i,0]
            
            for k in range(tam_pop):
                if(k!=i):
                    outros_vetores.append(populacao[k,0])
                    
            vetor1 = random.choice(outros_vetores)
            vetor2 = random.choice(outros_vetores)
            vetor3 = random.choice(outros_vetores)
            
            vetor_doador = vetor1 + f*(vetor2-vetor3)
            
            numero_sorteado = random.random()
            
            if(numero_sorteado<pc):
                vetor_experimental=vetor_doador
            else:
                vetor_experimental=vetor_alvo
                
            if(fit(vetor_experimental)<fit(vetor_alvo)):
                populacao[i,0]=round(vetor_experimental,2)
                populacao[i,1]=round(fit(vetor_experimental),2)
            
            outros_vetores = []
            
    return populacao        
            

for i in range(geracoes):
    populacao = cria_nova_geracao(populacao, tam_pop)
    #print(populacao)
    #print("======")
    

if(populacao[0,1]<0):
    menor_fitness=0
else:
    menor_fitness=populacao[0,1]

for i in range(tam_pop):
    if(populacao[i,1]<menor_fitness):
        menor_fitness = populacao[i,1]
        
print(menor_fitness)
