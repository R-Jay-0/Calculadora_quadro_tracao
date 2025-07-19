import time

# DEF's 
def _verify_input_str(array, mensagem, mensagem_erro):
    print(mensagem)
    var = input("\n: ").upper()
    while var not in array:
        print("\n**********************************************************************************")
        print(f"!! {mensagem_erro} !!")
        print("**********************************************************************************")
        var = input("\n:").upper()
    return var
def _verify_input_float(mensagem, mensagem_erro):
    print(mensagem)
    var = input("\n: ")
    while True:
        try:
            float(var)
        except ValueError:
            print("\n**********************************************************************************")
            print(f"!! {mensagem_erro} !!")
            print("**********************************************************************************")
            var = input("\n:")
        else:
            return float(var)
def _param_vag(count):
    qntd = _verify_input_float("\nEntre com a quantidade de vagões que trafegam nesse trecho",
        "ERRO: quantidade de vagões deve ser um número alphanumérico")
    while count < qntd:
        vagao = {}
        print("\nEntre com o nome/tipo do vagão")
        nome_v = input("\n: ")
        vagao["Nome"] = nome_v
        tara = _verify_input_float(f"\nTara de {nome_v} (ton)", f"ERRO: tara de {nome_v} deve ser um número alphanumérico")
        vagao["tara"] = tara
        lotacao = _verify_input_float(f"\nLotacao de {nome_v} (ton)", f"ERRO: lotação de {nome_v} deve ser um número alphanumérico")
        peso_c = tara+lotacao
        vagao["peso carregado"] = peso_c
        eixos = _verify_input_float(f"\nQuantidade de eixos de {nome_v}", f"ERRO: quantidade de eixos de {nome_v} deve ser um número alphanumérico")
        vagao["eixos"] = eixos
        area = _verify_input_float(f"\nÁrea de {nome_v} (m), se desconhecida entre com '0'", f"ERRO: área de {nome_v} deve ser um número alphanumérico")
        if area == 0:
            lado = _verify_input_float(f"\nComprimento do lado de {nome_v} (m)", f"ERRO: lado de {nome_v} deve ser um número alphanumérico")
            altura = _verify_input_float(f"\nComprimento da altura de {nome_v} (m)", f"ERRO: altura de {nome_v} deve ser um número alphanumérico")
            area = lado*altura
        vagao["área"] = area
        vagoes.append(vagao)
        count += 1
def _selec_vags():
    v1 = {
        "Nome": "",
        "tara": 0,
        "peso carregado": 0,
        "eixos": 0,
        "área": 0
    }
    v2 = {
        "Nome": "",
        "tara": 0,
        "peso carregado": 0,
        "eixos": 0,
        "área": 0
    }
    v3 = {
        "Nome": "",
        "tara": 0,
        "peso carregado": float("inf"),
        "eixos": 0,
        "área": 0
    }
    v4 = {
        "Nome": "",
        "tara": float("inf"),
        "peso carregado": 0,
        "eixos": 0,
        "área": 0
    }
    for i in vagoes:
        if v1["peso carregado"] < i["peso carregado"]:
            v1 = i
        if v2["tara"] < i["tara"]:
            v2 = i
        if v3["peso carregado"] > i["peso carregado"]:
            v3 = i
        if v4["tara"] > i["tara"]:
            v4 = i
    return [v1, v2, v3, v4]
def _calc_vag_vaz():
    result = []
    for i in vagoes:
        vag_vaz = {}
        vag_vaz["Nome"] = i["Nome"]
        vag_vaz["Peixo"] = round(i["tara"]/i["eixos"], 4)
        vag_vaz["Resistência normal"] = round(0.65+(13.15/vag_vaz["Peixo"])+(0.01405*velocidade)+(0.000945*i["área"]*velocidade**2/i["tara"]), 4)
        vag_vaz["Resistência de partida"] = round(11.2 - (0.3*vag_vaz["Peixo"]), 4)
        vag_vaz["Resistência total"] = round(vag_vaz["Resistência normal"]+vag_vaz["Resistência de partida"]+resis_aceleracao+resis_curva_v+resis_rampa, 4)
        if tunel == "S":
            vag_vaz["Resistência total"] += resis_tunel
        result.append(vag_vaz)
    return result
def _calc_vag_carr():
    result = []
    for i in vagoes:
        vag_carr = {}
        vag_carr["Nome"] = i["Nome"]
        vag_carr["Peixo"] = round(i["peso carregado"]/i["eixos"], 4)
        vag_carr["Resistência normal"] = round(0.65+(13.15/vag_carr["Peixo"])+(0.01405*velocidade)+(0.000945*i["área"]*velocidade**2/i["peso carregado"]), 4)
        vag_carr["Resistência de partida"] = round(11.2 - (0.3*vag_carr["Peixo"]), 4)
        vag_carr["Resistência total"] = round(vag_carr["Resistência normal"]+vag_carr["Resistência de partida"]+resis_aceleracao+resis_curva_v+resis_rampa, 4)
        if tunel == "S":
            vag_carr["Resistência total"] += resis_tunel
        result.append(vag_carr)
    return result

