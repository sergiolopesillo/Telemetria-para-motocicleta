DISEÑO DE UN SISTEMA DE TELEMETRÍA PARA UNA MOTOCICLETA
======

## Tabla de contenido
- [Introducción](#introducción).
- [Hardware del sistema](#Hardware del sistema).
- [Diseño del sistema](#Diseño del sistema).
- [Aplicación web](#Aplicación web).

Introducción
======

El proyecto consiste en sensorizar una motocicleta para poder obtener más 
información de la que podemos observar en el propio panel del vehículo. Esto lo podemos 
conseguir con un microcontrolador y diferentes sensores, destinados a recopilar la 
información necesaria que queremos conocer en el momento que estamos encima 
de la motocicleta. Estos datos se visualizaran mediante nuestro teléfono móvil.

Hardware del sistema
======

El sistema esta formado por una Raspberry pi, debido a su coste reducido, tamaño, capacidad computacional y 
conectividad. En la parte de la sensorización se ha seleccionado el mlx90614 para la medición de la temperatura de los neumáticos y la temperatura ambiente, medimos la inclinación del vehículo con la MPU6050. Por ultimo utilizaremos un regulador de voltaje LM2596 debido a que el sistema eléctrico trabaja a 12V.



| Hardware     | imagen |
| --- | --- |
| Raspberry Pi 3B+ |   ![Rasp](https://user-images.githubusercontent.com/75255813/141853399-65c0aeb0-9999-45dd-acdf-27b3b3954c6d.png) |
| Sensor temperatura (mlx90614) |   ![mlx](https://user-images.githubusercontent.com/75255813/141853963-1a0d0d3a-db5f-4a42-8906-777946e02cf9.png) |
| Sensor acelerómetro (MPU6050) | ![MPU](https://user-images.githubusercontent.com/75255813/141854464-3cbe857d-776e-4ab6-b628-ffeb35f8ee29.png) |
| Regulador de voltaje (LM2596) |![LM](https://user-images.githubusercontent.com/75255813/141870576-8a9ae058-468d-4963-a6b5-830ba5ead4bd.png) |







Diseño del sistema
======
En la siguiente imagen podemos observar donde se situarían los diferentes componentes. En la zona del guardabarros delantero y trasero irían los sensores de temperatura y en la parte inferior del asiento se localizarían el microcontrolador, el regulador de voltaje y el sensor de inclinación. Este sistema iría conectado al encendido del vehículo para que no consuma energía directamente de la batería.


![image](https://user-images.githubusercontent.com/75255813/135065740-c75b97ff-ebdf-4e3a-ac34-99ec1c4f4b43.png)

Aquí podemos observar de forma sencilla las diferentes conexiones de los elementos que componen proyecto. Uno de los sensores mlx90614 y la MPU6050 irán conectados al mismo bus I2C para la adquisición de los datos, debido a que tienen diferentes direcciones de memoria. Mientras que el segundo mlx90614 ira conectado al GPIO17 y al GPIO27 creando en esos dos pines un bus I2C diferente, para que no exista ninguna incompatibilidad.

![image](https://user-images.githubusercontent.com/75255813/135066754-ab6ee8e7-8bd7-445b-902e-6b92c74b12d3.png)




Aplicación web
======
El usuario necesitara conectarse con su teléfono móvil al punto de acceso wifi creado por el microcontrolador. Mediante el navegador web del teléfono puede acceder a la aplicación que le mostrara los diferentes parámetros de interés. Situando el teléfono en el manillar de la motocicleta mediante un soporte, podrá disponer de esta información adicional en todo momento.


![image](https://user-images.githubusercontent.com/75255813/135065777-dd8619f1-99fa-4533-858e-023e53d96de8.png)

Por otro lado, el sistema guardará en una base de datos todas las mediciones 
realizadas durante la ruta. Una vez finalizada esta, el usuario tiene la posibilidad de 
descargar los datos obtenidos hasta el momento para su posterior tratamiento o 
visualización y otra posibilidad que tiene, es la opción de eliminar todos los datos para 
volver a realizar nuevas mediciones.

![image](https://user-images.githubusercontent.com/75255813/135065862-ec62c9c4-4d9a-4553-a970-85763a989f1e.png)









