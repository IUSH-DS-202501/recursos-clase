# Lab A
# Nombre:
# Cod Estudiante:  

######################################  
#                                   #  
#             Punto #1               #  
#                                   #  
######################################

# Se le encarga diseñar la mejor forma de distribuir energia eléctrica entre diferentes ciudades. Para esto, se le entrega información sobre la ciudad donde se genera la energia, y las conexiones entre diferentes ciudades. Su tarea es determinar si es posible entregar energia con la infraestructura actual o si debe realizar más conexiones.
# Su programa debe recibir información a través del teclado del usuario de la siguiente forma:

# Primero recibe un numero entero positivo N que indica la cantidad de conexiones que hay entre las diferentes ciudades. 
# Luego se recibe el nombre de la ciudad donde se genera la energia eléctrica.
# Por último se reciben N pares de nombres de ciudades separados por guiones (-) que indica que existe infraestructura entre esas ciudades.

# Usted debe imprimir el resultado de si es posible entregar energia solo con la infraestructura existente o si no.

#Ejemplo de entrada:

#6
#Medellin
#Bogota-Neiva
#Neiva-Pasto
#Medellin-Bogota
#Manizales-Medellin
#Bogota-Manizales

#En este ejemplo, todas las ciudades pueden ser alimentadas a través del circuito.

# INICIO_SOLUCION
# FIN_SOLUCION

######################################  
#                                    #  
#             Punto #2               #  
#                                    #  
######################################

# Partiendo del enunciado del punto anterior, considere que la distancia entre ciudades es importante ya que a mas distancia, más pérdida de electricidad y más costos en mantenimiento. Usted deberá entonces determinar cual es la distancia mínima que hay a través del los cables para llegar a todas las demas ciudades. 

#La forma en la que entran los datos, cambia un poco con respecto al enunciado anterior:

# Primero recibe un numero entero positivo N que indica la cantidad de conexiones que hay entre las diferentes ciudades. 
# Luego se recibe el nombre de la ciudad donde se genera la energia eléctrica.
# Por último se reciben N lineas donde cada línea contendrá tres elementos separados por guiones (-). Los primeros dos elementos son nombres de ciudades entre los que existe infraestructura. El tercer elemento es la distancia en KM entre las ciudades.

# Al final usted debe imprimir el nombre de cada ciudad e indicar cual es la distancia mínima a través de la infraestructura eléctrica a cada ciudad.

#Ejemplo de entrada:

#7
#Manizales
#Bogota-Barranquilla-1032
#Neiva-Tolima-169
#Tolima-Bogota-203
#Manizales-Medellin-223
#Bogota-Manizales-293
#Medellin-Barranquilla-758

# INICIO_SOLUCION
# FIN_SOLUCION