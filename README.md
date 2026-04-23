# Automatización de Postulaciones (Mail Merge con Python)

Este proyecto es un script en Python diseñado para automatizar el envío masivo y personalizado de correos electrónicos para postulaciones de trabajo. Permite enviar un mensaje único a diferentes destinatarios (empresas de arquitectura), adaptando el saludo y el nombre de la empresa en el cuerpo del correo, y adjuntando automáticamente documentos en formato PDF.

## 🚀 Características
* **Lectura de datos desde CSV:** Extrae la lista de contactos, correos y saludos desde un archivo `.csv`.
* **Personalización del mensaje:** Adapta el asunto y el cuerpo del correo para cada empresa.
* **Adjuntos automáticos:** Incorpora un Currículum Vitae y un Portafolio en formato PDF a cada correo.
* **Control de envíos:** Incluye un retraso de 5 segundos entre cada envío para evitar bloqueos por SPAM en los servidores de Gmail.
* **Validación de archivos:** Verifica la existencia de los archivos adjuntos antes de iniciar el proceso, evitando fallos a mitad de ejecución.

## 📁 Estructura del Directorio
Para que el script funcione correctamente, todos los archivos deben estar en la misma carpeta:

> /Carpeta_del_Proyecto
> │
> ├── enviar_cv.py
> ├── destinatarios.csv
> ├── CV_Constanza_Espinoza.pdf
> └── Portafolio_Constanza_Espinoza.pdf

### Formato del archivo `destinatarios.csv`
El archivo CSV debe usar codificación UTF-8 y contar con las siguientes columnas exactas en su cabecera:
`nombre_oficina,email,saludo`

**Ejemplo:**
`Iglesis arquitectos,taller@iglesisarquitectos.cl,Estimados miembros de Iglesis arquitectos`
`Correa3,fmo@correa3.com,Estimado Felipe Martínez`

## ⚙️ Configuración y Requisitos

1. **Python:** Debes tener instalado Python en tu sistema. Las librerías utilizadas (`smtplib`, `csv`, `time`, `os`, `email`) vienen integradas por defecto en Python.
2. **Cuenta de Gmail y Seguridad:** * El script utiliza el servidor SMTP de Gmail (`smtp.gmail.com`).
   * Por seguridad, no se utiliza la contraseña habitual del correo. Es obligatorio generar una **"Contraseña de aplicación"** de 16 caracteres desde los ajustes de seguridad de la cuenta de Google (requiere tener activa la Verificación en dos pasos).
3. **Credenciales en el código:** Reemplaza las variables `MI_CORREO` y `MI_CONTRASEÑA` en el archivo `enviar_cv.py` con tu información.

## 💻 Instrucciones de Ejecución

1. Abre una terminal o símbolo del sistema.
2. Navega hasta el directorio donde se encuentran los archivos:
   `cd ruta/a/tu/carpeta`
3. Ejecuta el script:
   `python enviar_cv.py`
4. La consola te mostrará el estado de la conexión y confirmará cada correo enviado exitosamente.

## ⚠️ Advertencias
* **Límites de envío:** Gmail tiene límites de envío diarios. Este script está pensado para lotes de postulación pequeños o medianos.
* **Archivos pesados:** Asegúrate de que tus archivos PDF estén optimizados (idealmente que no superen los 10 MB - 15 MB en total).
* **Prueba previa:** Siempre es recomendable hacer un envío de prueba a tu propio correo electrónico antes de ejecutar la lista definitiva.