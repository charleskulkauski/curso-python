recipe = {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}

def cakes (recipe, available):
    valores_final = {}
    ing_faltantes = {}
    for ing_receita, valor in recipe.items():
        if ing_receita in available:
            valores_final[ing_receita] = available[ing_receita] // valor
        else:
            ing_faltantes[ing_receita] = valor
    
    if len(ing_faltantes) > 0:
        return 0
    else:
        menor_valor = min(valores_final.values())
        return menor_valor
            
    
    

cakes(recipe, available)