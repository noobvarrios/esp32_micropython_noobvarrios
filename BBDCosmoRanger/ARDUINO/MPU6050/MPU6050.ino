// Basic demo for accelerometer readings from Adafruit MPU6050

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

#define RAD_TO_DEG (180.0 / PI)

Adafruit_MPU6050 mpu;

void setup(void) {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("Adafruit MPU6050 test!");

  Wire.begin();

  // Aquí pasamos la dirección 0x69:
  if (!mpu.begin(0x69)) {
    Serial.println("Failed to find MPU6050 chip at 0x69");
    while (1) delay(10);
  }
  Serial.println("MPU6050 Found at 0x69!");

  // Resto de configuración…
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  // etc.
}

void loop() {

  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  float gx = g.gyro.x * 180 / 3.141516; 
  float gy = g.gyro.y * 180 / 3.141516;
  float gz = g.gyro.z * 180 / 3.141516;
  /* Print out the values */
  Serial.print("Acceleration X: ");
  Serial.print(a.acceleration.x);
  Serial.print(", Y: ");
  Serial.print(a.acceleration.y);
  Serial.print(", Z: ");
  Serial.print(a.acceleration.z);
  Serial.println(" m/s^2");

  Serial.print("Rotation X: ");
  Serial.print(gx);
  Serial.print(", Y: ");
  Serial.print(gy);
  Serial.print(", Z: ");
  Serial.print(gz);
  Serial.println(" °/s");

  Serial.print("Temperature: ");
  Serial.print(temp.temperature);
  Serial.println(" degC");

  Serial.println("");
  delay(2000);
}
