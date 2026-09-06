TOKEN_HEADER = b"Authorization"
token_texto = TOKEN_HEADER.decode("utf-8")

print(f"SISTEMA INICIADO | TOKEN [{token_texto}]")

CATEGORIAS = ("Estudo", "Trabalho", "Pessoal")

tarefas = []

def adicionar_tarefa(descricao, prioridade=None):

    if not descricao.strip():
        print("ERRO: A descrição da tarefa não pode estar vazia.")
        return

    prioridade_final = prioridade or "Média"

    nova_tarefa = (descricao.strip(), prioridade_final)

    tarefas.append(nova_tarefa)
    print(f'Tarefa adicionada com sucesso com prioridade [{prioridade_final}].')


def exibir_tarefas():
    print("\n LISTA TAREFAS: ")

    if not tarefas: 
        print("Nenhuma tarefa cadastrada.")
        return

    for i in range(len(tarefas)):
        nome, prio = tarefas[i]

        nome_curto = nome[:15] + "..." if len(nome) > 15 else nome
        print(f"{i+1}. [{prio}] {nome_curto}")


def gerar_relatorio_estatistico():
    total_tarefas = len(tarefas)

    blocos_completos = total_tarefas // 2

    sobra = total_tarefas % 2

    print("\nRELATÓRIO ESTATÍSTICO:")
    print(f"Total de tarefas: {total_tarefas} (Tipo: {type(total_tarefas).__name__})")
    print(f"Pares completos de tarefas: {blocos_completos}")
    print(f"Tarefas pendentes fora de pars: {sobra}")


def exportar_log_binario():
    conteudo_log = f"LOG_EXPORTADO | Total: {len(tarefas)} tarefas"
    bytes_log = conteudo_log.encode("utf-8")

    print("\nEXPORTANDO LOG BINÁRIO")
    print(f"Texto original: {conteudo_log}")
    print(f"Em bytes (.encode): {bytes_log}")


adicionar_tarefa("   ")

adicionar_tarefa("Estudar Tipos Embutidos em Python", prioridade="Alta")
adicionar_tarefa("Comprar café para o código", prioridade="")
adicionar_tarefa("Revisar código do projeto de automação")

exibir_tarefas()

gerar_relatorio_estatistico()
exportar_log_binario()