# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdgauge

"""
    ''_antdgauge(;kwargs...)

An AntdGauge component.

Keyword arguments:
- `id` (String; optional)
- `animation` (Dict | Bool; optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `axis` (optional)
- `className` (String; optional)
- `downloadTrigger` (String; optional)
- `endAngle` (Real; optional)
- `gaugeStyle` (optional): . gaugeStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `height` (Real; optional)
- `indicator` (optional): . indicator has the following type: lists containing elements 'pointer', 'pin', 'shape'.
Those elements have the following types:
  - `pointer` (optional): . pointer has the following type: lists containing elements 'style'.
Those elements have the following types:
  - `style` (optional)
  - `pin` (optional): . pin has the following type: lists containing elements 'style'.
Those elements have the following types:
  - `style` (optional)
  - `shape` (a value equal to: 'default', 'cursor', 'ring-cursor', 'simple'; optional)
- `innerRadius` (Real; optional)
- `key` (String; optional)
- `limitInPlot` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meter` (optional): . meter has the following type: lists containing elements 'steps', 'stepRatio'.
Those elements have the following types:
  - `steps` (Real; optional)
  - `stepRatio` (Real; optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `percent` (Real; required)
- `radius` (Real; optional)
- `range` (optional): . range has the following type: lists containing elements 'ticks', 'color', 'width'.
Those elements have the following types:
  - `ticks` (Array of Reals; optional)
  - `color` (String | Array of Strings; optional)
  - `width` (Real; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `startAngle` (Real; optional)
- `statistic` (optional): . statistic has the following type: lists containing elements 'title', 'content', 'style'.
Those elements have the following types:
  - `title` (optional): . title has the following type: Bool | lists containing elements 'style', 'content', 'formatter', 'customHtml', 'rotate', 'offsetX', 'offsetY'.
Those elements have the following types:
  - `style` (Dict; optional)
  - `content` (String; optional)
  - `formatter` (optional): . formatter has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `customHtml` (optional): . customHtml has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `rotate` (Real; optional)
  - `offsetX` (Real; optional)
  - `offsetY` (Real; optional)
  - `content` (optional): . content has the following type: Bool | lists containing elements 'style', 'content', 'formatter', 'customHtml', 'rotate', 'offsetX', 'offsetY'.
Those elements have the following types:
  - `style` (Dict; optional)
  - `content` (String; optional)
  - `formatter` (optional): . formatter has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `customHtml` (optional): . customHtml has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `rotate` (Real; optional)
  - `offsetX` (Real; optional)
  - `offsetY` (Real; optional)
  - `style` (optional)
- `style` (Dict; optional)
- `theme` (optional)
- `type` (a value equal to: 'meter'; optional)
- `width` (Real; optional)
"""
function ''_antdgauge(; kwargs...)
        available_props = Symbol[:id, :animation, :appendPadding, :autoFit, :axis, :className, :downloadTrigger, :endAngle, :gaugeStyle, :height, :indicator, :innerRadius, :key, :limitInPlot, :loading_state, :locale, :meter, :padding, :percent, :radius, :range, :renderer, :startAngle, :statistic, :style, :theme, :type, :width]
        wild_props = Symbol[]
        return Component("''_antdgauge", "AntdGauge", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

