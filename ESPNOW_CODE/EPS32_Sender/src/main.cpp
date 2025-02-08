#include <esp_now.h>
#include <WiFi.h>

hw_timer_t *timer = NULL;
volatile bool sendFlag = false;

uint8_t broadcastAddress[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF}; // Broadcast

typedef struct struct_message {
    char message[32];
} struct_message;

struct_message myData;

void IRAM_ATTR onTimer() {
    sendFlag = true;
}

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
    Serial.print("Last Packet Send Status: ");
    Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);

    if (esp_now_init() != ESP_OK) {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    esp_now_register_send_cb(OnDataSent);

    esp_now_peer_info_t peerInfo = {};
    memcpy(peerInfo.peer_addr, broadcastAddress, 6);
    peerInfo.channel = 0;
    peerInfo.encrypt = false;

    if (esp_now_add_peer(&peerInfo) != ESP_OK) {
        Serial.println("Failed to add peer");
        return;
    }

    // Initialize timer interrupt (100ms)
    timer = timerBegin(0, 80, true);  // Timer 0, prescaler 80 (1 tick = 1µs)
    timerAttachInterrupt(timer, &onTimer, true);
    timerAlarmWrite(timer, 1000 , true);  //ตรงนี้เอาไว้ตั้งเวลาเด้อวัยรุ่น
    timerAlarmEnable(timer);
}

void loop() {
    if (sendFlag) {
        sendFlag = false;
        strcpy(myData.message, "Hello, ESP-NOW!");
        esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *)&myData, sizeof(myData));

        if (result == ESP_OK) {
            Serial.println("Sent with success");
        } else {
            Serial.println("Error sending the data");
        }
    }
}
