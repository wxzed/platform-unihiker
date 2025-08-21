# UNIHIKER: development platform for [PlatformIO](https://platformio.org)

[![Build Status](https://github.com/wxzed/platform-unihiker/workflows/Examples/badge.svg)](https://github.com/wxzed/platform-unihiker/actions)

UNIHIKER是基于ESP32-S3微控制器的智能开发平台，专为DFRobot UNIHIKER K10开发板设计。该平台集成了AI识别、语音交互、图形显示等先进功能，为教育、创客和物联网项目提供强大的开发环境。

## 平台特性

- **AI人工智能**: 内置人脸识别、语音识别等AI功能
- **图形显示**: 2.8寸彩色触摸屏，支持图形绘制和交互
- **传感器集成**: 加速度计、陀螺仪等多种传感器
- **语音交互**: 支持中文语音识别和语音合成
- **Wi-Fi和蓝牙**: 内置无线连接功能
- **教育友好**: 专为学习和原型设计优化
- **开源**: 基于Apache-2.0许可证

## 支持的开发板

### UNIHIKER K10
- **处理器**: ESP32-S3 (240MHz)
- **内存**: 16MB Flash, 8MB PSRAM
- **显示**: 2.8寸彩色触摸屏 (240x320分辨率)
- **摄像头**: 200万像素摄像头
- **传感器**: 6轴IMU (加速度计+陀螺仪)
- **连接**: Wi-Fi 802.11 b/g/n, Bluetooth 5.0
- **USB**: Type-C接口，支持USB设备模式
- **扩展**: 丰富的GPIO接口和I2C/SPI总线

## 使用示例

以下是一个简单的LED闪烁示例，展示如何使用UNIHIKER平台：

```cpp
#include "unihiker_k10.h"

UNIHIKER_K10 k10;
uint8_t screen_dir = 2;

void setup() {
    k10.begin();
    k10.initScreen(screen_dir);
    k10.creatCanvas();
    k10.setScreenBackground(0xFFFFFF);
}

void loop() {
    // 在屏幕上绘制一个绿色圆点
    k10.canvas->canvasCircle(120, 160, 10, 0x00FF00, 0x00FF00, true);
    k10.canvas->updateCanvas();
    delay(1000);
    
    // 清除圆点
    k10.canvas->canvasCircle(120, 160, 10, 0xFFFFFF, 0xFFFFFF, true);
    k10.canvas->updateCanvas();
    delay(1000);
}
```

## 使用方法

### 1. 安装PlatformIO

首先安装PlatformIO IDE或CLI：
- [PlatformIO IDE](https://platformio.org/install/ide?install=vscode)
- [PlatformIO Core](https://docs.platformio.org/en/latest/core/installation/index.html)

### 2. 创建项目

在`platformio.ini`文件中配置平台：

```ini
[env:unihiker]
platform = https://github.com/wxzed/platform-unihiker.git
board = unihiker_k10
framework = arduino
build_flags = 
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
    -DModel=None
```

### 3. 编译和上传

```bash
# 编译项目
pio run

# 上传到开发板
pio run --target upload

# 监控串口输出
pio device monitor
```

## 快速开始

### 1. 克隆平台

```bash
git clone https://github.com/wxzed/platform-unihiker.git
cd platform-unihiker
```

### 2. 创建项目

创建一个新的PlatformIO项目，并在`platformio.ini`中配置：

```ini
[env:unihiker]
platform = https://github.com/wxzed/platform-unihiker.git
board = unihiker_k10
framework = arduino
build_flags = 
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
    -DModel=None
```

### 3. 编写代码

参考上面的使用示例，编写您的第一个UNIHIKER程序。

## 核心功能

### AI识别功能
- **人脸检测**: 实时检测人脸位置和尺寸
- **物体识别**: 支持多种物体识别
- **手势识别**: 识别手势动作

### 语音交互
- **语音唤醒**: 支持自定义唤醒词
- **命令识别**: 识别语音控制命令
- **语音合成**: 提供语音反馈

### 图形显示
- **图形绘制**: 支持线条、圆形、矩形等基本图形
- **文字显示**: 支持中英文文字显示
- **触摸交互**: 支持触摸屏交互

### 传感器支持
- **加速度计**: 检测设备倾斜和运动
- **陀螺仪**: 检测设备旋转
- **环境传感器**: 支持温湿度等传感器

## 开发环境

### 支持的框架
- **Arduino**: 简单易用的开发框架
- **ESP-IDF**: 功能强大的原生开发框架

### 开发工具
- **PlatformIO**: 推荐的开发环境
- **Arduino IDE**: 传统开发环境
- **VS Code**: 现代化编辑器

## 故障排除

### 常见问题

1. **上传失败**
   - 检查USB连接
   - 确认开发板选择正确
   - 尝试降低上传速度

2. **AI功能异常**
   - 确保摄像头连接正常
   - 检查环境光线条件
   - 验证模型文件完整性

3. **语音识别问题**
   - 检查麦克风连接
   - 确保环境噪音较低
   - 验证语音模型设置

4. **显示异常**
   - 检查屏幕连接
   - 确认显示方向设置
   - 验证图形库版本

### 获取帮助

- [PlatformIO文档](https://docs.platformio.org/)
- [ESP32官方文档](https://docs.espressif.com/projects/esp-idf/)
- [UNIHIKER产品页面](https://www.unihiker.com.cn)
- [DFRobot官网](https://www.dfrobot.com/)

## 贡献

欢迎提交Issue和Pull Request来改进这个平台！

## 许可证

本项目基于Apache-2.0许可证开源。

## 相关链接

- [PlatformIO Registry](https://registry.platformio.org/platforms/platformio/unihiker)
- [GitHub仓库](https://github.com/wxzed/platform-unihiker)
- [UNIHIKER官网](https://www.unihiker.com.cn)
- [DFRobot官网](https://www.dfrobot.com/)
