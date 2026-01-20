# 安装第三方库（pip / venv / uv / pipx）

本节是“操作指南”，不包含可运行代码。建议始终在虚拟环境里安装依赖，避免污染系统 Python。

## 1) 使用 venv 创建隔离环境

```bash
# 创建虚拟环境（目录名可自定义）
python3 -m venv .venv

# 激活（macOS/Linux）
source .venv/bin/activate
# 或在 Windows (cmd)
.venv\Scripts\activate

# 退出
deactivate
```

## 2) pip 安装/卸载/查看

```bash
# 升级 pip（建议）
python -m pip install --upgrade pip

# 安装单个包
pip install requests

# 安装指定版本
pip install "pydantic==2.8.0"

# 卸载
pip uninstall requests

# 查看已安装包
pip list
```

国内环境可使用镜像（示例：清华）：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
```

## 3) 更快的安装器：uv

[`uv`](https://github.com/astral-sh/uv) 是 Rust 实现的快速包管理工具，命令兼容 pip：

```bash
# 安装 uv（使用 pipx 或 pip 安装）
pip install uv
# 或：pipx install uv

# 创建虚拟环境
uv venv .venv
source .venv/bin/activate

# 安装依赖（与 pip 类似）
uv pip install requests

# 从 requirements.txt 安装
uv pip install -r requirements.txt
```

## 4) pipx：隔离安装 CLI 工具

`pipx` 适合把命令行工具（如 `httpie`、`uvicorn`）安装到隔离环境，并自动链接到全局 PATH。

```bash
python -m pip install --user pipx
python -m pipx ensurepath  # 让 PATH 生效

pipx install httpie
http --version
```

## 5) requirements/constraints 用法

- 记录依赖：`pip freeze > requirements.txt`
- 安装：`pip install -r requirements.txt`
- 约束版本：使用 `-c constraints.txt`（约束文件只限定版本，不决定安装内容）
- 可编辑安装（本地开发）：在项目根运行 `pip install -e .`（需项目有 `pyproject.toml` 或 `setup.py`）

## 6) 常见问题排查

- **权限不足**：优先使用虚拟环境或 `--user`；不要轻易 `sudo pip install`。
- **版本冲突**：使用 `pip install --upgrade` 或清理旧包；必要时重建虚拟环境。
- **网络受限**：配置镜像源；离线环境可用 `pip download` 先下载再安装。
- **Python 版本不匹配**：查看包的 `Requires-Python`；使用合适版本的解释器或新建 venv。
