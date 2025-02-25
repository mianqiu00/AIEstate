# 北京市二手房数据分析

本项目旨在对北京市二手房挂牌数据进行分析，用于预测房价趋势和分析影响房价的因素

## 环境要求

* Python 3.9
* [Anaconda](https://www.anaconda.com/) 包含所有必要包
* [PyTorch](https://pytorch.org/) 版本 2.6.0
* 详情查看 [Environment](./env.yaml)

## 安装依赖

- 创建并激活虚拟环境（推荐使用 `conda` 或 `venv`）：

```bash
conda env create -f env.yaml
conda activate estate
```

## 运行项目

使用以下脚本运行项目：

```bash
./run.sh
```

后台运行

```bash
nohup ./run.sh > output.log 2>&1 &
```

# 许可证

本项目采用 MIT 许可证，允许在学术和非商业用途下自由使用、修改和分发代码。详细内容请参阅 [LICENSE](./LICENSE) 文件