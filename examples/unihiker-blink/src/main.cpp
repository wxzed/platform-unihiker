/*
 * UNIHIKER ESP32 Blink Example
 * 
 * 这是一个简单的LED闪烁程序，用于测试UNIHIKER开发板
 * LED_BUILTIN 默认连接到GPIO2
 */

#include <Arduino.h>

// LED引脚定义
const int ledPin = LED_BUILTIN;  // 默认GPIO2

void setup() {
  // 初始化串口通信
  Serial.begin(115200);
  Serial.println("UNIHIKER ESP32 Blink Example Starting...");
  
  // 配置LED引脚为输出
  pinMode(ledPin, OUTPUT);
  
  Serial.println("LED pin configured as OUTPUT");
  Serial.println("Blink pattern: ON for 1s, OFF for 1s");
}

void loop() {
  // 点亮LED
  digitalWrite(ledPin, HIGH);
  Serial.println("LED ON");
  delay(1000);
  
  // 熄灭LED
  digitalWrite(ledPin, LOW);
  Serial.println("LED OFF");
  delay(1000);
}
