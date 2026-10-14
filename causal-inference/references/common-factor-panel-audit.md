# 共同因子、组级依赖与非线性FE审计

六篇连享会完整文字正文及原源指定章节/help记录经审阅综合。未安装软件、运行估计或读取研究数据，1496原论文只有元数据/材料目录；图片及证明未全核。允许探索因子数、滞后、FE与W，但留支持、约束和选择轨迹，不以最大p值挑设计。

## 1. 全局因子与局部空间相关不同
共同冲击×异质载荷可与X相关，导致系数偏误，不只SE问题；年份FE仅吸收共同截距。静态/动态CCE的外生性、秩和N/T条件不同，动态通常需均值滞后，不能从静态小T结果推广。cr_lags(2)为当期及两阶滞后不是前导；partialling-out是投影不是删观测；pooled指定相等系数限制，比较命令前对齐约束、归一化与样本。

来源：[1520](https://www.lianxh.cn/details/1520.html)、[1496](https://www.lianxh.cn/details/1496.html)；[Ditzen作者讲义](https://www.stata.com/meeting/uk19/slides/uk19_ditzen.pdf) CCE/dynamic/pooled段；[Saadaoui博文](https://www.jamelsaadaoui.com/illustrating-the-consequences-of-not-modeling-common-factors/)。1496教育回报与样本数仅二手，不认证能力测量或一般教育ATE。

## 2. 识别、相关结构和少簇分开
高层X重复到微观并不增加独立分配信息。全国X_t被完整年份FE吸收；Exposure_i*X_t是差异暴露目标不是全国平均效应。省年聚类不允许同省跨年相关；需要何种残余依赖由赋值/抽样/冲击决定，已吸收纯加性年份冲击不能再作唯一理由。少簇、杠杆与有效变化簇数另报，wild bootstrap/CR2不修复外生性或保证任意极少处理簇。

来源：[1873](https://www.lianxh.cn/details/1873.html)；[Cameron–Miller作者稿](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf) Moulton/聚类相关段。简化膨胀公式不是通用修正乘数，未运行教程模拟。

## 3. FE和不是条件均值，FE偏误校正非识别升级
ppmlhdfe d(fe_sum)保存FE和，ppml_fe_bias lambda()需要逐观测条件均值，不能直接lambda(fe_sum)。先锁原e(sample)、原实际保留回归量和系数，再预测同次估计条件均值；后处理覆盖e()需防护。

三维引力有限T结果针对特定模型/渐近，点估计一致不意味分布已居中或SE无偏。校正对象、方向/时间/配对FE、exact/twoway语义与版本分开；文档阈值1000/其他版本1500冲突不猜当前事实。singleton/separation/缺失和convergence逐项留账；保留零值不等于每个零都保留，也不自动运输到原总体。乘法DID反事实见did-target-sensitivity，不重复当新识别。

来源：[1807](https://www.lianxh.cn/details/1807.html)、[1813](https://www.lianxh.cn/details/1813.html)；[ppmlhdfe官方help](https://scorreia.com/help/ppmlhdfe.html) d/predict/Stored results；[bias作者help](http://fmwww.bc.edu/repec/bocode/p/ppml_fe_bias.sthlp) lambda/options；[Weidner–Zylkin](https://arxiv.org/pdf/1909.01327)定向理论段。另回查官方d语义，未审ado/复现SE差异和样本倍数问题，two-way后续新作仅主页元数据。

## 4. Moran针对W和零假设，不识别溢出
先声明W来源、邻居/距离/归一化、原变量还是残差，以及随机化/近似基准。HH/LL象限不是局部显著性；全局I不决定唯一模型，局部多检验另处理。pow是距离衰减不是邻接阶数；wvar改变权重而非回归控制；ties行为有原文公式不一致，未查实现不认证。非显著也不排除依赖。

来源：[1877](https://www.lianxh.cn/details/1877.html)；[Kondo DP2025-03](https://www.rieb.kobe-u.ac.jp/academic/ra/dp/English/DP2025-03.pdf) 指定方法/选项段。作者本机报错或日志不是普遍软件缺陷；未运行moransi。
