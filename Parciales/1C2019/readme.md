# Solve Parcial 1C2019

## Multiple Choice (la opción correcta en negrita)
1. ¿Cuál de estas no es una amenaza activa?
    - A. Keylogger. Ponerle un keylogger a alguien es atacar, ergo, activa.
    - **B. Sniffing**. No es activa ya que no interrumpe el flujo de la comunicación.
    - C. Man in the middle. Parecería que MITM es pasiva, pero en realidad convertirse en MITM es el ataque, o sea, con un ARP spoofing, para redirigir el tráfico,... o sea que es activa (mirar el esquemita)
    - D. DDOS . Totalmente activa.

2. Indique la opción falsa. El software [applocker](https://learn.microsoft.com/es-es/windows/security/application-security/application-control/app-control-for-business/applocker/applocker-overview) (en 2025 no vimos mucho esto, por eso dejo el link)
    - A. Permite restringir los programas que pueden ser ejecutados en un sistema operativo.
    - **B. Funciona tanto en linux como en windows.** . Es de Microsoft
    - C. Tiene un modo para auditar mediante logs, y otro de aplicación efectiva de restricciones.
    - D. Se pueden asignar permisos en forma global en el sistema o en forma individual a uno o varios grupos o usuarios.
3. ¿Cuál de las siguientes no es una característica del modelo Clark-Wilson?
    - A. Es un modelo que hace hincapié en la integridad. Esto es cierto.
    - B. Hace foco en las transacciones. Fue pensado justamente para eso, bases de datos financieras enfocado en datos transaccionales.
    - C. Hace foco en la separación de tareas. En una transacción, cada operación atómica depende de actores diferentes, evitando el fraude. 
    - **D. Hace foco en un modelo multinivel.** Esto es para lo que no fue pensado, eso es BLP
4. Indique la opción correcta. En un esquema de PKI, la autoridad de registro es la encargada de:
    - A. Emitir certificados. Falso, esta es la autoridad certificante
    - **B. Validar la identidad del solicitante de un certificado.** Verdadero
    - C. Auditar el sistema. 
    - D. Definir las políticas y procedimientos de certificación.
5. Indique la opción correcta. Las herramientas de control de integridad de archivos como tripwire o aide:
    - A. Firman digitalmente sus archivos de configuración.
    - B. Detectan el origen de los ataques.
    - **C. Almacenan metadata de los archivos a controlar.**
    - D. Deben estar ejecutándose en forma permanente.
6. El concepto de *return to libc* está relacionado con:
    - **A. Una forma de saltear restricciones cuando el stack de un proceso no es ejecutable.** Es exactamente hacer un buffer-overflow sin inyectar código. Utilizando funciones de la librería standard de C (*libc*) para ejecutar comandos arbitrarios.
    - B. Un tipo de ataque al cifrado con PFS.
    - C. Una forma de explotar una vulnerabilidad web de inyección de comandos.
    - D. Volver a utilizar ciertos lenguajes de programación más performantes.

## Desarrolle (identifique todo lo que asume):
1. Describa qué son las linux capabilities.(1 pto)

Linux Capabilities es un mecanismo de control en Linux en el que en vez de darle permisos de root a un proceso, se puede definir de manera granular el uso de recursos del sistema. 
*Para ver la lista y obtener más info, mirar: *
```bash
man capabilities
```

2. Usando dibujos y unas pocas palabras, ilustre el concepto de botnet. No escriba oraciones ni párrafos.(1pto)

![Botnet](https://raw.githubusercontent.com/ToniusRetonius/SegInf/main/Parciales/1C2019/botnet.png)
Una botnet es una red de dispositivos comprometidos controlados por un atacante. El atacante usa la botnet para envío masivo de spam, ataques DDoS, minería de criptomonedas, entre otras cosas. Para que suceda, debe comprometer un servidor llamado **C&C (comando y control)** que a través de él realizará dichos ataques. Es la infraestructura usada por el atacante para coordinar los bots. Permite enviar órdenes, recibir resultados, distribuir actualizaciones y manejar la botnet.

3. En control de acceso, ¿cuál es la dificultad que trae almacenar los permisos mediante listas de capacidades? (1pto)

Las listas de capacidades son listas que guardan los sujetos con los permisos que tienen sobre cada objeto del sistema, o sea, la fila de la matriz. El problema es si queremos ver quiénes y con qué permisos pueden acceder a cierto objeto, tenemos que recorrer todas las listas de capacidades que tiene cada uno de los sujetos del sistema.


4. ¿Cuáles son los usos que se les da en seguridad a los números aleatorios? ¿Se debe tener alguna consideración a la hora de generarlos? (1pto)

Los números aleatorios se suelen utilizar en criptografía para el vector de inicialización (IV) de algortimos de cifrado, claves secretas, protocolos challenge-response (el nonce que evita los replay-attacks), producir el flujo de claves en algortimos de flujo. Sí, que sean realmente aleatorios. Es decir, que no estén basados en fenómenos predictivos. Se distinguen dos tipos : aleatorios verdaderos (ruido físico, estado de computadora), pseudo-aleatorios (generado por algortimos que simulan aleatoriedad).

5. Describa cómo realizaría el robo de sesión a un usuario autenticado en un sitio de apuestas online en la que las cookies de sesión no viajen cifradas por HTTPS, asumiendo que en la aplicación web no se ha descubierto ninguna vulnerabilidad en la implementación del código (ni SQLi, ni XSS). ¿Qué herramientas usaría? ¿Qué requisitos son necesarios para realizar el ataque? (1 pto)

Usaría Wireshark para sniffear la red, como la cookie viaja en texto plano, la copio y cuando yo tenga que interactuar con la web, le pego en el paquete esa cookie (cookie poisoning / spoofing)
