# 中介与调节：时间、干预对象和尺度

六篇连享会文字正文及定向原源/官方帮助记录经审阅综合，非图像全审、软件运行或证明复现。机制探索可先于正式识别；加入候选中介、分组或描述关联可生成假说，不把政策总效应识别自动传递到M-Y关系。

## 先画W→A→Z→M→Y，再选参数
W为前定混杂，Z为处理改变的中介-结果混杂。自然效应配对为TE=PNDE+TNIE=TNDE+PNIE；有交互时不能随意把同一编号的direct/indirect相加。CDE(m)固定所有人的M为m，不是每人自然M(0)，TE-CDE一般不等于NIE。

随机干预中介从M(a)|W分布抽取，与个体中间混杂实现分开。IDE/IIE分解的是相应随机干预总对比；有Z时不自动等于普通自然TE。direct只排除所指定中介集合，不表示没有其他路径。多中介联合间接效应不自动给每条路径份额。

来源：[1825](https://www.lianxh.cn/details/1825.html)、[1802](https://www.lianxh.cn/details/1802.html)；[Farbmacher等](https://arxiv.org/html/2002.12710) estimands/assumptions/DML相关段；[Díaz等](https://arxiv.org/html/1912.09936) 定义、识别、正性/误差率。不是最终发表版全篇校对。

## 方法支持取决于处理后混杂
处理随机不随机化M；自然效应仍需M-Y条件外生、支持及其他跨状态限制。DML降低nuisance误差不消除遗漏混杂，root-n/渐近推断需实际收敛率和乘积误差条件，不能说任意学习器自动满足。trimming是支持/总体变化，不等于遗漏混杂敏感性。

CMAverse所查文档postc非空时走msm/gformula并转randomized analogues，不能塞进rb示例声称同一对象。rwrmed是regression-with-residuals，不是残差加权或IPW；残差化相对于已观测过去，仍需模型正确与无遗漏混杂。bootstrap应重拟合完整生成残差链；所查作者delta讨论未涵盖全部生成残差误差。

来源：[1797](https://www.lianxh.cn/details/1797.html)、[1422](https://www.lianxh.cn/details/1422.html)；[cmest官方Details](https://bs1125.github.io/CMAverse/reference/cmest.html)、[cmsens](https://bs1125.github.io/CMAverse/reference/cmsens.html)；[Linden–Huber–Wodtke作者稿](https://lindenconsulting.org/documents/RWRMED_Stata_post_review_FINAL.pdf) §§1–3，尤其2.2。此轮另回查cmest公开页，未运行包。

## 统计分解、敏感性和功效不能互相替代
KHB处理嵌套logit/probit系数重标度，因果中介解释另需顺序可忽略性等；APE是概率尺度而非潜在指数尺度。mediation E-value与TE的E-value对应不同混杂关系/额外RR转换假设。总效应近零或反号抵消时，中介比例不稳定或超出[0,1]，不可强行写机制贡献。

交互功效针对指定beta3和数据依赖；两组各自显著与否不等于差异检验。保留相关结构、信度、分布和簇级独立信息。含主效应完整OLS里中心化是重参数化，不一般提高交互检验功效。不要传播未核验的最佳相关系数区间或最小人工样本量。

来源：[1404](https://www.lianxh.cn/details/1404.html)、[1705](https://www.lianxh.cn/details/1705.html)；[Breen等出版社摘要](https://journals.sagepub.com/doi/abs/10.1177/0049124113494572)及[作者KHB说明](https://ora.ox.ac.uk/objects/uuid:3522f94e-dd91-4d35-bc5c-446d8379e8e3/files/m13ac0f5234729deb6e3e9f89a758ecd0) 同尺度段；[InteractionPoweR作者vignette](https://dbaranger.github.io/InteractionPoweR/articles/InteractionPoweRvignette.html)及[FAQ](https://dbaranger.github.io/InteractionPoweR/articles/CommonQuestions.html)。2013原文受限，未核所有证明/原样本比例/模拟。

## 版本与静态纠错的证据边界
medDML教程order参数与所查CRAN镜像Usage冲突，先查实际formals/版本，不称已测试失效。[medDML help](https://rdrr.io/cran/causalweight/man/medDML.html)。RWR教程direct/indirect标签、和的名称、交互分解和CI符号有转录不一致，须回到作者稿，不直接复制为模板。CMAverse官方quickstart数字不是更换DGP后的独立复现。centered EIF均值为零，one-step一般是plugin+平均EIF或等价uncentered score；不能把术语缩写当完整估计程序。
