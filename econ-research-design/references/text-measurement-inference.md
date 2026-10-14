# AI文本测量：构念、抽样与下游推断

六篇连享会完整文字正文与定向原源记录经审阅综合。代码、模拟、模型标注与数据下载均未执行；原论文仅指定章节/摘要或官方文档。embedding定理、OECD招聘覆盖全文和全部图像仍有缺口，不当成全面方法认证。

## 1. 构念与目标标注程序分开
先写谁、对什么、从哪个视角、按何规则判断。事实提取、规则分类、主观构念不同；人工一致率支持复现参照程序，不单独证明测到理论构念。prescriptive/descriptive标注无天然优劣，主观分歧可含信息。

来源：[1943](https://www.lianxh.cn/details/1943.html)、[1950](https://www.lianxh.cn/details/1950.html)；[Adcock–Collier摘要](https://doi.org/10.1017/S0003055401003100)仅概念/操作化；[Röttger等](https://aclanthology.org/2022.naacl-main.13.pdf) 摘要/引言/2.1；[LLM标注作者稿](https://faculty.wharton.upenn.edu/wp-content/uploads/2025/09/The-use-of-LLMs-to-Annotate-Data.pdf) validation/sensitivity指定段。不复制未核定量宣传。

## 2. 开发、冻结测试、挑战与校正样本职责
挑战样本找失效边界，不混入随机样本估总体错误率。看测试标签继续改prompt后已属开发。推断校正样本同时保留参照Y与同管道预测；不等概率标注保存纳入概率与正支持，完全不标某组无法凭空恢复其误差。依人工标签才知道的难判分层不假装部署前可用；先验证可见代理是否预测校正score残差。没有普适每类20–30或总计200条就够的规则。

来源：1950、[1945](https://www.lianxh.cn/details/1945.html)、[1946](https://www.lianxh.cn/details/1946.html)；[PPI原稿](https://arxiv.org/pdf/2301.09633) §§1.1–1.3/4.2，基准iid/独立预测与covariate-shift限制。非代表标签到目标总体的运输须另论证。

## 3. PPI/RePPI修正目标score，不重新定义真值
预测Y回归通常是另一个projection；均值rectifier不直接等于任意回归修正。一般目标按estimating equation校正。[ppi_py官方API](https://ppi-py.readthedocs.io/en/latest/ppi.html)的OLS接口用于两侧X可观察、人工Y与预测Y成对，含w参数不等于任意调查设计已认证，生成X/D的误差不能交该outcome接口自动解决。

RePPI一般学习条件梯度/score，OLS/GLM特例可作再校准。三折隔离初始参数、score学习与评价；效率不劣结论是正则/L2条件下渐近方差，不保证有限样本区间总缩短。

来源：1945；[Ji–Lei–Zrnic v2](https://arxiv.org/pdf/2501.09731v2) §§2–3、Algorithm1、Theorem1–2/方差；[当前作者代码](https://raw.githubusercontent.com/Wenlong2000/RePPI/main/reppi.py)静态记录。报告中当前代码的fold比例/简单平均与论文全标签比例/折大小权重不同：先锁commit、版本与算法再研究影响，不未经执行默认称bug或历史某日实现已认证。

## 4. DSL的设计矩条件与2024扩展
校正的是指定target labeling procedure下的目标，不要求专家标签等于理论真值。Y/X两侧生成变量应按完整g(W;beta)校正，不逐列伪X再当无误差普通回归。已知正纳入概率、设计随机性、冻结预测/适当cross-fitting及依赖方差需对应；无偏矩不等于非线性解有限样本无偏。

广义outcome/independent任意subset扩展需引2024，不只归于2023首次DSL；专家分歧扩展存在但本轮未核全套程序。来源：1946/1943；[2024作者稿](https://naokiegami.com/paper/dsl_ss.pdf) 引言/方法预览，[2023原稿](https://arxiv.org/pdf/2306.04746)仅摘要/开头；[官方FAQ](https://naokiegami.com/dsl/articles/faq.html)及[正式Rd](https://raw.githubusercontent.com/naoki-egami/dsl/master/man/dsl.Rd) sample_prob/cluster/cross_fit。不是运行验证。

## 5. 泄漏、表示充分性与平台漂移独立审计
分开prompt/codebook偷看测试、上游模型训练污染、校正learner过拟合、文本含处理后信息；cross-fitting不包办。embedding保留混杂的充分性是模型条件，不由高预测精度证明。

来源：[1921](https://www.lianxh.cn/details/1921.html)；[Freyaldenhoven作者稿](https://arxiv.org/pdf/2608.31059)仅摘要/引言起始，未核rank/维度/附录；[NBER框架](https://www.nber.org/papers/w33344)仅摘要。不宣称任意embedding控制均有效或ATE已识别。

招聘广告不等于职位空缺或实际雇佣；来源×时间覆盖、prompt/解析变更需桥接样本和识别维度错误率。固定来源改变总体，共同时期FE未必吸收组别漂移；控制受政策影响的发布率可能改变对象。允许测量与识别共同迭代，不一律禁止标签单位再利用。来源：[1909](https://www.lianxh.cn/details/1909.html)；[OECD官方记录](https://www.oecd.org/en/publications/how-well-do-online-job-postings-match-national-sources-in-european-countries_e1026d81-en.html)仅元数据/摘要，全文未恢复；不认证跨国覆盖数值。PPML、DID或shift-share均不能自动修复平台选择。
