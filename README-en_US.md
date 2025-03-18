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

[简体中文](./README.md) | English

A sub-project of the `feffery-components` plan, `Plotly Dash` third-party component library, based on `Antd Charts`, bringing common data visualization chart components into the `Dash` ecosystem 🥳, latest stable version: `0.1.5` (2025-02-04)

## Dash Version Compatibility

| fact version | Compatible Dash version |
| :-----: | :----------: |
| >=0.2.0 |   >=3.0.0    |
| <0.2.0  |    <3.0.0    |

## 1 Latest Version Installation

```bash
pip install feffery-antd-charts -U
```

## 2 Latest Pre-release Version Installation

> [!NOTE]  
> Latest pre-release version (2025-03-18): `0.2.0rc1`

```bash
pip install feffery-antd-charts --pre -U
```

## 3 Static Resource CDN Acceleration Method

```Python
# In non-debug mode, passing serve_locally=False to Dash() will force the browser to load
# static resources like xxx.min.js from unpkg cdn, avoiding server bandwidth usage,
# suitable for small to medium-sized sites to accelerate access
app = dash.Dash(serve_locally=False)
```

## 4 Online Documentation

[Documentation Link](https://fact.feffery.tech/)

## 5 Contributors

<a href = "https://github.com/CNFeffery/feffery-antd-charts/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=CNFeffery/feffery-antd-charts"/>
</a>