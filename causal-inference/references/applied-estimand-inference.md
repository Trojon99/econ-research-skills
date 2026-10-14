# 应用中的估计对象、样本选择与推断

## 来源与核验层级

本参考综合连享会八篇阅读中的五个主题。四篇因果文章及 sreg 文章完整正文已读；原源只核对相关章节、定理陈述或帮助文档，未复核全部证明、安装软件或运行命令。网页日期/软件状态可变化，使用时复查匹配版本。以下“实践”是综合建议，不等于每篇文章原作者结论；完整阅读清单保留在任务记录，不宣称全站覆盖。

## 预趋势：功效不等于校正

- 实践：定义经济上有意义的偏离路径，结合系数、协方差、事件时间支持报告可检测偏离和功效。允许探索不同窗口与端点合并，记录其改变的比较与限制；不能把 binning 当作数值 winsorization，也不能把非拒绝当证明。
- 明确功效工具使用的是逐项还是联合拒绝规则；所查 Stata pretrends 使用任一前期系数显著的规则。检验后选择可能改变估计与区间性质，功效计算自身不校正该选择。
- 所查 help 返回 `r(Bayes)`，部分说明文字称 `r(BF)`；调用前读实际 help/返回矩阵。该概率比不是平行趋势成立的后验概率。没有实跑不能承诺代码可执行。
- 支持：[连享会完整正文](https://www.lianxh.cn/details/1704.html)；[Roth 作者稿，相关章节已读](https://www.jonathandroth.com/assets/files/roth_pretrends_testing.pdf)；[软件](https://github.com/mcaceresb/stata-pretrends)及[help](https://raw.githubusercontent.com/mcaceresb/stata-pretrends/main/doc/pretrends.sthlp)。剩余边界：路径功效只针对指定偏离，不能解决错误事件研究估计器或证明处理后潜在趋势。

## 连续 DID：组间水平与组内剂量不是同一对象

- 实践：明确实际剂量下的 ATT、组内线性投影斜率、因果剂量导数分别是什么，再选择工具。强度与未处理趋势的限制，不等于强度与收益选择的限制。
- Yu 的两期固定剂量、零强度对照、无额外协变量的 cellwise 分解，把原系数分为组间水平和正强度组内斜率；不外推为任意 pooled staggered TWFE 分解。逐项画相应 leads、报告剂量分布与对照构成；代数恒等式不是因果识别。
- 支持：[连享会](https://www.lianxh.cn/details/1933.html)；[Yu 预印本相关第3–4节，v2](https://arxiv.org/html/2609.09488v2)；[contdid 文档](https://cran.r-project.org/web/packages/contdid/refman/contdid.html)。边界：contdid ACRT 与 treated-only OLS 斜率不能等同；渠道版本冲突未解决时报告而非猜测，未运行教学代码。

## 样本选择 DID：先保留选择指标，再讨论 bounds

- 实践：政策可影响就业、存续或报告时，保留基期总体与选择指标，明确 always-observed 潜在子群目标；不能把缺失结果补零或默认 complete cases 识别总体 ATT。
- 正向选择单调性与稳定子群平行趋势不足以自动导出选择率比值。所查原稿还需要选择概率的处理/对照运输限制（Assumption 4(a)），及无预期、正概率/矩条件。识别区间不等于置信区间。
- 计算审计：整数 floor 修剪与强行至少保留一人可能改变有限样本 bound；分数分位点、零子群份额、选择率样本与结果可观测样本必须一致处理。平均选择率排序不是个体单调性的证明。
- 支持：[连享会](https://www.lianxh.cn/details/1836.html)；[Rathnayake等原稿选择/识别章节](https://arxiv.org/html/2411.09221v3)。边界：发布日期元数据有冲突、期刊审稿状态未核验；`leebounds` 教学调用不是该非随机处理 DID 框架的完整实现，未执行软件。

## 空间推断：写清允许相关的观测对

- 实践：区分同单位跨期、同年跨地区、不同地区不同年份的协方差支持。坐标、距离单位、核、时空带宽与政策分配层级均需记录；允许有依据的带宽探索，不能把选择后名义检验视为独立确证。
- Conley 类 VCE 处理误差依赖，不消除空间遗漏变量或政策溢出导致的识别偏差。若对照被污染，应调整暴露/比较对象，而非只更换标准误。
- 软件注意：所查 acreg 坐标带宽单位 km，空间 Bartlett 和时间 HAC 分开；fixest 的 `distance="triangular"` 是距离算法，不是三角核，所查文档的 Conley 核为 uniform。空间带宽变大不必令标准误单调增大。
- 支持：[连享会](https://www.lianxh.cn/details/1876.html)；[acreg作者正式论文](https://people.unil.ch/mathiasthoenig/files/2023/04/stata_journal.pdf)；[fixest文档](https://lrberge.github.io/fixest/reference/vcov_conley.html)。边界：Conley(1999)原文本次未直接读，命令未实跑；全国强共同因子未必符合局部弱依赖。

## 分层随机实验：估计权重与设计方差

- 实践：分开审计随机分配层、处理概率、目标人口权重、群规模与随机抽样/固定样本随机化。不同层处理比例下，普通 strata-FE 系数不自动等于人数加权 ATE。
- 所查 sreg 的 `cluster()` 指随机分配单位，可改变点估计及方差，不是通用 VCE 开关；层编号/配对顺序、缺失删除后的支撑和实际调整状态应审计。官方示例也需要检查处理后控制，不从可运行推断因果适当。
- 支持：[连享会正文](https://www.lianxh.cn/details/1948.html)；[sreg官方help](https://raw.githubusercontent.com/jutrifonov/sreg-stata/main/ado/sreg.sthlp)；[实现说明](https://raw.githubusercontent.com/jutrifonov/sreg-stata/main/docs/estimators.md)；[Bugni等设定与定理陈述](https://arxiv.org/html/1806.04206)。边界：未执行 sreg、未复现 Monte Carlo，文章应用控制的测量时点未独立查数据字典；观察性分组不是随机化层。

## Further audits by method

For DID target/scale/trend sensitivity see `did-target-sensitivity.md`; for IV assignment/strength see `iv-identification-audit.md`; for RD support/output semantics see `rd-running-variable-audit.md`; for donor support and interval targets see `synthetic-control-audit.md`. Existing applied lessons and local project supplements remain unchanged.

## 组间反应、处理版本与事件反应的不同目标

高组显著低组不显著不等于差异显著；比较大小及含协方差的组间差。异质性图可生成事后机制，但同一组别可符合多种解释，处理后分组还可能条件化中介/选择。允许广泛分组/窗口/尺度探索；保留切点、样本、失败与零结果，适用时按实际搜索族做联合推断或独立验证；cross-fitting不自动修正筛组。来源：[1555](https://www.lianxh.cn/details/1555.html)、[1556](https://www.lianxh.cn/details/1556.html)为教学评论，以上是独立方法判断，不冒充对应主论文证明。

区分随机获得机会A与实际接受版本T；A随机不使T随机。版本反应与版本分配成分需要各自潜在结果/可忽略性和支持，不能从分解名称识别歧视或福利最优分配。来源：[1684](https://www.lianxh.cn/details/1684.html)；[Heiler–Knaus v1](https://arxiv.org/html/2507.01517v1) §§4–6、[作者notebook](https://mcknaus.github.io/assets/code/RNB_HK2_decomposition.nb.html) S.1–S.2。本轮另回读notebook：女性d1=-35.381946是组别均值分解成分，不是培训处理差；女性真正DiM=12.295069，男性DiM=19.909288。不能据前者称女性培训负效应。notebook当前版本与v1可能不同，未运行作者代码/审全证明。

把估计事件反应作为第二步outcome时，第一步是带噪声测量非真实ITE。事件总体稳定要个体潜在时点限制或另一路径，分布不变/不拒绝不证明个体不变。full-horizon限制改变总体；第二步政策识别、生成误差与簇级推断另审。来源：[1708](https://www.lianxh.cn/details/1708.html)；[作者指定v2](https://arxiv.org/html/2403.19563v2) §§2–4/B.3/A.1、[unitdid作者文档](https://kazuyanagimoto.com/unitdid/)。原页面题名和抽取服务新版摘要冲突，采用指定版不混引，未审所有附录或复现。
