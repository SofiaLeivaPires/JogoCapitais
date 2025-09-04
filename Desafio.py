import random
import os

placarAcertos = []
placarErros = []

def jogo_estados(estados):
    jogadas = 0
    acertos = 0
    erros = 0

    estadosSorteados = []
    while len(estadosSorteados) < 10:
        estado = random.choice(list(estados.keys()))
        if estado not in estadosSorteados:
            estadosSorteados.append(estado)

    while jogadas <= 10:

        while True:

            questaoEstado = estadosSorteados.pop()
            print("====================================")
            print(f"Qual a capital de {questaoEstado}?")

            alternativa = []

            alternativaCerta = estados[questaoEstado]

            alternativa.append(alternativaCerta)

            escolhaUsuario = 0
            
            for i in range(3):
                gerador = random.choice(list(estados.values()))
                for item in alternativa:
                    while gerador == alternativaCerta or gerador == item:
                            gerador = random.choice(list(estados.values()))

                alternativa.append(gerador)
            random.shuffle(alternativa)

            for i in range(4):
                aux = alternativa.pop()
                print(f"{i + 1} - {aux}")
                if aux == alternativaCerta:
                    alternativaCerta = i + 1

            while escolhaUsuario < 1 or escolhaUsuario > 4:
                escolhaUsuario = int(input())
                if escolhaUsuario > 4 or escolhaUsuario < 1:
                    print("Digite uma alternativa válida: ")

            if escolhaUsuario == alternativaCerta:
                print("VOCÊ ACERTOU!!! :D")
                acertos = acertos + 1
            else:
                alternativaCerta = estados[questaoEstado]
                print("VOCÊ ERROU :((")
                print(f"Alternativa certa: {alternativaCerta}")    
                erros = erros + 1

            jogadas = jogadas + 1
            
            if jogadas == 10:
                placar(acertos,erros)
                print("============================")
                print("Deseja continuar?")
                print("1. Sim, continuar nesse mode")
                print("2. Voltar ao Menu")
                print("3. Sair do sistema")
                print("============================")

                jogar = int(input())
                os.system("cls")

                match jogar:
                    case 1:
                        jogo_estados(estados)
                    case 2:
                        menu()
                    case 3:
                        print("==================")
                        print("OBRIGADA POR JOGAR")
                        print("SAINDO............")
                        print("==================")

                    case _:
                        print("Inválido")      
       
estados_brasil = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

paises_africa = {
    # África do Norte
    "Argélia": "Argel",
    "Egito": "Cairo",
    "Líbia": "Trípoli",
    "Marrocos": "Rabat",
    "Sudão": "Cartum",
    "Sudão do Sul": "Juba",
    "Tunísia": "Túnis",
    "Saara Ocidental": "El Aiune (reivindicada)",

    # África Ocidental
    "Benim": "Porto Novo (oficial), Cotonou (sede do governo)",
    "Burquina Fasso": "Uagadugu",
    "Cabo Verde": "Praia",
    "Costa do Marfim": "Iamussucro (oficial), Abidjan (administrativa)",
    "Gâmbia": "Banjul",
    "Gana": "Acra",
    "Guiné": "Conacri",
    "Guiné-Bissau": "Bissau",
    "Libéria": "Monróvia",
    "Mali": "Bamaco",
    "Níger": "Niamei",
    "Nigéria": "Abuja",
    "Senegal": "Dacar",
    "Serra Leoa": "Freetown",
    "Togo": "Lomé",

    # África Central
    "Angola": "Luanda",
    "Camarões": "Yaoundé",
    "Chade": "Jamena",
    "Congo-Brazzaville (República do Congo)": "Brazzaville",
    "Congo-Kinshasa (República Democrática do Congo)": "Kinshasa",
    "Gabão": "Libreville",
    "Guiné Equatorial": "Malabo (oficial), Oyala (administrativa)",
    "República Centro-Africana": "Bangui",
    "São Tomé e Príncipe": "São Tomé",

    # África Oriental
    "Burundi": "Gitega",
    "Comores": "Moroni",
    "Djibuti": "Djibuti",
    "Eritreia": "Asmara",
    "Etiópia": "Adis Abeba",
    "Quênia": "Nairóbi",
    "Madagascar": "Antananarivo",
    "Malaui": "Lilongwe",
    "Maurícia": "Port Louis",
    "Moçambique": "Maputo",
    "Ruanda": "Kigali",
    "Seychelles": "Victoria",
    "Somália": "Mogadíscio",
    "Tanzânia": "Dodoma",
    "Uganda": "Campala",
    "Zâmbia": "Lusaca",
    "Zimbábue": "Harare",

    # África Austral
    "África do Sul": "Pretória (administrativa), Bloemfontein (judiciária), Cidade do Cabo (legislativa)",
    "Botsuana": "Gaborone",
    "Essuatíni (Suazilândia)": "Mbabane (administrativa), Lobamba (real e legislativa)",
    "Lesoto": "Maseru",
    "Namíbia": "Windhoek"
}

