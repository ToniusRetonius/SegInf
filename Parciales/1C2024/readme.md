# Solve Parcial 1C2024

## Multiple choice (en negrita la respuesta correcta)
1. Qué forma de control de acceso está relacionada con la siguiente pregunta: ¿Es la persona que está procurando entrar realmente quién dice ser?
    - a. Autorización. Falso, ese escenario sería si esa persona tiene acceso a cierto recurso.
    - **b. Autenticación.** 
    - c. Auditoría. 
    - d. Control de acceso mandatario.

2. ¿Cuál de las siguientes definiciones describe mejor el “spoofing”?
    - a. El proceso de enviar información desde múltiples equipos con la intención de sobrecargar a la víctima. Esto sería un DoS.
    - b. El proceso de capturar datos, cambiar el contenido, y reenviarlos. Ataque a la integridad, no es spoofing.
    - c. El proceso de insertar código extra que puede ser utilizado luego para ganar acceso al sistema. Esto podría ser un XSS si es un código para una web.
    - **d. El proceso de reemplazar la dirección de origen de un paquete para hacerse pasar por otro equipo.** Este es un Spoofing. En particular, un IP spoofing, ya que cambia el header IP con otro IP src. Si fuese dentro de una LAN, el ARP spoofing consiste en falsificar respuestas ARP para asociar una IP legítima a la MAC del atacante.

3. La utilización de política targeted en SElinux garantiza:
    - a. que toda aplicación del sistema está segurizada por SELinux.
    - b. que la política se verifica (loguea) pero no se fuerza.
    - c. que un conjunto de servicios del sistema se encuentran segurizados por SELinux.
    - d. que no se pueden instalar aplicaciones adicionales al sistema.

4. Los principios de kerckhoffs tratan sobre:
    - **a. Criptografía**. Son como 6 o 7 creo. Hay uno que dice que las claves deben ser fáciles de recordar, que el sistema debe ser difícil de criptoanalizar y otro que habla de que el sistema criptográfico debe depender del secreto de la clave y no del algortimo.
    - b. Diseño seguro
    - c. Desarrollo Seguro
    - d. Control de acceso mandatorio

5. ¿Por qué 3DES es una mejora sobre el DES standard?
    - a. Utiliza claves públicas y privadas.
    - b. Genera un hash del texto claro antes de cifrar.
    - **c. Utiliza 3 claves y varias pasadas de cifrado y/o descifrado.** La diferencia principal es que aumenta el tamaño de clave y la cantidad de veces que se aplica por bloque.
    - d. 3DES es más rápido que DES.

6. ¿Cuál de las siguientes afirmaciones describe mejor el concepto de "TOPT"?
    - a. Es una técnica de cifrado de datos utilizada para proteger la integridad de la información. 
    - b. Se refiere a una lista de las principales amenazas de seguridad informática que enfrentan las organizaciones.
    - **c. Es un método para autenticar a los usuarios utilizando un código único generado en tiempo real.** Efectivamente, Time-based One-Time Password.
    - d. Se utiliza para prevenir ataques de denegación de servicio (DDoS) mediante la limitación de la tasa de solicitudes.

## Desarrollo
1. Se desea implementar una variante del mecanismo de Challenge-Response durante la etapa de autenticación entre un cliente y un servidor, utilizando criptografía asimétrica. El servidor tiene almacenada la clave pública del cliente. Describa dicha implementación. ¿Qué ventaja provee? (1 pto)
La implementación de un CRAM con criptorafía asimétrica donde las claves no viajan y sólo se define una clave de sesión efímera (implementando PFS) asegura que si el servidor es vulnerado, el cliente no compromete ninguna de sus comunicaciones previas a la sesión comprometida, y tampoco expone su clave privada que vive en su equipo. 

2. Describa brevemente SHA1 indicando qué es y para qué se utiliza. ¿Por qué no se recomienda utilizarlo en nuevas aplicaciones? (1pto)
SHA1 es una función de hash unidireccional que devuelve un resultado de 20 bytes que no se recomienda su uso ya que tiene vulnerabilidades debido a colisiones.
(Falta agregar las propiedades de una función de Hahs)
3. ¿Cómo se puede determinar de manera remota el sistema operativo de un equipo (sin tener credenciales en el mismo)?
La manera más sencilla es simulando un *three-way-handshake* con el dispositivo *target*. O sea, vamos a mandar segmentos TCP/80 con el flag ACK. Esto nos permite decidir si se trata de un *stateless* (si recibimos un RST) o *stateful* (si nos ignora). Sino, usamos 
```bash
nmap -sV ip_target
```
Y nmap se encarga de hacer el *OS-fingerprinting* con un mix de técnicas, midiendo TTL y cosas.

4. Describa las vulnerabilidades de inyección en aplicaciones web, indicando por lo menos dos tipos distintos, y dos mecanismos de prevención.

En aplicaciones web, si tenemos que llenar por ejemplo un formulario con nombre, apellido, y demás info, y esa información no es sanitizada, puede suceder que :

- Se inyecte códido SQL (SQLi), donde el atacante buscará obtener alguna información, tal vez de otros clientes con
```bash
tonius ; SELECT * 
```

XSS  (no es injection (mirar que en OWASP son categorías separadas)). La otra es la command injection.

5. Defina y compare los conceptos de honeypot y honeytoken. (1 pto)
Honeypot es un recurso deliberadamente expuesto con el objetivo de atraer, detectar y estudiar actividades maliciosas. La idea es que se comporte como un señuelo. Un honeytoken es un señuelo digital cuyo objetivo es detectar su uso no autorizado (cualquier interacción es considerada un inicio de compromiso).

6. La empresa joyanuncataxi.com provee un servicio web para publicar, en forma gratuita, anuncios clasificados de productos de segunda mano. Al realizar el alta de los mismos, además de la descripción del producto o servicio, se piden datos del anunciante, como email o teléfono celular. La empresa recibió reportes de varias personas que recibieron llamados a sus teléfonos celulares, en cualquier horario, relacionados con anuncios del sitio, pero que ellos no habían publicado. Proponga un mecanismo para minimizar la posibilidad de ocurrencia de estos incidentes. (1 pto)

El problema es que no chequean la data y por eso, no validan que los números sean de quién dicen ser.
