
SEM_CUPOM = "SEM CUPOM"
categoria = ("Eletrônicos", "Vestuário", "Livros")
pedidos = []

def validar_input(input):

    if not input.strip():
        print("ERRO: O input não pode estar vazio.")
        return False


def validar_cupom(cupom):

    if (not cupom.strip() or cupom != None):
        return SEM_CUPOM

    return cupom.strip()

def adicionar_pedido(cupom, cliente, valor, categoria):
    cupom = validar_cupom(cupom)
    if not validar_input(cliente):
        return
    if not validar_input(str(valor)):
        return
    if categoria not in categoria:
        print("ERRO: Categoria inválida.")
        return

    id = str(len(cliente) + len(cupom))

    codigo_rastreio = criar_codigo_rastreio(cliente, categoria, id)

    pedido = (id, codigo_rastreio, cupom, cliente.strip(), valor, categoria)
    pedidos.append(pedido)

    return pedido

def criar_codigo_rastreio(nome, categoria, id):
    nome_curto = nome[:3].upper() if len(nome) >= 3 else nome.upper()

    codigo = nome_curto + categoria + id

    return codigo

def imprimir_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido cadastrado.")
        return

    for i in range(len(pedidos)):
        id, codigo_rastreio, cupom, cliente, valor, categoria = pedidos[i]
        print(f"{i+1}. ID: {id}, Código de Rastreio: {codigo_rastreio}, Cupom: {cupom}, Cliente: {cliente}, Valor: {valor}, Categoria: {categoria}")

def estatistica_pedido(pedidos):

    total_pedidos = len(pedidos)
    total_caixas_grandes = total_pedidos // 3
    total_pedidos_sobraram = total_pedidos % 3

    print("\nRELATÓRIO ESTATÍSTICO:")
    print(f"Total de pedidos: {total_pedidos}")
    print(f"Tipo: {type(total_pedidos).__name__}")
    print(f"Total caixas grandes preenchidas: {total_caixas_grandes}")
    print(f"Total de pedidos que sobraram: {total_pedidos_sobraram}")


def exportar_log_binario():
    conteudo_log = f"LOG EXPORTADO | TOTAL: [{len(pedidos)}] PEDIDOS"
    bytes_log = conteudo_log.encode("utf-8")

    print("\nEXPORTANDO LOG BINÁRIO")
    print(f"Texto original: {conteudo_log}")
    print(f"Em bytes (.encode): {bytes_log}")