#include <Servo.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

#define SERVO 11

Servo miServo;
LiquidCrystal lcd(2, 3, 4, 5, 6, 7);

char contrasenia[5] = "ABCD";
char input[4];
int contador = 0;

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
  miServo.attach(SERVO,500,2500);
  lcd.begin(16, 2);
  seteo();
}

void loop() {
  inputTeclado();
  if(chequeoClave()){
    instruccionesCorrecta();
  }else{intsruccionesIncorrecta();}
  char input[4];
  seteo();
}

void inputTeclado(){
  lcd.setCursor(0,1);
  for(int i = 0;i < 4;i++){
    char key = keypad.getKey();
    while(key == NO_KEY){
      char key = keypad.getKey();
      if(key != NO_KEY){
        lcd.print("*");
        input[i] = key;
        break;
      }      
    }
  }
}

bool chequeoClave(){
  bool bandera = false;
  int contador = 0;  
  for(int i = 0;i < 4;i++){
    if(input[i] == contrasenia[i]){
      contador ++;
    }else{break;}
  }
  if(contador == 4){
    bandera = true;
  }
  return bandera;
}

void intsruccionesIncorrecta(){
  lcd.clear();
  lcd.print("Password");
  lcd.setCursor(0,1);
  lcd.print("Incorrecta");
  delay(3000);
}
  
void instruccionesCorrecta(){
  lcd.clear();
  lcd.print("Bienvenido/a!");
  unsigned long tiempoObjetivo = millis() + 5000;
  while(tiempoObjetivo >= millis()){
    int posicion = miServo.read();
    if(posicion == 90){
      miServo.write(0);
    }else if(posicion == 0){
      miServo.write(180);
    }else if(posicion == 180){
      miServo.write(0);
    }
    delay(1200);
  }
}
  
void seteo(){
  lcd.clear();
  miServo.write(90);
  lcd.print("Ingrese clave:");  
}
