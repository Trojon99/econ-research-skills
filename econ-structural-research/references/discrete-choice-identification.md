# 离散选择：偏好、持久异质性和概率对象

## 选择集与归一化
区分人、选择时点、alternative长行；choice set必须与实际可用且互斥穷尽的选项相符。明确outside option及条件选择样本。效用位置和尺度归一化后才谈参数，同一case内不变变量的共同系数从效用差消去。拒绝IIA不证明新tree/混合分布正确，也不识别价格外生性、供给或福利。

Choice margins还须区分outcome（哪一项概率）与alternative（改变哪一项属性），并注明simultaneous、可用选择集与平均人口；outcome(Car)不表示只改变Car属性。固定参数/菜单的价格预测对比不自动是供给调整后的政策效应。

## 持久taste的序列likelihood
Train第二版§6.7在同一人taste固定、给定taste的极值误差跨期独立时，先乘整段条件logit概率，再对共同taste积分。逐期分别积分后相乘是另一个依赖模型。条件logit仍有IIA，混合后一般放松；分布形状、相关性及符号限制仍需证据。模拟点数/序列/seed/多初值是数值设置而非识别。Stata19手册p16文本抽取与该积分顺序的表面冲突尚未视觉/源码核清，绝不据此宣称软件bug。

两层RUM nested logit的dissimilarity内点通常满足0<tau<=1；全部为1回到普通非混合logit。singleton nest的tau不识别，大SE不是已固定为1。nest是误差相关结构，不是已经观察到决策时间顺序；对齐RUM与旧nonnormalized版本再解释系数。

## 动态二元模型
滞后结果与当期创新不因滞后身份就必然相关；关键要分初始值、共享ci和真正状态依赖。xtpdyn所用条件异质性模型为ci|y0,X指定分布，保留随机项并对其积分，不是消灭ci。严格外生、残余分布、初始期/均值窗口和缺失/不平衡机制均是条件。FE或robust SE不自动修复这些问题；短期转移拟合也不背书稳定长期持续期。

## 内生连续协变量与ASF
所查ivprobit是连续内生协变量的三角正态模型，不直接适用于把二元内生处理当连续回归量。工具数order条件只是必要维数条件，排除、rank和分布另证。

后估写清预测functional、固定何种扰动、反事实值和平均人口：观测条件预测中残差随内生变量更新，与固定残差后的结构变化不是同一导数；fixedasf又对应结构误差总体平均。不能把Phi(xbeta)无条件叫观测条件概率。子群、各自分布平均和共同标准化需有共同支持；工具的条件预测导数非零不自动违反结构排除。保留软件版本/补丁及第一阶段不确定性，但本次不认证历史版本自编margins代码。

## 多量表、有序FE和非线性交互
mscologit是多量表各有切点、共同潜在斜率/尺度的模型，不是任意广义ologit。潜在构念、同向编码及锚定/不变性需有证据；自由切点不自动分离跨国均值与报告阈值漂移。作者原论文正文未取得，只核作者help相应范围。

feologit BUC将cutoff二分后的条件likelihood堆叠，复制不增加独立个体，SE仍按原panel聚类；BUC-tau另加共同阈值/位置限制。明确switchers、seed及复制数。其logitmarg为以结果累计频率构造的ME at the average，不是个体AME或协变量均值处ME；thresholds后将固定效应设共同代理的predict/margins仅是suggestive，不把它当已识别个人概率效应。

先选概率/odds与差值/比率：二元变量有限差分、连续变量交叉导数；logit的exp(交互系数)是条件odds比之比，不是概率DID或自动因果异质性。连续导数还含link曲率。跨组原始logit/probit系数混合斜率与latent scale；二元logit误差logistic、probit normal，与MNL的极值utility误差区分。可以探索多尺度/事后机制，但说明共同或各自平均分布，不用选中尺度抢定研究story。

### 原源与阅读边界

