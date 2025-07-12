from django.shortcuts import render

def inicio(request):
    return render(request, "sitebrba/index.html")

def elenco(request):
    return render(request, "sitebrba/elenco.html", {
        "elenco_brba": elenco_brba
    })

def sobre(request):
    return render(request, "sitebrba/sobre.html")


elenco_brba = [
    {
        "id": 1,
        "nome": "Walter White",
        "idade_em_serie": 50,
        "personagem": "Protagonista/Vilão",
        "descricao": "Professor de química que, ao descobrir um câncer terminal, passa a produzir metanfetamina.",
        "imagem": "sitebrba/img/walterbrba.jpeg",
    },
    {
        "id": 2,
        "nome": "Jesse Pinkman",
        "idade_em_serie": 24,
        "personagem": "Protagonista/Auxiliar",
        "descricao": "Ex-aluno de Walter, entra no mundo do crime como fabricante e distribuidor.",
        "imagem": "sitebrba/img/jessebrba.jpeg",
    },
    {
        "id": 3,
        "nome": "Saul Goodman",
        "idade_em_serie": 46,
        "personagem": "Protagonista/Advogado",
        "descricao": "Advogado esperto que auxilia Walter e Jesse.",
        "imagem": "sitebrba/img/saulbrba.jpeg",
    },
    {
        "id": 4,
        "nome": "Gus Fring",
        "idade_em_serie": 55,
        "personagem": "Antagonista",
        "descricao": "Dono de fast-food que esconde um império de metanfetamina.",
        "imagem": "sitebrba/img/gusbrba.jpeg",
    },
    {
        "id": 5,
        "nome": "Mike Ehrmantraut",
        "idade_em_serie": 62,
        "personagem": "Antagonista/Protagonista",
        "descricao": "Homem de confiança de Gus, cuida de serviços sujos e segurança. Auxilia Walter e Jesse depois de algum tempo.",
        "imagem": "sitebrba/img/mikebrba.jpeg",
    },
    {
        "id": 6,
        "nome": "Hank Schrader",
        "idade_em_serie": 38,
        "personagem": "Antagonista/Policial",
        "descricao": "Cunhado de Walt, sua investigação quase descobre tudo.",
        "imagem": "sitebrba/img/hankbrba.jpeg",
    },
    {
        "id": 7,
        "nome": "Skyler White",
        "idade_em_serie": 48,
        "personagem": "Antagonista/Protagonista",
        "descricao": "Envolvida nos esquemas, lava o dinheiro para proteger a família.",
        "imagem": "sitebrba/img/skylerbrba.jpeg",
    },
    {
        "id": 8,
        "nome": "Walter White Jr.",
        "idade_em_serie": 16,
        "personagem": "Coadjuvante/Filho",
        "descricao": "Jovem com paralisia cerebral leve, idolatra o pai sem saber o que ele faz pelas costas.",
        "imagem": "sitebrba/img/waltersonbrba.jpeg",
    },
    {
        "id": 9,
        "nome": "Marie Schrader",
        "idade_em_serie": 35,
        "personagem": "Coadjuvante/Irmã",
        "descricao": "Esposa de Hank, tem tendência a furtos compulsivos.",
        "imagem": "sitebrba/img/mariebrba.jpeg",
    },
    {
        "id": 10,
        "nome": "Todd Alquist",
        "idade_em_serie": 18,
        "personagem": "Antagonista/Capanga",
        "descricao": "Trabalha para Jack; frio e imprevisível.",
        "imagem": "sitebrba/img/toddbrba.jpeg",
    },
    {
        "id": 11,
        "nome": "Tuco Salamanca",
        "idade_em_serie": 48,
        "personagem": "Antagonista",
        "descricao": "Primeiro contato de Jesse no tráfico, extremamente agressivo.",
        "imagem": "sitebrba/img/tucobrba.jpeg",
    },
    {
        "id": 12,
        "nome": "Jack Welker",
        "idade_em_serie": 38,
        "personagem": "Antagonista",
        "descricao": "Chefe de gangue que cruza o caminho de Walt no fim da série.",
        "imagem": "sitebrba/img/jackbrba.jpeg",
    },
]