paises_america = {
    # América do Norte
    "Canadá": "Ottawa",
    "Estados Unidos": "Washington, D.C.",
    "México": "Cidade do México",
   
    # América Central
    "Belize": "Belmopan",
    "Costa Rica": "San José",
    "El Salvador": "San Salvador",
    "Guatemala": "Cidade da Guatemala",
    "Honduras": "Tegucigalpa",
    "Nicarágua": "Manágua",
    "Panamá": "Cidade do Panamá",
   
    # América do Sul
    "Argentina": "Buenos Aires",
    "Bolívia": "Sucre (constitucional), La Paz (sede do governo)",
    "Brasil": "Brasília",
    "Chile": "Santiago",
    "Colômbia": "Bogotá",
    "Equador": "Quito",
    "Guiana": "Georgetown",
    "Paraguai": "Assunção",
    "Peru": "Lima",
    "Suriname": "Paramaribo",
    "Uruguai": "Montevidéu",
    "Venezuela": "Caracas",

    # Caribe
    "Antígua e Barbuda": "Saint John's",
    "Bahamas": "Nassau",
    "Barbados": "Bridgetown",
    "Cuba": "Havana",
    "Dominica": "Roseau",
    "Granada": "Saint George's",
    "Haiti": "Porto Príncipe",
    "Jamaica": "Kingston",
    "República Dominicana": "Santo Domingo",
    "Santa Lúcia": "Castries",
    "São Cristóvão e Neves": "Basseterre",
    "São Vicente e Granadinas": "Kingstown",
    "Trindade e Tobago": "Porto de Espanha"
}

paises_asia = {
    # Ásia Ocidental (Oriente Médio)
    "Arábia Saudita": "Riad",
    "Armênia": "Erevã",
    "Azerbaijão": "Bacu",
    "Bahrein": "Manama",
    "Chipre": "Nicósia",
    "Emirados Árabes Unidos": "Abu Dhabi",
    "Geórgia": "Tbilisi",
    "Iêmen": "Sana",
    "Irã": "Teerã",
    "Iraque": "Bagdá",
    "Israel": "Jerusalém",
    "Jordânia": "Amã",
    "Kuwait": "Cidade do Kuwait",
    "Líbano": "Beirute",
    "Omã": "Mascate",
    "Palestina": "Jerusalém Oriental (reivindicada), Ramala (sede administrativa)",
    "Síria": "Damasco",
    "Turquia": "Ancara",
    "Catar": "Doha",

    # Ásia Central
    "Cazaquistão": "Astana (Nursultan)",
    "Quirguistão": "Bisqueque",
    "Tadjiquistão": "Duchambé",
    "Turcomenistão": "Asgabate",
    "Uzbequistão": "Tashkent",

    # Ásia do Sul
    "Afeganistão": "Cabul",
    "Bangladesh": "Daca",
    "Butão": "Thimphu",
    "Índia": "Nova Délhi",
    "Maldivas": "Malé",
    "Nepal": "Catmandu",
    "Paquistão": "Islamabade",
    "Sri Lanka": "Sri Jayawardenapura Kotte (administrativa), Colombo (comercial)",

    # Sudeste Asiático
    "Brunei": "Bandar Seri Begawan",
    "Camboja": "Phnom Penh",
    "Filipinas": "Manila",
    "Indonésia": "Jacarta",
    "Laos": "Vientiane",
    "Malásia": "Kuala Lumpur (oficial), Putrajaya (administrativa)",
    "Mianmar (Birmânia)": "Naypyidaw",
    "Singapura": "Singapura",
    "Tailândia": "Bangcoc",
    "Timor-Leste": "Díli",
    "Vietnã": "Hanói",

    # Leste Asiático
    "China": "Pequim",
    "Coreia do Norte": "Pyongyang",
    "Coreia do Sul": "Seul",
    "Japão": "Tóquio",
    "Mongólia": "Ulan Bator",
    "Taiwan": "Taipé",
    "Hong Kong (China)": "Hong Kong",
    "Macau (China)": "Macau"
}

