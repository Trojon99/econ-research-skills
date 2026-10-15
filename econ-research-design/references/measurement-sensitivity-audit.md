# 从数据模式到测量、选择与有界敏感性

基于六篇连享会完整文字正文及原源指定章节/摘要/help/README记录经审阅综合。鼓励先看图和结果，再形成事后假说；为重要模式写当前解释、竞争解释及最便宜区分证据。记录筛选不等于强制预注册；保持证据与推断分开，未执行的软件不当模板认证。

## 1. 方向、归零、大小与识别集分开

敏感性约束可能产生多根或不连续可行集，归零阈值大不保证反号阈值大。针对研究结论报告符号、经济大小或完整集合，同时说明选择比率、长回归R²及最大偏误的限制。固定共同样本比较控制贡献；识别集不含零不是已完成抽样显著性检验。不要把条件定理推广成所有回归方向不可靠。

来源：[1916](https://www.lianxh.cn/details/1916.html)；[Masten–Poirier作者稿](https://arxiv.org/html/2208.00552) §2、§3.1 Theorem2/假设A1–A4及Figure1。记录版本为2026-05-08，期刊最终表号/元数据未独立全部核验；正定、选择比率、非零控制载荷及控制指数正交等条件不能省去。未运行regsensitivity。

## 2. 代理是测量映射，不是换变量名

先定义预测、构念测量、构念效应或机制目标。P=pi X*+u时经典衰减结论需测量载荷、单位、误差与外生性条件；只有pi=1归一化才可直接用beta×信度表达。载荷方向/跨组稳定、共同记录偏误和测量误差需审计；多个代理一致不证明构念有效。替换指数保持原方向/分母/币值/年龄定义，不无条件取绝对值重新赋意。重复测量IV、验证样本或潜变量模型须有自己的识别证据。

来源：[1758](https://www.lianxh.cn/details/1758.html)；[Bharath等作者论文](https://webuser.bus.umich.edu/ppasquar/microcorp.pdf)首页/摘要及[作者书目](https://webuser.bus.umich.edu/ppasquar/publishedpapers.html)。核验支持资本结构/逆向选择风险研究，不支持教程全部相关系数或代理构造细节。尺度结论是明示条件下的独立代数判断，不冒充所有原论文已审。

## 3. 可观察结果被人为丢掉与选择性不可观察分开

按Y筛样本可诱发X-误差关联；按X筛选在指定模型下或无害，但异质效应下可改变目标分布。先考虑保留合法零/负值，或明示两部分对象，不为自己制造的缺失自动升级Heckman。真实不可观察时留总体选择指标，论证排除、误差分布、MAR/MNAR与overlap；选择模型、加权、插补、bounds由观察机制选择。Mills不显著不认证不存在选择偏差。

来源：[1815](https://www.lianxh.cn/details/1815.html)；[Davies原博客](https://bldavies.com/blog/understanding-selection-bias/)全文含异质性脚注；[Stata heckman](https://www.stata.com/manuals/rheckman.pdf)描述/语法。未运行教程模拟或mroz，种子/软件不同不预期数值相同。

## 4. 非线性由关系与对象选择，不由单变量正态性

OLS不要求X/Y无条件正态。区分E(logY|X)与logE(Y|X)，不要把任何变换或永不变换写成禁令。明确link及原尺度金额/概率/odds/百分比对象；logit系数指数是odds比不是概率倍数。非线性link下即无乘积项原尺度边际效应也可随协变量变动，需相应差异与不确定性。支持范围外拐点不叫数据证明U型。可用图、样条和预测学习函数形式，标明探索；同样本同对象比较，而非只看直方图或星号。

来源：[1612](https://www.lianxh.cn/details/1612.html)；[Rönkkö等出版社](https://journals.sagepub.com/doi/10.1177/1094428121991907)仅摘要/元数据恢复，PDF超时/HTML403，八条全部原论证未核。PPML细节转causal-inference的did-target-sensitivity参考，不重复搬入未核比较表。

## 5. 按最小反事实需要进入结构学习

模型分类不是可信度排名。把观测量、参数/载荷、不可观测对象、行为、清算/规范化、政策变化与福利连起来；以需要开放的选择和反馈决定复杂度。识别、给定参数反演、校准、基准求解与反事实验证分开。资源范围和工具包不等于论文全复现。

来源：[1960](https://www.lianxh.cn/details/1960.html)、[1968](https://www.lianxh.cn/details/1968.html)；[Low–Meghir](https://doi.org/10.1257/jep.31.2.33)相关片段；[Redding–Rossi-Hansberg](https://www.princeton.edu/~reddings/pubpapers/ARQSM-2017.pdf)引言/§2.7.4；[AB2022 README](https://github.com/Ahlfeldt/AB2022-toolkit)、[MRRH2018 README](https://github.com/Ahlfeldt/MRRH2018-toolkit)。未运行Stata/MATLAB，未通读全部模型证明。实际onboarding见结构技能evidence-to-equilibrium参考。

## 文本预测进入推断的专门审计

当代理来自LLM标注/embedding，加载 `text-measurement-inference.md`，分别审计构念、参照标注程序、校正抽样、目标score、训练泄漏和平台漂移。高一致率不替代上述环节；阅读/静态软件核对不等于已执行。原有测量、选择与尺度规则保持。

## 预测信息集、校准和政策对象

冻结index时点、实际可取得的特征、标签horizon与随访支持；claims诊断可能反映就医/记录而非潜在健康。事后回填支出可用于事后描述，不能进入事前风险特征。调参、ensemble权重、校准和最终测试分离；病例平衡后的概率不自动是原人群风险，理论基准率还原与经验校准须分别说明。未核完整抽样定义时不移植修正公式或超参数。

Einav等2018主文及附录A/B区分同一基线向前支出与死亡后回填口径；事后死亡者支出高不证明事前已知必死者的浪费。现行照护下的死亡预测不是不给治疗的死亡风险；AUC与风险分布不识别任何具体治疗的成本、生存、生活质量或最优政策。内部随机留出不叫外部验证，外部校准候选另留待核。这里只整合信息集/内部校准与政策对象边界，未执行预测或读取研究数据。

### 原源与阅读边界

- [Supplementary Materials for Predictive modeling of U.S. health care spending in late life](https://web.stanford.edu/~leinav/pubs/Science2018_Appendix.pdf)：PDF pp2–9 §§A.1–A.2,B.1–B.6。版本/范围：2018-06-29作者公开附录；同一研究子材料，不计独立研究；仅相关段落/静态文档核查，非全证明或软件运行。
- [Predictive modeling of US healthcare spending in late life](https://pmc.ncbi.nlm.nih.gov/articles/PMC6038121/)：Main Text: baseline predictors, spending definitions, final paragraph lines87–117。版本/范围：Science2018-06-29,360(6396):1462–1465,DOI10.1126/science.aar5045；PMC作者稿；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1403](https://www.lianxh.cn/details/1403.html)、[1324](https://www.lianxh.cn/details/1324.html)、[633](https://www.lianxh.cn/details/633.html)、[482](https://www.lianxh.cn/details/482.html)、[508](https://www.lianxh.cn/details/508.html)、[399](https://www.lianxh.cn/details/399.html)、[53](https://www.lianxh.cn/details/53.html)、[1541](https://www.lianxh.cn/details/1541.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
