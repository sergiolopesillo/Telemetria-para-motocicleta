DISEÑO DE UN SISTEMA DE TELEMETRÍA PARA UNA MOTOCICLETA
======

El proyecto consiste en sensorizar una motocicleta para poder obtener más 
información de la que podemos observar en el propio panel del vehículo. Esto lo podemos 
conseguir con un microcontrolador y diferentes sensores, destinados a recopilar la 
información necesaria que queremos conocer en el momento que estamos encima 
de la motocicleta. 

Hardware del sistema
======

El sistema esta formado por una Raspberry pi, debido a su coste reducido, tamaño, capacidad computacional y 
conectividad. En la parte de la sensorización se ha seleccionado el mlx90614 para la medición de la temperatura de los neumáticos y la temperatura ambiente, medimos la inclinación del vehiculo con la MPU6050. Ya que tenemos que tener en cuenta que todo este sistema ira 
perfectamente integrado en la motocicleta

| Hardware     | imagen |
| --- | --- |
| Raspberry Pi 3B+ |   ![Rasp](https://user-images.githubusercontent.com/75255813/141853399-65c0aeb0-9999-45dd-acdf-27b3b3954c6d.png) |
| Sensor temperatura (mlx90614) |   ![mlx](https://user-images.githubusercontent.com/75255813/141853963-1a0d0d3a-db5f-4a42-8906-777946e02cf9.png) |
| Sensor acelerómetro (MPU6050) | ![MPU](https://user-images.githubusercontent.com/75255813/141854464-3cbe857d-776e-4ab6-b628-ffeb35f8ee29.png) |






Diseño del sistema
======





Aplicación web
======
El usuario necesitara conectarse al punto de acceso wifi creado por el 
microcontrolador. Mediante el navegador web del teléfono puedes acceder a la aplicación web 
que le mostrara los diferentes parámetros de interés. Situando el teléfono en un simple 
soporte, en el manillar de la motocicleta y podrá disponer de esta información adicional en 
todo momento.

Por otro lado, el sistema guardara en una base de datos todas las mediciones 
realizadas durante la ruta. Una vez finalizada esta, el usuario tiene la posibilidad de 
descargar los datos obtenidos hasta el momento para su posterior tratamiento o 
visualización y otra posibilidad que tiene, es la opción de eliminar todos los datos para 
volver a realizar nuevas mediciones.




![image](https://user-images.githubusercontent.com/75255813/135065740-c75b97ff-ebdf-4e3a-ac34-99ec1c4f4b43.png)



![image](https://user-images.githubusercontent.com/75255813/135065777-dd8619f1-99fa-4533-858e-023e53d96de8.png)
![image](https://user-images.githubusercontent.com/75255813/135065862-ec62c9c4-4d9a-4553-a970-85763a989f1e.png)



Conexiones del proyecto
======


![image](https://user-images.githubusercontent.com/75255813/135066754-ab6ee8e7-8bd7-445b-902e-6b92c74b12d3.png)



