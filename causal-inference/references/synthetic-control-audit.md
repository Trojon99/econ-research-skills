# 合成反事实：支持、权重与区间对象

六篇连享会完整文字正文阅读记录经审阅后综合；原论文仅相关方法/摘要或help，不宣称全部证明、图片审核或软件运行。可广泛探索donor、窗口和约束，但留所有重要筛选，不根据显著性隐瞒候选。

## 1. 资格先于拟合，权重对象分开

审计donor直接处理、溢出、预期、同期冲击与缺失插补；选择前后资格表保留。分别报donor W、预测变量V、SDID前期时间lambda与处理/队列聚合gamma。留出拟合、窗口敏感性和主要donor删除回答具体威胁，不认证无遗漏冲击；共同污染无法靠leave-one-out解决。

来源：[1133](https://www.lianxh.cn/details/1133.html)、[1570](https://www.lianxh.cn/details/1570.html)；[synth2官方记录](https://www.stata-journal.com/article.html?article=st0722)仅记录/软件摘要；[独立案例原文](https://onlinelibrary.wiley.com/doi/10.1002/jae.2857) 引言/推断片段。复现目录404，未下载材料，不能认证全部原文数值或默认选项。

## 2. 惩罚估计与回归纠偏不是一个默认

pairwise discrepancy penalty是优化权衡，不是逐次删最远donor至满秩。所查allsynth方法先以lambda=0取得基础W，再在donor上逐期回归校正预测变量不平衡；不等于自动正lambda惩罚，也不保证前期轨迹更贴合或全部偏误消失。时间holdout不是有放回抽年bootstrap；不能用处理后结果训练其自身反事实。

来源：[854](https://www.lianxh.cn/details/854.html)；[Wiltshire作者文档](https://justinwiltshire.com/s/allsynth_Wiltshire.pdf) methods/inference；[惩罚SCM发表摘要](https://www.tandfonline.com/doi/abs/10.1080/01621459.2021.1971535)。前者期刊页眉占位不当正式发表证明；当前源码/完整命令未审、未执行。

## 3. SDID动态参数需要horizon支持账

队列gap扣除其前期lambda加权gap，再按该事件期可观察单位聚合；长horizon队列减少，变化可来自组成而非纯动态。去水平差异不免除未处理动态结构假设；所查设定是完整单位×时期面板与二元吸收处理，不随意套个人重复截面或撤销处理。bootstrap/placebo各需条件，few-treated与重复次数另检查。

来源：[1482](https://www.lianxh.cn/details/1482.html)；[Ciccia v2](https://arxiv.org/html/2407.09565v2) setting/decomposition段。当前软件catalog仅元数据，未查全部选项或方差证明。

## 4. 预测区间、抽样CI和placebo排名分开

scpi量化权重估计误差与处理后反事实随机误差，不能只画in-sample区间冒充完整预测。约束、样本外误差模型、alpha预算和pointwise/joint均声明；保证相对于假设，不因两个95%就得到合成95%。空间placebo记录集合、剔除规则、统计量、ties与尾部；非随机处理时不自动是精确随机化p值。

来源：[1096](https://www.lianxh.cn/details/1096.html)；[Cattaneo等大学记录/摘要](https://collaborate.princeton.edu/en/publications/prediction-intervals-for-synthetic-control-methods/)；[官方R手册](https://cloud.r-project.org/web/packages/scpi/scpi.pdf) preparation/constraints/out-of-sample段。手册仅相关段，不能推定Stata/Python版本一致；未来年份引用不据此称已发表。

## 5. QRF条件分布不是树点预测波动

QRF由树叶邻域构造训练响应的条件分布；树间算法波动不代表全部反事实误差，变量重要性不等于SCM W。条件关系前后稳定与训练支持关键，趋势外推可能退化成边界常数。若反事实区间[qL,qU]，效应实现区间为[Y-qU,Y-qL]；不是普通平均参数抽样CI或整路径覆盖。

来源：[1515](https://www.lianxh.cn/details/1515.html)；[原论文出版社摘要/引言](https://www.sciencedirect.com/science/article/abs/pii/S0304407624001350)；[公开help](http://fmwww.bc.edu/RePEc/bocode/q/qcm.sthlp)语法段（提取不全）。原错误DOI未当有效，全部算法/依赖和软件未验证；不发布未经执行的命令模板。

## 6. 矩阵补全：结构外推与assignment共同约束

核范数正则化限制低秩复杂度，不是无结构；所读2018 NBER工作稿允许单独不惩罚的unit/time FE。§5.1观测prefix停止点跨单位独立，Remark5.1允许其分布依赖潜在系统成分，但要求创新与assignment独立及相应末期支持。因此并非必须完全随机缺失，也不是可任意由不可预测负向创新触发政策。缺乏donor/晚期支持不能靠小惩罚恢复。

随机观察cells留出低RMSE不验证真实政策缺失形状；比较mask/cohort/horizon支持、可信未处理训练、rank/惩罚、donor和窗口，必要时增加模拟政策形状留出，后者是应用诊断建议而非原定理要求。2018 WP与2021最终版不混引；教程特定treated-cell聚合公式的命名仍待最终原源核验，不普遍指定全NT ATE或单位均权ATT。未复现证明、模型或数值。

### 原源与阅读边界

- [Matrix Completion Methods for Causal Panel Data Models](https://www.nber.org/system/files/working_papers/w25132/w25132.pdf)：§§4–5.1 and Remark5.1, §8.1–8.5; PDFpp14–19,30–34。版本/范围：NBER WP25132 October2018,50 PDF pages; NOT 2021 JASA final；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1693](https://www.lianxh.cn/details/1693.html)、[1279](https://www.lianxh.cn/details/1279.html)、[1661](https://www.lianxh.cn/details/1661.html)、[1128](https://www.lianxh.cn/details/1128.html)、[385](https://www.lianxh.cn/details/385.html)、[370](https://www.lianxh.cn/details/370.html)、[178](https://www.lianxh.cn/details/178.html)、[145](https://www.lianxh.cn/details/145.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。


## 经典SC的目标、插值与placebo口径

经典SC先用donor加权路径估计处理单位缺失的未处理结果；在可信识别条件下，逐期gap（实际结果减合成未处理结果）估计该单位该期的处理效应，而非未处理结果水平。该效应不自动是总体ATE或可迁移结构参数。W≥0、ΣW=1使同年合成结果处于donor结果凸包；避免的是负权/超额权的横截面线性外推，不消除前期到后期的预测结构外推或跨人口外部有效性。目标函数最优不一般保证W唯一。donor资格、政策包/结果单位与处理时点先于优化，低前期误差也不排除处理日独有冲击或donor污染。

训练/预测平均/优化误差期均须与首暴露期明确对齐，显式给出的年份不会因选项叫pre而自动安全。跨语言核X1/X0预测矩阵及Z1/Z0拟合结果矩阵：将若干年份均值作为一行，与各年分别入行不是同一规格；再对齐donor、缺失规则、V及其优化。假处理日的时间外检验用假日期前训练、真实处理前验证，不认证真实政策日无差异冲击。

为前/后窗口分别定义MSPE=Σgap²/实际期数，RMSPE=√MSPE。相同集合且pre>0时，post/pre MSPE比是RMSPE比的平方，排名相同但数值/筛选阈值不同；比率丢失方向，近零pre误差使它不稳定。所查SCtools作者源码的mspe.test按前期MSPE筛除，用含treated的实际保留集合和≥ties计算比例；不能填入同数值的RMSPE倍数或写死分母。是否把原treated返回placebo donor还需核具体构造，接口名不保证相同设计。

来源：Cunningham[第一版第10章](https://mixtape-1ed.netlify.app/10-synthetic_control) §§10.1–10.2，2026-10-15快照，经典SC有条件概念；[Synth dataprep](https://raw.githubusercontent.com/cran/Synth/master/man/dataprep.Rd) Arguments/Details/Value定向核special.predictors及X/Z定义；[SCtools mspe.test作者源码](https://raw.githubusercontent.com/bcastanho/SCtools/master/R/mspe.test.R) 函数体/返回值，作者master快照而非本机/CRAN版等价认证。只静态读源码，未运行SC、placebo或下载应用数据。精确RI的条件另见[分派参考](potential-outcomes-assignment.md)，不将此比例自动解释为非随机政策的exact p值。
