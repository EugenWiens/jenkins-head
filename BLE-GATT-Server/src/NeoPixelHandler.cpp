#include "NeoPixelHandler.hpp"

#include <Arduino.h>

namespace {
    uint16_t firstPixel = 0;
    uint16_t numberOfPixels = 7;
    uint16_t dataPinNumber = 16;
}

NeoPixelHandler::NeoPixelHandler()
  : m_NeoPixel(numberOfPixels, dataPinNumber, NEO_GRB + NEO_KHZ800)
{
}

void NeoPixelHandler::init() const
{
    m_NeoPixel.begin();
    m_NeoPixel.clear();
} 

void NeoPixelHandler::setColor(const RgbColor& rgbColor, uint32_t brightness) const
{
    Serial.println("NeoPixelHandler::setColor " + rgbColor.toString() + " brightness: " + String(brightness));
    m_NeoPixel.clear();
    
    for (uint16_t index=firstPixel; index < firstPixel + numberOfPixels; ++index)
    {
        m_NeoPixel.setPixelColor(index, rgbColor.getRgbValueAsInt());
        m_NeoPixel.show(); 
    }
}