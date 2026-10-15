# DID 的目标、尺度与趋势敏感性

## 证据与使用方式

基于六篇连享会完整文字正文的阅读记录及原论文指定章节/官方帮助核验，经综合审阅形成。不是原论文全部证明审查、软件运行或示例复现；图片并未全部逐图核验。可广泛探索尺度、窗口、控制和处理路径，再形成事后假说；保留规格账本并说明目标、样本和比较的变化，不把筛选后结果冒充唯一预设检验。既有预趋势功效/样本选择主题见 `applied-estimand-inference.md`，此处不重复。

## 1. 基线相关趋势：新比较不是同一 ATT 的免费修复

在真正未处理的样本中检查基线水平与后续变化；模拟与实际分配机制相近的伪处理。差分回归控制基期结果对应水平面板中的基期×时期交互，不能只加入被单位FE吸收的基期主效应。基期暂时冲击/均值回归仍可能带来偏误。匹配和共同支持删除改变目标人口，人口权重改变参数；按分配阈值比较结果变化得到局部参数，不是全体ATT。估计接近是证据，不证明所有假设。

来源：[连享会1902](https://www.lianxh.cn/details/1902.html)；[Sager–Singer 2023作者稿](https://www.lse.ac.uk/granthaminstitute/wp-content/uploads/2023/09/working-paper-376-Sager-Singer_Sept_2023.pdf) II.B–D与Table1。发表版PDF403，仅[官方发表记录/摘要](https://www.aeaweb.org/articles?id=10.1257/pol.20220745)另核；不跨版本复制未核表值。

## 2. PPML：条件均值的乘法反事实不是水平PT

区分 E[log(1+Y)|X]、log(1+E[Y|X])和原尺度条件均值。非负/零值多只是入口，须写明条件均值模型。指数均值下的两组两期共同时间结构是同比例变化，不是水平DID的同绝对增量；换尺度改变参数和反事实含义。处理为二元且共同相对效应模型具有可信因果解释时，再讨论 exp(beta)-1；连续剂量与异质效应另定义目标。筛选Y>0不自动识别因果内涵边际。

PPML无需真实Poisson分布，但仍需正确条件均值及适当推断。记录 `e(N_full)`、`e(num_singletons)`、`e(num_separated)`、最终样本和收敛；零值可进入不等于每个零值必保留。来源：[连享会1809](https://www.lianxh.cn/details/1809.html)；[Cohn–Liu–Wardlaw作者稿](https://faculty.mccombs.utexas.edu/jonathan.cohn/papers/Count_data%202022aug10.pdf) §1.1–1.5；[ppmlhdfe官方help](https://scorreia.com/help/ppmlhdfe.html) Background/Stored results。未独立核验教程应用原表，未运行命令。

## 3. 分批处理：对齐比较、支持和聚合权重

先选择group-time ATT、动态聚合、插补目标或切换处理参数；统一接口不意味着同一参数。CS需无/有限提前反应、指定never/not-yet对照的条件趋势与overlap；BJS反事实只用未处理观测拟合，预测支持与识别限制不能被好拟合取代。动态曲线每一期的队列构成可能不同。

经典无协变量、二元吸收处理Bacon分解的2×2比较权重，与进一步展开group-time效应的负权重不是同一对象；already-treated比较可有污染，不必有负的2×2权重。不要认证未查实现的 `negative_weight_share` 为问题比较占比。效应异质不必破坏未处理结果PT，污染来自将已处理变化当干净反事实。AIPW双重稳健不免除识别与支持条件。

来源：[连享会1805](https://www.lianxh.cn/details/1805.html)、[1399](https://www.lianxh.cn/details/1399.html)；[CS作者稿](https://arxiv.org/html/1803.09015) §2.3；[BJS作者稿](https://arxiv.org/html/2108.12419) §4.1–4.2；[Bacon WP25018](https://www.nber.org/system/files/working_papers/w25018/w25018.pdf) Theorem1/式7；[Stata异质DID后估计](https://www.stata.com/manuals/causalhdidregresspostestimation.pdf) aggregation/sci。StatsPAI未运行或核验实现；当前手册能力不保证历史版本可用。

## 4. 剂量切换：有stayers与quasi-stayers的条件分开

AOSS为switchers的平均区间斜率，WAOSS另按绝对剂量变化加权；两者一般不同。给定基期剂量的趋势可比和stayers支持不能省去。无真实stayers的quasi-stayer路线还需静态潜在结果、局部支持与平滑条件；常规参数速率需要额外函数族限制，不能把有stayers结果直接搬过去。

IV-WAOSS还需工具排除限制、第一阶段/约化式条件趋势、单调性和支持；目标是工具诱发的complier-switchers，不是总体剂量效应。正权重参数不保证有限样本估计符号；较窄区间不证明弱工具稳健。来源：[连享会1740](https://www.lianxh.cn/details/1740.html)；[有stayers作者稿v3](https://arxiv.org/html/2201.06898v3) §§2–4及5.1–5.3；[无stayers 2024短论文](https://gvazquezbare.github.io/papers/Chaisemartin-DHaultfoeuille-VazquezBare_2024_AEAPP.pdf) I–IV。未运行ado或访问案例数据，最新版本理论未全面对照。

## 5. HonestDiD：限制的是偏误路径，不是已检验为真

先选目标l' tau_post和合适的事件研究估计器。RM约束后期相邻偏误变化相对前期最大相邻变化；SD约束离散二阶差分，M=0仍允许非零线性差异趋势，不等于PT。记录结果单位、时间间隔、网格、目标和协方差；网格给的是结论破坏区间，不是偏误真值。保证依赖限制集合和推断条件，不是任意有限样本95%。

`pre/post` 为系数位置；`omit` 按遗漏标记处理，不是删除所有数值零；自定义b/V须显式传入并对齐排序。平均后期效应不等于默认首期目标。不能用趋势敏感性模块修复异质性污染的TWFE参数。来源：[连享会1467](https://www.lianxh.cn/details/1467.html)；[Rambachan–Roth发表版](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf) §§2.1–2.4；[作者Stata README](https://github.com/mcaceresb/stata-honestdid) RM/SD/average/staggered。未运行例子或验证本机插件。

## 6. 水平与对数异号：分布、方向与支持一起审

饱和四格log-OLS差的是E[logY]，exp(beta)是几何均值之比的比，不普遍是算术均值增长比；重变换因子须有额外抵消条件。共同正值样本/零负值删除、窗口和群体构成另列，两个尺度各有反事实限制，不能以某尺度pretrend不拒绝决定真实DGP。

[连享会1340](https://www.lianxh.cn/details/1340.html)与[McConnell v1](https://arxiv.org/html/2308.00167v1) §2/命题1的绝对值反号条件缺方向限制。独立标准库反例：四格确定正值10、20、20、29满足该绝对值不等式，但levels=-1且log DID=-0.3215836241，同为负。对算术四格比例比，正分母下需方向条件alpha4*(alpha1*alpha4-alpha2*alpha3)<0；真正E[logY]还依组内分布。反例不是作者代码运行或实证复现。

迁移DID实现先对齐单位/时间、缺失/单例、权重、自由度、对照及各horizon支持。DID2S第一阶段仅未处理，生成误差需进入正确两阶段推断；软件相同公式不证明同一estimand。来源：[1895](https://www.lianxh.cn/details/1895.html)；[PyFixest官方](https://pyfixest.org/tutorials/difference-in-differences.html)指定段、[Butts–Gardner](https://journal.r-project.org/articles/RJ-2022-048/)方法/聚合段。教程watermark/发布版不同，精确LP-DID API未恢复，未执行。


## 均值趋势、第三差分与动态构成

在同一人群/尺度、无提前反应及干净对照等条件下，2×2总体DID=ATT+{E[ΔY(0)|T]−E[ΔY(0)|C]}；样本四格差仍有抽样/分派波动。按水平或收益选择不必破坏Y(0)均值PT；按暂时冲击/未来增长选择则可能失败。该均值限制不普遍等价静态FE的全路径strict exogeneity，异质处理反应也不等于未处理趋势失败。

DDD=DID_eligible−DID_comparison，关键是无处理时eligible−comparison差距在处理/对照地区趋势可比，而非要求两个DD各自无偏。两个DD可有相同偏误并抵消，placebo DD非零不单独否定DDD；须另审其他格子的处理/溢出、尺度、composition和无提前反应。按2×2×2写清全部低阶项或解释等价吸收，不因回归叫DDD就默认实现了第三维。

第三维对照的暴露须按实际cohort×time复查，近年龄组可能共享冲击也可能被溢出或后来暴露。重复截面/完整平衡面板的筛选会改目标；若政策改变谁出生/被观测，cohort率的改变含composition，不无条件解释成固定同一组人的平均作用。

把公告、生效、实际暴露和提前反应分开；归零期若已受处理，leads相对它不等于纯未处理差异。不强制删过渡期，探索版本分别记账。每个horizon保留贡献cohort、对照、样本/处理簇及归零期；先识别cohort-time效应再按问题聚合，完整协方差进入SE。限制长期支持或平衡事件窗口会改构成/目标，不能平均污染TWFE系数来修偏误。

改变面板窗口可同时改2×2效应和分解权重，系数变化不一概是混杂变化。late-on-early比较的动态污染是早组ATT在两个比较期的signed增量的相反数，汇总还乘实际比较权重；绝对值增大不普遍推出负bias。非负2×2比较权重和可能为负的ATT展开权重继续分开，不扩展最简分解到任意控制、反转或不平衡面板。

来源：Cunningham[第一版第9章](https://mixtape-1ed.netlify.app/09-difference_in_differences) §§9.2、9.4–9.6，2026-10-15快照；[Olden–Møen](https://academic.oup.com/ectj/article/25/3/531/6545797)，Econometrics Journal2022，§5 Eqs5.1–5.7，定向原源核gap-PT而非全文证明。cohort聚合另对照[CS作者稿](https://arxiv.org/html/1803.09015) §3.1.1 Eq3.4；未执行作者实现。signed污染只作指定代数比较，未重估应用。当前软件选项/安装版另核，不由这份第一版阅读更新整个现代DID前沿。
