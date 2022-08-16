#Arthur Leme de Sousa Palma   BCC 2ºperíodo

#União
def uniao(vetX,vetY):

    ufinal = []

    somaU = vetX + vetY
    for i in somaU:
      if i not in ufinal:
        ufinal.append(i)
         
    return ufinal

#intersecção
def inter(vetX,vetY):

    i_final = []

    for i in vetX:
        if i in vetY:
            i_final.append(i)

    return i_final

  
#diferença
def diferenca(vetX,vetY):

    d_final = []

    for i in vetX:
        if i not in vetY:
            d_final.append(i)
    return d_final

#produto cartesiano

def plano1(j,vetY):
    n= []
    for i in (vetY):
        n.append([j,i])
    return n

def plano2(vetX,vetY):
    r= []
    for i in (vetX):
        r.append([plano1(i,vetY)])
    return r

def main():
    texto=open("texto.txt")
    linhas=texto.readlines()

    nfuncao=int(linhas[0])

    for i in range(nfuncao):
        funcao = linhas[1+i*3].strip('\n')
        
        conj1= [x.replace("\n","") for x in linhas[2+i*3].split(",")]
        conj2= [x.replace("\n","")for x in linhas[3+i*3].split(",")]
    
        if (funcao == "U"):
          u_uniaof=uniao(conj1,conj2)
          print("União: Conjunto 1 ",conj1,", Conjunto 2 ",conj2,". Resultado:",u_uniaof)

        elif (funcao == "I"):
          i_interf = inter(conj1,conj2)
          print("Intersecção: Conjunto 1 ",conj1,", Conjunto 2 ",conj2,". Resultado:",i_interf)
          
        elif (funcao == "D"):
          d_diferenca = diferenca(conj1,conj2)
          print ("Diferenca: Conjunto 1 ",conj1,", Conjunto 2 ",conj2,". Resultado:",d_diferenca)
        elif (funcao =="C"):
          pc_produto = plano2(conj1,conj2)
          print("Produto Cartesiano: Conjunto 1 ",conj1,", Conjunto 2 ",conj2,". Resultado:",pc_produto)
        
    texto.close

if __name__ == "__main__":
    main()