# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdchord

"""
    ''_antdchord(;kwargs...)

An AntdChord component.

Keyword arguments:
- `id` (String; optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `data` (Array of Dicts; optional)
- `downloadTrigger` (String; optional)
- `edgeStyle` (optional): . edgeStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meta` (optional)
- `nodePaddingRatio` (Real; optional)
- `nodeStyle` (optional): . nodeStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `nodeWidthRatio` (Real; optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `sourceField` (String; optional)
- `style` (Dict; optional)
- `targetField` (String; optional)
- `weightField` (String; optional)
- `width` (Real; optional)
"""
function ''_antdchord(; kwargs...)
        available_props = Symbol[:id, :appendPadding, :autoFit, :className, :data, :downloadTrigger, :edgeStyle, :height, :key, :loading_state, :locale, :meta, :nodePaddingRatio, :nodeStyle, :nodeWidthRatio, :padding, :renderer, :sourceField, :style, :targetField, :weightField, :width]
        wild_props = Symbol[]
        return Component("''_antdchord", "AntdChord", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

