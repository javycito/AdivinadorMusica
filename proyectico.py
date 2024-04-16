from tkinter import *
from tkinter import messagebox
import sys
import os

# Base de datos de canciones
base_de_datos = [
    {
        "cancion": "Cancioncitas de Amor",
        "artista": "Romeo Santos",
        "letra": ["San valentin se ha convertido en un negocio", "Y el carajito de la flecha me cae mal", "Que el amor no deberia de existir"],
        "genero": "Bachata",
        "tipo_letra": "románticas"
    },
    {
        "cancion": "Sola",
        "artista": "Anuel AA",
        "letra": ["Te vi caminando en lo oscuro sola", "En este juego tú tienes la bola", "Quiero comerte completita sola", "Y sigo recorriendo tu piel"],
        "genero": "Reggaetón",
        "tipo_letra": "románticas"
    },    
    {
        "cancion": "Bzrp Music Sessions, Vol. 52",
        "artista": "Quevedo y Bizarrap",
        "letra": ["Quedate, que la noche sin ti duele", "Nos fuimos en una, empezamos a la una", "Ando rezandole a Dios pa repetirlo otra vez"],
        "genero": "Reggaetón",
        "tipo_letra": "románticas"
    },
]

def buscar_cancion(datos_usuario, artista):
    coincidencias = []
    
    # Buscar coincidencias en la base de datos
    for cancion in base_de_datos:
        coincidencia = True
        
        # Verificar si el usuario proporcionó alguna parte de la letra
        if "letra" in datos_usuario:
            if datos_usuario["letra"] not in cancion["letra"]:
                coincidencia = False
        else:
            print(f"No se encontraron coincidencias, ya que {artista} tiene varias canciones. Sé más específico.")
            return None

        # Verificar si el usuario proporcionó el artista
        if "artista" in datos_usuario:
            if datos_usuario["artista"].lower() != cancion["artista"].lower():
                coincidencia = False
        
        # Verificar si el usuario proporcionó el género
        if "genero" in datos_usuario:
            if "genero" in cancion and datos_usuario["genero"].lower() != cancion["genero"].lower():
                coincidencia = False
        
        # Si hay coincidencia, añadir la canción a la lista de coincidencias
        if coincidencia:
            coincidencias.append(cancion)
    
    return coincidencias

def buscar_cancion_y_mostrar(entrada_letra, entrada_tipo_letra, entrada_artista, entrada_genero, texto_resultados):
    # Obtener los datos de búsqueda de la interfaz gráfica
    letra = entrada_letra.get().strip()
    tipo_letra = entrada_tipo_letra.get().strip()
    artista = entrada_artista.get().strip()
    genero = entrada_genero.get().strip()
    
    # Crear un diccionario con los datos proporcionados por el usuario
    datos_usuario = {}
    if letra:
        datos_usuario["letra"] = letra
    if tipo_letra:
        datos_usuario["tipo_letra"] = tipo_letra
    if artista:
        datos_usuario["artista"] = artista
    if genero:
        datos_usuario["genero"] = genero
    
    # Limpiar el texto en el área de resultados
    texto_resultados.config(state=NORMAL)
    texto_resultados.delete('1.0', END)
    
    # Buscar la canción basada en los datos del usuario
    coincidencias = buscar_cancion(datos_usuario, artista)
    
    # Mostrar los resultados
    if coincidencias:
        for cancion in coincidencias:
            texto_resultados.config(state=NORMAL)  # Habilitar la edición del texto
            texto_resultados.tag_configure("bold", font=('Microsoft YaHei UI Light', 15, 'bold'))  # Configurar un estilo de fuente
            texto_resultados.insert(END, f"La canción de la que hablas probablemente sea '{cancion['cancion']}' de {cancion['artista']}. Esta canción pertenece al género de {cancion['genero']}.\n", "bold")  # Insertar el texto con el estilo de fuente aplicado
            texto_resultados.config(state=DISABLED)  # Deshabilitar la edición del texto
    else:
        texto_resultados.config(state=NORMAL)  # Habilitar la edición del texto
        texto_resultados.insert(END, "Lo siento, no se encontraron coincidencias para los datos proporcionados. Inténtalo más tarde.\n")  # Insertar el texto
        texto_resultados.config(state=DISABLED)  # Deshabilitar la edición del texto

    
    texto_resultados.config(state=DISABLED)

