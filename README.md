<p align="center">
	<img src="./fact-logo.svg" height=300></img>
</p>
<h1 align="center">feffery-antd-charts</h1>
<div align="center">

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/feffery-antd-charts/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-antd-charts.svg?color=dark-green)](https://pypi.org/project/feffery-antd-charts/)
[![Downloads](https://static.pepy.tech/badge/feffery-antd-charts)](https://pepy.tech/project/feffery-antd-charts)
[![Downloads](https://static.pepy.tech/badge/feffery-antd-charts/month)](https://pepy.tech/project/feffery-antd-charts)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/CNFeffery/feffery-antd-charts.svg)](http://isitmaintained.com/project/CNFeffery/feffery-antd-charts "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/CNFeffery/feffery-antd-charts.svg)](http://isitmaintained.com/project/CNFeffery/feffery-antd-charts "Percentage of issues still open")

</div>

`feffery-components`计划子项目，`Plotly Dash`第三方组件库，基于`Antd Charts`，将常见的各类数据可视化图表组件引入`Dash`的生态中🥳，最新稳定版本：`0.1.0`（2025-01-06）

## 1 最新版本安装方式

```bash
pip install feffery-antd-charts -U
```

## 2 最新预发布版本安装方式

> [!NOTE]  
> 最新预发布版本（2024-11-04）：`0.1.0rc8`

```bash
pip install feffery-antd-charts --pre -U
```

## 3 静态资源 CDN 加速方法

```Python
# 非debug模式下对Dash()传入参数serve_locally=False会强制浏览器端从unpkg cdn加载各个依赖的
# xxx.min.js等静态资源，从而避免占用服务器带宽，适合中小型站点加速访问
app = dash.Dash(serve_locally=False)
```

## 4 在线文档

> 建设中，敬请期待

## 5 贡献者

<a href = "https://github.com/CNFeffery/feffery-antd-charts/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=CNFeffery/feffery-antd-charts"/>
</a>
