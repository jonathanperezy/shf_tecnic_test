# Prueba TECNICA para SHF

1. Analisis:
    Respuesta al primer punto (Analisis de codigo existente):
       En general se trata de una "Sobre escritura" del metodo write para el modelo account.move (asiento contable), en el cual se cargan todos los registros actuales
    para las lines de compra en la variable "old_purchases". Posteriormente se hace el llamado al write de la clase padre.
       Luego, accediendo a los indices de cada registro actual a traves de la funcion "enumerate" aplicado en el "for" sobre el "self" se lee
    en primer momento lo que seran las nuevas lineas de compras almacenado en "new_purchases", si no hay ningun nuevo registro se pasa al siguiente move con el
    "continue", en caso de que haya se hace una resta de objectos entre el "new_purchases" y "old_purchases[i]" (mismo indice del registro actual) y como consecuencia si
    existe algun nuevo registro en la linea ("diff_purchases") se crean anclas por cada registro hayado obteniendo el nombre desde el metodo "name_get", estas anclas son
    enlazadas a un mensaje usando la funcion "join" que luego es posteado en el hilo de registros del asiento contable.
    Finalmente, retorna el resultado original proporcionado por el "res" resultado del metodo padre write().
     

2. Desarrollo
    Todo el modulo