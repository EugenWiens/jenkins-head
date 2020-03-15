#pragma once

#include "ColorHanlderInterface.hpp"
#include "RgbColor.hpp"

#include <BLEUUID.h>
#include <BLECharacteristic.h>



class GattColorLedServer : public BLECharacteristicCallbacks {

public:
    explicit GattColorLedServer(const ColorHandlerInterface& colorHandler);
    void init();

private: 
    BLEUUID m_ServiceUuid;
    BLEUUID m_CharacteristicRedUuid;
    BLEUUID m_CharacteristicGreenUuid;
    BLEUUID m_CharacteristicBlueUuid;
    BLEUUID m_CharacteristicBrightnessUuid;
    RgbColor m_RgbValue;
    uint32_t m_BrightnessValue;
    const ColorHandlerInterface& m_ColorHandler;

    void initCharacteristic(BLEService * const pService,
                            const BLEUUID& characteristicUuid,
                            uint32_t characteristicValue,
                            const BLEUUID& descriptorUuid,
                            const std::string& descriptorString
                           );
    void initAdvertising();
    uint32_t* operator[](BLEUUID& key);

    virtual void onRead(BLECharacteristic* pCharacteristic) override;
	virtual void onWrite(BLECharacteristic* pCharacteristic) override;

};