import AntdLine from "./components/AntdLine.react";
import AntdArea from "./components/AntdArea.react";
import AntdBar from "./components/AntdBar.react";
import AntdColumn from "./components/AntdColumn.react";
import AntdPie from "./components/AntdPie.react";
import AntdScatter from "./components/AntdScatter.react";
import AntdStock from "./components/AntdStock.react";
import AntdRadar from "./components/AntdRadar.react";
import AntdSunburst from "./components/AntdSunburst.react";
import AntdChord from "./components/AntdChord.react";

// 屏蔽所有warning信息
window.console = (function () {
    var c = {};
    c.warn = function () { };
    return c;
})();

export {
    AntdLine,
    AntdArea,
    AntdBar,
    AntdColumn,
    AntdPie,
    AntdScatter,
    AntdStock,
    AntdRadar,
    AntdSunburst,
    AntdChord
};
