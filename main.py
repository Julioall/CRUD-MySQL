import mysql.connector
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar, Listbox, SINGLE
from tkinter import ttk
from tkinter.font import Font

# Função para criar uma nova conexão com o banco de dados


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Altere para o host do seu banco de dados
        user="root",  # Altere para o usuário do seu banco de dados
        password="Password",  # Altere para a senha do seu banco de dados
        database="db_client"  # Altere para o nome da sua base de dados
    )
    return connection

# Função para criar a tabela "registros" no banco de dados, se não existir


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            email VARCHAR(255),
            telefone VARCHAR(20)
        )
    """)
    connection.commit()

# Função para inserir um novo registro no banco de dados


def create_record(connection, record):
    cursor = connection.cursor()
    query = "INSERT INTO registros (nome, email, telefone) VALUES (%s, %s, %s)"
    cursor.execute(query, record)
    connection.commit()

# Função para ler todos os registros do banco de dados


def read_records(connection):
    cursor = connection.cursor()
    query = "SELECT id, nome, email, telefone FROM registros"
    cursor.execute(query)
    records = cursor.fetchall()
    return records

# Função para atualizar um registro existente no banco de dados


def update_record(connection, record_id, updated_record):
    cursor = connection.cursor()
    query = "UPDATE registros SET nome = %s, email = %s, telefone = %s WHERE id = %s"
    cursor.execute(query, (*updated_record, record_id))
    connection.commit()

# Função para excluir um registro existente do banco de dados


def delete_record(connection, record_id):
    cursor = connection.cursor()
    records = read_records(connection)
    query = "DELETE FROM registros WHERE id = %s"
    cursor.execute(query, (int(record_id),))
    connection.commit()


# Função para criar um novo registro a partir dos dados fornecidos na interface
def create_button_clicked():
    record = (entry_name.get(), entry_email.get(), entry_phone.get())
    create_record(connection, record)
    update_records_table()  # Atualiza a tabela, não a lista

# Função para atualizar um registro existente selecionado na interface


def update_button_clicked():
    selected_item = records_tree.selection()
    if selected_item:
        selected_record = records_tree.item(selected_item)["values"]
        updated_record = (entry_name.get(),
                          entry_email.get(), entry_phone.get())
        record_id = selected_record[0]
        update_record(connection, record_id, updated_record)
        update_records_table()  # Atualiza a tabela, não a lista

# Função para excluir um registro existente selecionado na interface


def delete_button_clicked():
    selected_item = records_tree.selection()
    if selected_item:
        selected_record = records_tree.item(selected_item)["values"]
        record_id = selected_record[0]
        delete_record(connection, record_id)
        update_records_table()  # Atualiza a tabela, não a lista

# Função para atualizar a tabela de registros exibida na interface


def update_records_table():
    records = read_records(connection)
    # Limpa a tabela antes de atualizar
    records_tree.delete(*records_tree.get_children())
    for record in records:
        records_tree.insert("", "end", values=record)


# Configurações da interface
window = Tk()
window.title("Gerenciador de Registros")
window.geometry("600x400")
custom_font = Font(family="Helvetica", size=12, weight="bold", )
window.configure(bg="#B6FFFE")
# Obtendo a cor de fundo da janela
cor_fundo_janela = window.cget("bg")

# Labels
label_name = Label(window, text="Nome:", font=custom_font, bg=cor_fundo_janela)
label_name.pack(pady=5)
entry_name = Entry(window)
entry_name.pack(pady=5)

label_email = Label(window, text="Email:", font=custom_font, bg=cor_fundo_janela)
label_email.pack(pady=5)
entry_email = Entry(window)
entry_email.pack(pady=5)

label_phone = Label(window, text="Telefone:", font=custom_font, bg=cor_fundo_janela)
label_phone.pack(pady=5)
entry_phone = Entry(window)
entry_phone.pack(pady=5)

# Botões
button_frame = Frame(window)
button_frame.pack(pady=10)

create_button = Button(button_frame, text="Criar", bg="#2196F3", fg="black", 
                       width=10, command=create_button_clicked)
create_button.pack(side="left", padx=5)

update_button = Button(button_frame, text="Atualizar", bg="#2196F3", fg="black",
                       width=10, command=update_button_clicked)
update_button.pack(side="left", padx=5)

delete_button = Button(button_frame, text="Excluir", bg="#2196F3", fg="black",
                       width=10, command=delete_button_clicked)
delete_button.pack(side="left", padx=5)

# Tabela de Registros
columns = ("ID", "Nome", "Email", "Telefone")
records_tree = ttk.Treeview(window, columns=columns, show="headings")

# Definindo os cabeçalhos das colunas
for col in columns:
    records_tree.heading(col, text=col)

records_tree.pack(pady=10)

# Barra de Rolagem
scrollbar = Scrollbar(window, orient="vertical", command=records_tree.yview)
scrollbar.pack(side="right", fill="y")

# Ligando a Treeview com a barra de rolagem
records_tree.config(yscrollcommand=scrollbar.set)

# Cria uma nova conexão com o banco de dados
connection = create_connection()

# Cria a tabela "registros" no banco de dados, se não existir
create_table(connection)

# Atualiza a tabela de registros exibida na interface
update_records_table()

window.mainloop()
