import tkinter as tk
from tkinter import messagebox
import sys

# Função para criar a matriz de células
def create_grid(grid_frame, rows, cols, start_x, start_y, end_x, end_y):
    """ Cria uma grade de células no frame especificado. """
    for widget in grid_frame.winfo_children():
        widget.destroy()  # Limpa o grid atual

    # Determina a largura e altura das células
    cell_width = (end_x - start_x - 20) / cols  # Subtrai 20 para o espaçamento
    cell_height = (end_y - start_y - 20) / rows  # Subtrai 20 para o espaçamento

    for row in range(rows):
        for col in range(cols):
            cell = tk.Entry(grid_frame, width=10)  # Usando Entry para permitir edição
            cell.place(x=start_x + col * cell_width, y=start_y + row * cell_height, width=cell_width, height=cell_height)

def update_grid(grid_frame, rows, cols, start_x, start_y, end_x, end_y):
    create_grid(grid_frame, rows, cols, start_x, start_y, end_x, end_y)

def draw_grid_lines(canvas, width, height):
    """ Desenha linhas a cada 5% da largura e altura do canvas. """
    for i in range(0, int(width), int(width * 0.05)):  # Linhas verticais
        canvas.create_line(i, 0, i, height, fill='lightgray', dash=(2, 2))
    for i in range(0, int(height), int(height * 0.05)):  # Linhas horizontais
        canvas.create_line(0, i, width, i, fill='lightgray', dash=(2, 2))

def main_screen(master):
    master.title("Tela Principal")

    # Definindo a largura e altura da janela para ocupar toda a tela, exceto a barra de tarefas
    total_width = master.winfo_screenwidth()  # Largura da tela
    total_height = master.winfo_screenheight()  # Altura da tela
    master.geometry(f"{total_width}x{total_height}")  # Ajusta a janela para ocupar toda a tela

    master.configure(bg='#061208')

    # Define o comportamento ao tentar fechar a janela
    master.protocol("WM_DELETE_WINDOW", lambda: on_closing(master))

    # Criar um canvas para desenhar a grade de fundo
    canvas = tk.Canvas(master, bg='white', width=total_width, height=total_height)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Desenha as listras a cada 5%
    draw_grid_lines(canvas, total_width, total_height)

    # Criar a barra lateral à esquerda
    sidebar_width = int(total_width * 0.15)  # Largura da barra lateral (15% da largura da tela)
    sidebar_frame = tk.Frame(master, bg='#2c3e50', width=sidebar_width)  
    sidebar_frame.place(x=0, y=0, height=total_height)  # Usar place para posicionar a barra lateral

    # Adicionar alguns itens na barra lateral, empilhados verticalmente
    for i in range(5):
        btn = tk.Button(sidebar_frame, text=f"Item {i+1}", bg='#34495e', fg='white', font=("Helvetica", 12), relief=tk.FLAT, width=20)  # Aumentando a largura
        btn.pack(fill=tk.X, pady=5)

    # Criar a área de "matriz/planilha" no canto superior esquerdo (fora da barra)
    grid_frame = tk.Frame(master, bg='white')
    grid_frame.place(x=int(total_width * 0.17), y=int(total_height * 0.05), width=int(total_width * 0.63), height=int(total_height * 0.6))  # Espaço fixo para as células

    # Definindo os pontos de início e fim para as células
    start_x = int(total_width * 0.17)  # 17% da largura total da tela do usuário
    start_y = int(total_height * 0.05)  # 5% da altura total da tela do usuário
    end_x = int(total_width * 0.5)  # 63% da largura total da tela do usuário (ajustado para 80% da largura)
    end_y = int(total_height * 0.65)  # 65% da altura total da tela do usuário

    # Criar a coluna de informações no lado direito da área da matriz
    info_frame = tk.Frame(master, bg='#061208')
    info_frame.place(x=int(total_width * 0.65), y=10, relwidth=0.3, height=580)  # Ajusta a posição e largura da coluna de informações

    # Labels e entradas para inserir o número de linhas e colunas
    tk.Label(info_frame, text="Número de Linhas (máx. 25):", bg='#061208', fg='white').pack(anchor='e', pady=(10, 0))
    entry_rows = tk.Entry(info_frame, width=5)
    entry_rows.pack(anchor='e', padx=5)

    tk.Label(info_frame, text="Número de Colunas (máx. 11):", bg='#061208', fg='white').pack(anchor='e', pady=(10, 0))
    entry_cols = tk.Entry(info_frame, width=5)
    entry_cols.pack(anchor='e', padx=5)

    # Botão para atualizar a grade com as entradas
    update_button = tk.Button(info_frame, text="Atualizar Grade", bg='#2980b9', fg='white', font=("Helvetica", 12),
                               command=lambda: update_grid_from_entries(grid_frame, entry_rows, entry_cols, start_x, start_y, end_x, end_y))
    update_button.pack(pady=10)

    # Adicionando espaçamento inferior ao botão para centralizar o conteúdo na coluna
    info_frame.pack_propagate(False)  # Impede que o frame redimensione automaticamente
    info_frame.update_idletasks()  # Atualiza o frame para calcular o tamanho
    info_frame_height = info_frame.winfo_height()
    update_button.place(relx=0.5, rely=0.1, anchor='n')  # Centraliza o botão na parte superior

def update_grid_from_entries(grid_frame, entry_rows, entry_cols, start_x, start_y, end_x, end_y):
    """ Atualiza a grade com base nas entradas do usuário. """
    try:
        rows = min(int(entry_rows.get()), 25)  # Limitar o máximo de linhas a 25
        cols = min(int(entry_cols.get()), 11)  # Limitar o máximo de colunas a 11
        update_grid(grid_frame, rows, cols, start_x, start_y, end_x, end_y)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos para linhas e colunas.")

def on_closing(master):
    """ Função chamada quando o usuário clica no 'X' para fechar a janela. """
    if messagebox.askokcancel("Fechar", "Tem certeza que deseja fechar o programa?"):
        master.destroy()  # Fecha a janela principal
        sys.exit()  # Encerra o processo completamente

# Código para executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    main_screen(root)
    root.mainloop()
