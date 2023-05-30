# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdradar

"""
    ''_antdradar(;kwargs...)

An AntdRadar component.

Keyword arguments:
- `id` (String; optional)
- `animation` (Dict | Bool; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `area` (optional): . area has the following type: lists containing elements 'smooth', 'color', 'style'.
Those elements have the following types:
  - `smooth` (Bool; optional)
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `endAngle` (Real; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `limitInPlot` (Bool; optional)
- `lineStyle` (optional): . lineStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (String; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | String; optional)
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
- `radius` (Real; optional)
- `recentlyAreaClickRecord` (optional): . recentlyAreaClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Bool | Real | String | Dict | Array; optional)
- `recentlyLegendInfo` (optional): . recentlyLegendInfo has the following type: lists containing elements 'triggerItemName', 'items'.
Those elements have the following types:
  - `triggerItemName` (Bool | Real | String | Dict | Array; optional)
  - `items` (Array of Dicts; optional)
- `recentlyTooltipChangeRecord` (optional): . recentlyTooltipChangeRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Array of Dicts; optional)
- `renderer` (String; optional)
- `seriesField` (String; optional)
- `smooth` (Bool; optional)
- `startAngle` (Real; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (String; required)
"""
function ''_antdradar(; kwargs...)
        available_props = Symbol[:id, :animation, :annotations, :appendPadding, :area, :autoFit, :className, :color, :data, :downloadTrigger, :endAngle, :height, :key, :label, :legend, :limitInPlot, :lineStyle, :loading_state, :locale, :meta, :padding, :point, :radius, :recentlyAreaClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :renderer, :seriesField, :smooth, :startAngle, :style, :theme, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdradar", "AntdRadar", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

