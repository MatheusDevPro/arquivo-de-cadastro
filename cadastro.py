import tkinter as tk

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    sexo = entry_sexo.get()
    idade = entry_idade.get()
    senha = entry_senha.get()
    confirmesenha = entry_senha.get()
    bairro = entry_bairro.get()
    estado = entry_estado.get()
    pais = entry_pais.get()
    cpf = entry_cpf.get()
    
    # Você pode fazer o que quiser com os dados do cadastro aqui, por exemplo, salvá-los em um banco de dados.
    
    # Limpar os campos após o cadastro
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_sexo.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_bairro.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_pais.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)

# Criar janela principal
root = tk.Tk()
root.title("Cadastro de usuario")

# Labels e campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_sexo = tk.Label(root, text="Sexo:")
label_sexo.pack()
entry_sexo = tk.Entry(root)
entry_sexo.pack()

label_idade = tk.Label(root, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(root, show="*")  # A senha será ocultada com "*"
entry_senha.pack()

label_confirmesenha = tk.Label(root, text="Confirme a Senha:")
label_confirmesenha.pack()
entry_confirmesenha = tk.Entry(root, show="*")  # A senha será ocultada com "*"
entry_confirmesenha.pack()

label_bairro = tk.Label(root, text="Bairro:")
label_bairro.pack()
entry_bairro = tk.Entry(root)
entry_bairro.pack()

label_estado = tk.Label(root, text="Estado:")
label_estado.pack()
entry_estado = tk.Entry(root)
entry_estado.pack()

label_pais = tk.Label(root, text="País:")
label_pais.pack()
entry_pais = tk.Entry(root)
entry_pais.pack()

label_cpf = tk.Label(root, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(root)
entry_cpf.pack()

# Botão de cadastro
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
btn_cadastrar.pack()

root.mainloop()