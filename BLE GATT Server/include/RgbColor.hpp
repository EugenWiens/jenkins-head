#pragma once

#include <Arduino.h>


class RgbColor {

public:
    uint32_t m_Red;
    uint32_t m_Green;
    uint32_t m_Blue;

    RgbColor();
    String toString() const;
};