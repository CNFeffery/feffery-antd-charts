# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdwordcloud

"""
    ''_antdwordcloud(;kwargs...)

An AntdWordCloud component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `colorField` (String; optional)
- `data` (Array of Dicts; optional)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `imageMask` (String; optional)
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
- `placementStrategy` (optional): . placementStrategy has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `randomState` (Real; optional)
- `recentlyLegendInfo` (optional): . recentlyLegendInfo has the following type: lists containing elements 'triggerItemName', 'items'.
Those elements have the following types:
  - `triggerItemName` (Bool | Real | String | Dict | Array; optional)
  - `items` (Array of Dicts; optional)
- `recentlyTooltipChangeRecord` (optional): . recentlyTooltipChangeRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Array of Dicts; optional)
- `recentlyWordClickRecord` (optional): . recentlyWordClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Dict; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `spiral` (a value equal to: 'archimedean', 'rectangular'; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `weightField` (String; required)
- `width` (Real; optional)
- `wordField` (String; required)
- `wordStyle` (optional): . wordStyle has the following type: lists containing elements 'fontFamily', 'fontWeight', 'padding', 'fontSize', 'rotation'.
Those elements have the following types:
  - `fontFamily` (String; optional)
  - `fontWeight` (String; optional)
  - `padding` (Real; optional)
  - `fontSize` (Array of Reals; optional)
  - `rotation` (Real; optional)
"""
function ''_antdwordcloud(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :downloadTrigger, :height, :imageMask, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :placementStrategy, :randomState, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :recentlyWordClickRecord, :renderer, :spiral, :style, :theme, :tooltip, :weightField, :width, :wordField, :wordStyle]
        wild_props = Symbol[]
        return Component("''_antdwordcloud", "AntdWordCloud", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

