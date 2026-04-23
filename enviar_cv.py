import smtplib
import csv
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- CONFIGURACIÓN DE TU CUENTA ---
MI_CORREO = "constanzabelenespinoza.v@gmail.com"
MI_CONTRASEÑA = "umtoebkdrweqmklf" 

# --- CONFIGURACIÓN DE LOS ARCHIVOS ADJUNTOS ---
ARCHIVO_CV = "CV_Constanza_Espinoza.pdf"
ARCHIVO_PORTAFOLIO = "Portafolio_Constanza_Espinoza.pdf"

def adjuntar_archivo(mensaje, nombre_archivo):
    """Función auxiliar para adjuntar archivos al correo"""
    try:
        with open(nombre_archivo, "rb") as adjunto:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(adjunto.read())
            encoders.encode_base64(parte)
            parte.add_header(
                'Content-Disposition', 
                f"attachment; filename= {nombre_archivo}"
            )
            mensaje.attach(parte)
            return True
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'")
        return False

def enviar_postulaciones():
    # Verificación inicial de archivos
    if not os.path.exists(ARCHIVO_CV) or not os.path.exists(ARCHIVO_PORTAFOLIO):
        print("❌ ERROR CRÍTICO: No se encuentran los PDFs en la carpeta.")
        print("Asegúrate de que 'CV_Constanza_Espinoza.pdf' y 'Portafolio_Constanza_Espinoza.pdf' estén aquí.")
        return

    try:
        print("Iniciando conexión con Gmail...")
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(MI_CORREO, MI_CONTRASEÑA)
        print("¡Conexión exitosa!")
        
        with open("destinatarios.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                nombre_oficina = fila['nombre_oficina']
                correo_destino = fila['email']
                saludo = fila['saludo']
                
                mensaje = MIMEMultipart()
                mensaje['From'] = MI_CORREO
                mensaje['To'] = correo_destino
                mensaje['Subject'] = f"Postulación Dibujante Modelador - Constanza Espinoza - {nombre_oficina}"
                
                # CUERPO DEL CORREO ACTUALIZADO
                cuerpo = f"""{saludo}:

Les escribo con gran entusiasmo para presentar mi candidatura al puesto de Dibujante Modelador. Como profesional titulada en Dibujo y modelamiento arquitectónico y estructural del Instituto Duoc UC Sede Alameda, me motiva enormemente la posibilidad de integrarme a una empresa referente en proyectos de arquitectura como lo es {nombre_oficina}.

En mi experiencia laboral reciente, me he enfocado en el desarrollo detallado de planos de torres de telecomunicaciones, incluyendo informes de corrosión. He tenido la oportunidad de colaborar en proyectos de gran demanda de habilidades técnicas, lo que me ha permitido comprender la precisión técnica, los plazos y los altos estándares que exigen este tipo de obras.

Comprendo que el dominio del software es fundamental para este rol. Por ello, destaco que poseo un nivel intermedio-avanzado tanto en AutoCAD como en Revit y Twinmotion, incluyendo un nivel de dominio básico en Navisworks Manage, cumpliendo a cabalidad con el requisito de la mayoría de las oficinas. Utilizo estas herramientas con agilidad para la modelación precisa y la generación eficiente de planimetría, asegurando que cada detalle estructural o arquitectónico esté correctamente representado para su ejecución.

Me entusiasma mucho la oportunidad de aportar mi proactividad y habilidades técnicas a su equipo de profesionales. Busco un lugar con un grato ambiente de trabajo donde se dé oportunidad a dibujantes/modeladores juniors y que pueda seguir desarrollándome profesionalmente, y estoy convencida de que {nombre_oficina} es el lugar ideal para ello.

Adjunto mi currículum vitae y un portafolio con una selección de mis trabajos destacados para que puedan revisar en detalle mi formación y proyectos anteriores. Quedo a su entera disposición para concertar una entrevista y conversar sobre cómo mi perfil puede sumar valor a sus próximos proyectos arquitectónicos.

Agradezco de antemano su tiempo y consideración.

Atentamente,
Constanza Espinoza.
LinkedIn: https://www.linkedin.com/in/constanza-espinoza-vargas-02b489251/"""

                mensaje.attach(MIMEText(cuerpo, 'plain'))
                
                # Adjuntar ambos archivos
                adjuntar_archivo(mensaje, ARCHIVO_CV)
                adjuntar_archivo(mensaje, ARCHIVO_PORTAFOLIO)
                
                # Enviar
                servidor.send_message(mensaje)
                print(f"✅ Enviado con CV y Portafolio a: {nombre_oficina}")
                
                # Pausa de seguridad
                time.sleep(5) 
                
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
        
    finally:
        try:
            servidor.quit()
        except:
            pass
        print("\n--- Proceso finalizado ---")

if __name__ == "__main__":
    enviar_postulaciones()