#include "NeoPixelHandler.hpp"

#include <Arduino.h>

namespace {
    uint16_t firstPixel = 5;
    uint16_t numberOfPixels = 3;
    uint16_t dataPinNumber = 12;
}

NeoPixelHandler::NeoPixelHandler()
  : m_NeoPixel(firstPixel + numberOfPixels, dataPinNumber, NEO_GRBW + NEO_KHZ400)
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

    
    for (uint16_t index=firstPixel; index < m_NeoPixel.numPixels(); ++index)
    {
        m_NeoPixel.setPixelColor(index, rgbColor.getRgbValueAsInt());
    }
    m_NeoPixel.show(); 
}