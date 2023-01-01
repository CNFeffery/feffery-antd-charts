# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdstock

"""
    ''_antdstock(;kwargs...)

An AntdStock component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `data` (Array of Dict with Strings as keys and values of type String | Reals; required)
- `downloadTrigger` (String; optional)
- `fallingFill` (String; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `limitInPlot` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
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
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `risingFill` (String; optional)
- `slider` (optional)
- `stockStyle` (optional): . stockStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (Array of Strings; required)
"""
function ''_antdstock(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :data, :downloadTrigger, :fallingFill, :height, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :recentlyAreaClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :renderer, :risingFill, :slider, :stockStyle, :style, :theme, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdstock", "AntdStock", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

