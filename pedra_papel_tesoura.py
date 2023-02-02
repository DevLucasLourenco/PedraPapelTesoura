import os 
import random


class ppd():      
    
    def titulo():
        os.system('cls')
        print('='*30, f'{"Pedra, Papel e Tesoura":^30}', f'{"by Lucas Lourenco":^30}', '='*30, sep='\n')    

        
    
    def opcoes_escolha() -> dict:
        op = {
            1 : 'Pedra',
            2 : 'Papel',
            3 : 'Tesoura',
            }
        
        return op
          


    def definir_vencedor(a, b):
        t = f'{a} x {b}'
        
        
        if a == 'Pedra':     
            possibilidades = [
                'Pedra x Pedra',
                'Pedra x Papel',
                'Pedra x Tesoura',
                ]
            
            if t == possibilidades[0]:
                return "Empate"
            
            elif t == possibilidades[1]:
                return "Derrota"
            
            elif t == possibilidades[2]:
                return "Vitória"
            
            
            
        elif a == 'Papel':
            possibilidades = [
                'Papel x Pedra',
                'Papel x Papel',
                'Papel x Tesoura',
                ]
            
            if t == possibilidades[0]:
                return "Vitória"
            
            elif t == possibilidades[1]:
                return "Empate"
            
            elif t == possibilidades[2]:
                return "Derrota"
            
        elif a == 'Tesoura':
            possibilidades = [
                'Tesoura x Pedra',
                'Tesoura x Papel',
                'Tesoura x Tesoura',
                ]
            
            if t == possibilidades[0]:
                return "Derrota"
            
            elif t == possibilidades[1]:
                return "Vitória"
            
            elif t == possibilidades[2]:
                return "Empate"
            
                
    
    def lista_numeros():
        lista = [num for num, op in ppd.opcoes_escolha().items()]
        return lista 
    
    
    def bot()-> str:      
        n = random.randint(ppd.lista_numeros()[0], ppd.lista_numeros()[-1])
        escolha = ppd.opcoes_escolha()[n]
        
        return escolha


    def usuario():
        textos = ['Escolha:', '1 | Pedra', '2 | Papel', '3 | Tesoura','\n']
        print('\n'.join(textos))
        
        while True:
            try:
                n = int(input(''))
                if not n in ppd.lista_numeros():
                    print('Escolha somente um dos números apresentados')
                    
                else:
                    escolha = ppd.opcoes_escolha()[n]
                    return escolha
                    
            except Exception as e:
                print('Escreva apenas os números')
            


    def run():
        pontos = [0, 0]
        
        n = 0
        while True:
            n += 1
            
            ppd.titulo()
            
            print(f'Jogador: {pontos[0]}', f'Bot: {pontos[1]}', sep='\n')
            print('\n')

            resultado = ppd.definir_vencedor(ppd.usuario(), ppd.bot())
            print('='*10, f'{resultado}', '='*10, '\n')
            
            if resultado == 'Vitória':
                pontos[0] += 1
                
            elif resultado == 'Derrota':
                pontos[1] += 1
            
            ask = input('Deseja Continuar? (S/N)').title()
            
            if ask == 'S':
                continue
            elif ask == 'N':
                print('Pedra, Papel e Tesoura foi encerrado!','', sep='\n')
                break
            else:
                print('Selecione entre S ou N')        
                
ppd.run()