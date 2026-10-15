# 条件均值、线性投影与推断基础

## 1. 三种误差不能混同

先区分描述/预测问题和干预问题；零相关不排除某种因果作用，行动对冲击的反馈可能抵消观察相关，但不能据此断言任何观察关系都内生。[1, ch1 §§1.2–1.3]

令m(X)=E[Y|X]。CEF残差ε=Y−m(X)的E[ε|X]=0来自定义，乘积可积时E[h(X)ε]=0。总体线性投影残差与所纳入的线性设计正交；含截距OLS样本残差与设计列正交来自正规方程。三者均不证明结构方程Y=X′β+u中的E[u|X]=0。[1, ch2 §§2.11–2.18]

有截距可吸收误差无条件均值，不会制造条件均值独立。所需矩存在时，完整独立蕴含均值独立，后者蕴含与X的适当函数正交；零协方差不能通常反推独立，相关系数还要求正有限方差。[1]

条件概率P(A|B)=P(A∩B)/P(B)要求P(B)>0；全概率分解的条件事件须互斥且穷尽。Bayes更新应写清观察/选择机制，不能在不同观察协议下机械搬用同一个后验。联合概率、条件概率和边际概率的分母分别核，不以零协方差代替独立。[1, ch2 §§2.1–2.6]

## 2. 预测最优在哪个函数类

有限二阶矩下，任何平方可积预测g满足

    E[(Y−g(X))²] = E[Var(Y|X)] + E[(m(X)−g(X))²].

因此m在可测预测类中按平方损失最优，等同只需几乎处处。含截距的设计向量Q若E[QQ′]非奇异，总体最佳线性预测系数为E[QQ′]⁻¹E[QY]；非线性CEF下它是分布加权的线性近似，不能当作结构斜率或任意新样本的预测保证。样本R²高、残差正交、控制后系数翻号均不是外生性测试。[1, §§2.19–2.24；2]

OLS有限样本无偏需关于完整样本设计矩阵的零条件均值及满秩，并要求相关期望存在；先条件于设计，再取外层期望。不能从样本残差恒等式、E[u]=0或一个协方差矩直接跳到有限样本无偏。无偏是重复机制性质，不保证此次估计接近真值。[1, §2.16]

## 3. FWL揭示剩余比较，不能替代设计

对同一无权OLS样本，Z含截距及其他控制且满秩，M_Z=I−Z(Z′Z)⁻¹Z′，r=M_ZD，r′r>0，则完整回归D系数为

    βhat_D = (r′r)⁻¹ r′Y = (r′r)⁻¹ r′M_ZY.

这是投影代数，不要求Z的线性拟合等于真实CEF。仅残差化D后对原Y回归虽有相同系数，却未必有完整模型残差；朴素SE不自动相同。双边残差化也须匹配自由度、HC/cluster修正；加权时使用同一加权投影，而非直接套无权矩阵。[1, §2.24；本节为规范化代数整理]

比较增删控制的结果时先固定样本/权重，再审控制是否打开collider、截断中介或改变支持。在线性关系Y=α+βD+γX+e且Cov(D,e)=0、Var(D)>0下，短回归斜率为β+γ Cov(D,X)/Var(D)；这只是该投影/结构下的分解，不保证长回归因果正确。非线性曲线不由FWL自动保持原目标，另读[非线性分仓参考](nonlinear-binned-functions.md)。[1]

若线性模型含D及D×G，G=1组的D斜率是主项加交互项；任意对比l′b的方差为l′V l，不能直接相加SE或用两组各自星号代替差异检验。须使用同一模型、尺度和完整协方差，不以未知列标题猜测估计对象。[1, ch4 §4.1.5；代数对比，不移植原应用数值]

## 4. FE等价的范围

静态加性单位截距可由单位demean消去；LSDV/within在同一投影空间、样本、权重及rank下给相同斜率，不保证手工两步输出有相同SE/自由度。因果解释另需如E[e_it|D_i1,…,D_iT,α_i]=0的全路径限制，而非仅当期正交。冲击反馈未来处理可使within不满足相应矩；固定载荷乘时变因子也不是单位常数。[1, ch8 §§8.2–8.3]

这些是静态模型条件，不把“不能有反馈/动态”的口号推广到所有DID或含FE的动态设计；动态模型应另查信息集、初始条件和工具矩，而非机械新增滞后项。[1；3]

## 5. 不确定性对象与协方差

误差SD、回归RMSE、系数重复抽样SD及其估计SE不同。简单含截距回归在零条件均值、条件同方差且误差跨观测不相关下，Var(βhat_D|D)=σ²/Σ(D_i−Dbar)²；多元回归用相应完整矩阵。异方差不单独推翻零条件均值下的无偏性，却改变传统VCE的适用性。[1, §§2.25–2.27]

群内可依赖、群间满足所用独立/弱依赖条件的无权OLS cluster sandwich未附小样本乘子形式为

    (Q′Q)⁻¹ [Σ_g Q_g′ uhat_g uhat_g′ Q_g] (Q′Q)⁻¹.

聚类层级跟随抽样/分派/冲击，不按显著性选择；cluster SE可大可小，少有效群与杠杆失衡要专门推断。HC与cluster的有限样本乘子/df须核具体版本；稳健VCE不修内生性。[1；4]

Monte Carlo从指定DGP重复生成数据，bootstrap从观测样本按适当依赖结构重抽，随机化推断重分指定设计的处理；不是同一参照分布。模拟表现只对所设DGP/估计规则成立，不能证明实证识别。[1；另见causal-inference的potential-outcomes-assignment主题]

## 来源与证据边界

[1] Cunningham，在线第一版[第1章](https://mixtape-1ed.netlify.app/01-introduction)、[第2章](https://mixtape-1ed.netlify.app/02-probability_and_regression)、[第4章](https://mixtape-1ed.netlify.app/04-potential_outcomes)、[第8章](https://mixtape-1ed.netlify.app/08-panel_data)，2026-10-15快照，以上指定小节。区分教材定义、规范化矩阵整理与结构假设；不照录有冲突的推导或程序，不称全证明独立验证。

[2] Yen-Chi Chen，[STAT512 Lecture5](https://faculty.washington.edu/yenchic/20A_stat512/Lec5_prediction.html)，网页标2022 Autumn，定向核Mean-square error prediction的风险分解；非整门课程。

[3] Imai–Kim，[When Should We Use Unit Fixed Effects Regression Models for Causal Inference with Longitudinal Data?](https://imai.fas.harvard.edu/research/files/FEmatch.pdf)，AJPS2019，pp467–470选读，静态unit-FE与DID的区别；非全篇/所有动态FE定理。

[4] Stata官方[robust/cluster FAQ](https://www.stata.com/support/faqs/statistics/standard-errors-and-vce-cluster-option/)，Comparing the three variance estimators相关段；核score-sum结构与SE可能较小，不代表任何本机软件已执行。全文中的投影/分解是有条件概念和代数，非研究结果复现。
