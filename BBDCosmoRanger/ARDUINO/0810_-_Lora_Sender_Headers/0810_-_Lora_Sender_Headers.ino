/*
Codigo extraido/modificado de las librerias de sandeepmistry/arduino-LoRa
Trabajado con IA
*/

#include <SPI.h>
#include <LoRa.h>

// Dirección de destino (255 = broadcast en u-lora)
byte header_to = 255;
// Dirección del remitente
byte header_from = 1;
// ID del mensaje (puedes incrementar si quieres seguimiento)
byte header_id = 0;
// Flags del mensaje (0 si no usas ACKs)
byte header_flags = 0;

int counter = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  // Opcional: Configuración LoRa para coincidir con ulora.ModemConfig.Bw125Cr45Sf128
  LoRa.setSpreadingFactor(7);      // SF7
  LoRa.setSignalBandwidth(125E3);  // 125 kHz
  LoRa.setCodingRate4(5);          // CR 4/5
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);

  LoRa.beginPacket();

  // Escribir cabeceras primero
  LoRa.write(header_to);
  LoRa.write(header_from);
  LoRa.write(header_id);
  LoRa.write(header_flags);

  // Escribir el mensaje
  LoRa.print("hello ");
  LoRa.print(counter);

  LoRa.endPacket();

  counter++;
  header_id++; // opcional, para que cada paquete tenga un ID único

  delay(5000);
}
  
