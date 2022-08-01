# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdline

"""
    ''_antdline(;kwargs...)

An AntdLine component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `connectNulls` (Bool; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `isStack` (Bool; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `lineStyle` (optional): . lineStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `point` (optional): . point has the following type: lists containing elements 'color', 'shape', 'style'.
Those elements have the following types:
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `shape` (optional): . shape has the following type: String | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `recentlyPointClickRecord` (optional): . recentlyPointClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Dict; optional)
- `recentlyTooltipChangeRecord` (optional): . recentlyTooltipChangeRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Array of Dicts; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `seriesField` (String; optional)
- `slider` (optional)
- `smooth` (Bool; optional)
- `stepType` (String; optional)
- `style` (Dict; optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (String; required)
"""
function ''_antdline(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :connectNulls, :data, :downloadTrigger, :height, :isStack, :key, :label, :legend, :lineStyle, :loading_state, :locale, :meta, :padding, :point, :recentlyPointClickRecord, :recentlyTooltipChangeRecord, :renderer, :seriesField, :slider, :smooth, :stepType, :style, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdline", "AntdLine", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

