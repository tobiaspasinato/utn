/*El circuito debe simular una cerradura 
electronica. Para ello, ingresaremos
una contraseña de 4 caracteres por el 
teclado. La contraseña correcta debe
ser "ABCD".

Una vez ingresados 4 caracteres, el sistema
debe comparar ambas contraseñas automati-
camente y verificar si son iguales.

El display LCD mostrara en que estado esta
el sistema (esperando el ingreso de una
contraseña por defecto, "Bienvenido" si la
password ingresada coincide con la 
almacenada o "Password incorrecta" en caso
de ser distintas. Al ingresar caracteres
NO MOSTRARLOS por el display, mostrar un *

El servo representa la cerradura de la
puerta. El mismo debe empezar en un angulo
de 90 grados. De introducirse la contraseña
correcta, el mismo se movera a 0 o 180 grados
(vertical) simulando que la cerradura se 
movio. 

En caso de ingresar una contraseña correcta
el sistema mostrara el mensaje correspondiente
y movera el servo a 0/180 grados por 5 segundos,
luego el sistema debe reiniciarse. En caso 
de contraseña invalida, el sistema debe informar
al usuario y reiniciarse luego de 3 segundos
*/
#include <Servo.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

#define SERVOMOTOR 11

Servo servomotor;
LiquidCrystal pantalla(2, 3, 4, 5, 6, 7);

char contra[5] = "ABCD";
char input[4];
int contador_chequeo = 0;
long int tiempo = millis() + 5000;
bool bandera_chequeo = false;

const byte ROWS = 4; // cuatro filas
const byte COLS = 4; // cuatro columnas
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {A0, A1, A2, A3}; // conecta a los pines de fila del teclado
byte colPins[COLS] = {A4, A5, 8, 9}; // conecta a los pines de columna del teclado

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup() {
  Serial.begin(9600);
  servomotor.attach(SERVOMOTOR,500,2500);
  pantalla.begin(16, 2);
  pantalla.clear();
  servomotor.write(90);
  pantalla.print("Ingrese contra:");
}

void loop() {
  inputTeclado();
  bool bandera_chequeo = false;
  for(int i = 0;i < 4;i++){
    if(input[i] == contra[i]){
      contador_chequeo ++;
    }
    else{
      break;
    }
  }
  if(contador_chequeo == 4){
    bandera_chequeo = true;
  }
  if(bandera_chequeo == true){
    pantalla.clear();
    pantalla.print("Bienvenido");
    while(tiempo >= millis()){
      int posicion_servo = servomotor.read();
      if(posicion_servo == 90){
        servomotor.write(0);
      }
      else if(posicion_servo == 0){
        servomotor.write(180);
      }
      else if(posicion_servo == 180){
        servomotor.write(0);
      }
    delay(1000);
    }
  }
  else{
    pantalla.clear();
    pantalla.print("Contraseña");
    pantalla.setCursor(0,1);
    pantalla.print("Incorrecta");
    delay(3000);
  }
  char input[4];
  pantalla.clear();
  servomotor.write(90);
  pantalla.print("Ingrese contra:");
}

void inputTeclado(){
  pantalla.setCursor(0,1);
  for(int i = 0;i < 4;i++){
    char key = keypad.getKey();
    while(key == NO_KEY){
      char key = keypad.getKey();
      if(key != NO_KEY){
        pantalla.print("*");
        input[i] = key;
        break;
      }
    }
  }
}