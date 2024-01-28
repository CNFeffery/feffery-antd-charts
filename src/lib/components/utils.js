import { G2 } from '@ant-design/plots';
import { deepMix } from '@antv/util';
import { transform, isEqual, isObject } from 'lodash';

const difference = (object, base) => {
    const changes = (object, base) => {
        return transform(object, function (result, value, key) {
            if (!isEqual(value, base[key])) {
                result[key] = (isObject(value) && isObject(base[key])) ? changes(value, base[key]) : value;
            }
        });
    }
    return changes(object, base);
}

const withTheme = (theme, customTheme) => {
    // 取得theme对应的内置主题
    let builtInTheme = G2.getTheme(theme);

    // 返回融合后的新主题
    return deepMix(
        {},
        builtInTheme,
        customTheme
    )
}

export { difference, withTheme };