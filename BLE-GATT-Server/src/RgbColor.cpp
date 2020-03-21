#include "RgbColor.hpp"

RgbColor::RgbColor()
    : m_Red(0), m_Green(0), m_Blue(0)
 {
 }

 RgbColor::RgbColor(uint32_t red, uint32_t green, uint32_t blue)
    : m_Red(red), m_Green(green), m_Blue(blue)
 {

 }

String RgbColor::toString() const
{
    return "{red:" + String(m_Red) + ", green:" + String(m_Green) + ", blue:" + String(m_Blue) + "}";
}

uint32_t RgbColor::getRgbValueAsInt() const
{
    return ((uint32_t)m_Red << 16) | ((uint32_t)m_Green <<  8) | m_Blue;
}