# 持续期：时钟、风险集与不同生存对象

## 先定义观察机制
列事件、单位、时间尺度/time zero、何时成为风险对象及实际可观察entry。origin、enter和逐记录time0不互换；同人多记录未指定time0的默认接续不证明真实gap也被观察。保留(start,stop]、重叠/非正区间、gap、person-time和每种退出原因；数据一致性不能验证独立左截断或非信息删失。

左截断是早期失败者未入组，左删失是已知事件更早但时间不清，区间删失是同一事件仅知位于区间。按码本显式failure，R Surv的0/1、1/2和factor编码不可猜。粗年月记录还要明确暴露/失败同期间先后，不能以单个>=符号替代时序判断。

## Immortal time与时变系数不同
不按最终是否治疗回填基线组：治疗前人时归未暴露，实际开始后才改变状态，在共同time zero下按事件时风险集比较。只挪treated起点或删等待期不是一般修复；landmark限定为该时点仍在观察且未失败者，改变起点与总体。

实际X_i(t)变化不同于固定X的beta(t)变化；tvc/texp构造时间交互，不知道何时开始治疗，不能替代真实暴露分段。终点定义状态时核区间内提前归属。修复immortal time仍不处理治疗选择、时变混杂或后处理选择；动态暴露组KM/RMST也不自动是固定基线组曲线，不发布未核合法性的具体命令模板。

## 选目标而非替换标签
PH中exp(beta)为hazard倍率，不是固定期限风险比或风险差；AFT为时间缩放，nohr系数非百分比。分开S、F、h、H，RMST写共同tau而非无限平均寿命。

若其他事件阻止目标事件发生，区分cause-specific hazard与真实世界CIF。把其他事件作删失可估cause-specific hazard，不使其1-KM成为CIF；Fine–Gray subhazard ratio不是普通HR或风险比。全因死亡本身不需再将各死因当这种目标的竞争事件。事件编码缺失不能靠换命令恢复，模型/PH诊断不构成政策识别。

## 相对生存与标准化
在相应背景死亡/超额hazard假设下，相对生存可解释为去除其他死因的net survival，不是生命表给出了无癌随机对照。Lambert方法的1/S*(t)逆期望生存与p_ref/p_sample外部标准化权重目的不同，需按子组计算权重和期望hazard。分割间隔、人内相关、生命表外推和参照人群分别审计；应用中的某个步长不是通用阈值。mrsprep当前实现/单位、frame及分母未独立核，不能复制成tested流程。

## 生命历程序列是另一种对象
Halpin所查段落以整条离散状态路径而非单次hazard为对象。先定义状态、时间对齐、长度/缺失与替换/indel成本再聚类；转移率不等于替换成本，距离矩阵相关不等于分类一致性，可另比较ARI。描述性分群可帮助探索，但这里不声称政策识别或唯一正确类别数，未核全部实现版本。允许探索窗口/状态/机制，保存改变的支持与对象，不强制预注册。

### 原源与阅读边界

- [stset — Declare data to be survival-time data](https://www.stata.com/manuals/ststset.pdf)：PDF pp5–7,30–33,36–38。版本/范围：在线手册r19示例，取得于2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [Create a Survival Object (Surv)](https://stat.ethz.ch/R-manual/R-devel/library/survival/html/Surv.html)：Arguments: event,time2,type；Details: interval2与逻辑事件编码。版本/范围：survival3.8-6；R-devel动态文档，取得于2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [Immortal Time Bias in Observational Studies of Time-to-Event Outcomes: Assessing Effects of Postmastectomy Radiation Therapy Using the National Cancer Database](https://pmc.ncbi.nlm.nih.gov/articles/PMC6053873/)：Methods: Other measures, Landmark analysis, Time-dependent Cox models。版本/范围：2018公开原文，取得于2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [stcox — Cox proportional-hazards model](https://www.stata.com/manuals/ststcox.pdf)：PDF pp3,5,11–16。版本/范围：在线手册r19示例，取得于2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [streg — Parametric survival models](https://www.stata.com/manuals/ststreg.pdf)：PDF pp4–7。版本/范围：在线手册r19示例，取得于2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [stcrreg — Competing-risks regression](https://www.stata.com/manuals/ststcrreg.pdf)：PDF pp5–7。版本/范围：在线手册r19示例，取得于2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。
- [Direct modelling of age standardized marginal relative survival through incorporation of time-dependent weights](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-021-01266-1)：Background; Methods Eqs1–7; Discussion。版本/范围：BMC Medical Research Methodology2021,DOI10.1186/s12874-021-01266-1；仅相关段落/静态文档核查，非全证明或软件运行。
- [SADI: Sequence analysis tools for Stata](https://www.rama.mahidol.ac.th/ceb/sites/default/files/public/pdf/stata_journal/sj17-3.pdf)：Printed pp546–555 §§1–6.5开头及p556 ARI段；PDF pp36–46。版本/范围：Stata Journal2017,17(3):546–572,st0486；大学公开镜像；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1403](https://www.lianxh.cn/details/1403.html)、[1324](https://www.lianxh.cn/details/1324.html)、[633](https://www.lianxh.cn/details/633.html)、[482](https://www.lianxh.cn/details/482.html)、[508](https://www.lianxh.cn/details/508.html)、[399](https://www.lianxh.cn/details/399.html)、[53](https://www.lianxh.cn/details/53.html)、[1541](https://www.lianxh.cn/details/1541.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
