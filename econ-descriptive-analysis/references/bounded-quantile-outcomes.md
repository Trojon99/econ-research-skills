# 有界结果、端点质量与分位数对象

六篇连享会完整文字正文与原源/作者help指定段落经审阅综合；未执行R/Stata、安装或复现数值。允许数据先行探索尺度、分位点、边界模型，保存全部重要选择与支持；不以复杂度或显著性替代目标解释。

## 1. 先核支持集和端点的经济含义
比例、无界比率和和为1的组成不同。分母0是未定义不自动是结果0；标准Beta仅(0,1)，fractional logit可含[0,1]端点且依正确条件均值，不要求真实Bernoulli分布。OLS投影不因有界或异方差就必不一致，越界是函数/支持警告。有限分母次数需保留分母及人口权重；逐项Beta不保证组成约束。

来源：[1658](https://www.lianxh.cn/details/1658.html)、[1659](https://www.lianxh.cn/details/1659.html)、[1660](https://www.lianxh.cn/details/1660.html)；[原教程](https://www.andrewheiss.com/blog/2021/11/08/beta-regression-guide/)；官方[fracreg](https://www.stata.com/manuals/rfracreg.pdf)、[betareg](https://www.stata.com/manuals/rbetareg.pdf)相关段；三教程同源不当三份独立证据。

## 2. 内部均值、边界概率、总体均值分开
ZIB总体均值=(1-zi)*mu；ZOIB=(1-zoi)*mu+zoi*coi。变量影响两部分时，内部beta不能代表总体边际效应。精确0不证明结构性因果机制，检测限/舍入/有限分母可能需观察模型；反转1-Y后原0变1，标准ZIB不能接纳这些新1。Beta相同phi不等于相同方差/形状；plogis单独斜率不是处理后的均值。

posterior_epred抽的是条件期望的不确定性，不含新观测残差；re_formula=NA排除组效应不等于按随机效应分布积分。AME与均值协变量处对比不同。来源：1659/1660；[brms官方families](https://paulbuerkner.com/brms/articles/brms_families.html)、[epred文档](https://paulbuerkner.com/brms/reference/posterior_epred.brmsfit.html)。未核教程所有应用文献或运行模型。

## 3. QR、QTE和个人效应不可互换
条件QR、边际QTE、complier LQTE与ITE分布不同；低分位提高不保证固定底部那批人获益，跨状态排序需额外限制。历史档案的征兵/存活/留存和暴露测量不会被QR自动修复。IV单调性针对处理，不是所有人结果同向；Wald分母是工具引起的处理概率差，不是结果差，更不是通用LQTE公式。

来源：[1529](https://www.lianxh.cn/details/1529.html)；[2021作者预印本](https://arxiv.org/pdf/2108.06055) §§2.1–2.2、4。2023正式版未读，暴露年龄组差异记版本冲突不擅判最终错误；未复现。

## 4. 未观察潜在工资不是真实零
选择修正QR需propensity、排除、copula/秩稳定与支持等，不能因婚姻/孩子不放工资方程就认定有效排除。arhomme的taupoints是矩目标网格，不等于最终quantiles；重抽样含所有估计阶段且记录失败/替换。旧qregsel帮助未列e(V)，不凭点估计输出构造伪显著性。

来源：[1579](https://www.lianxh.cn/details/1579.html)；[arhomme作者help](http://fmwww.bc.edu/repec/bocode/a/arhomme.sthlp)2020、[qregsel help](http://fmwww.bc.edu/repec/bocode/q/qregsel.sthlp)2021及[作者幻灯片](https://www.stata.com/meeting/us20/slides/us20_Siravegna.pdf)。原始完整证明未通读、现版本兼容未执行。

## 5. 角解零平台不是被截尾的负结果
完整观察结果零质量p0(X)下，tau<=p0的条件分位数为0，正部需调整分位点(tau-p0)/(1-p0)；删0后在同tau回归改变对象。fqreg的拟合零比例不是实际Y零比例；负check目标的ml日志不证明概率MLE，margins会改变保存结果语义。正区支持少、非凸优化与crossing另审，收敛不保证全局最优。

来源：[1461](https://www.lianxh.cn/details/1461.html)；[2016接受稿](https://repository.essex.ac.uk/16913/1/1-s2.0-S0014292116301040-main.pdf) §§1–2.3；[作者help](http://fmwww.bc.edu/repec/bocode/f/fqreg.sthlp)2016。条件只对内部正区密度，不在闭区间要求绝对连续排除自身零质量；本轮不提供tested语法。
