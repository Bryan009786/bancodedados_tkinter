
import sqlite3
import tkinter as tk
from tkinter import messagebox, Toplevel

# Criar o banco e a tabela
def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Salvar os dados no banco
def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    
    if not nome or not email:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Visualizar os usuários cadastrados
def ver_usuarios():
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("SELECT nome, email FROM usuarios")
    dados = c.fetchall()
    conn.close()

    janela_lista = Toplevel()
    janela_lista.title("Usuários Cadastrados")
    janela_lista.geometry("400x300")

    for i, (nome, email) in enumerate(dados):
        tk.Label(janela_lista, text=f"{i+1}. Nome: {nome} | Email: {email}").pack(anchor="w", padx=10, pady=2)

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("300x200")

tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

tk.Label(janela, text="Email:").pack(pady=5)
entry_email = tk.Entry(janela, width=30)
entry_email.pack()

tk.Button(janela, text="Salvar", command=salvar).pack(pady=5)
tk.Button(janela, text="Ver Usuários", command=ver_usuarios).pack(pady=5)

criar_banco()
janela.mainloop()
