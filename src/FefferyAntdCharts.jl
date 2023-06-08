
module FefferyAntdCharts
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1-rc19"

include("jl/''_antdarea.jl")
include("jl/''_antdbar.jl")
include("jl/''_antdbox.jl")
include("jl/''_antdbullet.jl")
include("jl/''_antdchord.jl")
include("jl/''_antdcolumn.jl")
include("jl/''_antddualaxes.jl")
include("jl/''_antdfunnel.jl")
include("jl/''_antdgauge.jl")
include("jl/''_antdhistogram.jl")
include("jl/''_antdline.jl")
include("jl/''_antdliquid.jl")
include("jl/''_antdpie.jl")
include("jl/''_antdradar.jl")
include("jl/''_antdrose.jl")
include("jl/''_antdsankey.jl")
include("jl/''_antdscatter.jl")
include("jl/''_antdstock.jl")
include("jl/''_antdsunburst.jl")
include("jl/''_antdtinyline.jl")
include("jl/''_antdtreemap.jl")
include("jl/''_antdwordcloud.jl")
include("jl/''_antddecompositiontree.jl")
include("jl/''_antdfundflow.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_antd_charts",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_antd_charts.min.js",
    external_url = "https://unpkg.com/feffery_antd_charts@0.0.1-rc19/feffery_antd_charts/feffery_antd_charts.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_antd_charts.min.js.map",
    external_url = "https://unpkg.com/feffery_antd_charts@0.0.1-rc19/feffery_antd_charts/feffery_antd_charts.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
