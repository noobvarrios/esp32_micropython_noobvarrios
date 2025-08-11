#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp;  // objeto para I2C

void setup() {
  Serial.begin(115200);
  while (!Serial);    // espera monitor serie listo
  Serial.println("Prueba BMP280");

  // Intenta inicializar el sensor en la dirección detectada (0x76 o 0x77)
  if (!bmp.begin(0x76)) {
    Serial.println("Error: no se halló BMP280 en 0x76. Verifica dirección y cableado.");
    while (1) delay(10);
  }
}

void loop() {
  float temperatura = bmp.readTemperature();     // °C
  float presion    = bmp.readPressure() / 100.0F; // hPa

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");

  Serial.print("Presión: ");
  Serial.print(presion);
  Serial.println(" hPa\n");

  delay(2000);
}
