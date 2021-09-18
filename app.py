from flask import Flask,send_file, jsonify,render_template, request, redirect, url_for, flash, Response
from smbus2 import SMBus
from mlx90614 import MLX90614
from flask_mysqldb import MySQL
from selenium import webdriver
import requests
import urllib
import time
import math
import sys
import pymysql
import pyodbc
import io
import csv
import datetime
from mpu6050 import mpu6050 



mpu = mpu6050(0x68)

bus = SMBus(1)
bus2=SMBus(2)
sensor = MLX90614(bus, address=0x5A)
sensor2=MLX90614(bus2, address=0x5A)


app = Flask(__name__, static_folder="export")

#conexion Mysql

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'pi'
app.config['MYSQL_PASSWORD']= 'pelikan22'
app.config['MYSQL_DB']= 'mpu'
mysql = MySQL(app)

#settings
app.secret_key = 'key'

@app.route('/')


def index():

	  return render_template("index.html")


@app.route('/getData')


def getData():

	cur = mysql.connection.cursor()

	while True:

	  temp_obj2 = sensor2.get_object_1()
      temp_obj = sensor.get_object_1()
	  temp_amb = sensor2.get_ambient()
	  #inclinacion=mpu.get_gyro_data()
	  accel_data=mpu.get_accel_data()
	  #datetime=datetime.datetime.now()
	  inclinacionX=round(math.atan(accel_data['x']/math.sqrt(math.pow(accel_data['y'],2)+math.pow(accel_data['z'],2)))*(180.0/3.14))
	  templateData= {
		#'objeto1': temp_obj,
		#'ambiente' : temp_amb,
		#'objeto2' : temp_obj2,
		"inclinacion" : inclinacionX 
	  }
	  #cur.execute('INSERT INTO datos (ruedaDel, ruedaTra, temperaturaAmb, inclinacion) VALUES({}, {}, {}, {})'.format(temp_obj, temp_obj2, temp_amb, inclinacionX))
	  #mysql.connection.commit()
	 # cur.execute('INSERT INTO datosmpu (inclinacion,fecha) VALUES({}, %s)'.format(inclinacionX, fecha))
         # mysql.connection.commit()
 
	  return jsonify(templateData), 200

	  bus.close()





#Metodo para borrar los datos obtenidos hasta el momento
@app.route('/delete', methods=['POST'])
def delete_info():

     if request.method=='POST':
	cur=mysql.connection.cursor()
	cur.execute('DELETE  FROM datos')
	mysql.connection.commit()
	# flash('Los datos han sido borrados')
	print ('Ha sido eliminado')
	return  redirect(url_for('index'))
	 #return 'Ha sido eliminado'


@app.route('/export', methods=['POST'])
def export():
     if request.method=='POST':	
	cursor=mysql.connection.cursor()
	
	cursor.execute('SELECT id, inclinacion FROM datosmpu')

#	cursor.execute('SELECT id, ruedaDel, ruedaTra,temperaturaAmb, inclinacion FROM datos')
	result=cursor.fetchall()
	with open('ruta.xls','w') as file:
	 for row in result:
	   csv.writer(file).writerow(row)
	

     print ('Excel generado')
     cursor.close() 
  	
     easygui.msgbox("Documento generado", title="AVISO");

     return  redirect(url_for('index'))

@app.route('/export')
def download():
	path= "ruta.xls"
        return send_file(path,as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True,port=3000,  host='0.0.0.0')