def iniciar(root, user, code):
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("BRUJO MUSICAL")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        screen.iconbitmap("applem.ico") 
        
        # Cargar la imagen y ajustar su tamaño
        img = PhotoImage(file='guitarritas.png')
        Label(screen, image=img).place(x=0,y=0)

        # Interfaz de búsqueda de canciones
        etiqueta_letra = Label(screen, text="¿Te sabes alguna parte de la letra?", fg='#6B0000', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        etiqueta_letra.grid(row=0, column=0, sticky=W)
        entrada_letra = Entry(screen, bd=5)
        entrada_letra.grid(row=0, column=1)

        etiqueta_tipo_letra = Label(screen, text="¿Qué tipo de letra tiene la canción?", fg='#6B0000', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        etiqueta_tipo_letra.grid(row=1, column=0, sticky=W)
        entrada_tipo_letra = Entry(screen, bd=5)
        entrada_tipo_letra.grid(row=1, column=1)

        etiqueta_artista = Label(screen, text="¿Sabes qué artista la canta?", fg='#6B0000', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        etiqueta_artista.grid(row=2, column=0, sticky=W)
        entrada_artista = Entry(screen, bd=5)
        entrada_artista.grid(row=2, column=1)

        etiqueta_genero = Label(screen, text="¿Cuál género crees que es la canción?", fg='#6B0000', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        etiqueta_genero.grid(row=3, column=0, sticky=W)
        entrada_genero = Entry(screen, bd=5)
        entrada_genero.grid(row=3, column=1)

        boton_buscar = Button(screen, text="Buscar", command=lambda: buscar_cancion_y_mostrar(entrada_letra, entrada_tipo_letra, entrada_artista, entrada_genero, texto_resultados), fg='#6B0000', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        boton_buscar.grid(row=4, columnspan=2)

        texto_resultados = Text(screen, width=50, height=10, wrap=WORD)
        texto_resultados.grid(row=5, columnspan=2)
        texto_resultados.config(state=DISABLED)

        screen.mainloop()
    
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Malísimo", "Ta to' mal, pana")

    elif username != "admin":
        messagebox.showerror("Hay bobo", "Ese no e' su usuario, por si acaso")

    elif password != "1234":
        messagebox.showerror("¿Se te olvidó la contraseña?", "No e' esa, pariguayo")

#PARA OBTENER RUTA DE RECURSOS

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

def create_login_screen():
    root = Tk()
    root.title('BRUJO MUSICAL')
    root.geometry("925x500+300+200")
    root.config(bg="#fff")
    root.resizable(False, False)

    # Cargar la imagen y ajustar su tamaño
    img = PhotoImage(file='guitarritas.png')
    Label(root, image=img).place(x=0,y=0)

    frame = Frame(root,width=350,height=350,bg="white") 
    frame.place(x=300,y=70)

    heading=Label(frame,text='Inicia sesión', fg='#6B0000', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=80,y=5)
 
 #Separador, esto es el usuario
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Usuario')


    user = Entry(frame,width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30,y=80)
    user.insert(0, 'Usuario')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2, bg='black').place(x=25,y=107)

 #Separador, esto es la contraseña

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Contraseña')

    code = Entry(frame,width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=30,y=150)
    code.insert(0, 'Contraseña')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2, bg='black').place(x=25,y=177)

    Button(frame,width=39,pady=7,text='Inicia sesión', bg='#6B0000', fg='white', border=0, command=lambda: iniciar(root, user, code)).place(x=35,y=204)
    label=Label(frame,text="¿Eres nuevo por aquí?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=53,y=270)

    sing_up = Button(frame,width=12,text='Crea una cuenta',border=0, bg='white', cursor='hand2', fg='#6B0000')
    sing_up.place(x=185,y=270)

    root.mainloop()

create_login_screen()