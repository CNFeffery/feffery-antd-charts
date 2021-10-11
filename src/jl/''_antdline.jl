# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdline

"""
    ''_antdline(;kwargs...)

An AntdLine component.

Keyword arguments:
- `id` (String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `connectNulls` (Bool; optional)
- `data` (Array of Dicts; required)
- `height` (Real; optional)
- `isStack` (Bool; optional)
- `legend` (optional): . legend has the following type: lists containing elements 'position', 'layout', 'offsetX', 'offsetY', 'background', 'flipPage', 'maxWidth', 'maxHeight', 'reversed', 'itemHeight', 'itemWidth', 'itemName', 'itemValue', 'itemSpacing', 'selected'.
Those elements have the following types:
  - `position` (String; optional)
  - `layout` (String; optional)
  - `offsetX` (Real; optional)
  - `offsetY` (Real; optional)
  - `background` (optional): . background has the following type: lists containing elements 'padding'.
Those elements have the following types:
  - `padding` (Real | Array of Reals; optional)
  - `flipPage` (Bool; optional)
  - `maxWidth` (Real; optional)
  - `maxHeight` (Real; optional)
  - `reversed` (Bool; optional)
  - `itemHeight` (Real; optional)
  - `itemWidth` (Real; optional)
  - `itemName` (optional): . itemName has the following type: lists containing elements 'spacing'.
Those elements have the following types:
  - `spacing` (Real; optional)
  - `itemValue` (optional): . itemValue has the following type: lists containing elements 'alignRight'.
Those elements have the following types:
  - `alignRight` (Bool; optional)
  - `itemSpacing` (Real; optional)
  - `selected` (Dict; optional) | Bool
- `lineStyle` (optional): . lineStyle has the following type: String | lists containing elements 'lineWidth', 'lineDash', 'lineOpacity', 'shadowColor', 'shadowBlur', 'shadowOffsetX', 'shadowOffsetY', 'cursor'.
Those elements have the following types:
  - `lineWidth` (Real; optional)
  - `lineDash` (Array of Reals; optional)
  - `lineOpacity` (Real; optional)
  - `shadowColor` (String; optional)
  - `shadowBlur` (Real; optional)
  - `shadowOffsetX` (Real; optional)
  - `shadowOffsetY` (Real; optional)
  - `cursor` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (String; optional)
- `padding` (Real | Array of Reals; optional)
- `point` (optional): . point has the following type: lists containing elements 'color', 'shape', 'style'.
Those elements have the following types:
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `shape` (optional): . shape has the following type: String | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func', 'r', 'fill', 'fillOpacity', 'stroke', 'lineWidth', 'lineDash', 'strokeOpacity', 'cursor'.
Those elements have the following types:
  - `func` (String; optional)
  - `r` (Real; optional)
  - `fill` (String; optional)
  - `fillOpacity` (Real; optional)
  - `stroke` (String; optional)
  - `lineWidth` (Real; optional)
  - `lineDash` (Array of Reals; optional)
  - `strokeOpacity` (Real; optional)
  - `cursor` (String; optional)
- `renderer` (String; optional)
- `seriesField` (String; optional)
- `smooth` (Bool; optional)
- `stepType` (String; optional)
- `style` (Dict; optional)
- `tooltip` (optional): . tooltip has the following type: lists containing elements 'fields', 'follow', 'enterable', 'showTitle', 'title', 'position'.
Those elements have the following types:
  - `fields` (Array of Strings; optional)
  - `follow` (Bool; optional)
  - `enterable` (Bool; optional)
  - `showTitle` (Bool; optional)
  - `title` (String; optional)
  - `position` (String; optional)
- `width` (Real; optional)
- `xField` (String; required)
- `yField` (String; required)
"""
function ''_antdline(; kwargs...)
        available_props = Symbol[:id, :autoFit, :className, :color, :connectNulls, :data, :height, :isStack, :legend, :lineStyle, :loading_state, :locale, :padding, :point, :renderer, :seriesField, :smooth, :stepType, :style, :tooltip, :width, :xField, :yField]
        wild_props = Symbol[]
        return Component("''_antdline", "AntdLine", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

