print("Por favor, tenha cuidado e leia atentamente as instruções dadas")
print("")
nome = input("Por nome do 'dono' do arquivo:")
print("Digite: [L] para locomotiva; [V] para vagão e [T] para efetuar o cálculo totalmente")
print("")
selecionado = input("Diga qual material rodante será calculado:")
if selecionado not in ["L","l","V","v","T","t"]:
    raise("Erro: elemento inválido")

# Parâmetros via permanente (VP)
i = float(input("Inclinação da rampa (%):"))
bitola = input("Bitola Métrica: digite [M]. Bitola larga: digite [L]:")
if bitola not in ["M","l","m","L"]:
    raise("Erro: elemento inválido")
G20 = float(input("G20. Se desconhecido: digite [-1]:"))
if G20 == -1:
    raio = float(input("por raio da curva:"))
    G20 = 1146/raio
elif G20 not in [0,-1] and G20 < 0:
    raise("Erro: elemento inválido")
tunel = input("contém túnel? [S/N]?")
if tunel not in ["S","N","s","n"]:
    raise("Erro: elemento inválido")
if bitola in ["M","m"]:
    bitola = 1
elif bitola in ["L","l"]:
    bitola = 1.6

# parâmetros gerais
velocidade = float(input("Velocidade em regime constante (km/h):"))
aceleraçao = float(input("Aceleraçao da composição (km/m/s^2):"))

# parâmetros locomotiva
if selecionado in ["L","l","T","t"]:
    locomotiva_nome = input("Nome da locomotiva:")
    hp = float(input("Potência (HP):"))
    rendimento = float(input("Rendimento (%):"))
    peso_l = float(input("Peso da locomotiva (ton):"))
    c_aderencia = float(input("Coeficiente de aderência (%):"))
    eixos_l = int(input("Número de eixos da locomotiva:"))
    area_l = float(input("Área da locomotiva (m). Se desconhecida: digite '0':"))
    if area_l == 0:
        lado_l = float(input("Comprimento do lado da locomotiva (m):"))
        altura_l = float(input("Comprimento da altura da locomotiva (m):"))
        area_l = lado_l*altura_l
    elif area_l < 0:
        raise("Erro: elemento inválido")
    fator_t = 273.7494

# parâmetros vagão
if selecionado in ["V","v","T","t"]:
    # Vagão 1
    nome_v1 = input("Nome do vagão 1:")
    tara_v1 = float(input(f"Tara do {nome_v1} (ton):"))
    lotacao_v1 = float(input(f"Lotação do {nome_v1} (ton):"))
    if tara_v1 > lotacao_v1:
        raise("Erro: elemento inválido")
    area_v1 = float(input(f"Área do {nome_v1} (m^2). Se desconhecida: digite '0':"))
    if area_v1 == 0:
        lado_v1 = float(input(f"Comprimento do lado do {nome_v1} (m):"))
        altura_v1 = float(input(f"Comprimento da altura do {nome_v1} (m):"))
        area_v1 = lado_v1*altura_v1
    elif area_v1 < 0:
        raise("Erro: elemento inválido")
    eixos_v1 = int(input(f"Eixos do {nome_v1}:"))
    # Vagão 2
    nome_v2 = input("Nome do vagão 2:")
    tara_v2 = float(input(f"Tara do {nome_v2} (ton):"))
    lotacao_v2 = float(input(f"Lotação do {nome_v2} (ton):"))
    if tara_v2 > lotacao_v2:
        raise("Erro: elemento inválido")
    area_v2 = float(input(f"Área do {nome_v2} (m^2). Se desconhecida: digite '0':"))
    if area_v2 == 0:
        lado_v2 = float(input(f"Comprimento do lado do {nome_v2} (m):"))
        altura_v2 = float(input(f"Comprimento da altura do {nome_v2} (m):"))
        area_v2 = lado_v2*altura_v2
    elif area_v2 < 0:
        raise("Erro: elemento inválido")
    eixos_v2 = int(input(f"Eixos do {nome_v2}:"))    
    # Vagão 3
    nome_v3 = input("Nome do vagão 3:")
    tara_v3 = float(input(f"Tara do {nome_v3} (ton):"))
    lotacao_v3 = float(input(f"Lotação do {nome_v3} (ton):"))
    if tara_v3 > lotacao_v3:
        raise("Erro: elemento inválido")
    area_v3 = float(input(f"Área do {nome_v3} (m^2). Se desconhecida: digite '0':"))
    if area_v3 == 0:
        lado_v3 = float(input(f"Comprimento do lado do {nome_v3} (m):"))
        altura_v3 = float(input(f"Comprimento da altura do {nome_v3} (m):"))
        area_v3 = lado_v3*altura_v3
    elif area_v3 < 0:
            raise("Erro: elemento inválido")
    eixos_v3 = int(input(f"Eixos do {nome_v3}:"))
    # Vagão 4
    nome_v4 = input("Nome do vagão 4:")
    tara_v4 = float(input(f"Tara do {nome_v4} (ton):"))
    lotacao_v4 = float(input(f"Lotação do {nome_v4} (ton):"))
    if tara_v4 > lotacao_v4:
        raise("Erro: elemento inválido")
    area_v4 = float(input(f"Área do {nome_v4} (m^2). Se desconhecida: digite '0':"))
    if area_v4 == 0:
        lado_v4 = float(input(f"Comprimento do lado do {nome_v4} (m):"))
        altura_v4 = float(input(f"Comprimento da altura do {nome_v4} (m):"))
        area_v4 = lado_v4*altura_v4
    elif area_v4 < 0:
        raise("Erro: elemento inválido")
    eixos_v4 = int(input(f"Eixos do {nome_v4}:"))

