# 🎬 Cine-Django

**Proyecto universitario para la materia de Programación Web 2**

Cine-Django es una aplicación web hecha con Django que permite a los usuarios explorar películas y reservar entradas para funciones de cine de manera sencilla y moderna.

---

## 🚀 Funcionalidades Principales

### 👤 Usuarios
- **Registro y autenticación:**  
  Regístrate, inicia y cierra sesión fácilmente.
- **Catálogo de películas:**  
  Explora películas destacadas, busca y consulta información de cada una (portada, sinopsis, tráiler, horarios).
- **Reserva de entradas:**  
  Elige función, selecciona tus asientos y obtén un QR con tu reserva.
- **Historial de reservas:**  
  Consulta tus reservas anteriores y detalles (próximamente).

### 🛠️ Administradores
- **Gestión de películas:**  
  Agrega, edita o elimina títulos, actualiza portadas, géneros, clasificaciones y horarios.
- **Gestión de salas y funciones:**  
  Administra salas, tipos de formato, funciones, precios y disponibilidad de asientos.

---

## 🖥️ Tecnologías Utilizadas

- **Backend:** Python 3.9, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Base de datos:** SQLite (soporta PostgreSQL/MySQL)
- **QR:** Librería QR Code
- **Otros:** Bootstrap (opcional para estilos), Django Auth

---

## ⚡ Instalación Rápida

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/Acedi-a/Cine-Django.git
   cd Cine-Django
   ```

2. **Crea y activa un entorno virtual**
   ```bash
   python -m venv entorno
   # En Linux/Mac
   source entorno/bin/activate
   # En Windows
   entorno\Scripts\activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones y crea superusuario**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Ejecuta el servidor**
   ```bash
   python manage.py runserver
   ```
   Ingresa a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🙌 ¿Cómo usar la app?

1. **Regístrate** o inicia sesión.
2. **Explora** el catálogo de películas.
3. **Selecciona** la función y tus asientos.
4. **Reserva** y recibe tu QR.
5. **(Opcional)** Ingresa como admin para gestionar el catálogo y las funciones.

---

## 💡 Capturas de Pantalla *(agrega las tuyas aquí)*

<!--
![Pantalla de inicio](ruta/a/tu/captura1.png)
![Detalle de película](ruta/a/tu/captura2.png)
-->

---

## 🤝 Contribuciones

¡Las contribuciones y sugerencias son bienvenidas!  
Puedes abrir un **issue** o enviar un **pull request**.

---

## 📄 Licencia

Proyecto educativo, sin licencia específica.

---

> **Desarrollado para la materia de Programación Web 2 — Universidad**