- [Discrete Choice Methods with Simulation, 2nd ed., Chapter 2](https://eml.berkeley.edu/books/choice2nd/Ch02_p9-33.pdf)：§2.2 printed pp11–14; §2.5.1–2 printed pp19–26；§2.5.2 printed pp23–26, group-scale example。版本/范围：2009 second edition author-hosted chapter；仅相关段落/静态文档核查，非全证明或软件运行。
- [Discrete Choice Methods with Simulation, 2nd ed., Chapter 6](https://eml.berkeley.edu/books/choice2nd/Ch06_p134-150.pdf)：§6.1–6.4 pp134–141; §6.7 eqs(6.2)–(6.3) pp145–147。版本/范围：2009 second edition author-hosted chapter；仅相关段落/静态文档核查，非全证明或软件运行。
- [margins — Adjusted predictions, predictive margins, and marginal effects (choice models)](https://www.stata.com/manuals/cmmargins.pdf)：Quick start pp1–2; Options p3 outcome/alternative/simultaneous/altsubpop。版本/范围：Stata 19 manual; copyright 2025; retrieved 2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [nlogit — Nested logit regression](https://www.stata.com/manuals/cmnlogit.pdf)：Technical note p17; Methods and formulas pp20–21 eqs(3)–(5)。版本/范围：Stata 19 manual; copyright 2025; retrieved 2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [xtpdyn: A community-contributed command for fitting dynamic random-effects probit models with unobserved heterogeneity](https://www.stata-journal.com/sjpdf.html?articlenum=st0543)：§1–2 pp844–846; §3.5–3.6 pp848–852。版本/范围：Stata Journal 18(4), 844–862, 2018, st0543; DOI 10.1177/1536867X1801800406；仅相关段落/静态文档核查，非全证明或软件运行。
- [ivprobit — Probit model with continuous endogenous covariates](https://www.stata.com/manuals/rivprobit.pdf)：Description p1; Model setup/identification p5。版本/范围：Stata 19 manual; copyright 2025; retrieved 2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [ivprobit postestimation — Postestimation tools for ivprobit](https://www.stata.com/manuals/rivprobitpostestimation.pdf)：predict options p3; Marginal effects pp6–7; Methods and formulas p8。版本/范围：Stata 19 manual; copyright 2025; retrieved 2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [mscologit — Multiscale ordered logit model (author help)](http://fmwww.bc.edu/repec/bocode/m/mscologit.sthlp)：Description/depvars options L15–40; logit/acc/lo/up L50–77。版本/范围：author help fetched 2026-10-15; file does not declare exact package build; not official StataCorp command；仅相关段落/静态文档核查，非全证明或软件运行。
- [feologit: A new command for fitting fixed-effects ordered logit models](https://www.econ.uzh.ch/dam/jcr:2377e4ff-bdbe-42dc-adcf-79b7c67ec616/stata.journal.pdf)：§2.1–2.3 pp256–259; §3.2–3.4 pp259–261；§3.5 p261; §4.3 pp263–264; §4.4 pp264–265。版本/范围：Stata Journal 20(2),253–275,2020; DOI 10.1177/1536867X20930984；仅相关段落/静态文档核查，非全证明或软件运行。
- [Stata tip 87: Interpretation of interactions in non-linear models](http://www.maartenbuis.nl/publications/interactions.pdf)：pp1–4 of author manuscript, especially p3 categorical finite difference。版本/范围：author manuscript has yyyy placeholders; published citation independently listed by article as SJ10(2),305–308 (2010); not identical typeset pagination；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[748](https://www.lianxh.cn/details/748.html)、[260](https://www.lianxh.cn/details/260.html)、[44](https://www.lianxh.cn/details/44.html)、[1519](https://www.lianxh.cn/details/1519.html)、[1291](https://www.lianxh.cn/details/1291.html)、[507](https://www.lianxh.cn/details/507.html)、[616](https://www.lianxh.cn/details/616.html)、[1332](https://www.lianxh.cn/details/1332.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
