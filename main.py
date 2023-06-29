import mysql.connector
from tkinter import Tk, Label, Entry, Button, Listbox

# Função para criar uma nova conexão com o banco de dados
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Altere para o host do seu banco de dados
        user="root",  # Altere para o usuário do seu banco de dados
        password="Password",  # Altere para a senha do seu banco de dados
        database="bd_client"  # Altere para o nome da sua base de dados
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
    query = "SELECT nome, email, telefone FROM registros"
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
    query = "DELETE FROM registros WHERE id = %s"
    cursor.execute(query, (int(record_id),))
    connection.commit()


# Função para criar um novo registro a partir dos dados fornecidos na interface
def create_button_clicked():
    record = (entry_name.get(), entry_email.get(), entry_phone.get())
    create_record(connection, record)
    update_records_listbox()

# Função para atualizar um registro existente selecionado na interface
def update_button_clicked():
    selected_index = records_listbox.curselection()
    if selected_index:
        selected_record = records_listbox.get(selected_index)
        updated_record = (entry_name.get(), entry_email.get(), entry_phone.get())
        record_id = selected_record[0]
        update_record(connection, record_id, updated_record)
        update_records_listbox()

# Função para excluir um registro existente selecionado na interface
def delete_button_clicked():
    selected_index = records_listbox.curselection()
    if selected_index:
        selected_record = records_listbox.get(selected_index)
        record_id = selected_record[0]
        delete_record(connection, record_id)
        update_records_listbox()

# Função para atualizar a lista de registros exibida na interface
def update_records_listbox():
    records = read_records(connection)
    records_listbox.delete(0, "end")
    for record in records:
        records_listbox.insert("end", record)

# Configurações da interface
window = Tk()
window.title("Gerenciador de Registros")
window.geometry("400x300")

label_name = Label(window, text="Nome:")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(window, text="Email:")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone = Label(window, text="Telefone:")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

create_button = Button(window, text="Criar", command=create_button_clicked)
create_button.pack()

update_button = Button(window, text="Atualizar", command=update_button_clicked)
update_button.pack()

delete_button = Button(window, text="Excluir", command=delete_button_clicked)
delete_button.pack()

records_listbox = Listbox(window)
records_listbox.pack()

# Cria uma nova conexão com o banco de dados
connection = create_connection()

# Cria a tabela "registros" no banco de dados, se não existir
create_table(connection)

# Atualiza a lista de registros exibida na interface
update_records_listbox()

window.mainloop()
