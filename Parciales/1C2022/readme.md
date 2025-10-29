# Solución Parcial 1C2022
El profe comentó que la solución es una sola. A veces parece que son varias, pero es la que más sea.

## Multiple-Choice (respuesta en negrita es la correcta)

1. En qué principio está basado el modelo de Clark-Wilson ?
    - **A : Intgridad**. El modelo de Clark-Wilson surge como un modelo práctico de integridad para bases de datos financieras y sistemas de transacciones. O sea que el punto fuerte es se una política de integridad basada en la noción de transacción (comenzar en un estado consistente y ejecutar una serie de operaciones atómicas que lo llevan de ese a otro consistente).

    - B : Disponibilidad. No, por lo mencionado antes.
    - C : Confidencialidad. No, por lo mencionado antes.
    - D : Auditabilidad. No, por lo mencionado antes.

2. Ud. fue seleccionado para encontrar e implementar soluciones de multiple factor de auth. Cuál es realmente de múltiple factor ?
    - A : usuario y contraseña. No porque en este caso es de primer factor. Sólo la contraseña es un factor. El usuario es identificador.

    - **B : Huella dactilar y contraseña** . Es una contraseña de multiple factor ya que para que sea de múltiple factor, los factores **deben ser de naturaleza diferente**, o sea, en este caso, tenemos biométrico y contraseña.

    - C : Contraseña y PIN . Es la tricky, en 2022, el PIN era como una contraseña, entonces tenía sentido en ese entonces que esta sea incorrecta (ya que ambos factores son de la misma naturaleza). Hoy, ese PIN puede ser generado para un dispositivo de manera local y no sería de la misma naturaleza.

    - D : Huella dactilar y escaneo de retina. Son los dos del mismo tipo de factor, ambos biométricos.

3. Compramos una compañía de nuestra línea de negocios. Detectamos que utilizan WEP para sus redes wifi. WEP es considerado :
    - A. el mecanismo de cifrado preferido para redes wireless. Esto es falso ya que fue el primer mecanismo de seguridad que utilizaba RC4 con IV débil, no garantiza integridad ya que utiliza CRC-32, permite modificar el paquete y recalcularle el CRC.
    - B. Standard por defecto para routers wifi que se compran en la actualidad. Falso, el standard mínimo es WPA2
    - **C. Inseguro**. Verdadero, El vector de inicialización tiene 24 bits con lo cual es fácil que se repita.
    - D. Seguro. Falso

4. Si estamos usando la propiedad simple de seguridad del modelo Bell-LaPadula, ¿Qué podemos hacer?
    - A. Escribir hacia abajo. Falso, la propiedad de condición simple es sobre lectura.
    - B. Leer hacia arriba. Falso, en BLP no se permite leer objetos con mayor nivel de seguridad (si no tengo acceso a confidencial, menos tengo a top secret)
    - C. Escribir hacia arriba. Falso, la propiedad de condición simple es sobre lectura.
    - **D. Leer hacia abajo.** Es esta, la propiedad es Read-Down. Niveles de clearence altos pueden leer de su nivel para abajo. 
5. Tenemos 100 usuarios que necesitan comunicarse cada uno con el otro. Si usamos criptografía asimétrica, ¿cuantas claves serán necesarias?
    - A. 2000. Falso
    - B. 100. Falso.
    - **C. 200.** Cada uno debe crear su par de claves pública-privada
    - D. 4950. Falso. Este sería el caso de simétrica. O sea, cada par de usuarios necesita una compartida única. Entonces 
    $2 \times \frac{n(n-1)}{2} = \frac{100 \times 99}{2} = 4950$ claves

6. ¿Qué es tu clave pública en un algoritmo de cifrado asimétrico?
    - **A. Compartida**. Una clave pública es una clave compartida. 
    - B. Secreta. Falso, esa sería la privada.
    - C. Usada por alguien más para desencriptar mensajes dirigidos a vos. Totalmente falso e ilógico.
    - D. Usada por vos para desencriptar mensajes enviados a vos. En el mecanismo asimétrico usamos nuestra privada para descifrar.


## Desarrollo
Las respuestas no deben ser tan largas. Tal vez haga una intro al tema porque es práctica de parcial.

1. Una forma de clasificar las vulnerabilidades en el software es según se presenten en la etapa de diseño, implementación u operación. De un ejemplo de cada una. (1 pto). 

    Existen tres estapas del desarrollo :
    - Arquitectura / Diseño : son las vulnerabilidades introducidas al concebir la aplicación, como decisiones estructurales o mecanismos de validación. Los protocolos del modelo TCP/IP no fueron concebidos para el iternet hostil de hoy. Como consecuencia, el tráfico de IP, TCP,.. viaja en texto plano, esto permite *sniffing* o *MITM*. Además podemos mencionar que en TCP el three-way-handshake no implementa mecanismos para autenticar al cliente, como consecuencia, se puede hacer un *SYN-Floofing* y mandarle miles de paquetes SYN falsos con IPs falsas (por IP spoofing) y consumir todos los recursos de memoria del servidor, ocasionando un DoS.

    - Implementación : son los errores cometidos durante la codificación, como un buffer overflow, inyecciones, manejo inseguro de datos. Un ejemplo típico es el bufferoverflow que puede ocasionar el uso de *strcpy()* es C que copia todo sin chequear longitud (recordar que en C pedimos cierta memoria para el buffer, pero si copiamos con strcpy y se pasa, pisa el stack). Como consecuencia, se puede modificar la dirección de retorno y allí mandar un payload... etc. Por eso, hay que usar *strncopy()* para escrituras que mitigen este riesgo, y chequear la data que viene del exterior.

    - Operación : problemas que surgen una vez que la aplicación está en producción, donde se explotan vulnerabilidades de las etapas anteriores. Los problemas operacionales suelen deberse a dejar credenciales de fábrica (cuentas con claves por defecto) o mismo instalaciones por defecto (configuraciones de seguridad como puertos abiertos por defecto). También se puede dar que el administrador del sistema no aplique las actualizaciones de seguridad a tiempo y lo deja expuesto.


