acertou = False
palavra_secreta = 'jabuticaba'
mascara = list(palavra_secreta)
mascara = ['*' for letra in mascara]

while True:
    letra = input('Digite uma letra: ').lower()
    
    if len(letra) > 1 and letra not in " ":
        print('Digite apenas uma letra!')
        continue

    if letra in palavra_secreta:
        if letra in mascara:
            print('Você já digitou essa letra, continue')
            continue
        
        i = 0
        while i <= len(palavra_secreta)-1:
            if letra == palavra_secreta[i]:
                mascara[i] = letra
            i+=1
    else:
        print('Letra errada! Continue')
          
    mascara_string = "".join(mascara)      
    print(f'Palavra formatada: {mascara_string}')
    
    if mascara_string == palavra_secreta:
        print(f'\nVocê acertou a palavra formatada!')
        break
        
        