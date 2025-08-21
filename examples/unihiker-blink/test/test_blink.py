#!/usr/bin/env python3
"""
UNIHIKER Blink 项目测试脚本
用于验证项目配置和基本功能
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            cwd=cwd,
            capture_output=True, 
            text=True,
            timeout=60
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)

def test_project_structure():
    """测试项目结构"""
    print("🔍 检查项目结构...")
    
    project_dir = Path(__file__).parent.parent
    required_files = [
        "platformio.ini",
        "src/main.cpp",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not (project_dir / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ 缺少文件: {missing_files}")
        return False
    else:
        print("✅ 项目结构完整")
        return True

def test_platformio_config():
    """测试PlatformIO配置"""
    print("🔍 检查PlatformIO配置...")
    
    project_dir = Path(__file__).parent.parent
    config_file = project_dir / "platformio.ini"
    
    if not config_file.exists():
        print("❌ platformio.ini 文件不存在")
        return False
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_configs = [
        "platform = file:///D:/PlatformIO/platforms/unihiker",
        "framework = arduino",
        "board = unihiker_k10",
        "LED_BUILTIN=2"
    ]
    
    missing_configs = []
    for config in required_configs:
        if config not in content:
            missing_configs.append(config)
    
    if missing_configs:
        print(f"❌ 缺少配置: {missing_configs}")
        return False
    else:
        print("✅ PlatformIO配置正确")
        return True

def test_compile():
    """测试编译"""
    print("🔍 测试编译...")
    
    project_dir = Path(__file__).parent.parent
    
    success, stdout, stderr = run_command("pio run", cwd=project_dir)
    
    if success:
        print("✅ 编译成功")
        return True
    else:
        print("❌ 编译失败")
        print("错误信息:")
        print(stderr)
        return False

def main():
    """主测试函数"""
    print("🚀 开始测试 UNIHIKER Blink 项目...")
    print("=" * 50)
    
    tests = [
        ("项目结构", test_project_structure),
        ("PlatformIO配置", test_platformio_config),
        ("编译测试", test_compile),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} 失败")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！项目配置正确。")
        print("\n📝 下一步:")
        print("1. 连接您的UNIHIKER开发板")
        print("2. 运行: pio run --target upload")
        print("3. 运行: pio device monitor")
        return True
    else:
        print("⚠️  部分测试失败，请检查配置。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
