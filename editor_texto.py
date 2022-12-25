#virtualenv env
#.\env\scripts\activate    o deactivate
import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de Texto')
        #configuracion de tamaño minimo en la ventana
        self.rowconfigure(0,minsize=600,weight=1)
        #Configuracion minima de la segunda columna
        self.columnconfigure(1,minsize=600,weight=1)
        #atributo de campo texto
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        #atributo de archivo
        self.archivo=None
        #atributo  para saber si ya se abrio un archivo anteriormente 
        self.archivo_abierto = False
        #creacion de componentes de la aplicacion 
        self._crear_componentes()
        #crear menu
        self._crear_menu()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self,relief=tk.RAISED,bd=2)
        boton_abrir = tk.Button(frame_botones,text='Abrir',command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones,text='Guardar',command=self._guardar)
        boton_guardar_como=tk.Button(frame_botones,text='Guardar como...',command=self._guardar_como)
        #los botones se expanden de manera horizontal (sticky='we')
        boton_abrir.grid(row=0,column=0,sticky='we',padx=5,pady=5)
        boton_guardar.grid(row=1,column=0,sticky='we',padx=5,pady=5)
        boton_guardar_como.grid(row=2,column=0,sticky='we',padx=5,pady=5)
        #se coloca el frame de manera vertical
        frame_botones.grid(row=0,column=0,sticky='ns')
        #agregamos el campoo de texto se expandira el espacio disponible que le reste 
        self.campo_texto.grid(row=0,column=1,sticky='nswe')

    def _crear_menu(self):
        #creamos el menu de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        #agregamos las opciones a nuestro menu 
        #agregamos munu archivo
        menu_archivo=tk.Menu(menu_app,tearoff=False)
        menu_app.add_cascade(label='Archivo',menu=menu_archivo)
        #agregamos las opciones del menu de archivo 
        menu_archivo.add_command(label='Abrir',command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar',command=self._guardar)
        menu_archivo.add_command(label='Guardar como',command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir',command=self.quit)

    def _abrir_archivo(self):
        #se abre el archivo para edicion (lectura y escritura)
        self.archivo_abierto = askopenfile(mode='r+')
        #eliminamos el texto anterior
        self.campo_texto.delete(1.0,tk.END)
        #revisamos si hay un archivo 
        if not self.archivo_abierto:
            return
        #abrimos el archivo en modo archivo lectura escritura

        with open(self.archivo_abierto.name, 'r+') as self.archivo:
            #leemos el contenido del archivo
            texto = self.archivo.read()
            #insertamos todo el contenido del archivo del campo de texto 
            self.campo_texto.insert(1.0, texto)
            #modificamos el titulo de la aplicacion 
            self.title(f'*Editor Texto - {self.archivo.name}')


    def _guardar(self):
        #si ya se abrio previamneteun archivo, lo sobreescribimos
        if self.archivo_abierto:
            #salvamos el archivo (lo abrimos en modo escritura)
            with open(self.archivo_abierto.name,'w') as self.archivo:
                #leemos el contenido de la caje de texto 
                texto = self.campo_texto.get(1.0, tk.END)
                #escribimos el contenido al mismo archivo 
                self.archivo.write(texto)
                #cambiamos el nombre del  titulo de al app
                self.title(f'Editor Texto - {self.archivo.name}')

        else:
            self._guardar_como()



    def _guardar_como(self):
        #Salvamos el archivo actual como un archivo nuevo 
        self.archivo = asksaveasfilename( defaultextension='txt', filetypes=[('Archivo de Texto','*.txt'),('Todos los archivos','*.*')])
        if not self.archivo:
            return
        #Abrimos el archivo en modo escrituta (write)
        with open(self.archivo, 'w') as self.archivo:
            #leemos el contenido de la caja de texto 
            texto = self.campo_texto.get(1.0, tk.END)
            #escribimos el contenido al nuevo archivo 
            self.archivo.write(texto)
            #combinamos el nombredelarchivo 
            self.title(f'editor texto - {self.archivo.name}')
            #indicamos que ya abrimos un archivo 
            self.archivo_abierto = archivo




if __name__ =='__main__':
    editor = Editor()
    editor.mainloop()