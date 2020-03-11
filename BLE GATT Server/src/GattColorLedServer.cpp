#include "GattColorLedServer.hpp"

#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>


GattColorLedServer::GattColorLedServer(BLECharacteristicCallbacks& characteristicCallbackHandler)
    : m_ServiceUuid("3bea760b-ea72-44d6-a189-2c27766bdcc4"),
    m_CharacteristicCallbackHandler(characteristicCallbackHandler)
{
}

void GattColorLedServer::init()
{
    Serial.println("Starting BLE...");

    BLEDevice::init("Jenkins Head");
    BLEServer *pServer = BLEDevice::createServer();
    BLEService *pService = pServer->createService(m_ServiceUuid);

    initCharacteristic(pService, BLEUUID("2e252e00-2f8b-4326-91de-26742dda4aa7"), m_RgbValue.red,
                                 BLEUUID("2947adbf-b502-4d1d-a9a8-54d9b6b56039"), "red value (0-255)");
    initCharacteristic(pService, BLEUUID("6aeba5cd-4476-43b6-830b-021109ae6dea"), m_RgbValue.green,
                                 BLEUUID("9d317dcf-5987-4d8b-a9eb-a358172a600e"), "green value (0-255)");
    initCharacteristic(pService, BLEUUID("46f27bf3-5b1c-403e-bc20-90934a784e66"), m_RgbValue.blue,
                                 BLEUUID("eec3aa59-88fc-49cd-9926-7cdbba6f0cdb"), "blue value (0-255)");
    initCharacteristic(pService, BLEUUID("fc75589b-54ae-4b28-b54d-a35979f42b39"), m_BrightnessValue,
                                 BLEUUID("c09e62d1-5af9-4473-b40f-a3a0c698eef4"), "brigness value (0-255)");
    pService->start();

    initAdvertising();
    Serial.println("...BLE init complete");
}

void GattColorLedServer::initCharacteristic(BLEService * const pService,
                                            const BLEUUID& characteristicUuid,
                                            uint32_t characteristicValue,
                                            const BLEUUID& descriptorUuid,
                                            const std::string& descriptorString
                                            ) const
{
    BLECharacteristic *pCharacteristic = pService->createCharacteristic( characteristicUuid, BLECharacteristic::PROPERTY_WRITE | BLECharacteristic::PROPERTY_READ);

    pCharacteristic->setValue(characteristicValue);
    pCharacteristic->setCallbacks(&m_CharacteristicCallbackHandler); 

    BLEDescriptor* pDescriptor = new BLEDescriptor(descriptorUuid);
    pDescriptor->setValue(descriptorString);
    pCharacteristic->addDescriptor(pDescriptor);
}

void GattColorLedServer::initAdvertising() const
{
    BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
    pAdvertising->addServiceUUID(m_ServiceUuid);
    pAdvertising->setScanResponse(true);
    pAdvertising->setMinPreferred(0x06); // functions that help with iPhone connections issue
    pAdvertising->setMinPreferred(0x12);
    BLEDevice::startAdvertising();
}

 