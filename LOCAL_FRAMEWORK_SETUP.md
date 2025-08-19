# 本地Framework配置指南

## 概述
本指南说明如何在platform-unihiker中使用本地的framework-arduinoespressif32。

## 前提条件
1. 已下载本地的framework-arduinoespressif32
2. 本地framework包含完整的目录结构，特别是`package/package_esp32_index.template.json`文件

## 配置方法

### 方法一：修改platform.json（推荐）

1. 编辑`platform.json`文件
2. 找到`framework-arduinoespressif32`配置项
3. 将version改为本地路径：

```json
"framework-arduinoespressif32": {
  "type": "framework",
  "optional": true,
  "owner": "platformio",
  "version": "file:///C:/path/to/your/framework-arduinoespressif32"
}
```

**路径格式说明：**
- Windows: `file:///C:/path/to/framework-arduinoespressif32`
- Linux/macOS: `file:///path/to/framework-arduinoespressif32`

### 方法二：在项目中使用

在您的项目`platformio.ini`文件中：

```ini
[env:unihiker]
platform = file:///G:/platform-unihiker
framework = arduino
board = your-unihiker-board

; 指定本地framework路径
board_build.arduino.package_index_url = file:///C:/path/to/your/framework-arduinoespressif32/package/package_esp32_index.template.json
```

## 验证配置

1. 确保本地framework目录结构正确：
```
framework-arduinoespressif32/
├── package/
│   └── package_esp32_index.template.json
├── cores/
├── libraries/
├── tools/
└── variants/
```

2. 运行构建命令验证：
```bash
pio run -e unihiker
```

## 故障排除

### 问题1：找不到本地framework
**解决方案：**
- 检查路径是否正确
- 确保路径使用正确的格式（Windows需要`file:///C:/`格式）
- 验证framework目录是否存在

### 问题2：找不到package_esp32_index.template.json
**解决方案：**
- 确保下载的framework是完整的
- 检查`package/`目录是否存在
- 重新下载framework

### 问题3：工具链版本不匹配
**解决方案：**
- 检查本地framework的`package_esp32_index.template.json`中的工具链版本
- 确保platform.json中的工具链版本兼容

## 示例配置

### Windows示例
```json
"framework-arduinoespressif32": {
  "type": "framework",
  "optional": true,
  "owner": "platformio",
  "version": "file:///D:/esp32/arduino-esp32"
}
```

### Linux/macOS示例
```json
"framework-arduinoespressif32": {
  "type": "framework",
  "optional": true,
  "owner": "platformio",
  "version": "file:///home/user/esp32/arduino-esp32"
}
```

## 注意事项

1. **路径格式**：必须使用`file:///`协议
2. **目录结构**：本地framework必须包含完整的目录结构
3. **版本兼容性**：确保本地framework版本与platform兼容
4. **工具链**：本地framework会自动配置相应的工具链版本

## 回退到远程版本

如果需要回退到使用远程版本，只需将version改回：
```json
"version": "~3.20017.0"
```
