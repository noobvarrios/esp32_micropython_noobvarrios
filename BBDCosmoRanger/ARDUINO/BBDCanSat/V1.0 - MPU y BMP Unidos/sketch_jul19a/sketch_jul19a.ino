#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <MPU6500_WE.h>          // <— librería para MPU6500

#define BMP_ADDR   0x76
#define MPU_ADDR   0x68

Adafruit_BMP280 bmp;             // objeto BMP280
MPU6500_WE        mpu(MPU_ADDR); // objeto MPU6500

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // 1) Arranca I²C
  Wire.begin();

  // 2) Inicializa BMP280
  Serial.print("Inicializando BMP280 en 0x76… ");
  if (!bmp.begin(BMP_ADDR)) {
    Serial.println("FALLO");
    while (1) delay(10);
  }
  Serial.println("OK");

  // 3) Inicializa MPU6500
  Serial.print("Inicializando MPU6500 en 0x68… ");
  if (!mpu.init()) {
    Serial.println("FALLO");
    Serial.println("  • Verifica cableado: VCC→3.3V, GND→GND, SDA→SDA, SCL→SCL");
    Serial.println("  • Asegura AD0 a GND para dirección 0x68");
    while (1) delay(10);
  }
  Serial.println("OK");

  // 4) Calibración (autodetección de offsets)
  Serial.println("Calibrando acelerómetro y giroscopio (mantén el módulo quieto)...");
  delay(1000);
  mpu.autoOffsets();
  Serial.println("Calibración completada");

  // 5) Configuración giroscopio
  mpu.enableGyrDLPF();              // activa DLPF (filtro pasa-bajos)
  mpu.setGyrDLPF(MPU6500_DLPF_6);   // elige ancho de banda (por ejemplo DLPF_6 ≈ 5 Hz)
  mpu.setGyrRange(MPU6500_GYRO_RANGE_250);  // rango ±250°/s
  mpu.setSampleRateDivider(5);      // tasa de muestreo = GyroRate / (1 + divider)

  // 6) Configuración acelerómetro
  mpu.enableAccDLPF(true);          // activa DLPF para acelerómetro
  mpu.setAccDLPF(MPU6500_DLPF_6);   // ancho de banda similar al giroscopio
  mpu.setAccRange(MPU6500_ACC_RANGE_2G);    // rango ±2 g

  Serial.println("Setup completo. Enter your loop!");
}

void loop() {
  //BMP
  float temperatura = bmp.readTemperature();     // °C
  float presion    = bmp.readPressure() / 100.0F; // hPa

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");

  Serial.print("Presión: ");
  Serial.print(presion);
  Serial.println(" hPa\n");


  //MPU
  xyzFloat gValue = mpu.getGValues();
  xyzFloat gyr = mpu.getGyrValues();
  float temp = mpu.getTemperature();
  float resultantG = mpu.getResultantG(gValue);

  Serial.println("Acceleration in g (x,y,z):");
  Serial.print(gValue.x);
  Serial.print("   ");
  Serial.print(gValue.y);
  Serial.print("   ");
  Serial.println(gValue.z);
  Serial.print("Resultant g: ");
  Serial.println(resultantG);

  Serial.println("Gyroscope data in degrees/s: ");
  Serial.print(gyr.x);
  Serial.print("   ");
  Serial.print(gyr.y);
  Serial.print("   ");
  Serial.println(gyr.z);

  Serial.print("Temperature in °C: ");
  Serial.println(temp);

  Serial.println("----------------------------------------"); 

  delay(2000);
}