# !! COMEÇO DO PROGRAMA !! #

while True:
    print("\n============================ Bem vindo à calculadora ============================")
    print("\n** Por favor, tenha cuidado e leia atentamente as instruções dadas **")
    nome = input("\nEntre com o nome do 'dono' do arquivo que será gerado: ")
    selecionado = _verify_input_str(["V", "L", "Q"],
        "\nDigite: [L] para locomotiva; [V] para vagão e [Q] para quadro de tração","ERRO: Selecione entre vagão [V], locomotiva [L] ou quadro de tração [Q]"
    )

    # Parâmetros via permanente (VP)
    i = _verify_input_float("\nInclinação da rampa (%):",
        "Inclinação da rampa deve ser um número alphanumérico"
    )
    bitola = _verify_input_str(["M", "L"], 
        "\nBitola Métrica: digite [M]. Bitola larga: digite [L]","ERRO: escolha [M] para métrica ou [L] para larga"
    )
    if bitola == "M":
        bitola = 1
    else:
        bitola = 1.6
    G20 = _verify_input_float("\nEntre com o G20. (Se desconhecido entre com '-1')",
        "ERRO: G20 deve ser um número alphanumérico"
    )
    if G20 == -1:
        raio = float(input("por raio da curva:"))
        raio = _verify_input_float(raio, "Entre com o raio da curva",
            "ERRO: raio da curva deve ser um alphanumérico"
        )
        if raio != 0:
            G20 = 1146/raio
        else:
            G20 = 0
    tunel = _verify_input_str(["S","N"],
        "\nContém túnel? [S/N]", "ERRO: Escolha entre 'S' ou 'N', por favor"
    )
    if tunel == "S":
        linha = _verify_input_str(["D", "S"],
            "\nA linha é singela ou dupla? 'S' para singela e 'D' para dupla","ERRO: escolha entre singela [S] ou dupla [D]"
        )
        if linha == "S":
            resis_tunel = 2
        else:
            resis_tunel = 1

    # parâmetros gerais
    velocidade = _verify_input_float("\nVelocidade em regime constante (km/h)", "ERRO: velocidade deve ser um número alphanumérico")
    aceleracao = _verify_input_float("\nAceleração da composição (km/m/s²)", "ERRO: aceleração deve ser um número alphanumérico")

    # parâmetros locomotiva
    if selecionado in ["L", "Q"]:
        print("\nNome da locomotiva")
        locomotiva_nome = input("\n: ")
        hp = _verify_input_float("\nPotência da locomotiva (hp)", "ERRO: potência deve ser um número alphanumérico")
        rendimento = _verify_input_float("\nRendimento da locomotiva (%)", 
            "ERRO: Rendimento deve ser um número alphanumérico"
        )
        peso_l = _verify_input_float("\nPeso da locomotiva (ton)", 
            "ERRO: Peso deve ser um número alphanumérico"
        )
        c_aderencia = _verify_input_float("\nCoeficiente de aderência (%)",
            "ERRO: coeficiente de aderência deve ser um número alphanumérico"
        )
        eixos_l = _verify_input_float("\nQuantidade de eixos da locomotiva",
            "ERRO: eixos deve ser um número alphanumérico"
        )
        area_l = _verify_input_float("\nÁrea da locomotiva (m), se desconhecida entre com '0'", 
            "ERRO: área da locomotiva deve ser um número alphanumérico"
        )
        if area_l == 0:
            lado_l = _verify_input_float("\nEntre com o lado da parte frontal da locomotiva (m)", 
                "ERRO: lado deve ser um número alphanumérico"
            )
            altura_l = _verify_input_float("\nEntre com a altura da parte frontal da locomotiva (m)", 
                "ERRO: altura deve ser um número alphanumérico"
            )
            area_l = altura_l*lado_l

    # parâmetros vagões
    if selecionado in ["V","Q"]:
        vagoes = []
        _param_vag(0)
        if selecionado == "Q":
            vagoes = _selec_vags()
        
    # Resistências gerais
    if i > 0:
        resis_rampa = 10*i
    else:
        resis_rampa = 0

    resis_aceleracao = 31.1*aceleracao

    # Cálculos locomotiva
    if selecionado in ["L", "Q"]:
        peixo_l = peso_l/eixos_l

        resis_normal_l = 0.65+(13.15/peixo_l)+(0.00932*velocidade)+((0.00456*area_l*velocidade**2)/peso_l)

        resis_partida_l = 11.2 - (0.3*peixo_l)

        if G20 > 0:
            raio = 1146/G20
            resis_curva_l = 500*bitola/raio
        elif G20 == 0:
            raio = 0
            resis_curva_l = 0

        # Resistência total
        resis_total = resis_aceleracao+resis_curva_l+resis_rampa+resis_partida_l+resis_normal_l
        if tunel == "S":
            resis_total += resis_tunel

        # Tração
        tracao = hp*(rendimento/100)*273.7494/velocidade

        # Aderência
        aderencia = peso_l*10*c_aderencia/(1+(0.01*velocidade))

        # Capacidade de reboque
        if tracao > aderencia:
            t_pratica = aderencia
        else:
            t_pratica = tracao
        c_r = t_pratica - (resis_total*peso_l)

    # Cálculos vagôes
    if selecionado in ["V","Q"]:
        if bitola == 1:
            resis_curva_v = 0.54*G20
        else:
            resis_curva_v = 0.65*G20
        
        # Vagões vazios
        vag_vaz_results = _calc_vag_vaz()

        # Vagões carregados:
        vag_carr_results = _calc_vag_carr()

        # Cálculos finais (QT)
        if selecionado == "Q":
            V1 = vag_carr_results[0]
            V2 = vag_vaz_results[1]
            V3 = vag_carr_results[2]
            V4 = vag_vaz_results[3]

            lv1 = c_r/V1["Resistência total"]
            lv4 = c_r/V4["Resistência total"]

            Nv2 = c_r/(V2["Resistência total"]*vagoes[2]["tara"])
            Nv3 = c_r/(V3["Resistência total"]*vagoes[3]["peso carregado"])

            CF = (lv1-lv4)/(Nv2-Nv3)

            if Nv2 >= int(Nv2) + 0.75:
                Nv2a = int(Nv2) + 1
            else:
                Nv2a = int(Nv2)
            if Nv3 >= int(Nv3) + 0.75:
                Nv3a = int(Nv3) + 1
            else:
                Nv3a = int(Nv3)

            La = ((lv1+(CF*Nv3a))+(lv4+(CF*Nv2a)))/2

    # !! RESULTADOS !! #
    if selecionado == "L":
        selecionado = "Locomotiva"
    elif selecionado == "V":
        selecionado = "Vagões"
    else:
        selecionado = "Quadro-tração"
    
    with open(f"Resultados-{selecionado}_{nome}.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"O trecho analisado contém:\n\n")
        if bitola == 1:
            arquivo.write(f"    - Bitola métrica\n")
        else:
            arquivo.write(f"    - Bitola larga\n")
        arquivo.write(f"    - Rampa compensada = {i}%\n")
        arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
        if tunel == "S":
            if linha == "S":
                arquivo.write(f"    - Túnel em linha singela\n")
            else:
                arquivo.write(f"    - Túnel em linha dupla\n")
        # locomotiva
        if selecionado in ["Locomotiva", "Quadro-tração"]:
            arquivo.write(f"\n*A locomotiva analisada foi: {locomotiva_nome}:*\n\n")
            arquivo.write(f"    - Eixos: {eixos_l}\n")
            arquivo.write(f"    - Peso total: {peso_l} t\n")
            arquivo.write(f"    - Taxa de aceleração: {aceleracao} km/m/s\n")
            arquivo.write(f"    - Potência: {hp} hp\n"),
            arquivo.write(f"    - Velocidade constante: {velocidade} km/h\n")
            arquivo.write(f"    - Área: {round(area_l, 4)} m²\n"),
            arquivo.write(f"    - Aderência em velocidade nula = {round(c_aderencia, 4)}%\n")
            arquivo.write(f"    - Rendimento das locomotivas = {round(rendimento, 4)}%\n")
            arquivo.write(f"\n*Cálculos de resistência da VP:*\n\n"),
            arquivo.write(f"    Resistência rampa = 10 x i% ==> {round(resis_rampa, 4)} Kgf/t = 10 x {i}\n\n"),
            arquivo.write(f"    Resistência aceleração (Ra) = 31,1 x a ==> {round(resis_aceleracao, 4)} Kgf/t = 31,1 x {aceleracao}\n")
            if tunel == "S":
                if linha == "S":
                    arquivo.write(f"    Resistência tunel (Rt) = 2 Kgf/t \n")
                else:
                    arquivo.write(f"    Resistência tunel (Rt) = 1 Kgf/t \n")
            arquivo.write(f"\n\n*Cálculos referentes à locomotiva*\n")
            arquivo.write(f"\n\n    Peixo locomotiva (Peixo_l) = Pl / eixos_l ==> {round(peixo_l, 4)} Kgf/t = {peso_l} / {eixos_l}\n")
            arquivo.write(f"\n    Resistência normal locomotiva (Rnl) = 0.65+(13.15/Peixo_l)+(0.00932 x V)+(0.00456 x Área_l x V^2/peso_l) ==> {round(resis_normal_l, 4)} Kgf/t = 0.65+(13.15/{round(peixo_l, 4)})+(0.000932 x {velocidade})+(0.00456 x {round(area_l, 4)} x {round(velocidade, 4)}^2/{round(peso_l, 4)})\n")
            arquivo.write(f"\n    Resistência partida locomotiva (Rpl) = 11,2 - (0,3 x Peixo_l) ==> {round(resis_partida_l, 4)} Kgf/t = 11.2 - (0.3 x {round(peixo_l, 4)})\n")
            arquivo.write(f"\n    Resistência curva (Rcl) = 500 x bitola / raio ==> {round(resis_curva_l, 4)} Kgf/t = 500 x {bitola} / {round(raio, 4)}\n\n")
            if tunel == "N":
                arquivo.write(f"    Resistência total  locomotiva (Rtl) = Ra+Rcl+Rr+Rpl+Rnl ==> {round(resis_total, 4)} Kgf/t  = {round(resis_aceleracao, 4)} + {round(resis_curva_l, 4)} + {round(resis_rampa, 4)} + {round(resis_partida_l, 4)} + {round(resis_normal_l, 4)}\n")
            else:
                arquivo.write(f"    Resistência total  locomotiva (Rtl) = Rnl+Rpl+Rcl+Rr+Ra+Rt ==> {round(resis_total, 4)} Kgf/t = {round(resis_aceleracao, 4)} + {round(resis_curva_l, 4)} + {round(resis_rampa, 4)} + {round(resis_partida_l, 4)} + {round(resis_normal_l, 4)} + {resis_tunel}\n")
            arquivo.write(f"\n    Força tratora (Ft) = P(hp) x n(rendimento) x 273.7494 / V ==> {round(tracao, 4)} Kgf = {hp} x {rendimento/100} x 273.7494 / {velocidade}\n")
            arquivo.write(f"\n    Aderência = Pl x Ca (coeficiente de aderência) / (1 + (0.01 x V)) ==> {round (aderencia, 4)} Kgf = {peso_l*1000} x {c_aderencia/100} / (1 + (0.01 x {velocidade}))\n")
            arquivo.write(f"\n    Esforço trator (Et) = {round(t_pratica, 4)} kgf\n")
            arquivo.write(f"\n    Capacidade de reboque (Cr) = Et - Rtl x Pl ==> {round(c_r, 4)} kgf = {round(t_pratica, 4)} - {round(resis_total, 4)} x {peso_l}\n\n")
        # vagôes
        if selecionado in ["Vagões", "Quadro-tração"]:
            arquivo.write(f"\n Resultados vagões vazios\n")
            for i in vag_vaz_results:
                for key, value in i.items():
                    arquivo.write(f"\n {key}: {value}\n")
            arquivo.write(f"\n\n Resultados vagôes carregados\n")
            for i in vag_carr_results:
                for key, value in i.items():
                    arquivo.write(f"\n {key}: {value}\n")


    # Quadro de tração
        if selecionado == "Quadro-tração": 
            arquivo.write(f"\n\n\n*Cálculos referentes à lotação ajustada:*\n\n")
            arquivo.write(f"    Vagões utilizados nos cálculos:\n")
            arquivo.write(f"    V1 = {V1["Nome"]} carregado\n")
            arquivo.write(f"    V2 = {V2["Nome"]} vazio\n")
            arquivo.write(f"    V3 = {V3["Nome"]} carregado\n")
            arquivo.write(f"    V4 = {V4["Nome"]} vazio\n\n")
            arquivo.write(f"\n    Carro fator (Cf) = (lv1-lv4) / (Nv2-Nv3) ==> {round(CF, 4)} = ({round(lv1, 4)} - {round(lv1, 4)}) / ({round(Nv2, 4)} - {round(Nv3, 4)})\n")
            arquivo.write(f"\n    Lotação ajustada = ((Lv1 + (Cf x Nv3)) + (Lv4 + (Cf x Nv2))) / 2 ==> {round(La, 4)} t = (({round(lv1, 4)} + ({round(CF, 4)} x {round(Nv3a, 4)})) + ({round(lv1, 4)} + ({round(CF, 4)} x {round(Nv2a, 4)}))) / 2\n")

    print("Concluído com sucesso")
    time.sleep(0.5)
    print("\nDeseja efetuar outro cálculo? [S/N]")
    continuar = input("\n:").upper()
    while continuar not in ["S","N"]:
            print("\nERRO: Por favor, entre com 'S' ou 'N'")
            continuar = input("\n: ").upper()
    if continuar == "N":
        print("\nClosing ...")
        time.sleep(1.5)
        exit()
    else:
        print("\nReiniciando o processo...")
        time.sleep(1)