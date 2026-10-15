# 前沿效率：潜变量、空间反馈与DEA推断

## SFA不是普通残差排名
分开前沿技术、非负无效率u、双侧噪声和异质性。scaling u=h(Z)u*与截断正态均值mu=Zgamma+WZphi不是同一模型。分布、异方差与独立限制决定似然及预测；显著工具只涉及相关性，不认证排除限制或控制函数条件。

区分Wy联立反馈、WX前沿投入溢出和WZ无效率决定因素，不能把WZ当任意自回归u。W外生性、行列身份、归一化、可逆乘数和rho约束必须独立核验；time-constant W帮助不应转述为允许任意时变W。Kutlu所查内生扩展采用特定联合正态/独立基底与控制函数，不是任意内生性的通用修复。

## 效应矩阵与效率预测对象
在Galli特定前沿方程中，投入效应为(I-rho W)^(-1)(beta I+theta W)，直接效应取对角平均，间接效应汇总非对角反馈。裸beta不等于总效应。这个线性前沿式不能直接推广成任意E(u)或技术效率的导数；相关非线性截断修正仍未独立核全。

后估须区分E(u|e)、exp[-E(u|e)]和E[exp(-u)|e]；sdsfe帮助的u、jlms、bc对应不同对象，te汇报也不自动等于bc。空间反馈总损失与局部u另核，预测分布不是观测到真实效率或政策福利。帮助内部genwvars/genwxvars冲突保留，未运行安装版不承诺可执行语法。

## DEA基准与环境变量
先定义可比DMU、技术集合、凸性/可处置性、方向、规模报酬、参考集及离群点/维度支持。输出导向Farrell距离与其倒数尺度不同；VRS切换方向不能普遍只取倒数。SW两阶段的separability要求环境影响效率分布而非技术边界形状；环境改变技术时不能强行留在第二阶段。

## 抽样推断不修复政策内生性
共同估计参考前沿诱发效率得分依赖，不只是面板序列相关。所查SW软件论文以独立DMU截面为基础，不能直接当未经处理的聚类面板算法。边界得分的估计误差不同于Tobit删失DGP。算法1的截断回归/bootstrap与算法2另做DEA内层偏差校正不同，reps与bcreps分别记录；保留失败抽样、外部得分、方向和置信水平。bootstrap不令环境或治理变量外生。

旧SSC帮助头2016默认crs与2019软件论文默认vrs存在真实版本差异；显式指定rts、方向、参考集、算法及置信水平，并在实际运行前核安装版本。不推断今天程序默认，不把NIRS误解为递增。不运行研究数据，具体教程数值及全部证明均未复现。

### 原源与阅读边界

- [A spatial stochastic frontier model with endogenous frontier and environmental variables](https://eprints.lancs.ac.uk/149581/1/12042018_KKT_Spatial_SFA_Endogeneity_v.2_LK.pdf)：§2.1 accepted pp3—6，scaling/独立性/联合正态、控制函数及Jacobian。版本/范围：Lancaster作者接受稿；发表EJOR286(1),2020,389–399，非排版最终版；仅相关段落/静态文档核查，非全证明或软件运行。
- [sdsfe postestimation author help](https://raw.githubusercontent.com/kerrydu/sdsfe/main/sdsfe_postestimation.sthlp)：Syntax/Options for predict u, jlms, bc；Remarks。版本/范围：作者main快照；模板头1.0.0/10mar2015不作真实发布日；仅相关段落/静态文档核查，非全证明或软件运行。
- [A spatial stochastic frontier model introducing inefficiency spillovers](https://cris.unibo.it/retrieve/083788e9-c6d2-4576-a6da-503fdc4e4d84/11585_918308.pdf)：§3.3式9；§3.4式11。版本/范围：机构库最终接受稿；JRSS-C72(2),2023,346–367；DOI10.1093/jrsssc/qlad012；仅相关段落/静态文档核查，非全证明或软件运行。
- [sdsfe author help](https://raw.githubusercontent.com/kerrydu/sdsfe/main/sdsfe.sthlp)：Reporting te与genwvars段。版本/范围：作者main快照；版本号unknown；仅相关段落/静态文档核查，非全证明或软件运行。
- [Simar and Wilson two-stage efficiency analysis for Stata](https://journals.sagepub.com/doi/10.1177/1536867X19893640)：§2.1 common frontier/separability和Farrell方向；§2.3 reference/invert；§2.1脚注10及估计得分相关段；§2.2 Algorithms1—2；§2.3；§3.2 rts(crs|nirs|vrs)。版本/范围：Stata Journal19(4),2019,950–988；发表原作者软件论文；仅相关段落/静态文档核查，非全证明或软件运行。
- [simarwilson SSC help](http://fmwww.bc.edu/RePEc/bocode/s/simarwilson.sthlp)：help header v1.1/2may2016；rts选项。版本/范围：下载帮助头v1.1/2may2016；旧快照默认crs，与2019论文不同；仅相关段落/静态文档核查，非全证明或软件运行。
- [prodest maintainer README](https://raw.githubusercontent.com/GabrieleRovigatti/prodest/master/README.md)：软件定位与Citations段。版本/范围：抓取master快照；当前读取日2026-10-15；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1848](https://www.lianxh.cn/details/1848.html)、[900](https://www.lianxh.cn/details/900.html)、[331](https://www.lianxh.cn/details/331.html)、[13](https://www.lianxh.cn/details/13.html)、[1545](https://www.lianxh.cn/details/1545.html)、[1465](https://www.lianxh.cn/details/1465.html)、[1389](https://www.lianxh.cn/details/1389.html)、[791](https://www.lianxh.cn/details/791.html)。这些是相应组文字正文阅读记录；不是所有图片已读。生产组记录9幅实质图已查看，其余相关组图像大多未读；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
