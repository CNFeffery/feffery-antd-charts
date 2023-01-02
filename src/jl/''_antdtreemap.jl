# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdtreemap

"""
    ''_antdtreemap(;kwargs...)

An AntdTreemap component.

Keyword arguments:
- `id` (String; optional)
- `animation` (Dict; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `colorField` (String; required)
- `data` (Dict; optional)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `interactions` (optional): . interactions has the following type: Array of lists containing elements 'type'.
Those elements have the following types:
  - `type` (a value equal to: 'treemap-drill-down', 'view-zoom', 'drag-move'; required)s
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
- `rawFields` (Array of Strings; optional)
- `recentlyAreaClickRecord` (optional): . recentlyAreaClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Dict; optional)
- `recentlyLegendInfo` (optional): . recentlyLegendInfo has the following type: lists containing elements 'triggerItemName', 'items'.
Those elements have the following types:
  - `triggerItemName` (Bool | Real | String | Dict | Array; optional)
  - `items` (Array of Dicts; optional)
- `recentlyTooltipChangeRecord` (optional): . recentlyTooltipChangeRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Array of Dicts; optional)
- `rectStyle` (optional): . rectStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
"""
function ''_antdtreemap(; kwargs...)
        available_props = Symbol[:id, :animation, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :downloadTrigger, :height, :interactions, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :rawFields, :recentlyAreaClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :rectStyle, :renderer, :style, :theme, :tooltip, :width]
        wild_props = Symbol[]
        return Component("''_antdtreemap", "AntdTreemap", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

