#include <Wire.h>
#include "MAX30105.h"
#include "spo2_algorithm.h"
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

MAX30105 particleSensor;

#define echoPin 2 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 3 //attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

int comm;

int32_t bufferLength; //data length
int32_t spo2; //SPO2 value
int8_t validSPO2; //indicator to show if the SPO2 calculation is valid
int32_t heartRate; //heart rate value
int8_t validHeartRate; //indicator to show if the heart rate calculation is valid


void setup()
{
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.setTimeout(1);

  if (!particleSensor.begin())
  {
    while (1);
  }


  if (!mlx.begin()) {
     while (1);
  }

  particleSensor.setup(60, 4, 2, 800, 411, 4096);
}

void loop()
{
  uint16_t irBuffer[50]; //infrared LED sensor data
  uint16_t redBuffer[50];  //red LED sensor data
  bufferLength = 50; //buffer length of 100 stores 4 seconds of samples running at 25sps

  while(1)
  {
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);
      // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
      // Reads the echoPin, returns the sound wave travel time in microseconds
      duration = pulseIn(echoPin, HIGH);
      // Calculating the distance
      distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
    //dumping the first 25 sets of samples in the memory and shift the last 75 sets of samples to the top

    
    for (byte i = 15; i < 50; i++)
    {
      redBuffer[i - 15] = redBuffer[i];
      irBuffer[i - 15] = irBuffer[i];
    }

    //take 25 sets of samples before calculating the heart rate.
    for (byte i = 35; i < 50; i++)
    {
      while (particleSensor.available() == false) //do we have new data?
        particleSensor.check(); //Check the sensor for new data


      redBuffer[i] = particleSensor.getRed();
      irBuffer[i] = particleSensor.getIR();
      particleSensor.nextSample(); //We're finished with this sample so move to next sample
    }

      while (!Serial.available());
      comm = Serial.readString().toInt();
     
      Serial.println(distance);
      Serial.println(mlx.readObjectTempC());
      Serial.println(spo2);
    
      if (comm == 9)
      {
       digitalWrite(13, HIGH);
       delay(5000);
       digitalWrite(13, LOW);
      }


    maxim_heart_rate_and_oxygen_saturation(irBuffer, bufferLength, redBuffer, &spo2, &validSPO2, &heartRate, &validHeartRate);
  }
}
