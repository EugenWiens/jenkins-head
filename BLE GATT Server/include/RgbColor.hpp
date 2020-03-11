#pragma once

#include <Arduino.h>


class RgbColor {

public:
    RgbColor();

    void setRedValue( const uint32_t red);
    void setGreenValue( const uint32_t green);
    void setBlueValue( const uint32_t blue);
 
    uint32_t getRedValue() const;
    uint32_t getGreenValue() const;
    uint32_t getBlueValue() const;

private:
    uint32_t m_Red;
    uint32_t m_Green;
    uint32_t m_Blue;
};