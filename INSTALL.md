# "PRESA - PREDADOR - SIMULACION""
## GUIA DE INSTALACION
###### @navarromatiassr

###### **Primeros pasos:**

Como primera instancia se debera tener instalado:

>git , python3

Una vez asegurado ambos paquetes, cree una carpeta e internamente ejecute la terminal con el siguiente
comando para obtener los files correspondientes:

```
git clone https://github.com/navarromatiassr/modeysim.git

```
Ingrese **dentro de la carpeta 'PRESA-PREDADOR'** recibida y cree un entorno virtual para evitar instalar las dependencias necesarias
de manera global, para esto deberá:
```
python3 -m venv **env**
```
Una vez creado, deberá activar el entorno actual a través de:
```
cd env/Scripts
activate.bat
```
Vuelva al folder de PRESA-PREDADOR, y ejecute nuestro 'requirements.txt' para obtener las dependencias necesarias:
```
pip install -r requirements.txt
```
Al finalizar, deberá haber recibido e instalado las dependencias. Ya es posible llevar a cabo el modelado PRESA - PREDADOR:
```
python presapredador.py
```

**Si los pasos fueron realizados correctamente, tendrá ya disponible la simulación.**
######                            ¡ Buena suerte :+1: !