# Resistências gerais
if i > 0:
   resis_rampa = 10*i
else:
  resis_rampa = 0

resis_aceleraçao = 31.1*aceleraçao

# Cálculos locomotiva
if selecionado in ["L","l","T","t"]:
    peixo_l = peso_l/eixos_l

    resis_normal_l = 0.65+(13.15/peixo_l)+(0.00932*velocidade)+((0.00456*area_l*velocidade*velocidade)/peso_l)

    resis_partida_l = 11.2 - (0.3*peixo_l)

    if G20 > 0:
        raio = 1146/G20
        resis_curva_l = 500*bitola/raio
    elif G20 == 0 or raio == 0:
        resis_curva_l = 0

    resis_total = resis_aceleraçao+resis_curva_l+resis_rampa+resis_partida_l+resis_normal_l
    if tunel in ["S","s"]:
        resis_total = resis_total+1

    # Tração
    tracao = hp*(rendimento/100)*fator_t/velocidade

    # Aderência
    aderencia = peso_l*10*c_aderencia/(1+(0.01*velocidade))

    # Capacidade de reboque
    if tracao > aderencia:
        t_pratica = aderencia
    else:
        t_pratica = tracao
    c_r = t_pratica - (resis_total*peso_l)

# Cálculos vagôes
if selecionado in ["V","v","T","t"]:
    if bitola == 1:
        resis_curva_v = 0.54*G20
    elif bitola == 1.6:
        resis_curva_v = 0.65*G20
    
    # Vagões vazios:
    
    #vagão 1
    peixo_V1v = tara_v1/eixos_v1

    resis_norm_V1v = 0.65+(13.15/peixo_V1v)+(0.01405*velocidade)+(0.000945*area_v1*velocidade*velocidade/tara_v1)

    resis_pt_V1v = (11.2 - (0.3*peixo_V1v))
    
    resis_total_V1v = resis_aceleraçao+resis_curva_v+resis_norm_V1v+resis_rampa+resis_pt_V1v
    if tunel in ["S","s"]:
        resis_total_V1v = resis_total_V1v+1

    #vagão 2 
    peixo_V2v = tara_v2/eixos_v2

    resis_norm_V2v = 0.65+(13.15/peixo_V2v)+(0.01405*velocidade)+(0.000945*area_v2*velocidade*velocidade/tara_v2)

    resis_pt_V2v = (11.2 - (0.3*peixo_V2v))
    
    resis_total_V2v = resis_aceleraçao+resis_curva_v+resis_norm_V2v+resis_rampa+resis_pt_V2v
    if tunel in ["S","s"]:
        resis_total_V2v = resis_total_V2v+1
    
    #vagão 3 
    peixo_V3v = tara_v3/eixos_v3

    resis_norm_V3v = 0.65+(13.15/peixo_V3v)+(0.01405*velocidade)+(0.000945*area_v3*velocidade*velocidade/tara_v3)

    resis_pt_V3v = (11.2 - (0.3*peixo_V3v))
    
    resis_total_V3v = resis_aceleraçao+resis_curva_v+resis_norm_V3v+resis_rampa+resis_pt_V3v
    if tunel in ["S","s"]:
        resis_total_V3v = resis_total_V3v+1

    #vagão 4
    peixo_V4v = tara_v4/eixos_v4

    resis_norm_V4v = 0.65+(13.15/peixo_V4v)+(0.01405*velocidade)+(0.000945*area_v4*velocidade*velocidade/tara_v4)

    resis_pt_V4v = (11.2 - (0.3*peixo_V4v))
    
    resis_total_V4v = resis_aceleraçao+resis_curva_v+resis_norm_V4v+resis_rampa+resis_pt_V4v
    if tunel in ["S","s"]:
        resis_total_V4v = resis_total_V4v+1

    # Vagões carregados:

    #vagão 1
    peixo_V1c = (lotacao_v1+tara_v1)/eixos_v1

    resis_norm_V1c = 0.65+(13.15/peixo_V1c)+(0.01405*velocidade)+(0.000945*area_v1*velocidade*velocidade/(lotacao_v1+tara_v1))

    resis_pt_V1c = (11.2 - (0.3*peixo_V1c))
    
    resis_total_V1c = resis_aceleraçao+resis_curva_v+resis_rampa+resis_norm_V1c+resis_pt_V1c
    if tunel in ["S","s"]:
        resis_total_V1c = resis_total_V1c+1

    #vagão 2
    peixo_V2c = (lotacao_v2+tara_v2)/eixos_v2

    resis_norm_V2c = 0.65+(13.15/peixo_V2c)+(0.01405*velocidade)+(0.000945*area_v2*velocidade*velocidade/(tara_v2+lotacao_v2))

    resis_pt_V2c = (11.2 - (0.3*peixo_V2c))
    
    resis_total_V2c = resis_aceleraçao+resis_curva_v+resis_rampa+resis_norm_V2c+resis_pt_V2c
    if tunel in ["S","s"]:
        resis_total_V2c = resis_total_V2c+1

    #vagão 3
    peixo_V3c = (lotacao_v3+tara_v3)/eixos_v3

    resis_norm_V3c = 0.65+(13.15/peixo_V3c)+(0.01405*velocidade)+(0.000945*area_v3*velocidade*velocidade/(tara_v3+lotacao_v3))

    resis_pt_V3c = (11.2 - (0.3*peixo_V3c))
    
    resis_total_V3c = resis_aceleraçao+resis_curva_v+resis_rampa+resis_norm_V3c+resis_pt_V3c
    if tunel in ["S","s"]:
        resis_total_V3c = resis_total_V3c+1

    #vagão 4
    peixo_V4c = (lotacao_v4+tara_v4)/eixos_v4

    resis_norm_V4c = 0.65+(13.15/peixo_V4c)+(0.01405*velocidade)+(0.000945*area_v4*velocidade*velocidade/(tara_v4+lotacao_v4))

    resis_pt_V4c = (11.2 - (0.3*peixo_V4c))
    
    resis_total_V4c = resis_aceleraçao+resis_curva_v+resis_rampa+resis_norm_V4c+resis_pt_V4c
    if tunel in ["S","s"]:
        resis_total_V4c = resis_total_V4c+1

    # lotações:
    if selecionado in ["T","t"]:
        vagoes_v = [tara_v1,tara_v2,tara_v3,tara_v4]
        vagoes_c = [(lotacao_v1+tara_v1),(lotacao_v2+tara_v2),(lotacao_v3+tara_v3),(lotacao_v4+tara_v4)]
        v1 = float('-inf')
        v2 = float('-inf')
        v3 = float('inf')
        v4 = float('inf')

        for vagao in vagoes_c:
            if v1 < vagao:
                v1 = vagao
                V1_name = nome_v1
            if v3 > vagao:
                v3 = vagao
                V1_name = nome_v2
        for vagao in vagoes_v:
            if v2 < vagao:
                v2 = vagao
                V1_name = nome_v3
            if v4 > vagao:
                v4 = vagao
                V1_name = nome_v4

        if v1 == vagoes_c[0]:
            Rt1 = resis_total_V1c
            V1_name = nome_v1
        elif v1 == vagoes_c[1]:
            Rt1 = resis_total_V2c
            V1_name = nome_v2
        elif v1 == vagoes_c[2]:
            Rt1 = resis_total_V3c
            V1_name = nome_v3
        elif v1 == vagoes_c[3]:
            Rt1 = resis_total_V4c
            V1_name = nome_v4
        
        if v2 == tara_v1:
            Rt2 = resis_total_V1v
            lotv2 = lotacao_v1
            V2_name = nome_v1
        elif v2 == tara_v2:
            Rt2 = resis_total_V2v
            lotv2 = lotacao_v2
            V2_name = nome_v2
        elif v2 == tara_v3:
            Rt2 = resis_total_V3v
            lotv2 = lotacao_v3
            V2_name = nome_v3
        elif v2 == tara_v4:
            Rt2 = resis_total_V4v
            lotv2 = lotacao_v4
            V2_name = nome_v4
        else:
            raise("ERRO: dados incondizentes")

        if v3 == vagoes_c[0]:
            Rt3 = resis_total_V1c
            tarv3 = tara_v1
            V3_name = nome_v1
        elif v3 == vagoes_c[1]:
            Rt3 = resis_total_V2c
            tarv3 = tara_v2
            V3_name = nome_v2
        elif v3 == vagoes_c[2]:
            Rt3 = resis_total_V3c
            tarv3 = tara_v3
            V3_name = nome_v3
        elif v3 == vagoes_c[3]:
            Rt3 = resis_total_V4c
            tarv3 = tara_v4
            V3_name = nome_v4
        else:
            raise("ERRO: dados incondizentes")
        
        if v4 == tara_v1:
            Rt4 = resis_total_V1v
            V4_name = nome_v1
        elif v4 == tara_v2:
            Rt4 = resis_total_V2v
            V4_name = nome_v2
        elif v4 == tara_v3:
            Rt4 = resis_total_V3v
            V4_name = nome_v3
        elif v4 == tara_v4:
            Rt4 = resis_total_V4v
            V4_name = nome_v4

        lv1 = c_r/Rt1
        lv4 = c_r/Rt4

        Nv2 = c_r/(Rt2*v2)
        Nv3 = c_r/(Rt3*v3)

        CF = (lv1-lv4)/(Nv2-Nv3)
        if CF < 0:
            raise("ERRO: dados incondizentes")

        if Nv2 >= int(Nv2) + 0.75:
            Nv2a = int(Nv2) + 1
        elif Nv2 < int(Nv2) + 0.75:
            Nv2a = int(Nv2)
        if Nv3 >= int(Nv3) + 0.75:
            Nv3a = int(Nv3) + 1
        elif Nv3 < int(Nv3) + 0.75:
            Nv3a = int(Nv3)

        La = ((lv1+(CF*Nv3a))+(lv4+(CF*Nv2a)))/2


