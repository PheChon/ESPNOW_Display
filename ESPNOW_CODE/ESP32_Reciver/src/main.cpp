#include <esp_now.h>
#include <WiFi.h>

typedef struct struct_message {
    float speed;
    float rpm;
    float fuel;
    float temp;
} struct_message;

struct_message myData;

void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len) {
    memcpy(&myData, incomingData, sizeof(myData));

    // Print received data to the serial monitor
    Serial.print("Received Speed: ");
    Serial.println(myData.speed);
    Serial.print("Received RPM: ");
    Serial.println(myData.rpm);
    Serial.print("Received Fuel: ");
    Serial.println(myData.fuel);
    Serial.print("Received Temp: ");
    Serial.println(myData.temp);
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);

    if (esp_now_init() != ESP_OK) {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
    // Nothing to do here, everything is handled in the callback
}
