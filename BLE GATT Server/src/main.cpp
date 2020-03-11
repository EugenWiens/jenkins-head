#include <Arduino.h>
#include "GattColorLedServer.hpp"

BLECharacteristicCallbacks characteristicCallbacks;
GattColorLedServer gattColorLedServer(characteristicCallbacks);

void setup() {
  Serial.begin(115200);

  gattColorLedServer.init();
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
}