# UNIHIKER ESP32 Blink Example

这是一个简单的LED闪烁示例项目，用于测试UNIHIKER开发板的基本功能。

## 项目结构

```
unihiker-blink/
├── platformio.ini    # 项目配置文件
├── src/
│   └── main.cpp      # 主程序文件
└── README.md         # 项目说明
```

## 功能说明

- LED以1秒间隔闪烁（亮1秒，灭1秒）
- 通过串口输出状态信息
- 使用GPIO2作为LED控制引脚

## 硬件要求

- UNIHIKER ESP32开发板
- USB数据线
- 板载LED（连接到GPIO2）

## 使用方法

### 1. 编译项目
```bash
cd examples/unihiker-blink
pio run
```

### 2. 上传程序
```bash
pio run --target upload
```

### 3. 监控串口输出
```bash
pio device monitor
```

## 配置说明

### platformio.ini 配置

- `platform = file:///G:/platform-unihiker` - 使用本地platform
- `board = esp32dev` - 使用ESP32开发板配置
- `LED_BUILTIN = 2` - 定义LED引脚为GPIO2
- `UNIHIKER_BOARD = 1` - 标识为UNIHIKER开发板

### 如果需要使用本地framework

取消注释并修改以下行：
```ini
board_build.arduino.package_index_url = file:///path/to/your/framework-arduinoespressif32/package/package_esp32_index.template.json
```

## 预期输出

程序运行后，您应该看到：
1. LED开始闪烁
2. 串口输出类似以下信息：
```
UNIHIKER ESP32 Blink Example Starting...
LED pin configured as OUTPUT
Blink pattern: ON for 1s, OFF for 1s
LED ON
LED OFF
LED ON
LED OFF
...
```

## 故障排除

1. **LED不闪烁**：检查LED是否连接到正确的引脚
2. **串口无输出**：检查串口连接和波特率设置
3. **编译错误**：确保platform路径正确
4. **上传失败**：检查USB连接和开发板选择

## 修改LED引脚

如果需要使用其他引脚，修改`platformio.ini`中的`LED_BUILTIN`定义：

```ini
build_flags = 
    -D LED_BUILTIN=5  # 改为GPIO5
    -D UNIHIKER_BOARD=1
```
