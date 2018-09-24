import jogovelha
import sys

erroInicializar = False

jogovelha.inicializar()
jogo = jogovelha.tabuleiro()

if len(jogo) != 3:
	erroInicializar = True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True
		if erroInicializar:
		print('Erro!')
		sys.exit(1)
else:
		sys.exit(0)
    
    import jogovelha
import sys

erro = False
lin = 1
col = 1
jogador = 'X'
jogovelha.inicializar()
jogovelha.jogar(jogador, lin, col)
jogo = jogovelha.tabuleiro()

if len(jogo) != 3:
	erro = True
else:
	for linha in range(0,3):
		if len(jogo[linha]) != 3:
			erro = True
		else:
			for coluna in range(0,3):
				if linha == lin and coluna == col:
					if jogo[linha][coluna] != jogador:
						erro = True
				elif jogo[linha][coluna] != '.':
					erro = True
if erro:
	print('Erro!')
	sys.exit(1)
else:
	sys.exit(0)