paises_europa = {
    # Europa Ocidental
    "Alemanha": "Berlim",
    "Áustria": "Viena",
    "Bélgica": "Bruxelas",
    "França": "Paris",
    "Liechtenstein": "Vaduz",
    "Luxemburgo": "Luxemburgo",
    "Mônaco": "Mônaco",
    "Países Baixos (Holanda)": "Amsterdã",
    "Suíça": "Berna",

    # Europa Meridional (Sul)
    "Andorra": "Andorra-a-Velha",
    "Croácia": "Zagreb",
    "Eslovênia": "Liubliana",
    "Espanha": "Madri",
    "Grécia": "Atenas",
    "Itália": "Roma",
    "Malta": "Valeta",
    "Portugal": "Lisboa",
    "San Marino": "San Marino",
    "Sérvia": "Belgrado",
    "Montenegro": "Podgorica",
    "Bósnia e Herzegovina": "Saraievo",
    "Macedônia do Norte": "Escópia",
    "Kosovo": "Pristina",
    "Vaticano": "Cidade do Vaticano",
    "Albânia": "Tirana",

    # Europa Setentrional (Norte)
    "Dinamarca": "Copenhague",
    "Estônia": "Tallinn",
    "Finlândia": "Helsinque",
    "Islândia": "Reykjavik",
    "Irlanda": "Dublin",
    "Letônia": "Riga",
    "Lituânia": "Vilnius",
    "Noruega": "Oslo",
    "Suécia": "Estocolmo",
    "Reino Unido": "Londres",

    # Europa Oriental
    "Bielorrússia": "Minsk",
    "Bulgária": "Sófia",
    "Hungria": "Budapeste",
    "Moldávia": "Chisinau",
    "Polônia": "Varsóvia",
    "República Tcheca": "Praga",
    "Romênia": "Bucareste",
    "Eslováquia": "Bratislava",
    "Ucrânia": "Kiev",
    "Rússia": "Moscou",
}

paises_oceania = {
    # Australásia
    "Austrália": "Camberra",
    "Nova Zelândia": "Wellington",

    # Melanésia
    "Fiji": "Suva",
    "Papua-Nova Guiné": "Port Moresby",
    "Ilhas Salomão": "Honiara",
    "Vanuatu": "Port Vila",

    # Micronésia
    "Estados Federados da Micronésia": "Palikir",
    "Kiribati": "Tarawa do Sul",
    "Ilhas Marshall": "Majuro",
    "Nauru": "Yaren (distrito, sede do governo)",
    "Palau": "Ngerulmud",

    # Polinésia
    "Samoa": "Apia",
    "Tonga": "Nucualofa",
    "Tuvalu": "Funafuti"
}

def continentes():
    os.system("cls")
    print("===============================")
    print("Escolha o continente desejado: ")
    print("1. África")
    print("2. América")
    print("3. Ásia")
    print("4. Europa")
    print("5. Oceania")
    print("===============================")
    continente = int(input())
    os.system("cls")

    match continente:
        case 1:
            print("BEM VINDO AO CONTINENTE AFRICANO")
            jogo_estados(paises_africa)
        case 2:
            print("BEM VINDO AO CONTINENTE AMERICANO")
            jogo_estados(paises_america)
        case 3:
            print("BEM VINDO AO CONTINENTE ASIÁTICO")
            jogo_estados(paises_asia)
        case 4:
            print("BEM VINDO AO CONTINENTE EUROPEU")
            jogo_estados(paises_europa)
        case 5:
            print("BEM VINDO AO CONTINENTE OCEANICO")
            jogo_estados(paises_oceania)
                    
        case _:
            print("Digite um continente válido")

def placar(acertos, erros):
   
    placarAcertos.append(acertos)
    placarErros.append(erros)
    somaAcertos = 0
    somaErros = 0

    for itemAcertos in placarAcertos:
        somaAcertos += itemAcertos

    for itemErros in placarErros:
        somaErros += itemErros

    print("===================")
    print("PLACAR: ")
    print(f"Acertos: {somaAcertos}")
    print(f"Erros: {somaErros}")

def menu():
    while True:
        print("===================================")
        print("BEM VINDO AO JOGO PAÍSES & CAPITAIS")
        print("1. Estados e Capitais do Brasil")
        print("2. Países e Capitais do Mundo")
        print("3. Sair")
        print("===================================")

        print("Escolha seu mode: ")
        tipoMode = int(input())

        os.system("cls")
        match tipoMode:
            
            case 1:
                print("BEM VINDO AO BRASIL")
                jogo_estados(estados_brasil)
            case 2:
                continentes()
            case 3:
                print("==================")
                print("OBRIGADA POR JOGAR")
                print("SAINDO............")
                print("==================") 
                return False
            case _:
                print("Digite um mode válido: ")

menu()