2. Describa el concepto de forward secrecy. (1pto)
Forward secrecy es una propiedad criptográfica (PFS) en protocolos de establecimiento de claves. El objetivo es que si se compromete la clave privada luego de cierta sesión, las sesiones anteriores no se compromenten. Se implementa con claves de sesión únicas y temporales.

3. Discuta la siguiente afirmación: "Mi aplicación web es segura porque mantengo el servidor con los parches al día y sólo permito conexiones HTTPS". (1 pto)

Esta respuesta se puede encausar por el lado del rol de la confianza. Asumir que el fabricante de los parches testeó en todos los entornos, que los parches no son vulnerables, entre otras consideraciones, podría llegar a ser una asunción desacertada. Por otra parte, consideramos mecanismos para esterilizar la información que ingresa un usuario en nuestra web ? Seguir una política Zero Trust nos permite dudar de toda información externa. Evitando ataques XSS, SQLi (en caso de utilizar SQL).

4. Describa la idea de type-enforcement en SE-linux (1 pto)
Type-Enforcement en SE-Linux es un mecanismo de control en SE-Linux donde canda proceso y objeto del sistema tiene asociado un *tipo de seguridad*. De esta manera, sólo las combinaciones entre tipos autorizados por las políticas podrán acceder a los recursos del sistema. Las transiciones son cuando un proceso o archivo crea otro, se definen transiciones para definir los tipos de seguridad de los mismos.

5. ¿Cual es la característica principal de un firewall stateful? (1 pto)
Un firewall stateful es un tipo de firewall que guarda información respecto de las sesiones de red desde el comienzo hasta el final y filtra según ello. Es decir, el firewall puede registrar número de seq TCP, estado de conexión, y otras cosas. Por tanto, el control se hace sobre la sesión y no sobre cada paquete como lo hace el stateless (analiza paquete por paquete y no mantiene el estado de las conexiones para el filtrado)

6. La universidad quiere implementar un sistema para que los profesores puedan registrar las actas de finales. Al analizar el mecanismo de autenticación, deben elegir entre usar usuario y contraseña, o usar pares de claves públicas/privadas para cada usuario. Indique dos ventajas del 2do mecanismo. (1 pto)

Utilizar un mecanismo de clave pública/privada tiene varias ventajas. La fundamental para mí en este contexto es que la clave privada no viaja por el canal inseguro. Es la esencia de la criptografía asimétrica, confidencialidad cuando hay alguien sniffeando la red. Despúes, fundamental también, integridad del final y no repudio, ya que sube el alumno el final firmado (o sea, aplica una función de hash al pdf y cifra con su privada ese hash). Esto último, también podría ser útil cuando el docente pone la nota, firmarla para garantizar más seguridad. Se puede mencionar también que si se vulnera un servidor, sólo existen las públicas allí, y por tanto, si se vulnera una base de datos, no se filtran contraseñas.

7. Una licitación es el procedimiento administrativo para la adquisición de suministros, realización de servicios o ejecución de obras que celebran los organismos que forman parte del Sector Público. Consta de un anuncio de la licitación, un plazo para recepción de ofertas (que son secretas en sobre cerrado, e incluyen una propuesta económica, además del detalle de la propuesta de tareas a realizar/productos a entregar), un proceso de apertura de ofertas (en ese momento se hacen públicas para todos los oferentes) y un proceso de adjudicación. Defina consideraciones necesarias para digitalizar el circuito, impidiendo que tanto los oferentes como el organismo solicitante, puedan hacer trampa. (2 ptos). Es decir:
    - Que el oferente no pueda cambiar su propuesta, una vez realizada.

    - Que el oferente no pueda aducir que él no presentó la propuesta.
    
    - Que el organismo no pueda leer las propuestas recibidas, antes de que cierre el plazo de presentación de ofertas, para no poder pasar información a los competidores del oferente.
    
    - Que el oferente no pueda presentar una propuesta, una vez cerrado el plazo de presentación de ofertas.
    
    - Que el proceso de apertura puede ser auditado por todos los oferentes.

Este es un escenario típico de un **commit-reveal scheme**. No vimos directamente eso en la materia, pero es al modelo al que llegaríamos intuitivamente. Al documento firmado para garantizar integridad y no repudio, y una autoridad de timestamping para verificar la fecha (en plazo), se le aplica un hash y se manda ese mismo. El día de la lectura, el estado recibe el documento, le aplica el hash y compara. Esto resuelve todos los puntos anteriores.