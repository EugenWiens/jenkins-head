#pragma once

#include "ColorHanlderInterface.hpp"
#include "RgbColor.hpp"

#include <Arduino.h>
#include <Adafruit_NeoPixel.h>


class NeoPixelHandler : public ColorHandlerInterface
{
public:
    NeoPixelHandler();

    void init() const;
    virtual void setColor(const RgbColor& rgbColor, uint32_t brightness) const override;

private:
    mutable Adafruit_NeoPixel m_NeoPixel;

};