#include "GattColorLedServer.hpp"
#include "NeoPixelHandler.hpp"

#include <Arduino.h>

NeoPixelHandler neoPixelHandler;
GattColorLedServer gattColorLedServer(neoPixelHandler);

void setup() {
  Serial.begin(115200);

  gattColorLedServer.init();
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
}