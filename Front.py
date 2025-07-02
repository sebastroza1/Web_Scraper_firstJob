import tkinter as tk
from tkinter import ttk, scrolledtext
import webbrowser
import json
from scraper import Firstjob_Scraper, save_to_json  # Assuming scraper.py is in the same folder

class JobScraperApp:
    def __init__(self, root):
        
###################################[Estructura de la interfaz]################################################

        self.root = root
        root.title("FirstJob Scraper GUI")        
        # Frame principal
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # Selector de cantidad
        ttk.Label(frame, text="Cantidad de ofertas:").grid(row=0, column=0, sticky=tk.W)
        self.spin = ttk.Spinbox(frame, from_=1, to=100, width=5)
        self.spin.set(10)
        self.spin.grid(row=0, column=1, sticky=tk.W, padx=(5, 0))

        # Botón de búsqueda
        self.btn_search = ttk.Button(frame, text="Buscar", command=self.buscar)
        self.btn_search.grid(row=0, column=2, padx=(10, 0))

        # Área de texto con scroll
        self.text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        self.text_area.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        self.text_area.config(state=tk.DISABLED)

        # Contador para tags de enlaces
        self.link_count = 0

###################################[Funcionalidades de la interfaz]################################################
    
    def buscar(self):
        # Limpia área de texto
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)

        # Obtiene la cantidad de ofertas
        try:
            limit = int(self.spin.get())
        except ValueError:
            limit = 10

#################################[Scraper]############################################################################
        
        # Scrapea
        jobs = Firstjob_Scraper(limit=limit)
        # Opcional: guarda también en JSON
        save_to_json(jobs)

        # Muestra cada oferta
        for job in jobs:
            title    = job['title']
            company  = job['company']
            location = job['location']
            url       = job['url']

            # Inserta texto descriptivo
            self.text_area.insert(tk.END, f"Título: {title}\nEmpresa: {company}\nUbicación: {location}\n")

            # Marca inicio del enlace
            start_index = self.text_area.index(tk.INSERT)
            # Inserta la URL
            self.text_area.insert(tk.END, url + "\n\n")
            # Calcula fin del enlace (solo texto URL)
            end_index = self.text_area.index(f"{start_index} + {len(url)}c")

            # Crea y configura un tag para el enlace
            tag_name = f"link{self.link_count}"
            self.link_count += 1
            self.text_area.tag_add(tag_name, start_index, end_index)
            self.text_area.tag_config(tag_name, foreground="blue", underline=True)
            self.text_area.tag_bind(tag_name, "<Button-1>", lambda e, link=url: webbrowser.open(link))

        self.text_area.config(state=tk.DISABLED)

################################################[Main]##########################################################################
if __name__ == '__main__':
    root = tk.Tk()
    app = JobScraperApp(root)
    root.mainloop()
