# DSGE：动态系统、参数来源与计算边界

## 先列对象再求根
把偏好/技术、状态与控制、lead/lag、预期、资本运动、财政资源约束及冲击过程联立。静态稳态方程去掉时间变化后可用来找根；它的Jacobian不能仅靠切行就产生完整动态状态转移或IRF。冲击当期impact不是跨期路径。先确定变量顺序、单位、冲击尺度和观测方程，再选择近似/解法并检查动态稳定性。

教程1625的静态草图遗漏部分参数/函数与动态实现，不当作可执行DSGE模板。政府支出已进入声明模型时，资源约束不得静默改成无政府的版本。这里未运行MATLAB/Dynare/Julia，也未核Sims MATLAB原文件签名；不能把别种语言文档当原代码复现。

## 从效用核Euler，不以稳态掩盖动态不一致
CRRA边际效用为C^(-sigma)，sigma=2不能换成1/C。自拟确定性两期算术例C0=2、C1=4、beta=.99、gross return=4/.99：正确Euler残差为0，而套对数效用的残差为-.5。仅验证这一边际条件反例，不是完整均衡、估计或求解性能复现。内点等式也不替代角点所需条件。

## dsgenl：固定、估计、求解各有证据
官方文档的solve在给定初值构造模型解，没有同一次估计的标准误；from()单独给初值不等于固定参数。参数来源应分外部固定/约束、校准、统计估计和仅用于敏感性求解。非线性方程输入仍在确定性稳态附近线性或log-linear近似，不因此得到全局非线性动态解。不要将教程1531带solve的参数改变称为重新估计，也不从其文字与代码不一致的折旧值推导通用效应。

每次交付保留稳态/动态残差、近似阶数、参数来源、稳定性、观测映射与未用矩验证；GDP增长率、水平与偏差单位需要明确桥梁，默认去均值本身不是这种桥梁。允许教学假设和参数探索，结果要明确其条件，不据未读IRF图声称经济方向已复现。

### 原源与阅读边界

- [dsgenl — Nonlinear dynamic stochastic general equilibrium models](https://www.stata.com/manuals/dsgedsgenl.pdf)：Options Main/Maximization与Methods and formulas, pp.2–5。版本/范围：在线官方PDF版权1985–2025，未推断Stata精确release；仅相关段落/静态文档核查，非全证明或软件运行。
- [Dynare model file: model declaration, steady state and stochastic simulation](https://www.dynare.org/manual/the-model-file.html)：§4.5 RBC例、§4.10.3、§4.13.1开头。版本/范围：在线页标注Dynare7.2；非本机安装版本；仅相关段落/静态文档核查，非全证明或软件运行。
- [DSGE.jl: Solving the Model](https://frbny-dsge.github.io/DSGE.jl/latest/solving/)：The gensys routine：canonical representation及transition/measurement。版本/范围：页面生成2022-06-30、Julia1.5.4；不代表最新运行环境；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1970](https://www.lianxh.cn/details/1970.html)、[1971](https://www.lianxh.cn/details/1971.html)、[1965](https://www.lianxh.cn/details/1965.html)、[1966](https://www.lianxh.cn/details/1966.html)、[1961](https://www.lianxh.cn/details/1961.html)、[1755](https://www.lianxh.cn/details/1755.html)、[1625](https://www.lianxh.cn/details/1625.html)、[1531](https://www.lianxh.cn/details/1531.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
