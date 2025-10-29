# Solve Parcial 1C2017

## Multiple-choice (las respuestas están marcadas en negrita)
1. ¿Qué política de control de acceso está relacionada principalmente con la función que cumple un individuo en la organización?
    - A. MAC
    - B. DAC
    - **C. RBAC** Role-Based Access Control
    - D. PAC
2. Toma tiempo distribuir completamente la CRL. ¿Qué protocolo nos permite verificar en forma inmediata el estado de un certificado X509?
    - A. CA. No es un protocolo
    - B. CP. Certificate Policy
    - C. TLS. Transport Layer Security
    - **D. OCSP** . Online Certificate Status Protocol
3. ¿Qué tipo de ataque está diseñado para sobrecargar un protocolo o servicio en particular?
    - A. Spoofing
    - B. MiTM
    - C. Backdoor
    - **D. Flood**
4. En criptografía, ¿con que está relacionada la sigla MAC?
    - A. Media Access Control
    - B. Message authentication code
    - C. Multiple advisory committees
    - **D. Mandatory Access Control.**
5. ¿Qué algoritmo de clave simétrica usa cifrado por flujos para cifrar la información?
    - **A. RC4**
    - B. Blowfish
    - C. Rijndael
    - D. DSA
6. ¿Cuál de las siguientes medidas **no** agrega seguridad contra los ataques de sql injection en aplicaciones web?
    - A. Validación de parámetros de entrada que recibe la aplicación.
    - **B. Uso de Firewall Stateful Inspection.** Esto sirve para mirar los paquetes entrantes a la red y filtrar los que no tienen conexiones activas.
    - C. Uso de Web Application Firewall
    - D. Asignación de mínimos privilegios a los usuarios de bases de datos utilizados por la aplicación web.

## Desarrollo
1. ¿Para qué sirven y cuándo se utilizan los mecanismos de challenge-response? (1 pto)

Se utilizan para autenticarse con un servidor sin mandar la contraseña de la sesión en claro al momento de iniciar una comunicación cifrada (TLS handshake).

2. Describa en qué consiste el arp spoofing. ¿Cómo se puede detectar? (1pto)

El *ARP spoofing* es un ataque a una vulnerabilidad de diseño del protocolo ARP. En este, no existe la autenticación y en particular, se permite asociar cualquier IP con cualquier dirección MAC. El atacante lo que hace es mandar ARP replies falsos : decirle al gateway que la IP del *target* está asociada a su MAC y al *target* que la IP del gateway está asociada a su MAC. Con lo cual, todo el tráfico pasa por la máquina del atacante. Esto siempre que tenga que *IP forwarding* activado sino, la comunicación será interrumpida y sospecharán. Para mitigar este riesgo se puede usar TLS y cifrar todo. Sino, hay algunos programas como DHCP snooping.

3. Tiene que diseñar e implementar una aplicación web para acceso por parte de sus clientes a información confidencial a través de Internet. Proponga un algoritmo seguro de almacenamiento de claves. Adicionalmente, proponga un mecanismo de autenticación más robusto, que no utilice usuario/clave. (1pto)

Guardamos los hashes, o sea, el usuario tiene una clave privada con la cual cifra su contraseña y guardamos eso, y luego comparamos los hashes. Por supuesto, que para garantizar seguridad en la comunicación, necesitamos que ese hash viaje cifrado con un mecanismo asimétrico con mi servidor web donde se define una clave de sesión (con un diffie hellman efímero) con un challenge response.



4. ¿Para qué mecanismo de cifrado se utiliza el ataque de Kasiski? ¿Cuál es la dea del mismo? (1pto)

Se usa para *Vigenère*, masomenos era buscar secuelas repetidas en el cifrado donde las separaciones entre repeticiones suelen ser múltiplos de la longitud de la clave con esa data se aplica análisis de frecuencias para recuperar los desplazamientos.

5. Indique qué es un IDS, para que sirve y para que no. Clasifique según el tipo. (1pto)

Un IDS *Intrusion Detection System* es un mecanismo de detección de intrusiones, es decir, un sistema que permite detectar actividad sospechosa, por ejemplo un NIDS monitorea la red y define reglas del tipo *alert ...* en caso de que haya cosas sospechosas en los paquetes. El HIDS es para el host, analiza logs y genera reportes.

Son mecanismos de detección, no de *Prevención*, no actúan, sólo detectan.

6. Juan y Marina quieren jugar al “piedra, papel o tijera”, pero lo quieren hacer a través de Internet, sin ningún tipo de intermediarios ni terceras partes. Proponga un protocolo criptográfico que no permita a ninguno de los dos hacer trampa. No se preocupe demasiado por los protocolos de red. (1,5 ptos)

Asumimos que ya tenemos establecida una conexión cifrada con TLS.
Asumimos que Juan debe descartar primero, entonces le aplica una función de hash a la carta, la firma (cifra con la privada) y manda: la carta más la firma. Marina calcula el hash de la carta y descifra con la pública y compara. Hace lo mismo y manda. Y así hasta terminar.

7. El ministerio de Modernización, a través de la Resolución 204-E/2017, dispuso la obligatoriedad de uso de un mecanismo de control de acceso biométrico para administrar el control de asistencia y presentismo del personal de la administración pública nacional. Describa como implementaría la solución, teniendo en cuenta la seguridad de los lectores de huella digital, la conectividad, la protección de los registros de acceso, y la seguridad de una aplicación web que le permite a cada empleado ver su historial de ingresos/egresos y presentar justificaciones, por ejemplo, por enfermedad. (1,5 ptos)