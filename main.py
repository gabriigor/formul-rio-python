import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

#BANCO
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="registro"
)
cursor = db.cursor()
# CRIAR BANCO
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    idade INT,
    curso VARCHAR(255),
    endereco VARCHAR(255),
    telefone VARCHAR(15),
    email VARCHAR(255),
    nome_responsavel VARCHAR(255),
    telefone_responsavel VARCHAR(15)
)
""")

db.commit()

# JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Sistema de Registro")
janela.geometry("700x600")
janela.configure(bg="#F0F0F0")

def registrar_aluno():
    nome = entrada_nome_aluno.get()
    idade = int(entrada_idade_aluno.get())
    curso = entrada_curso_aluno.get()
    endereco = entrada_endereco_aluno.get()
    telefone = entrada_telefone_aluno.get()
    email = entrada_email_aluno.get()
    nome_responsavel = entrada_nome_responsavel.get()
    telefone_responsavel = entrada_telefone_responsavel.get()

    sql = """
    INSERT INTO alunos (nome, idade, curso, endereco, telefone, email, nome_responsavel, telefone_responsavel)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome, idade, curso, endereco, telefone, email, nome_responsavel, telefone_responsavel)
    cursor.execute(sql, valores)
    db.commit()


    limpar_campos()
    messagebox.showinfo("Sucesso", "Aluno registrado com sucesso!")

def limpar_campos():
    entrada_nome_aluno.delete(0, tk.END)
    entrada_idade_aluno.delete(0, tk.END)
    entrada_curso_aluno.delete(0, tk.END)
    entrada_endereco_aluno.delete(0, tk.END)
    entrada_telefone_aluno.delete(0, tk.END)
    entrada_email_aluno.delete(0, tk.END)
    entrada_nome_responsavel.delete(0, tk.END)
    entrada_telefone_responsavel.delete(0, tk.END)

# Estilo para os frames
s = ttk.Style()
s.configure('TFrame', background='#F0F0F0')

# ABAS
abas = ttk.Notebook(janela)
abas.pack(fill='both', expand=True)

# Aba de Registro de Aluno
#tem que criar mais 2 abas
aba_aluno = ttk.Frame(abas)
abas.add(aba_aluno, text='Registro de Aluno')

# Cabeçalho - linha preta
cabecalho = tk.Label(aba_aluno, text="Cadastro de Alunos", font=("Tenorite", 20), fg="white", bg="black")
cabecalho.grid(row=0, column=0, columnspan=50, padx=240, pady=40, sticky="w")

# Formulário
label_explicativo = tk.Label(aba_aluno, text="Preencha o formulário", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_explicativo.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

label_nome_aluno = tk.Label(aba_aluno, text="Nome:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_nome_aluno.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entrada_nome_aluno = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_nome_aluno.grid(row=2, column=1, padx=10, pady=5)

label_idade_aluno = tk.Label(aba_aluno, text="Idade:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_idade_aluno.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entrada_idade_aluno = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_idade_aluno.grid(row=3, column=1, padx=10, pady=5)

label_curso_aluno = tk.Label(aba_aluno, text="Curso:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_curso_aluno.grid(row=4, column=0, padx=10, pady=5, sticky="w")

entrada_curso_aluno = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_curso_aluno.grid(row=4, column=1, padx=10, pady=5)

label_endereco_aluno = tk.Label(aba_aluno, text="Endereço:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_endereco_aluno.grid(row=5, column=0, padx=10, pady=5, sticky="w")

entrada_endereco_aluno = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_endereco_aluno.grid(row=5, column=1, padx=10, pady=5)

label_telefone_aluno = tk.Label(aba_aluno, text="Telefone:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_telefone_aluno.grid(row=6, column=0, padx=10, pady=5, sticky="w")

entrada_telefone_aluno = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_telefone_aluno.grid(row=6, column=1, padx=10, pady=5)

label_email_aluno = tk.Label(aba_aluno, text="Email:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_email_aluno.grid(row=7, column=0, padx=10, pady=5, sticky="w")

entrada_email_aluno = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_email_aluno.grid(row=7, column=1, padx=10, pady=5)

label_nome_responsavel = tk.Label(aba_aluno, text="Nome do Responsável:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_nome_responsavel.grid(row=8, column=0, padx=10, pady=5, sticky="w")

entrada_nome_responsavel = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_nome_responsavel.grid(row=8, column=1, padx=10, pady=5)

label_telefone_responsavel = tk.Label(aba_aluno, text="Telefone do Responsável:", font=("Arial", 12), fg="black", bg="#F0F0F0")
label_telefone_responsavel.grid(row=9, column=0, padx=10, pady=5, sticky="w")

entrada_telefone_responsavel = tk.Entry(aba_aluno, font=("Arial", 12))
entrada_telefone_responsavel.grid(row=9, column=1, padx=10, pady=5)

botao_enviar = tk.Button(aba_aluno, text="Enviar", command=registrar_aluno, font=("Arial", 12), fg="black")
botao_enviar.grid(row=10, column=0, columnspan=2, pady=10)

janela.mainloop()