# Resultados locomotiva
if selecionado in ["L", "l"]:
    with open(f"Resultados-Locomotiva_{nome}.txt", "a", encoding="utf-8") as arquivo:
        if tunel in ["N", "n"]:
            arquivo.write(f"O trecho analisado contém:\n")
            if bitola == 1:
                arquivo.write(f"    - Bitola métrica\n")
            elif bitola == 1.6:
                arquivo.write(f"    - Bitola larga\n")
            if G20 > 0:
                arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
            else:
                arquivo.write(f"    - Raios de mínimo de curvatura = {raio}m\n")
            arquivo.write(f"    - Rampa compensada = {i}%\n")
            arquivo.write(f"    - Aderência em velocidade nula = {c_aderencia}%\n")
            arquivo.write(f"    - Rendimento das locomotivas = {rendimento}%\n")
        else:
            arquivo.write(f"O trecho analisado contém:\n")
            if bitola == 1:
                arquivo.write(f"    - Bitola métrica\n")
            elif bitola == 1.6:
                arquivo.write(f"    - Bitola larga\n")
            if G20 > 0:
                arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
            else:
                arquivo.write(f"    - Raios de mínimo de curvatura = {raio}\n")
            arquivo.write(f"    - Rampa compensada = {i}\n")
            arquivo.write(f"    - Aderência em velocidade nula = {c_aderencia}\n")
            arquivo.write(f"    - Rendimento das locomotivas = {rendimento}\n")
            arquivo.write(f"    - Túnel em linha singela\n")
        arquivo.write(f"\n")
        arquivo.write(f"*A locomotiva analisada foi: {locomotiva_nome}:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"    - Eixos: {eixos_l}\n")
        arquivo.write(f"    - Peso total: {peso_l}\n")
        arquivo.write(f"    - Taxa de aceleração: {aceleraçao}\n")
        arquivo.write(f"    - Potência: {hp}\n")
        arquivo.write(f"    - Velocidade constante: {velocidade}\n")
        arquivo.write(f"    - Área: {area_l}\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos de resistência da VP:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência rampa = 10 x i% ==> {resis_rampa} Kgf/tf = 10 x {i}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência aceleração (Ra) = 31,1 x a ==> {resis_aceleraçao} Kgf/tf = 31,1 x {aceleraçao}\n")
        arquivo.write(f"\n")
        if tunel in ["S", "s"]:
            arquivo.write(f"    Resistência tunel (Rt) = 2 Kgf/tf \n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos referentes à locomotiva*\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Peixo locomotiva (Peixo_l) = Pl / eixos_l ==> {peixo_l} Kgf/tf = {peso_l} / {eixos_l}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência normal locomotiva (Rnl) = 0.65+(13.15/Peixo_l)+(0.00932 x V)+(0.00456 x Área_l x V^2/peso_l) ==> {resis_normal_l} Kgf/tf = 0.65+(13.15/{peixo_l})+(0.000932 x {velocidade})+(0.00456 x {area_l} x {velocidade}^2/{peso_l})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência partida locomotiva (Rpl) = 11,2 - (0,3 x Peixo_l) ==> {resis_partida_l} Kgf/tf = 11.2 - (0.3 x {peixo_l})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência curva (Rcl) = 500 x bitola / raio ==> {resis_curva_l} Kgf/tf = 500 x {bitola} / {raio}\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"    Resistência total  locomotiva (Rtl) = Ra+Rcl+Rr+Rpl+Rnl ==> {resis_total} Kgf/tf  = {resis_aceleraçao} + {resis_curva_l} + {resis_rampa} + {resis_partida_l} + {resis_normal_l}\n")
        else:
            arquivo.write(f"    Resistência total  locomotiva (Rtl) = Rnl+Rpl+Rcl+Rr+Ra+Rt ==> {resis_total} Kgf/tf = {resis_aceleraçao}+{resis_curva_l}+{resis_rampa}+{resis_partida_l}+{resis_normal_l}+2\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Força tratora (Ft) = P(hp) x n(rendimento) x {fator_t} / V ==> {tracao} Kgf = {hp} x {rendimento/100} x {fator_t} / {velocidade}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Aderência = Pl x Ca (coeficiente de aderência) / (1 + (0.01 x V)) ==> {aderencia} Kgf = {peso_l*1000} x {c_aderencia/100} / (1 + (0.01 x {velocidade}))\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Esforço trator (Et) = {t_pratica} kgf\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Capacidade de reboque (Cr) = Et - Rtl x Pl ==> {c_r} kgf = {t_pratica} - {resis_total} x {peso_l}\n")

# Resultados vagôes
if selecionado in ["V", "v"]:
    with open(f"Resultados-Vagões_{nome}.txt", "a", encoding="utf-8") as arquivo:
        if tunel in ["N", "n"]:
            arquivo.write(f"O trecho analisado contém:\n")
            if bitola == 1:
                arquivo.write(f"    - Bitola métrica\n")
            elif bitola == 1.6:
                arquivo.write(f"    - Bitola larga\n")
            if G20 > 0:
                arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
            else:
                arquivo.write(f"    - Raios de mínimo de curvatura = {raio}m\n")
            arquivo.write(f"    - Rampa compensada = {i}%\n")
            arquivo.write(f"    - Aderência em velocidade nula = {c_aderencia}%\n")
            arquivo.write(f"    - Rendimento das locomotivas = {rendimento}%\n")
        else:
            arquivo.write(f"O trecho analisado contém:\n")
            if bitola == 1:
                arquivo.write(f"    - Bitola métrica\n")
            elif bitola == 1.6:
                arquivo.write(f"    - Bitola larga\n")
            if G20 > 0:
                arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
            else:
                arquivo.write(f"    - Raios de mínimo de curvatura = {raio}\n")
            arquivo.write(f"    - Rampa compensada = {i}\n")
            arquivo.write(f"    - Aderência em velocidade nula = {c_aderencia}\n")
            arquivo.write(f"    - Rendimento das locomotivas = {rendimento}\n")
            arquivo.write(f"    - Túnel em linha singela\n") 
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Vagões analisados:*\n")
        arquivo.write(f"    {nome_v1}:\n")
        arquivo.write(f"    - Tara: {tara_v1}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v1}:\n")
        arquivo.write(f"    - Área: {area_v1}:\n")
        arquivo.write(f"    - Eixos: {eixos_v1}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"    {nome_v2}:\n")
        arquivo.write(f"    - Tara: {tara_v2}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v2}:\n")
        arquivo.write(f"    - Área: {area_v2}:\n")
        arquivo.write(f"    - Eixos: {eixos_v2}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"    {nome_v3}:\n")
        arquivo.write(f"    - Tara: {tara_v3}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v3}:\n")
        arquivo.write(f"    - Área: {area_v3}:\n")
        arquivo.write(f"    - Eixos: {eixos_v3}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"    {nome_v4}:\n")
        arquivo.write(f"    - Tara: {tara_v4}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v4}:\n")
        arquivo.write(f"    - Área: {area_v4}:\n")
        arquivo.write(f"    - Eixos: {eixos_v4}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos dos vagões:*\n")
        arquivo.write(f"\n")
        if bitola == 1:
            arquivo.write(f"    Resistência curva dos vagões (Rcv) = 0,54 x G20 ==> {resis_curva_v} Kgf/tf = 0,54 x {G20}\n")
        elif bitola == 1.6:
            arquivo.write(f"    Resistência curva dos vagões (Rcv) = 0,65 x G20 ==> {resis_curva_v} Kgf/tf = 0,65 x {G20}\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v1} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V1v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v1} vazio (Rnv1v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2) / tara) ==> {resis_norm_V1v} Kgf/tf = 0.65 + (13.15 / {peixo_V1v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v1} x {velocidade}^2 / {tara_v1})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v1} vazio (Rpv1v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V1v} Kgf/tf = 11,2 - (0,3 x {peixo_V1v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v1} vazio (Rtv1v) = Rnv1v+Rpv1v+Rcv+Rr+Ra ==> {resis_total_V1v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1v} + {resis_rampa} + {resis_pt_V1v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v1} vazio (Rtv1v) = Rnv1v+Rpv1v+Rcv+Rr+Ra+Rt ==> {resis_total_V1v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1v} + {resis_rampa} + {resis_pt_V1v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v2} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V2v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v2} vazio (Rnv2v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2 / tara) ==> {resis_norm_V2v} Kgf/tf = 0.65 + (13.15 / {peixo_V2v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v2} x {velocidade}^2 / {tara_v2})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v2} vazio (Rpv2v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V2v} Kgf/tf = 11,2 - (0,3 x {peixo_V2v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v2} vazio (Rtv2v) = Rnv2v+Rpv2v+Rcv+Rr+Ra ==> {resis_total_V2v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2v} + {resis_rampa} + {resis_pt_V2v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v2} vazio (Rtv2v) = Rnv2v+Rpv2v+Rcv+Rr+Ra+Rt ==> {resis_total_V2v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2v} + {resis_rampa} + {resis_pt_V2v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v3} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V3v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v3} vazio (Rnv3v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2 / tara) ==> {resis_norm_V1v} Kgf/tf = 0.65 + (13.15 / {peixo_V3v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v3} x {velocidade}^2 / {tara_v3})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v3} vazio (Rpv3v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V3v} Kgf/tf = 11,2 - (0,3 x {peixo_V3v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v3} vazio (Rtv3v) = Rnv3v+Rpv3v+Rcv+Rr+Ra ==> {resis_total_V3v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3v} + {resis_rampa} + {resis_pt_V3v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v3} vazio (Rtv3v) = Rnv3v+Rpv3v+Rcv+Rr+Ra+Rt ==> {resis_total_V3v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3v} + {resis_rampa} + {resis_pt_V3v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v4} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V4v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v4} vazio (Rnv4v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2 / tara) ==> {resis_norm_V4v} Kgf/tf = 0.65 + (13.15 / {peixo_V4v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v4} x {velocidade}^2 / {tara_v4})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v4} vazio (Rpv4v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V4v} Kgf/tf = 11,2 - (0,3 x {peixo_V4v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v4} vazio (Rtv4v) = Rnv4v+Rpv4v+Rcv+Rr+Ra ==> {resis_total_V4v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4v} + {resis_rampa} + {resis_pt_V4v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v4} vazio (Rtv4v) = Rnv4v+Rpv4v+Rcv+Rr+Ra+Rt ==> {resis_total_V4v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4v} + {resis_rampa} + {resis_pt_V4v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v1} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V1c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v1} carregado (Rnv1v) = 0,65 + (13,15 / peixo) + ((0,001405 x V) + (0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V1c} Kgf/tf = 0.65 + (13.15 / {peixo_V1c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v1} x {velocidade}^2 / {tara_v1+lotacao_v1})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v1} carregado (Rpv1v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V1c} Kgf/tf = 11,2 - (0,3 x {peixo_V1c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v1} carregado (Rtv1v) = Rnv1c+Rpv1c+Rcc+Rr+Ra ==> {resis_total_V1c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1c} + {resis_rampa} + {resis_pt_V1c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v1} carregado (Rtv1v) = Rnv1c+Rpv1c+Rcc+Rr+Ra+Rt ==> {resis_total_V1c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1c} + {resis_rampa} + {resis_pt_V1c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v2} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V2c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v2} carregado (Rnv2c) = 0,65 + (13,15 / peixo) + (0,001405 x V) + ((0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V2c} Kgf/tf = 0.65 + (13.15 / {peixo_V2c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v2} x {velocidade}^2 / {tara_v1+lotacao_v2})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v2} carregado (Rpv2c) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V2c} Kgf/tf = 11,2 - (0,3 x {peixo_V2c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v2} carregado (Rtv2c) = Rnv2c+Rpv2c+Rcc+Rr+Ra ==> {resis_total_V2c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2c} + {resis_rampa} + {resis_pt_V2c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v2} carregado (Rtv2c) = Rnv2c+Rpv2c+Rcc+Rr+Ra+Rt ==> {resis_total_V2c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2c} + {resis_rampa} + {resis_pt_V2c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v3} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V3c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v3} carregado (Rnv3c) = 0,65 + (13,15 / peixo) + (0,001405 x V) + ((0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V3c} Kgf/tf = 0.65 + (13.15 / {peixo_V3c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v3} x {velocidade}^2 / {tara_v3+lotacao_v3})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v3} carregado (Rpv3c) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V3c} Kgf/tf = 11,2 - (0,3 x {peixo_V3c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v3} carregado (Rtv3c) = Rnv3c+Rpv3c+Rcc+Rr+Ra ==> {resis_total_V3c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3c} + {resis_rampa} + {resis_pt_V3c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v3} carregado (Rtv3c) = Rnv3c+Rpv3c+Rcc+Rr+Ra+Rt ==> {resis_total_V3c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3c} + {resis_rampa} + {resis_pt_V3c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v4} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V4c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v4} carregado (Rnv4c) = 0,65 + (13,15 / peixo) + (0,001405 x V) + ((v0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V4c} Kgf/tf = 0.65 + (13.15 / {peixo_V4c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v4} x {velocidade}^2 / {tara_v4+lotacao_v4})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v4} carregado (Rpv4c) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V4c} Kgf/tf = 11,2 - (0,3 x {peixo_V4c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v4} carregado (Rtv4c) = Rnv4c+Rpv4c+Rcc+Rr+Ra ==> {resis_total_V4c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4c} + {resis_rampa} + {resis_pt_V4c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v4} carregado (Rtv4c) = Rnv4c+Rpv4c+Rcc+Rr+Ra+Rt ==> {resis_total_V4c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4c} + {resis_rampa} + {resis_pt_V4c} + 2\n")

# Resultados completos
if selecionado in ["T", "t"]: 
    with open(f"Resultados-Total_{nome}.txt", "a", encoding="utf-8") as arquivo:
        if tunel in ["N", "n"]:
            arquivo.write(f"O trecho analisado contém:\n")
            if bitola == 1:
                arquivo.write(f"    - Bitola métrica\n")
            elif bitola == 1.6:
                arquivo.write(f"    - Bitola larga\n")
            if G20 > 0:
                arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
            else:
                arquivo.write(f"    - Raios de mínimo de curvatura = {raio}m\n")
            arquivo.write(f"    - Rampa compensada = {i}%\n")
            arquivo.write(f"    - Aderência em velocidade nula = {c_aderencia}%\n")
            arquivo.write(f"    - Rendimento das locomotivas = {rendimento}%\n")
        else:
            arquivo.write(f"O trecho analisado contém:\n")
            if bitola == 1:
                arquivo.write(f"    - Bitola métrica\n")
            elif bitola == 1.6:
                arquivo.write(f"    - Bitola larga\n")
            if G20 > 0:
                arquivo.write(f"    - Raios de mínimo de curvatura: G20 = {G20}\n")
            else:
                arquivo.write(f"    - Raios de mínimo de curvatura = {raio}\n")
            arquivo.write(f"    - Rampa compensada = {i}\n")
            arquivo.write(f"    - Aderência em velocidade nula = {c_aderencia}\n")
            arquivo.write(f"    - Rendimento das locomotivas = {rendimento}\n")
            arquivo.write(f"    - Túnel em linha singela\n") 
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*A locomotiva analisada foi: {locomotiva_nome}:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"    - Eixos: {eixos_l}\n")
        arquivo.write(f"    - Peso total: {peso_l}\n")
        arquivo.write(f"    - Taxa de aceleração: {aceleraçao}\n")
        arquivo.write(f"    - Potência: {hp}\n")
        arquivo.write(f"    - Velocidade constante: {velocidade}\n")
        arquivo.write(f"    - Área: {area_l}\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Vagões analisados:*\n")
        arquivo.write(f"    {nome_v1}:\n")
        arquivo.write(f"    - Tara: {tara_v1}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v1}:\n")
        arquivo.write(f"    - Área: {area_v1}:\n")
        arquivo.write(f"    - Eixos: {eixos_v1}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"    {nome_v2}:\n")
        arquivo.write(f"    - Tara: {tara_v2}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v2}:\n")
        arquivo.write(f"    - Área: {area_v2}:\n")
        arquivo.write(f"    - Eixos: {eixos_v2}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"    {nome_v3}:\n")
        arquivo.write(f"    - Tara: {tara_v3}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v3}:\n")
        arquivo.write(f"    - Área: {area_v3}:\n")
        arquivo.write(f"    - Eixos: {eixos_v3}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"    {nome_v4}:\n")
        arquivo.write(f"    - Tara: {tara_v4}:\n")
        arquivo.write(f"    - Lotação: {lotacao_v4}:\n")
        arquivo.write(f"    - Área: {area_v4}:\n")
        arquivo.write(f"    - Eixos: {eixos_v4}:\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Vagões que serão utilizados:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"    V1 (mais pesado carregado): {V1_name}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    V2 (mais pesado vazio): {V2_name}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    V3 (mais leve carregado): {V3_name}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    V4 (mais leve vazio): {V4_name}\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos de resistência da VP:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência rampa = 10 x i% ==> {resis_rampa} Kgf/tf = 10 x {i}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência aceleração (Ra) = 31,1 x a ==> {resis_aceleraçao} Kgf/tf = 31,1 x {aceleraçao}\n")
        arquivo.write(f"\n")
        if tunel in ["S", "s"]:
            arquivo.write(f"    Resistência tunel (Rt) = 2 Kgf/tf \n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos referentes à locomotiva*\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Peixo locomotiva (Peixo_l) = Pl / eixos_l ==> {peixo_l} Kgf/tf = {peso_l} / {eixos_l}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência normal locomotiva (Rnl) = 0.65+(13.15/Peixo_l)+(0.00932 x V)+(0.00456 x Área_l x V^2/peso_l) ==> {resis_normal_l} Kgf/tf = 0.65+(13.15/{peixo_l})+(0.000932 x {velocidade})+(0.00456 x {area_l} x {velocidade}^2/{peso_l})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência partida locomotiva (Rpl) = 11,2 - (0,3 x Peixo_l) ==> {resis_partida_l} Kgf/tf = 11.2 - (0.3 x {peixo_l})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Resistência curva (Rcl) = 500 x bitola / raio ==> {resis_curva_l} Kgf/tf = 500 x {bitola} / {raio}\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"    Resistência total  locomotiva (Rtl) = Ra+Rcl+Rr+Rpl+Rnl ==> {resis_total} Kgf/tf  = {resis_aceleraçao} + {resis_curva_l} + {resis_rampa} + {resis_partida_l} + {resis_normal_l}\n")
        else:
            arquivo.write(f"    Resistência total  locomotiva (Rtl) = Rnl+Rpl+Rcl+Rr+Ra+Rt ==> {resis_total} Kgf/tf = {resis_aceleraçao}+{resis_curva_l}+{resis_rampa}+{resis_partida_l}+{resis_normal_l}+2\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Força tratora (Ft) = P(hp) x n(rendimento) x {fator_t} / V ==> {tracao} Kgf = {hp} x {rendimento/100} x {fator_t} / {velocidade}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Aderência = Pl x Ca (coeficiente de aderência) / (1 + (0.01 x V)) ==> {aderencia} Kgf = {peso_l*1000} x {c_aderencia/100} / (1 + (0.01 x {velocidade}))\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Esforço trator (Et) = {t_pratica} kgf\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Capacidade de reboque (Cr) = Et - Rtl x Pl ==> {c_r} kgf = {t_pratica} - {resis_total} x {peso_l}\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos dos vagões:*\n")
        arquivo.write(f"\n")
        if bitola == 1:
            arquivo.write(f"    Resistência curva dos vagões (Rcv) = 0,54 x G20 ==> {resis_curva_v} Kgf/tf = 0,54 x {G20}\n")
        elif bitola == 1.6:
            arquivo.write(f"    Resistência curva dos vagões (Rcv) = 0,65 x G20 ==> {resis_curva_v} Kgf/tf = 0,65 x {G20}\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v1} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V1v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v1} vazio (Rnv1v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2) / tara) ==> {resis_norm_V1v} Kgf/tf = 0.65 + (13.15 / {peixo_V1v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v1} x {velocidade}^2 / {tara_v1})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v1} vazio (Rpv1v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V1v} Kgf/tf = 11,2 - (0,3 x {peixo_V1v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v1} vazio (Rtv1v) = Rnv1v+Rpv1v+Rcv+Rr+Ra ==> {resis_total_V1v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1v} + {resis_rampa} + {resis_pt_V1v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v1} vazio (Rtv1v) = Rnv1v+Rpv1v+Rcv+Rr+Ra+Rt ==> {resis_total_V1v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1v} + {resis_rampa} + {resis_pt_V1v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v2} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V2v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v2} vazio (Rnv2v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2 / tara) ==> {resis_norm_V2v} Kgf/tf = 0.65 + (13.15 / {peixo_V2v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v2} x {velocidade}^2 / {tara_v2})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v2} vazio (Rpv2v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V2v} Kgf/tf = 11,2 - (0,3 x {peixo_V2v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v2} vazio (Rtv2v) = Rnv2v+Rpv2v+Rcv+Rr+Ra ==> {resis_total_V2v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2v} + {resis_rampa} + {resis_pt_V2v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v2} vazio (Rtv2v) = Rnv2v+Rpv2v+Rcv+Rr+Ra+Rt ==> {resis_total_V2v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2v} + {resis_rampa} + {resis_pt_V2v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v3} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V3v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v3} vazio (Rnv3v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2 / tara) ==> {resis_norm_V1v} Kgf/tf = 0.65 + (13.15 / {peixo_V3v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v3} x {velocidade}^2 / {tara_v3})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v3} vazio (Rpv3v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V3v} Kgf/tf = 11,2 - (0,3 x {peixo_V3v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v3} vazio (Rtv3v) = Rnv3v+Rpv3v+Rcv+Rr+Ra ==> {resis_total_V3v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3v} + {resis_rampa} + {resis_pt_V3v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v3} vazio (Rtv3v) = Rnv3v+Rpv3v+Rcv+Rr+Ra+Rt ==> {resis_total_V3v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3v} + {resis_rampa} + {resis_pt_V3v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v4} vazio:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = tara / eixos ==> {peixo_V4v} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v4} vazio (Rnv4v) = 0,65 + (13,15 / peixo) + (0,001405 x V) + (0,000945 x area x V^2 / tara) ==> {resis_norm_V4v} Kgf/tf = 0.65 + (13.15 / {peixo_V4v}) + (0.001405 x {velocidade}) + (0.000945 x {area_v4} x {velocidade}^2 / {tara_v4})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v4} vazio (Rpv4v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V4v} Kgf/tf = 11,2 - (0,3 x {peixo_V4v})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v4} vazio (Rtv4v) = Rnv4v+Rpv4v+Rcv+Rr+Ra ==> {resis_total_V4v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4v} + {resis_rampa} + {resis_pt_V4v}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v4} vazio (Rtv4v) = Rnv4v+Rpv4v+Rcv+Rr+Ra+Rt ==> {resis_total_V4v} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4v} + {resis_rampa} + {resis_pt_V4v} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v1} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V1c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v1} carregado (Rnv1v) = 0,65 + (13,15 / peixo) + ((0,001405 x V) + (0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V1c} Kgf/tf = 0.65 + (13.15 / {peixo_V1c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v1} x {velocidade}^2 / {tara_v1+lotacao_v1})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v1} carregado (Rpv1v) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V1c} Kgf/tf = 11,2 - (0,3 x {peixo_V1c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v1} carregado (Rtv1v) = Rnv1c+Rpv1c+Rcc+Rr+Ra ==> {resis_total_V1c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1c} + {resis_rampa} + {resis_pt_V1c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v1} carregado (Rtv1v) = Rnv1c+Rpv1c+Rcc+Rr+Ra+Rt ==> {resis_total_V1c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V1c} + {resis_rampa} + {resis_pt_V1c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v2} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V2c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v2} carregado (Rnv2c) = 0,65 + (13,15 / peixo) + (0,001405 x V) + ((0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V2c} Kgf/tf = 0.65 + (13.15 / {peixo_V2c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v2} x {velocidade}^2 / {tara_v1+lotacao_v2})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v2} carregado (Rpv2c) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V2c} Kgf/tf = 11,2 - (0,3 x {peixo_V2c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v2} carregado (Rtv2c) = Rnv2c+Rpv2c+Rcc+Rr+Ra ==> {resis_total_V2c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2c} + {resis_rampa} + {resis_pt_V2c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v2} carregado (Rtv2c) = Rnv2c+Rpv2c+Rcc+Rr+Ra+Rt ==> {resis_total_V2c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V2c} + {resis_rampa} + {resis_pt_V2c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v3} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V3c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v3} carregado (Rnv3c) = 0,65 + (13,15 / peixo) + (0,001405 x V) + ((0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V3c} Kgf/tf = 0.65 + (13.15 / {peixo_V3c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v3} x {velocidade}^2 / {tara_v3+lotacao_v3})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v3} carregado (Rpv3c) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V3c} Kgf/tf = 11,2 - (0,3 x {peixo_V3c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v3} carregado (Rtv3c) = Rnv3c+Rpv3c+Rcc+Rr+Ra ==> {resis_total_V3c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3c} + {resis_rampa} + {resis_pt_V3c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v3} carregado (Rtv3c) = Rnv3c+Rpv3c+Rcc+Rr+Ra+Rt ==> {resis_total_V3c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V3c} + {resis_rampa} + {resis_pt_V3c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"    *Resistências do {nome_v4} carregado:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Peixo = (tara + lotação) / eixos ==> {peixo_V4c} Kgf/tf\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência normal {nome_v4} carregado (Rnv4c) = 0,65 + (13,15 / peixo) + (0,001405 x V) + ((v0,000945 x area x V^2) / (tara + lotação)) ==> {resis_norm_V4c} Kgf/tf = 0.65 + (13.15 / {peixo_V4c}) + (0.001405 x {velocidade}) + (0.000945 x {area_v4} x {velocidade}^2 / {tara_v4+lotacao_v4})\n")
        arquivo.write(f"\n")
        arquivo.write(f"        Resistência partida {nome_v4} carregado (Rpv4c) = 11,2 - (0,3 x Peixo) ==> {resis_pt_V4c} Kgf/tf = 11,2 - (0,3 x {peixo_V4c})\n")
        arquivo.write(f"\n")
        if tunel in ["N", "n"]:
            arquivo.write(f"        Resistência total {nome_v4} carregado (Rtv4c) = Rnv4c+Rpv4c+Rcc+Rr+Ra ==> {resis_total_V4c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4c} + {resis_rampa} + {resis_pt_V4c}\n")
        else:
            arquivo.write(f"        Resistência total {nome_v4} carregado (Rtv4c) = Rnv4c+Rpv4c+Rcc+Rr+Ra+Rt ==> {resis_total_V4c} Kgf/tf = {resis_aceleraçao} + {resis_curva_v} + {resis_norm_V4c} + {resis_rampa} + {resis_pt_V4c} + 2\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"\n")
        arquivo.write(f"*Cálculos referentes à lotação ajustada:*\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Lotação do vagão {V1_name} (Lv1) = Cr / Rtv1 ==> {lv1} t = {c_r} / {Rt1}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Lotação do vagão {V4_name} (Lv4) = Cr / Rtv4 ==> {lv4} t = {c_r} / {Rt4}\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Número de vagões {V2_name} (Nv2) = Cr / Rtv2 ==> {Nv2} vagões = {c_r} / ({Rt2} x {v2})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Número de vagões {V3_name} (Nv3) = Cr / (Rtv3 x Pv3c)==> {Nv3} vagões = {c_r} / ({Rt3} x {v3})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Carro fator (Cf) = (lv1-lv4) / (Nv2-Nv3) ==> {CF} = ({lv1} - {lv4}) / ({Nv2} - {Nv3})\n")
        arquivo.write(f"\n")
        arquivo.write(f"    Lotação ajustada = ((Lv1 + (Cf x Nv3)) + (Lv4 + (Cf x Nv2))) / 2 ==> {La} t = (({lv1} + ({CF} x {Nv3a})) + ({lv4} + ({CF} x {Nv2a}))) / 2\n")

import time
print("Consluído com sucesso")
time.sleep(2)