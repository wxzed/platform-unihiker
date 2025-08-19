#!/usr/bin/env python3
"""
UNIHIKER Blink 项目快速启动脚本
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def run_command(cmd, cwd=None, show_output=True):
    """运行命令"""
    try:
        if show_output:
            print(f"🔄 执行: {cmd}")
            result = subprocess.run(cmd, shell=True, cwd=cwd)
            return result.returncode == 0
        else:
            result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        print(f"❌ 执行失败: {e}")
        return False

def check_platformio():
    """检查PlatformIO是否安装"""
    print("🔍 检查PlatformIO...")
    success, stdout, stderr = run_command("pio --version", show_output=False)
    if success:
        print("✅ PlatformIO 已安装")
        return True
    else:
        print("❌ PlatformIO 未安装，请先安装PlatformIO")
        print("安装命令: pip install platformio")
        return False

def build_project():
    """构建项目"""
    print("\n🔨 构建项目...")
    project_dir = Path(__file__).parent
    success = run_command("pio run", cwd=project_dir)
    if success:
        print("✅ 构建成功")
        return True
    else:
        print("❌ 构建失败")
        return False

def upload_project():
    """上传项目"""
    print("\n📤 上传项目...")
    project_dir = Path(__file__).parent
    success = run_command("pio run --target upload", cwd=project_dir)
    if success:
        print("✅ 上传成功")
        return True
    else:
        print("❌ 上传失败")
        return False

def monitor_serial():
    """监控串口"""
    print("\n📺 启动串口监控...")
    print("按 Ctrl+C 退出监控")
    project_dir = Path(__file__).parent
    try:
        run_command("pio device monitor", cwd=project_dir)
    except KeyboardInterrupt:
        print("\n👋 监控已停止")

def show_menu():
    """显示菜单"""
    print("\n" + "=" * 50)
    print("🚀 UNIHIKER Blink 项目控制面板")
    print("=" * 50)
    print("1. 🔨 构建项目")
    print("2. 📤 上传项目")
    print("3. 📺 监控串口")
    print("4. 🔄 构建并上传")
    print("5. 🎯 完整流程（构建+上传+监控）")
    print("6. 🧪 运行测试")
    print("0. 🚪 退出")
    print("=" * 50)

def run_tests():
    """运行测试"""
    print("\n🧪 运行测试...")
    test_script = Path(__file__).parent / "test" / "test_blink.py"
    if test_script.exists():
        success = run_command(f"python {test_script}", cwd=Path(__file__).parent)
        return success
    else:
        print("❌ 测试脚本不存在")
        return False

def main():
    """主函数"""
    print("🎉 欢迎使用 UNIHIKER Blink 项目！")
    
    # 检查PlatformIO
    if not check_platformio():
        return
    
    while True:
        show_menu()
        choice = input("请选择操作 (0-6): ").strip()
        
        if choice == "0":
            print("👋 再见！")
            break
        elif choice == "1":
            build_project()
        elif choice == "2":
            upload_project()
        elif choice == "3":
            monitor_serial()
        elif choice == "4":
            if build_project():
                upload_project()
        elif choice == "5":
            if build_project():
                if upload_project():
                    print("\n⏳ 等待3秒后启动监控...")
                    time.sleep(3)
                    monitor_serial()
        elif choice == "6":
            run_tests()
        else:
            print("❌ 无效选择，请重新输入")
        
        input("\n按回车键继续...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 程序已退出")
