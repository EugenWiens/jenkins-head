#pragma once

#include <Arduino.h>


class RgbColor {

public:
    uint32_t m_Red;
    uint32_t m_Green;
    uint32_t m_Blue;

    RgbColor();
    RgbColor(uint32_t red, uint32_t green, uint32_t blue);
    String toString() const;
    uint32_t getRgbValueAsInt() const;
};