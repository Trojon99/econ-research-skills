# 动态面板：信息集到实际矩条件

## 从经济时序列允许工具
对加性个体效应模型y_it=rho y_i,t-1+x_it beta+alpha_i+u_it，先写初始观测、反馈和特异误差序列结构。在基准无序列相关误差及相应初始正交条件下，差分方程的y水平工具通常从2阶、前定x从1阶、同期内生x从2阶；严格外生x才可按相应条件使用当期/其他期。深滞后不是天然外生，遗漏持续因素、预期和误测会破坏这些矩。

逐变量保存回归角色、信息集、工具基础变量、相对lag、支持方程、变换、collapse和样本。GMM不因生成内部工具就制造外生性。FE去不变异质性，冲击到未来x的反馈仍可能进入within/FD误差；leads或FE/FD差异是条件性的警报，非拒绝不解决同期内生，两个估计量相近可同时有偏。

## 系统水平矩和初始条件
典型新增水平矩要求Delta y_i,t-1与alpha_i+u_it正交，不由原误差无序列相关自动推出。BB1998对初始偏离与个体长期水平的限制要单列；均值平稳是充分而非必要，不是要求完全分布平稳。高持续性使差分工具弱的可能性不等于rho过某阈值就能合法换SYS。新增方程的有效性、支持与强度均须另审。

## 有效性、强度、数量及检验分开
分别审排除渠道、实际方程工具矩阵的条件相关/rank和工具膨胀。展开差分/水平2SLS类似物能辅助揭露弱点，不是一般GMM的强度合格证。lag窗口限制时间距离，collapse按变量×lag合并时期列；两者不同且削减工具会损失信息。工具数少于组数、特定lag上限或rho阈值都不是普遍安全规则。允许比较有理论依据的窗口与矩，透明保留筛选，不按Hansen漂亮或星号定模型，不要求探索前预注册。

在基准误差设定下差分AR(1)拒绝/AR(2)不拒绝只是预期诊断模式。Hansen与difference-in-Hansen不检验强度，非拒绝不证明有效性，子集检验还依赖保留矩；工具多会削弱功效，恰好识别无多余矩可检验。robust/cluster/Windmeijer只修相应方差问题，不使无效矩有效。

## 不等间隔及非时变参数
保留日历单位，区分上一行、上一访谈和上一年。Sasaki–Xin所读引言列前定性、弱平稳、rank及US-spacing条件，不是任意缺口修复。FOD减少变换损失不代表可压缩时间。xtusreg旧帮助与SJ版本选项未核一致，不判某版本失效。

非时变变量与任意个体效应不能靠within分离；序贯法二阶段仍需相关且对复合误差有效的水平工具/额外结构。第一阶段合并非时变部分后，SYS工具需对合并效应有效。生成残差的第二阶段标准误要纳入第一阶段误差，软件解析调整仍以第一阶段一致为条件。

## 静态软件与长期解释
所查xtabond2的noleveleq排除水平方程，不把alpha设0；默认gmm变量的lag1对应前定而非通常同期内生设定。laglimits相对括号变量计数，L.y还额外偏一期。xtdpdgmm的model()规定方程，difference规定工具变换，全窗口可含leads，不应默默用于反馈变量。实际命令用前再核安装版，当前后估选项与旧文有版本差异。

稳定线性模型的永久x路径稳态差，与x过程一次创新的累计响应不同。额外的x持久性分母只属于相应创新实验，不是普遍长期修正；AR(2)应查根而非只查两系数和。时间序列加滞后处理误差设定，不自动解决短T FE的Nickell偏差。反事实还要论证参数/反馈不变性。这里未重估或执行来源程序，选读工作稿不冒充最终刊版。

### 原源与阅读边界

- [Generalized method of moments estimation of linear dynamic panel data models](http://repec.org/usug2019/Kripfganz_uk19.pdf)：slides9–11。版本/范围：London Stata Conference, 2019-09-05；仅相关段落/静态文档核查，非全证明或软件运行。
- [Initial conditions and moment restrictions in dynamic panel data models](https://www.homepages.ucl.ac.uk/~uctp39a/Blundell-Bond-1998.pdf)：§4.2, pp124–125 initial-deviation prose。版本/范围：Journal of Econometrics 87 (1998), 115–143；仅相关段落/静态文档核查，非全证明或软件运行。
- [Blunt Instruments: On Establishing the Causes of Economic Growth](https://www.files.ethz.ch/isn/100568/171.pdf)：§3, PDF pp15–20, footnote16 and recommendations p22。版本/范围：CGD Working Paper171, May20 2009；不是2013 AEJ刊版；仅相关段落/静态文档核查，非全证明或软件运行。
- [xtabond2 author repository help](https://raw.githubusercontent.com/droodman/xtabond2/master/xtabond2.hlp)：Description L160–174; Options L315–357；Description L152–174；Options L244–245, L277–290。版本/范围：作者仓库master所取help，文件头14 July 2014；未据此认定运行包版本；仅相关段落/静态文档核查，非全证明或软件运行。
- [Panel-Data Estimation in Finance: Testable Assumptions and Parameter (In)Consistency](https://www.cambridge.org/core/product/identifier/S0022109018000996/type/journal_article)：pp3–5 and §II.D pp7–10, equations(2)–(5), footnotes8–10。版本/范围：JFQA 54(1), 2019, 1–29；所读PDF为Wayback 2020-03-12快照；仅相关段落/静态文档核查，非全证明或软件运行。
- [Unequal spacing in dynamic panel data: Identification and estimation](https://www.sciencedirect.com/science/article/abs/pii/S0304407616301932)：Introduction paragraphs3,6–7; section snippets only。版本/范围：Journal of Econometrics 196(2), 2017, 320–330；仅相关段落/静态文档核查，非全证明或软件运行。
- [Estimation of linear dynamic panel data models with time-invariant regressors](https://www.econstor.eu/bitstream/10419/78229/1/756554209.pdf)：§2 Assumption3; §3 equations(11)–(15), PDF pp9,12–13。版本/范围：Bundesbank Discussion Paper 25/2013；不是2019刊版；仅相关段落/静态文档核查，非全证明或软件运行。
- [xtseqreg author help](https://www.kripfganz.de/stata/xtseqreg.sthlp)：Description L108–119。版本/范围：1.2.4 02sep2021；仅相关段落/静态文档核查，非全证明或软件运行。
- [xtdpdgmm author help](https://www.kripfganz.de/stata/xtdpdgmm.sthlp)：Options L173–203。版本/范围：2.7.2 17jul2025；仅相关段落/静态文档核查，非全证明或软件运行。
- [To Lag or Not to Lag?: Re-Evaluating the Use of Lagged Dependent Variables in Regression Analysis](https://www.cambridge.org/core/product/identifier/S2049847017000048/type/journal_article)：Debating LDVs eqs(1)–(4), stationarity; LONG-RUN EFFECT OF X ON Y opening paragraphs。版本/范围：Political Science Research and Methods 6(2), 2018, 393–411；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1151](https://www.lianxh.cn/details/1151.html)、[1105](https://www.lianxh.cn/details/1105.html)、[867](https://www.lianxh.cn/details/867.html)、[1062](https://www.lianxh.cn/details/1062.html)、[1150](https://www.lianxh.cn/details/1150.html)、[827](https://www.lianxh.cn/details/827.html)、[531](https://www.lianxh.cn/details/531.html)、[470](https://www.lianxh.cn/details/470.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
