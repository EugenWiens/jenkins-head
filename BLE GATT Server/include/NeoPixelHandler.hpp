#pragma once

#include "ColorHanlderInterface.hpp"
#include "RgbColor.hpp"

#include <Arduino.h>


class NeoPixelHandler : public ColorHandlerInterface
{
public:
    NeoPixelHandler();

    void writeRgbColor(const RgbColor& rgbColor) const;

    virtual void setColor(const RgbColor& rgbColor, uint32_t brightness) const override;
};