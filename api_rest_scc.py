#SCRIPT PARA LA EJECUCION DE DOCKER CON DOKER - COMPOSE
#SCRIPT PARA BIOMETRICOS CON TECNOLOGIA ZK
# from REQUEST <ATTENDANCE API REST -  POWER BY UTIC-FHCE>

import json
import requests
from zk import ZK, const
from base import scc

#Create API REST - TOMCAT  sistema EGOVF modulo SCC
api_url = 'url'
headers = {"Content-Type": "application/json"}
respuesta = 0

#Create Conection whit the Biometric
conn = None
zk = ZK(scc.IP, port=scc.PORT, timeout=scc.TIMEOUT, password=scc.PASSWORD, force_udp=scc.FORCEUDP, ommit_ping=scc.OMMITPING)

#Bucle para evitar la desconeccion del Contenedor
while True:
    try:
        # Connect to Device
        conn = zk.connect()

        # Capturamos los registros
        for attendance in conn.live_capture():
            if attendance is None:
                print('Esperando Attendance for Biometric')
                pass
            else:
                times = attendance.timestamp
                fecha = times.strftime("%Y-%m-%d")
                hora = times.strftime("%H:%M:%S")
                gestion = times.strftime("%Y")
                mes = times.strftime("%m")
                dia = times.strftime("%d")
                h = times.strftime("%H")
                m = times.strftime("%M")
                marcado = {
                   "_01uid": attendance.uid,
                   "_02user_id": attendance.user_id,
                   "_03fecha": fecha,
                   "_04hora": hora,
                   "_05gestion": gestion,
                   "_06mes": mes,
                   "_07dia": dia,
                   "_08h": h,
                   "_09m": m,
                   "_10punch": attendance.punch,
                   "_11rstatus": attendance.status,
                   "_12lugar": scc.LUGAR
                }
                response = requests.post(api_url, data=json.dumps(marcado), headers=headers)
                respuesta = response.status_code
                print(marcado, respuesta)
    except Exception as e:
       print("Proceso Terminado : {}".format(e))
    finally:
       if conn:
           conn.disconnect()