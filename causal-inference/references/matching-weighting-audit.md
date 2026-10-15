# 匹配与历史加权：目标、支持和不确定性

## 设计与估计对象
先写ATE/ATT及目标人群，协变量资格来自制度/时序/因果结构。得分直方图或balance不能检验隐藏混杂。删treated/never-treated、限制支持或截尾权重要分别说明改变的人群/实际加权对象。所查Stata teffects ipw默认ATE，ATET需显式选项；overlap容差报错不是自动修剪，非线性加权回归系数不普遍是边际ATE。

## 模块化Bayes设计不消除无混杂假设
Liao–Zigler在positivity、SUTVA与strong ignorability下讨论设计/分析不确定性；设计模块不使用结果，所得模块化分布不能笼统当标准联合Bayes后验，也不由此禁止所有联合模型。只画每个设计的OLS点估计密度漏掉within-design分析不确定性。其合并方差包含条件分析方差与设计间方差及有限K因子，条件V须适用于实际估计量；教程近似或lm默认SE不因此有效。未运行后验或Stan，不将抽样次数写成通用默认。

## 时变处理路径与MSM
先定义当期、滞后、累计还是整段处理历史对比，再论证顺序可交换、路径positivity、一致性/无干扰及模型。权重分母混杂历史与MSM因果lag长度是不同选择。累乘观察处理状态的条件概率/密度比前，核单位时间键、排序、基线与吸收处理风险集；country/year、随机截距或AR1不证明历史充分。

所查ipwtm的type需显式；first在首次从最低处理状态切换后固定权重，与all用全部时期不同，连续处理需要条件密度比。吸收后结构不再切换，不应当可反复0/1分配。截尾并非自动，阈值敏感性与目标支持另报。lmer weights定义残差精度的prior weights，参数同名不保证MSM概率加权估计及SE正确；也不据这点宣称其点估计必错。估计方程、单位依赖和权重估计误差需另匹配。

## BLOP和CEM
BLOP所读2012工作稿先最小化个人特征到对侧凸组合的距离，再在第一阶段最优权重集合中最小化加权个人距离；不是把同一目标跑两遍。投影点与可能不唯一的权重表示不同，仍需可忽略处理分配、overlap及其支持条件，未核最终全部证明或LP性能。

CEM按有经济意义的粗化边界匹配，MIB不等于原尺度所有差异为零。比较L1须固定变量/分箱及可比样本权重，保留原尺度残留诊断。SATT基准、baseline与删除treated后的保留人群要明确，不外推成原全样本ATE；k2k还会随机再删样。匹配后系数下降不能证明原OLS高估。

## PS函数形式与推断语义
psestimate从给定允许集合选一/二阶与交互函数形式，不发现充分混杂集合；限定totry，base保留必要事前变量，不让自动搜索结果/处理后变量。所查作者ado比较LR而非绝对LL，genlor为log odds；iterate帮助与实现差异未执行核清，不认定当前默认。可以广泛比较PS与匹配规格，但记录支持、分布/尾部、保留人群和失败，不把不显著balance等同exchangeability。

psmatch2默认ATT、ATE显式；_weight在ties/k-NN和kernel有不同归一语义，不能通用转整数fweight。缺失结果、多outcome共同样本、排序/ties和方差假设需报告；cluster后回归不自动计入匹配/得分估计误差，普通bootstrap并非自动有效。matching加回归不自动双重稳健：AIPW/IPWRA是特定构造在识别/overlap/正则条件下的任一模型正确性质，不是任意两步或两个模型都错仍有效。

### 原源与阅读边界

