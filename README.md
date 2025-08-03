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

简体中文 | [English](./README-en_US.md)

`feffery-components`计划子项目，`Plotly Dash`第三方组件库，基于`Antd Charts`，将常见的各类数据可视化图表组件引入`Dash`的生态中🥳，最新稳定版本：`0.2.1`（2025-08-03）

## Dash版本兼容性说明

| fact版本 | 适用Dash版本 |
| :-----: | :----------: |
| >=0.2.0 |   >=3.0.0    |
| <0.2.0  |    <3.0.0    |

## 1 最新版本安装方式

```bash
pip install feffery-antd-charts -U
```

## 2 最新预发布版本安装方式

> [!NOTE]  
> 最新预发布版本（2025-07-04）：`0.2.0rc5`

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

[文档地址](https://fact.feffery.tech/)

## 5 贡献者

<a href = "https://github.com/CNFeffery/feffery-antd-charts/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=CNFeffery/feffery-antd-charts"/>
</a>

## 6 更多应用开发教程

> 微信公众号「玩转 Dash」，欢迎扫码关注 👇

<p align="center" >
  <img src="./imgs/公众号.png" height=220 />
</p>

> 「玩转 Dash」知识星球，海量教程案例模板资源，专业的答疑咨询服务，欢迎扫码加入 👇

<p align="center" >
  <img src="./imgs/知识星球.jpg" height=220 />
</p>
