#include "NeoPixelHandler.hpp"

#include <Arduino.h>

namespace {
    uint16_t firstPixel = 5;
    uint16_t numberOfPixels = 3;
    uint16_t dataPinNumber = 12;
}

NeoPixelHandler::NeoPixelHandler()
  : m_NeoPixel(16, dataPinNumber, NEO_GRBW + NEO_KHZ800)
{
}

void NeoPixelHandler::init() const
{
    m_NeoPixel.begin();
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