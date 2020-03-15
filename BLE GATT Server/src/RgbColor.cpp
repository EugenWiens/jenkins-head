#include "RgbColor.hpp"

RgbColor::RgbColor()
 : m_Red(0), m_Green(0), m_Blue(0)
 {

 }

String RgbColor::toString() const
{
    return "{red:" + String(m_Red) + ", green:" + String(m_Green) + ", blue:" + String(m_Blue) + "}";
}