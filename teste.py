def alphabet_position(text):
    alfabeto_txt = "abcdefghijklmnopqrstuvwxyz"
    alfabeto = list(alfabeto_txt)
    frase_final = ''
    
    if len(text) < 1:
        pass
    
    texto_formatado = text.replace(" ", "").lower()
    letras = list(texto_formatado)
    
    for i, letra in enumerate(letras):
        if letra == " ":
            pass
        
        for i_alfabeto, letra_alfabeto in enumerate(alfabeto):
            if letra == letra_alfabeto:
                frase_final += str(i_alfabeto+1) + " "
                
    print(frase_final)
                
                
def main():
    alphabet_position("The sunset sets at twelve o' clock.")
    
if __name__ == "__main__":
    main()
        