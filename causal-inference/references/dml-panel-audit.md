# DML：面板变换、动态信息集与异质性评价

## 证据与适用边界
六篇连享会文字正文阅读记录及原源指定章节/官方文档经审阅综合。不是原论文全证明、全部图片、软件安装或估计复现。识别、nuisance预测、正交得分、分折和推断分工；低RMSE/更显著结果不认证外生性。允许广泛比较学习器、分折、子组，再形成事后假说；保存目标、样本、支持、seed及选择过程。

## 静态面板：变换不与非线性预测交换
Q(g(X))通常不等于g(Q(X))。先对所有变量去均值再学习非线性函数，不自动构造正确within nuisance。精确FD程序可用本期/上期水平X预测差分；CRE须明确固定效应与协变量均值的关系，而非把线性Mundlak性质普遍移植。静态、无反馈、同质/可加限制和有限维异质性扩展分别记录。

独立单位整条轨迹假设下采用单位block cross-fitting及相应得分聚类；但若学习单位dummy，留出新单位无法预测，与另一模拟框架不同。不能把某模拟建议写成面板一律逐行随机分折。先问固定效应如何消除/建模以及新单位可预测性，再选split。共同时间冲击、跨单位相关和少数簇另审；分折不代替方差处理。

CRE校正处理预测的均值项是Dbar_i，而不是D_it：对应 mhat_it + Dbar_i - mhatbar_i。教程1664的当期D写法改变残差，须查所用实现。DML2合并得分与重复分折平均应分别记录，原稿/教程歧义不伪称已解决。1665数据文件名、样本尺寸和变换衔接有静态疑点，未下载数据不认证输出。

来源：[1687](https://www.lianxh.cn/details/1687.html)、[1664](https://www.lianxh.cn/details/1664.html)、[1665](https://www.lianxh.cn/details/1665.html)；[Fuhr–Papies v1](https://arxiv.org/html/2409.01266v1) §§1–3、5（点估计模拟，不提供一般有效CI）；[Clarke–Polselli v5](https://arxiv.org/html/2312.08174v5) §§3–5与CRE Step3公式。最终OUP全文未取得，XTDML完整源码和历史默认未审。

## CATE与政策规则：平均对象不是个人真值
CATE、预设组GATE、按预测排序GATES、路径效应和政策价值不同。CATE不是个体不可同时观测的真实差值；AIPW伪结果不是已观测ITE。森林honesty、nuisance cross-fitting、排序组样本外学习与政策独立评价有不同职责。噪声可制造预测效应分散；变量重要性/SHAP或异质性投影不证明机制。

不是所有meta-learners都双重稳健或自带有效CI；EconML观测混杂框架仍需相应可忽略性和支持。DeepIV第二步损失对第一阶段处理条件分布积分，不是直接拟合观测E[Y|T,X]；有效IV条件不能被神经网络替代。

来源：[1657](https://www.lianxh.cn/details/1657.html)、[1635](https://www.lianxh.cn/details/1635.html)；[EconML DML官方](https://econml.azurewebsites.net/spec/estimation/dml.html)、[meta-learners](https://www.pywhy.org/EconML/spec/estimation/metalearners.html)、[forest](https://www.pywhy.org/EconML/spec/estimation/forest.html)相关段；[Stata cate](https://www.stata.com/manuals/causalcate.pdf)及[后估计](https://www.stata.com/manuals/causalcatepostestimation.pdf)仅可恢复的描述/语法开头；[DeepIV作者摘要](https://proceedings.mlr.press/v70/hartford17a.html)。全部gatetest语法、旧DeepIV示例与证明未核。

## DynamicDML：未来处理nuisance与倒推不可省
在所查线性动态框架中，每期t需学习最终结果E[Y_m|X_t]，并对j>=t学习E[T_j|X_t]；再由末期向前剥离未来处理效应解矩条件。每期各做静态残差回归不是此算法。序贯外生性、残余处理变异和路径干预解释须明确；未来处理固定下的路径效应不等于自然自适应决策继续发生时总效应。

传入前检查id/time顺序、等长组与缺期；groups不自动理解日历。所查API只用第一期X作异质性，后期作控制。不要把演示tests模块手工复制成默认部署方案。来源：[1577](https://www.lianxh.cn/details/1577.html)；[Lewis–Syrgkanis](https://arxiv.org/html/2002.07285) §2–2.2/Algorithm1；[官方DynamicDML](https://econml.azurewebsites.net/_autosummary/econml.panel.dml.DynamicDML.html) fit/cv/effect相关段。未审一般SNMM附录或运行包。
