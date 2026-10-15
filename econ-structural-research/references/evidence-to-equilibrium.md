# 从简约式证据到均衡反事实

## 来源及证据层级

已读连享会[简约式与结构估计](https://www.lianxh.cn/details/1967.html)和[柏林墙到QSM](https://www.lianxh.cn/details/1958.html)完整正文。另核对[Gentzkow透明结构估计讲稿](https://web.stanford.edu/~gentzkow/research/fisher-schultz.pdf)相关页、[Chetty充分统计量作者稿](https://rajchetty.com/wp-content/uploads/2021/04/suffstat_ar.pdf)导言/相关章节、[Finkelstein访谈方法段](https://www.minneapolisfed.org/article/2015/interview-with-amy-finkelstein)及[柏林墙原论文](https://www.princeton.edu/~reddings/pubpapers/Berlin-Ecta-10876.pdf)设计、识别矩和反事实章节。未逐行证明、重估模型或执行工具包。下述是有边界的综合工作流建议，不是每位受访者或所有引用文献已核验。

## 方法选择不等于升级排名

简约式与结构证据互补。先展示数据事实，说明哪些变异和矩约束关键参数，区分模型原则上的识别与实际估计器使用的信息。对福利问题先判断是否可以用适当推导的充分统计量映射；该映射仍有模型、财政、外部性及规范性假设，不是任意DID系数加福利公式。不能概括为“只有全结构模型才能反事实”或“充分统计量绝不考虑均衡反馈”。选最小够用模型，区分识别、估计、反演、数值收敛和未用证据验证。

## 历史空间冲击如何约束结构

柏林原论文相关简约式是西柏林街区相对战前CBD距离的长期变化/空间异质暴露，不应简化成所有墙边对非墙边的标准两组事件研究。结构部分反演地点基本面并施加它们的变化与识别用距离暴露正交的矩限制；不是所有地点基本面绝对不变。生产和居住外部性的分离及通勤参数还依赖排除限制和其他信息。

实践：为每个参数写出数据对象、变异、矩、规范化和排除；历史冲击不自动识别所有深层参数。给定参数的唯一反演不同于参数全球识别，也不同于均衡唯一。记录优化非凸性、多起点/网格诊断及反事实均衡选择，不把拟合当这些条件的证明。

## 闭合决定反事实含义

柏林交通反事实采用开放城市、固定外部reservation utility和建筑面积总供给，并重新求解人口、通勤、工资和价格。封闭城市固定人口则不能照搬就业变化。识别用历史事实若已用于估计，不再作为独立验证；记录未用矩和外部检查。模型某交通实验不等于同时核算拥堵、污染与财政的完整福利。

适用时逐项声明开放/封闭、固定/内生人口、容量和供给、融资、偏好技术不变性、均衡选择。用局部处理系数线性乘一个新冲击不能冒充重新求解的均衡反事实。

## 复制学习边界

[ARSW2015 toolkit](https://github.com/Ahlfeldt/ARSW2015-toolkit)所读README说明它是部分模型量化的教学子集，不是全部论文复现。先核验数据/工具箱/内存和文件差异，再在授权环境做最小测试。读取文档、成功执行、数值验证和掌握模型为不同成果；本次没有执行MATLAB或复核所有附录证明。

## 最小模型的入门验收

从观测数量/份额与条件样本出发，连结参数、给定参数反演的基本面、行为方程、清算/规范化、政策变化与福利。只加反事实需要的选择模块；分离识别、反演唯一、算法退出与均衡选择。记录贸易平衡空间单元、赤字/财政闭合、人口与供给是否内生，检查标准化残差、约束、份额加总与多初值，再使用未进入校准/反演的事实验证。改变率求解可减少恢复水平基本面的需要，不自动减少识别假设。

来源：[连享会1960](https://www.lianxh.cn/details/1960.html)、[1968](https://www.lianxh.cn/details/1968.html)完整文字阅读记录；[Low–Meghir](https://doi.org/10.1257/jep.31.2.33) separability/validation相关片段；[Redding–Rossi-Hansberg](https://www.princeton.edu/~reddings/pubpapers/ARQSM-2017.pdf)引言与§2.7.4；[SciPy root官方说明](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html) Returns/examples。success只表示算法成功退出，不能代替经济方程残差与可行性验收。

[AB2022](https://github.com/Ahlfeldt/AB2022-toolkit)及[MRRH2018](https://github.com/Ahlfeldt/MRRH2018-toolkit)仅README定向阅读，后者明确教学变体不对应论文实质分析。工具包范围、平台/依赖和修改文件先审，未运行Stata/MATLAB，不以教学包或时间安排宣称全论文复现/模型掌握。

## 配置成本、支持规模和净福利的三层映射

等价财政支持不等于预算直接支出、净资源毁损或GE福利。现金/税收/信贷/土地各有观测与反事实基准；上市企业支持率外推和近邻地价比较保留选择、用途及开发条件限制。TFPR差异的楔子解释依赖技术、需求、竞争与计量基准，不把TFPR当物理技术排名。

IMF WP/25/155所读§2、§3将财政度量与政策计数—错配相关分析分开，原文明确后者不是因果估计。把条件残差方差映射到聚合TFP及资本调整后的GDP，需要该模型参数与闭合；不能混成同一个已识别中介链。财政规模加总与配置反事实有不同均衡处理，不笼统说全部PE或全面GE净福利。知识外溢、学习、融资、转移接受者与过渡成本未同账计量时，仅报告特定配置渠道，不冒充政策最优性。未复现原数据/量化值。

### 原源与阅读边界

- [Industrial Policy in China: Quantification and Impact on Misallocation](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025155-source-pdf.pdf)：§2 pp9—12 land/Total Size/caveats；p4潜在收益遗漏；§3 pp12—14模型、式1—2及associations声明；p19 Aggregate TFP Impact。版本/范围：IMF WP/25/155, August2025；PDF注明作者列表08/15/2025更新；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1848](https://www.lianxh.cn/details/1848.html)、[900](https://www.lianxh.cn/details/900.html)、[331](https://www.lianxh.cn/details/331.html)、[13](https://www.lianxh.cn/details/13.html)、[1545](https://www.lianxh.cn/details/1545.html)、[1465](https://www.lianxh.cn/details/1465.html)、[1389](https://www.lianxh.cn/details/1389.html)、[791](https://www.lianxh.cn/details/791.html)。这些是相应组文字正文阅读记录；不是所有图片已读。生产组记录9幅实质图已查看，其余相关组图像大多未读；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
