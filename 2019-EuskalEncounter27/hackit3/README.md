# HACK IT 3: 

_Antes de nada aclarar que este (y todos los posteriores hackits) fueron resueltos **fuera** de la Euskal tras haber asistido a la reunión post-hackit y escuchar la solución del mismo._
_Pese a todo, se ha querido tratar de resolver por completo la prueba, explicando aquí los pasos a seguir._

El primer paso es averiguar con que clase de fichero estamos trabajando. En este caso, se puede tratar de abrirlo con los típicos programas de los hackits (Wireshark, Audacity, Hex Workshop...) como hicimos nosotros; o, si eres inteligente usas el comando `file` y ves si es algún fichero útil y reconocido:

```
➜ file dump
dump: tcpdump capture file (little-endian) - version 2.4 (Linux "cooked", capture length 262144)
```

Ahora que sabemos que se trata de un fichero de Wireshark, lo abrimos, y dentro observamos una conversación entre el equipo `10.11.12.52:49754` y el equipo `51.15.21.7:25565`.

A primera vista ninguno de estos puertos nos recuerda a nada, mientras que a las IPs, nos encontramos con una privada y una pública, por lo que puede que la pública se trate de algún servidor al que conectarse.

Tras una búsqueda rápida en Google, nos encontramos con que efectivamente, el **puerto `25565` es usado por servidores de Minecraft**, y como tenemos el tráfico de paquetes intercambiado entre el cliente y el servidor, toca ponerse a investigar el funcionamiento del protocolo de Minecraft.

Como va a haber que operar el paquete con sus mas de 9000 paquetes TCP, es conveniente exportar las cárgas de datos que transportan los mismos a un fichero de datos para su manipulación. Para ello podemos hacerlo en Wireshark mediante la opción `Follow TCP Stream`, y exportando los datos en formato Raw, o bien mediante Python con la ayuda del paquete Scapy:

```python
from scapy.all import rdpcap

# archivo pcap original con las tramas
dump = rdpcap('dump')

# archivo al que se exportarán los datos
f = open('load.txt', 'w')

for i in range(len(dump)):
    try:
        f.write(dump[i].load.hex() + '\n')
    except:
        pass
    
f.close()
```

Primeras líneas del fichero con los datos transportados en los paquetes:
```
1b0010408d2e07aeae7d91401400000000000040855ae9b632828401
12004a0000000059c86aa10000000000001ac9
0a0021000000028daf8dbd
0a000e000000028daf8dbd
...
```

Una vez obtenido los campos de datos de todos los paquetes es hora de tratar de entender el funcionamiento del protocolo de Minecraft. Empezando por el [formato del paquete](https://wiki.vg/Protocol#Packet_format), vemos que...

### Work in progress... 