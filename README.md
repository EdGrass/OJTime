# OJ-Time-Tool

---

**OJ-Time-Tool** 是一个命令行工具，用于快速查看主流在线评测平台 (OJ) 的近期比赛信息。

![OJ-Time-Tool](https://i.imgur.com/w98dgSs.png)

## ✨ 主要功能

自动获取以下平台的比赛信息：

- 🌟 **Codeforces** - 全球最大的算法竞赛平台
- 🎌 **AtCoder** - 日本最受欢迎的竞赛平台
- 🍴 **CodeChef** - 印度顶级算法竞赛平台
- 🐂 **牛客网** - 中国知名的竞赛平台

## 🚀 快速开始

### 环境要求

- Python 3.7+
- Chrome 浏览器（用于 Selenium）
- pip 包管理工具

### 安装步骤

1. **克隆仓库**  
   克隆本项目到本地：
   ```bash
   git clone https://github.com/yourusername/OJ-Time-Tool.git
   cd OJ-Time-Tool
   ```

2. **安装依赖包**  
   安装项目所需的 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. **配置快捷命令**（macOS/Linux）  
   将 `OJTimeTool.py` 脚本链接到系统路径，方便在终端直接使用：
   ```bash
   sudo ln -s $(pwd)/OJTImeTool.py /usr/local/bin/OJT
   chmod +x OJTImeTool.py
   ```

## 💻 使用方法

在终端中运行以下命令，即可查看各平台的近期比赛信息：

```bash
OJT
```

**输出内容**：
- 比赛名称
- 比赛开始时间
- 比赛时长


## ⚖️ 许可证

本项目采用 MIT 许可证，详细信息请参见 [LICENSE](LICENSE) 文件。

## 📮 联系方式

如有任何问题或建议，欢迎提交 Issue 或通过以下方式与我联系：

- GitHub Issues
- Email: 1213710430@qq.com

