import re

def atualizar_pagamento(intention):
    if intention == "atualizar" or intention == "mudar":
        return f"Parece que você quer {intention} o pagamento do seu cartão, para isso vá até o site: 123deoliveira4.com.br"
    
def status_pedido(intention):
    if intention == "status":
     return f"Parece que você quer {intention}, para ver seu pedido vá até o site: 567dossantos8.com.br"


intent_dict = {
    r"\b(?:[Pp]reciso|[Qq]uero)?(?:[Cc]omo)?(?:Método)?\s(?:posso)?\s?([Mm]udar)?\s?([Aa]tualizar)?\s?(?:de)?\s?(?:a)?\s?(?:meu|minhas)?\s?(?:[Ff]orma|[Ii]nformações)?(?:[Pp]agamento)?\s?(?:[Dd]esatualizado)?(?:,)?\s?(?:como)?\s?(?:proceder)?\s?(?:para)?\s?([Aa]tualizar)?(?:cartão)?\s?(?:de)?\s?(?:[Pp]agamento)?(?:,)?\s?(?:o)?\s?(?:que)?\s?(?:fazer)?(?:crédito)?\??": "atualizar",
    r""
}

action_dict = {
    "atualizar": atualizar_pagamento,
    "status": status_pedido
}

command = input("Digite o seu comando: ")
for key, value in intent_dict.items():
    pattern = re.compile(key)
    groups = pattern.findall(command)
    if groups:
        print(f"{action_dict[value](groups[0])}", end=" ")
print()