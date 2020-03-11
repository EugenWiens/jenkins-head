#include <BLEUUID.h>
#include <BLECharacteristic.h>


class GattColorLedServer {

public:
    struct RgbColor {
        uint32_t red;
        uint32_t green;
        uint32_t blue;

        RgbColor() : red(0), green(0), blue(0) {}
    };

    explicit GattColorLedServer(BLECharacteristicCallbacks& characteristicCallbackHandler);
    void init();

private: 
    BLEUUID m_ServiceUuid;
    RgbColor m_RgbValue;
    uint32_t m_BrightnessValue;
    BLECharacteristicCallbacks& m_CharacteristicCallbackHandler;

    void initCharacteristic(BLEService * const pService,
                            const BLEUUID& characteristicUuid,
                            uint32_t characteristicValue,
                            const BLEUUID& descriptorUuid,
                            const std::string& descriptorString
                           ) const;
    void initAdvertising() const;
};