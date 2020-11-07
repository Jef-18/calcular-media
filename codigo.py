#notas
v_nota1 = float(input("Digite a primeira nota: "))
v_nota2 = float(input("Digite a segunda nota: "))

#media 
v_media = (v_nota1 + v_nota2) / 2

#situação
print("")
if (v_media <= 4):
    print("REPROVADO")
    
elif(v_media <=6 ):
    print("RECUPERAÇÃO")
    
else:
    print("APROVADO COM DISTINÇÃO")

#resultado
print("Sua média é: ", v_media)
