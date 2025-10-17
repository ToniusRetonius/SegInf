# Levantar la VM Dojo-3.4.1 en VirtualBox

La VM que vamos a usar es [Dojo-3.4.1.ova](https://sourceforge.net/projects/websecuritydojo/files/Version_3.4.1/). Hay que descargarla y la vamos a levantar con [VirtualBox](https://www.virtualbox.org/).

## Pasos

1. **Importar la VM**
   - Abrir VirtualBox.
   - Ir a `File > Import Appliance`.
   - Seleccionar el archivo `.ova` descargado.

2. **Posible error en VirtualBox**
   - Al levantar la VM, puede aparecer el siguiente error:
     ```
     VirtualBox can't operate in VMX root mode. Please disable the KVM kernel extension, recompile your kernel and reboot (VERR_VMX_IN_VMX_ROOT_MODE)
     ```
   - Si tenemos procesador Intel, solucionamos corriendo:
     ```bash
     sudo modprobe -r kvm_intel
     ```

3. **Configurar la red antes de levantar la VM**
   - En la consigna dice que la red debe ser *Host-Only*.
   - Para crearla: `File > Tools > Network Management > Create`.

4. **Levantar la VM**
   - Una vez hecho lo anterior, iniciar la VM desde VirtualBox.
