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
