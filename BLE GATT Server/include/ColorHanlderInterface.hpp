#pragma once

#include <RgbColor.hpp>
#include <Arduino.h>


class ColorHandlerInterface
{
public:
    virtual void setColor(const RgbColor& rgbColor, uint32_t brightness) const = 0;
};
