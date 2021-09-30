if (Fco2_ponto1 + Fco2_ponto2 + Fco2_ponto3 + Fco2_ponto4 + Fco2_ponto5 == -19.506):
    print("O calculo tá certo, parabéns \U0001F389")
    print("Você pode continuar com o próximo código")
    teste = True
elif (np.exp(Fco2_ponto1) != 3.126535320098089e-05):
    print("Opa, o ponto 1 tá errado, recorde verificar as unidades e só usar 3 decimais")
elif (np.exp(Fco2_ponto2) != 4.4816890703380645):
    print("Opa, o ponto 2 tá errado, recorde verificar as unidades e só usar 3 decimais")
elif (np.exp(Fco2_ponto3) != 4.2781067258980255e-06):
    print("Opa, o ponto 3 tá errado, recorde verificar as unidades e só usar 3 decimais")
elif (np.exp(Fco2_ponto4) != 0.751262615946886):
    print("Opa, o ponto 4 tá errado, recorde verificar as unidades e só usar 3 decimais")
elif (np.exp(Fco2_ponto5) != 7.500727381202963):
    print("Opa, o ponto 5 tá errado, recorde verificar as unidades e só usar 3 decimais")
