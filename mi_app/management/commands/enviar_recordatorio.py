import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from mi_app.models import Cita # Asegúrate de importar tu modelo correctamente

class Command(BaseCommand):
    help = 'Busca citas programadas para dentro de 3 días y envía recordatorios por email.'

    def handle(self, *args, **options):
        # 1. Definir el rango de tiempo
        
        # Obtener la fecha y hora de hoy
        hoy = timezone.now().date()
        
        # Calcular la fecha que es exactamente 3 días a partir de ahora (en formato de fecha)
        fecha_recordatorio = hoy + datetime.timedelta(days=3)
        
        # 2. Filtrar las citas
        # Buscamos citas cuya fecha_cita coincida con la fecha_recordatorio
        # Usamos __date para comparar solo la fecha, ignorando la hora
        citas_pendientes = Cita.objects.filter(
            fecha_cita__date=fecha_recordatorio
        ).select_related('cliente') # Optimizamos la consulta para obtener el cliente de una vez

        if not citas_pendientes:
            self.stdout.write(self.style.SUCCESS('No se encontraron citas para enviar recordatorios.'))
            return

        # 3. Procesar y enviar emails
        emails_enviados_count = 0
        
        for cita in citas_pendientes:
            
            # Formatear la fecha y hora para el correo
            fecha_formato = cita.fecha_cita.strftime("%d/%m/%Y a las %H:%M")
            
            # Datos del cliente
            nombre_cliente = cita.cliente.nombre
            email_cliente = cita.cliente.email

            asunto = f"¡Recordatorio de Cita! Tienes una cita pendiente."
            mensaje = (
                f"Hola, {nombre_cliente}.\n\n"
                f"Te recordamos que tienes una cita programada para el día {fecha_formato} "
                f"por el motivo: {cita.motivo}.\n\n"
                f"Por favor, si necesitas cancelar o reprogramar, contáctanos.\n\n"
                f"Gracias."
            )

            try:
                send_mail(
                    asunto,
                    mensaje,
                    None, # Usa DEFAULT_FROM_EMAIL o tu EMAIL_HOST_USER de settings.py
                    [email_cliente],
                    #fail_silently=False,
                    fail_silently=True,
                )
                emails_enviados_count += 1
                self.stdout.write(self.style.SUCCESS(f'Email enviado a {email_cliente}'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error al enviar email a {email_cliente}: {e}'))

        self.stdout.write(self.style.SUCCESS(f'\nProceso finalizado. Total de recordatorios enviados: {emails_enviados_count}'))