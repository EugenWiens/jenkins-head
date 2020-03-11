#include "RgbColor.hpp"


RgbColor::RgbColor()
 : m_Red(0), m_Green(0), m_Blue(0)
{
}

void RgbColor::setRedValue( const uint32_t red)
{
    m_Red = red;
}

void RgbColor::setGreenValue( const uint32_t green)
{
    m_Green = green;
}

void RgbColor::setBlueValue( const uint32_t blue)
{
    m_Blue = blue;
}

uint32_t RgbColor::getRedValue() const
{
    return m_Red;
}

uint32_t RgbColor::getGreenValue() const
{
    return m_Green;
}

uint32_t RgbColor::getBlueValue() const
{
    return m_Blue;
}
