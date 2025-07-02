# Web Scraper FirstJob

**Web Scraper FirstJob** es una solución completa en Python para extraer ofertas de trabajo desde [FirstJob](https://firstjob.me/ofertas) y consumirlas de tres maneras:

1. **CLI**: Ejecución por consola y generación de un archivo JSON.
2. **GUI de Escritorio**: Interfaz con Tkinter para buscar y mostrar resultados.
3. **Web App**: Interfaz web con Flask, diseño en tonos azul y blanco.

---

## 📌 Casos de Uso

**1. Uso en Línea de Comandos (CLI)**
Ejecuta el scraper directamente en la terminal:

```bash
python scraper.py
```

* El script extrae **10 ofertas** por defecto y las guarda en `Listado_Trabajos.json`.
* Para cambiar el número de vacantes, edita la última sección de `scraper.py`:

  ```python
  if __name__ == '__main__':
      jobs = Firstjob_Scraper(limit=20)  # Ajusta `limit` al número deseado
      save_to_json(jobs)
  ```

![image](https://github.com/user-attachments/assets/a6d8fe38-2fb1-40fb-9b2c-52b87dacd130)



**2. Uso con Interfaz de Escritorio (Tkinter)**
Inicia la aplicación de escritorio con:

```bash
python front.py
```

* Aparecerá una ventana con:

  * Un **Spinbox** para seleccionar cuántas ofertas recuperar.
  * Un botón **Buscar** que lanza el scraping al instante.
  * Un área de texto scrollable donde se muestran las ofertas con **título**, **empresa**, **ubicación** y enlaces clicables.
* Haz clic en cualquier link para abrir la oferta en tu navegador predeterminado.
* Al buscar, también se actualiza `Listado_Trabajos.json` en el directorio.

**3. Uso como Aplicación Web (Flask)**
Levanta el servidor web local con:

```bash
python app.py
```

* Abre tu navegador en `http://localhost:5000`.
* Verás un formulario donde ingresar la cantidad de ofertas a obtener.
* Al enviar, la página recarga mostrando las ofertas en tarjetas con diseño azul-blanco y bordes redondeados.
* Cada tarjeta incluye **Título**, **Empresa**, **Ubicación** y un enlace para ver más detalles en una nueva pestaña.

---

## 📂 Estructura de Archivos

| Archivo                 | Descripción                                                                                                                                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scraper.py`            | Módulo principal. Contiene la función `Firstjob_Scraper(limit)` que realiza el scraping y retorna una lista de diccionarios con **title**, **company**, **location** y **url**. También define `save_to_json()` para guardar los resultados en `Listado_Trabajos.json`. |
| `front.py`              | Cliente de escritorio. Interfaz Tkinter con un **Spinbox** para seleccionar la cantidad de ofertas, un botón **Buscar** y un **ScrolledText** que despliega cada oferta con enlaces clicables. Usa internamente `scraper.py`.                                           |
| `app.py`                | Servidor web con Flask. Página única (`/`) que muestra un formulario numérico y, al enviar, lista las ofertas en un diseño azul/blanco con tarjetas redondeadas. También guarda el JSON generado.                                                                       |
| `requirements.txt`      | Listado de dependencias: `requests`, `beautifulsoup4`, `flask`.                                                                                                                                                                                                         |
| `Listado_Trabajos.json` | Salida generada tras cada ejecución de scraper o Web App; contiene el array de ofertas en formato JSON.                                                                                                                                                                 |

---

## ⚙️ Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/sebastroza1/Web_Scraper_firstJob.git
   cd Web_Scraper_firstJob
   ```

2. **(Opcional) Crea y activa un entorno virtual**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```