- [teffects ipw — Inverse-probability weighting](https://www.stata.com/manuals/causalteffectsipw.pdf)：PDF pp1–4 Description, Options, Overview。版本/范围：Stata CAUSAL manual copyright2025; no installed Stata checked；仅相关段落/静态文档核查，非全证明或软件运行。
- [Uncertainty in the design stage of two-stage Bayesian propensity score analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC9170228/)：§§2.1–3.2; eqs(1)–(4)；§§4.1.2–4.3, eqs(10)–(12)。版本/范围：2020 accepted manuscript / PMC；仅相关段落/静态文档核查，非全证明或软件运行。
- [How to Make Causal Inferences with Time-Series Cross-Sectional Data under Selection on Observables](https://mattblackwell.org/files/papers/causal-tscs.pdf)：Assumption1 PDFpp5–6; MSM eqs(27)–(32) PDFpp9–11。版本/范围：APSR 2018 112(4),1067–1082 author-hosted published PDF；仅相关段落/静态文档核查，非全证明或软件运行。
- [ipwtm: Estimate Inverse Probability Weights (Time Varying)](https://rdrr.io/cran/ipw/man/ipwtm.html)：Usage/Arguments/Details/Value。版本/范围：rdrr CRAN documentation built 2025-12-08; installed version unknown；仅相关段落/静态文档核查，非全证明或软件运行。
- [lmer: Fit Linear Mixed-Effects Models](https://lme4.github.io/lme4/reference/lmer.html)：Arguments weights lines146–156。版本/范围：online lme4 documentation snapshot; installed version unknown；仅相关段落/静态文档核查，非全证明或软件运行。
- [A matching estimator based on a bi-level optimization problem](https://www.econ.uchile.cl/uploads/publicacion/280e391de0f639a8d43ac5b27c9a5d2e241c70f2.pdf)：§2.1 Assumptions1–3; §2.2 eqs(10)–(11), PDFpp5–8。版本/范围：SDT351 March2012 cover; manuscript Jan17,2012; not 2015 final journal；仅相关段落/静态文档核查，非全证明或软件运行。
- [cem: Coarsened Exact Matching in Stata](https://mattblackwell.org/files/stata/cem-stata.pdf)：§§2.2–3.2,4.1,4.3–4.5; PDFpp2–7,12–14。版本/范围：July27,2020 author manual；仅相关段落/静态文档核查，非全证明或软件运行。
- [psestimate author help](https://raw.githubusercontent.com/acarril/psestimate/master/psestimate.sthlp)：Description/Options lines38–103。版本/范围：help1.5 Nov2016 master snapshot；仅相关段落/静态文档核查，非全证明或软件运行。
- [psestimate author source (static audit)](https://raw.githubusercontent.com/acarril/psestimate/master/psestimate.ado)：syntax lines1–15; lrtest loops79–91,198–215; generate266–273。版本/范围：ado1.5.3 25nov2016; static read only；仅相关段落/静态文档核查，非全证明或软件运行。
- [psmatch2 author help in SSC archive](http://fmwww.bc.edu/repec/bocode/p/psmatch2.sthlp)：Description lines43–98; generated variables317–359。版本/范围：SSC help snapshot; no version header; not installed；仅相关段落/静态文档核查，非全证明或软件运行。
- [Double-robust treatment effects](https://www.stata.com/stata-news/news29-1/double-robust-treatment-effects/)：正文conditional independence与AIPW/IPWRA explanations lines986–1003,1093–1108。版本/范围：Stata News29(1) official exposition；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1693](https://www.lianxh.cn/details/1693.html)、[1279](https://www.lianxh.cn/details/1279.html)、[1661](https://www.lianxh.cn/details/1661.html)、[1128](https://www.lianxh.cn/details/1128.html)、[385](https://www.lianxh.cn/details/385.html)、[370](https://www.lianxh.cn/details/370.html)、[178](https://www.lianxh.cn/details/178.html)、[145](https://www.lianxh.cn/details/145.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。


## 标准化与实际权重的基础账

令m_d(x)=E[Y|D=d,X=x]。ATE对目标总体积分m1−m0，需两潜在结果的相应条件均值可交换及双侧支持；ATT只需恢复treated的Y(0)，故所需对照支持以treated分布为准。总体positivity、有限样本空cell及估计PS近无重叠不同；真e(X)的balancing性质不保证估计得分的有限样本平衡或隐藏混杂消失。

分层估计Σ_k q_k(Ȳ1k−Ȳ0k)，q取总体/treated/control的strata份额分别对应ATE/ATT/ATU目标；标签不改变权重。IPW的D/e、(1−D)/(1−e)是ATE型；ATT用treated均值减control odds e/(1−e)加权均值。HT与两臂各自归一的Hájek不是有限样本同一估计器。trim须重算保留集合的归一量、说明改变的目标和支持，不固定一个经验区间为通用最优。

有放回M近邻ATT中，treated各权重1/N_T，control j按复用次数K_j负载−K_j/(M N_T)；ties/变动M须按实际映射重构，不能将共享donor的pair差当独立。bias correction拟合相应反事实臂的响应面，不由全样本任意Y~X回归自动给出μ0；AIPW的特定增广性质与任意matching加回归不同，其推断须含nuisance步骤而非最后一步朴素SE。

固定M近邻的普通n-out-of-n bootstrap不能默认有效；这不是一切PS估计/加权方法的禁令。Lin–Han所读arXiv v2的发散M结果另有IID、strong overlap、密度/支持几何及M速率限制；bias-corrected推断还需其光滑和估计率条件。不能将固定5邻居换个bootstrap标签就套用，也不直接推广到ATT、簇相关或任意估计PS。

来源：Cunningham[第一版第5章](https://mixtape-1ed.netlify.app/05-matching_and_subclassification) §§5.1–5.3，2026-10-15快照，定义/有条件概念按教材阅读支持；[Stata AIPW](https://www.stata.com/manuals/causalteffectsaipw.pdf) pp1–5定向文档核查；[Lin–Han arXiv v2](https://arxiv.org/html/2410.23525v2) §§2–3、Assumptions3.1/3.2/4.1、Theorem3.3，发散M且Mlog(n)/n→0、log(n/M)/M→0，BC另需M/n^γ→0等文内条件。理论读的是v2非最终刊版全证明；未执行匹配或bootstrap。调整集依据见[因果图参考](causal-graphs-adjustment.md)。
