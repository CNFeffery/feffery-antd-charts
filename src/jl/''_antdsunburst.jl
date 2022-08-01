# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdsunburst

"""
    ''_antdsunburst(;kwargs...)

An AntdSunburst component.

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
- `data` (Dict; required)
- `downloadTrigger` (String; optional)
- `drilldown` (optional): . drilldown has the following type: lists containing elements 'enabled', 'breadCrumb'.
Those elements have the following types:
  - `enabled` (Bool; optional)
  - `breadCrumb` (optional): . breadCrumb has the following type: lists containing elements 'rootText', 'dividerText', 'textStyle', 'activeTextStyle', 'position'.
Those elements have the following types:
  - `rootText` (String; optional)
  - `dividerText` (String; optional)
  - `textStyle` (optional)
  - `activeTextStyle` (optional)
  - `position` (a value equal to: 'top-left', 'bottom-left'; optional)
- `height` (Real; optional)
- `hierarchyConfig` (optional): . hierarchyConfig has the following type: lists containing elements 'field', 'ignoreParentValue'.
Those elements have the following types:
  - `field` (String; optional)
  - `ignoreParentValue` (Bool; optional)
- `innerRadius` (Real; optional)
- `key` (String; optional)
- `label` (optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `radius` (Real; optional)
- `rawFields` (Array of Strings; optional)
- `reflect` (Bool; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `style` (Dict; optional)
- `sunburstStyle` (optional): . sunburstStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `tooltip` (optional)
- `width` (Real; optional)
"""
function ''_antdsunburst(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :downloadTrigger, :drilldown, :height, :hierarchyConfig, :innerRadius, :key, :label, :loading_state, :locale, :meta, :padding, :radius, :rawFields, :reflect, :renderer, :style, :sunburstStyle, :tooltip, :width]
        wild_props = Symbol[]
        return Component("''_antdsunburst", "AntdSunburst", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

