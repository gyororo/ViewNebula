# view-nebula

一个轻量级的边缘计算自动化扩展平台。

## 安装

确保环境已安装 Python 3.8+，通过以下命令安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

导入 `viewnebula` 模块并初始化边缘节点：

```python
from viewnebula import NebulaNode

# 初始化节点
node = NebulaNode(config="config.yaml")

# 启动自动扩展监控
node.start_autoscaling()
```

运行测试用例以验证功能：

```bash
python test_viewnebula.py
```

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。



