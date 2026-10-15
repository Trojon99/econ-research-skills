# RD：支点、地理边界、协变量与推断口径

基于六篇连享会完整文字正文及定向原源核验记录综合，图片未全OCR，未执行R/Stata或读取应用数据。允许探索窗口、边界点与子组；展示探索范围和选择记录，适用时安排独立信息/联合推断，不把不拒绝诊断当识别认证。

## 1. 参数先于距离或命令

sharp是断点局部效应，不是总体ATE；fuzzy除连续性需第一阶段、排除、单调性等。地理RD逐边界点tau(b)与pooling边界加权平均不同：相同最短距离未必地理相近，无法恢复每点效应不等于任何条件下都不能识别平均。检查密度、几何、两侧支持、复合政策、迁居与传播。非参数不自动处理空间相关，多个邻域共享观测还需协方差。

来源：[1792](https://www.lianxh.cn/details/1792.html)、[1793](https://www.lianxh.cn/details/1793.html)、[1193](https://www.lianxh.cn/details/1193.html)；[Keele–Titiunik](https://rdpackages.github.io/references/Keele-Titiunik_2015_PA.pdf?download=1) 识别/估计段；[BD v3预印本](https://arxiv.org/html/2511.06474v3) pooling/pointwise理论段。Keele提取有截断，新泽西制度细节未完全核查；1193原指南仅摘要/记录，不延伸认证其所有应用。

## 2. 估计、SE、p与CI必须同口径

带宽mserd不把返回矩阵第一行Conventional变成Robust。按具名行检查；Stata区分tau_cl/tau_bc、pv_cl/pv_rb、ci_l_rb/ci_r_rb。可明确报常规点估计加RBC推断，但不能把常规p/SE冒充RBC。控制后样本变化、h/b变化应分开；失败回退对象要保留真实标签，固定较小h不自动证明欠平滑。

来源：1793、[517](https://www.lianxh.cn/details/517.html)；[rdrobust R源码](https://raw.githubusercontent.com/rdpackages/rdrobust/master/R/rdrobust/R/rdrobust.R) 返回行；[Stata作者help](https://raw.githubusercontent.com/rdpackages/rdrobust/master/stata/rdrobust.sthlp) Stored results。文档级核对不承诺旧API/本机版本，未复制教程为tested模板。

## 3. 操纵检验的对象和离散支点限制

密度检验考察左右密度极限，不证明潜在结果连续或处理效果；先查舍入、heaping、记录与样本选入。`bwselect(each)`分别选两侧，`diff`为密度差的共同带宽；按真实阈值与实际help设置。真正粗离散支点不可机械套连续密度检验；masspoints数值检查不补足离散外推识别。

来源：[869](https://www.lianxh.cn/details/869.html)；[Cattaneo–Jansson–Ma](https://nppackages.github.io/references/Cattaneo-Jansson-Ma_2020_JASA.pdf) 方法段；[作者rddensity help](https://raw.githubusercontent.com/rdpackages/rddensity/master/stata/rddensity.sthlp) 带宽选项。未运行。

## 4. 支点数量决定外推信息

报告两侧独特取值、距断点最近距离、支点人数和各h下支持；增加同一支点人数不缩小固定间距。按running-value聚类不能修正函数误设偏差。bias-aware/honest区间依赖明示曲率/Lipschitz函数类及单位、上界依据与敏感性，不是无条件保守认证；局部随机化要额外论证赋值机制。

来源：[565](https://www.lianxh.cn/details/565.html)；[Kolesár–Rothe作者稿](https://arxiv.org/pdf/1606.04086) discrete support/coverage段；[官方发表摘要](https://www.aeaweb.org/articles?id=10.1257/aer.20160945)。旧RDHonest接口仅镜像交叉核验，作者页面失败；不认证旧代码已迁移可运行。

## 5. 控制变量是精度路径，不是修复sorting

有效无控制RD本来可一致；共同加性调整在协变量断点均值连续等条件下保留原参数。预定不受处理变量可改善精度，不自动拆分复合政策。共同完整样本/固定h-b比较后，再单报重选带宽结果。阈值token冲突保留原值并查制度，不擅自把59.1968、59.198和59.1984统一；资格/鼓励不等于实际参与。

来源：517；[Calonico等作者稿](https://arxiv.org/html/1809.03904) Lemma1/Head Start表。原教程p/CI混用为已记录错误，处理分类影响和制度token差异未用数据解决。


## 局部连续性、资格与时间定义

sharp的D=1{X≥c}在给定X没有常规matching式双侧处理支持；在两侧可趋近c、相应潜在结果均值连续等条件下，观察均值两侧极限差识别τ(c)。这不要求X与Y无关，也不自动使任何有限带宽内成为随机分派；局部随机化须另写窗口、赋值机制及相应限制。

fuzzy先保留资格Z、实际D、ΔY与ΔD；局部排除、单调、一致性及非零FS等成立时才把ΔY/ΔD解释为cutoff被移动人群效应。资格的reduced form本身可以是政策对象，不冒称take-up LATE；多维覆盖/待遇同时变化也不能无论证缩成单一处理效应。使用一致的局部比较方向/样本及相容拟合，弱跳跃另审推断。

donut扩大到c的外推缺口，不自动消除sorting或识别另一个LATE。比较窗口/语言实现前固定assignment时点、running-variable时点、结果horizon和样本筛选；中心化及左右交互决定系数是否为c处截距差，bins、kernel、带宽和多项式阶数不是同一选择。

来源：Cunningham[第一版第6章](https://mixtape-1ed.netlify.app/06-regression_discontinuity) §§6.1–6.4，2026-10-15快照；以上是reading-level有条件概念综合，非原应用、RKD全理论或最新软件复制。RBC/离散支持等既有门槛继续保留；不从教材年代的软件可用性断言当前不存在实现。
