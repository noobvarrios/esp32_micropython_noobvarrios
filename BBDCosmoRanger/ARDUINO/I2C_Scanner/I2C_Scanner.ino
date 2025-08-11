#include <Wire.h>
//Wire es la libreria I2C (Inter integrated Circuit).
//https://docs.arduino.cc/language-reference/en/functions/communication/wire/
//https://docs.arduino.cc/learn/communication/wire/ mejor explicado y ejemplos.

void setup() {
  Serial.begin(115200); //inicia la comunicacion a velocidad de 115200 baudios. El monitor de serie debe modificarse a la misma velocidad
  Wire.begin(); //Inicializa I2C bus.
  Serial.println("\nEscaneo I2C iniciado...");
}

void loop() {
  Serial.println("Buscando...");
  for (byte addr = 1; addr < 127; addr++) {//bucle de direcciones.
    //byte = uint8_t (1 byte = 8bits) 
    //add < 127 (0 y 127 estan reservados para i2c)
    Wire.beginTransmission(addr); //Begins queueing up a transmission
    if (Wire.endTransmission() == 0) { //codigo de estado 0 = Exito. 
      Serial.print("0x");
      if (addr < 16) Serial.print("0"); //Si la direccion es menor a 16 entonces imprime un 0 para mantener formato. 
      Serial.println(addr, HEX); //Imprime el valor en base 16. 
    }
  }
  Serial.println();
  delay(5000);
}
