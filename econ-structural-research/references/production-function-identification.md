# 生产函数：投入时序、代理与生产率计量

## 技术、信息与投入决策
写y=投入技术贡献+企业决策时可观察的omega+决策后噪声epsilon，并按数据频率画资本、劳动、中间投入和创新的时间线。OP投资代理和LP中间投入代理的反演均要条件单调、足够支持及合适未观测维度；换代理不取消这些限制。零投资删样会改变目标企业总体。

ACF指出劳动可能与第一阶段非参数控制函数发生函数依赖，不是要求劳动与代理无条件独立。将劳动纳入代理需求条件后，劳动贡献一起进入第一阶段复合函数；第二阶段矩要从劳动/资本实际信息集推导。当期可调劳动不能未经论证当作与当期生产率创新正交的工具。检查采购与耗用、企业价格异质性和代理条件支持；提高多项式阶数或优化成功都不能补出排除/秩。

## 增加值不是总产出的一键选项
ACF §4.1的增加值解释有非平凡条件；在原有标量未观测设定下，将材料加入非Leontief总产出方程，原代理矩不自动识别。额外FOC或收入份额限制需独立陈述。软件接受valueadded/gross-output规格不认证其经济聚合和识别。

## 多代理测量误差：识别与实现分层
HHS 2020在给定潜在生产率和控制后施加代理条件独立、相应积分算子单射、区别性及归一化等限制。仅有多个相关代理不充分。核资本构造：若控制的相邻资本机械决定投资，投资代理的剩余变异会退化。

该文§3明确GMM所用矩不是§2.2识别条件直接推出，另需Condition5及动态近似。代理方程的测量误差与同一变量作为生产回归量的误测是两层问题；滞后误测投入工具还需跨期独立等限制。持续/共同录入误差可能同时污染产出、代理和工具；proxy(m)不自动修复所有投入误差。

## 解释与计算诊断
维护者predict所称logTFP残差是观测y减估计投入贡献，不自动是无噪声的omega、物理技术或福利。收入产出还可能混入价格/需求/质量差异。平滑生产率与直接观测残差须分别定义，不能以核密度位置、相关系数或星号挑正确TFP。

非线性GMM保存同样本/同准则下多初值、目标函数、收敛及参数可行性。robustpf作者§4.2/§6明确多初值与e(objective)比较不保证全局最优。文章打印不收敛不能作方法优越性或本次复现成功；未运行数据，不猜测不同表值的版本/初值原因。一致性也不等于有限样本无偏。

### 原源与阅读边界

- [Identification Properties of Recent Production Function Estimators](https://file.lianxh.cn/Refs/TE/Gong/Ackerberg-2015-Econometrica.pdf)：§2.2假设1—5；§3.1；§4.1假设3C—5C、式25—29；§4.1 p2428，gross-output/Leontief限制段；§2生产函数式1与ω/ε信息集讨论；引言measurement-error段。版本/范围：Econometrica 83(6), 2015, 2411–2451；发表版镜像，DOI 10.3982/ECTA13408；仅相关段落/静态文档核查，非全证明或软件运行。
- [prodest predict maintainer help](https://raw.githubusercontent.com/GabrieleRovigatti/prodest/master/stata/dofile/prodest_p.sthlp)：Options for predict: Cobb-Douglas/Translog residuals。版本/范围：抓取master快照；帮助头1.0.1/06Jun2017；仅相关段落/静态文档核查，非全证明或软件运行。
- [Estimating production functions with robustness against errors in the proxy variables](https://www.econ2.jhu.edu/People/Hu/Website/HuHuangSasaki2020.pdf)：§2.2 Conditions1—4，p379；资本累计讨论§2.1；§2.4.1 measurement error；§3 Condition5式13—14；§3.1。版本/范围：JoE 215(2), 2020, 375–398；作者网站发表版，DOI 10.1016/j.jeconom.2019.05.024；仅相关段落/静态文档核查，非全证明或软件运行。
- [robustpf: A command for robust estimation of production functions](https://www.econ2.jhu.edu/People/Hu/Website/HuHuangSasaki2023.pdf)：§4.2 p91、§6 p95；§5 p92作者表。版本/范围：Stata Journal 23(1), 2023, 86–96；DOI 10.1177/1536867X231161977；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1848](https://www.lianxh.cn/details/1848.html)、[900](https://www.lianxh.cn/details/900.html)、[331](https://www.lianxh.cn/details/331.html)、[13](https://www.lianxh.cn/details/13.html)、[1545](https://www.lianxh.cn/details/1545.html)、[1465](https://www.lianxh.cn/details/1465.html)、[1389](https://www.lianxh.cn/details/1389.html)、[791](https://www.lianxh.cn/details/791.html)。这些是相应组文字正文阅读记录；不是所有图片已读。生产组记录9幅实质图已查看，其余相关组图像大多未读；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
