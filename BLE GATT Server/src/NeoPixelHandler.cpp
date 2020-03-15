#include "NeoPixelHandler.hpp"

#include <Arduino.h>


NeoPixelHandler::NeoPixelHandler()
{
}

void NeoPixelHandler::writeRgbColor(const RgbColor& rgbColor) const
{

}

void NeoPixelHandler::setColor(const RgbColor& rgbColor, uint32_t brightness) const
{
    Serial.println("NeoPixelHandler::setColor " + rgbColor.toString() + " brightness: " + String(brightness));
}