# IV：目标、强度、分配与诊断的分工

六篇连享会文字正文已由本轮阅读任务读完，本文审阅其原源核验记录后综合；原论文仅指定章节/help，未全证明审核、未运行Stata/R。允许透明规格和工具候选探索，但不从最大F、最显著系数或不拒绝J检验反推有效性。

## 1. 强度不是排除限制，稳健VCE不是弱识别稳健

分别写工具分配、工具到处理的边际、对结果的其他渠道；2SLS系数不自动是ATE。F>10不通用，零相关检验与偏误/尺寸准则不同。一般KP统计量不能机械套Stock–Yogo临界值；多内生变量须匹配协方差与目标。强度预检验后切换推断本身也影响整体尺寸。AR/CLR等置信集可能无界、分段或为空，不能只报常规有限区间。

`weakivtest2`为偏误准则强度检验，不是beta弱稳健置信集；当前help与旧教程默认不同须记录渠道版本。LIML、GMM与2SLS是不同估计器。来源：[1504](https://www.lianxh.cn/details/1504.html)、[1351](https://www.lianxh.cn/details/1351.html)；[Lewis–Mertens 2022作者稿](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1020.pdf) 模型/步骤；[作者help](http://fmwww.bc.edu/RePEc/bocode/w/weakivtest2.sthlp)；[Stata后估计](https://www.stata.com/manuals/rivregresspostestimation.pdf?public=1) firststage/weakrobust。最终修订证明未全对照，1351原论文只作者元数据/摘要。

## 2. Formula/shift-share：冲击与暴露的识别路线分开

冲击外生性包含条件分配与经济排除限制；预定但非随机的份额不自动外生。明确采用冲击识别还是份额识别，写分配支持、条件冲击均值、份额和、集中与依赖、有效冲击数量。再中心化z-E[z|w]可恢复相应期望矩，但仍需相关性和一致性/推断条件；地区数不等于独立冲击数。模拟条件均值应取平均不是未归一化求和；置换须保留可信可交换组和限制。控制预期暴露与再中心化不是有限样本系数/显著性必相同的定理。

来源：[1398](https://www.lianxh.cn/details/1398.html)；[Borusyak–Hull作者发表版](https://www.dropbox.com/scl/fi/4e24ujdhzd8ne618sgxnw/recenteredIV.pdf?rlkey=2tejlz7zfr7ma45ql1dz381tb&raw=1) §§3.1–3.3；[Hull 2024讲义](https://www.stata.com/symposiums/economics24/presentations/Econ24_Hull.pdf) identification/ADH。未审GPS全部证明或高铁实际分配有效性。

版本审计：[2026-05-31作者勘误](https://www.dropbox.com/scl/fi/vdpmnrszmlry6mjew5dgx/table_ii_corrected.pdf?rlkey=ttvk29vgrrzwvcdhwnxt5xkln&st=5yu5opwj&raw=1)一页已独立回读；Table II未调整市场可达性被地理解释的R²由82%改为33%（0.332），不是Table I就业处理效应勘误。不以旧数值宣传方法。

## 3. 好IV可能是坏控制：只在指定线性机制内

有效相关Z在X中贡献外生变异；常数斜率线性模型下把Z当普通OLS控制会缩小处理残差方差而保留内生协方差，可能放大总体偏误。这不是任意非线性/异质模型、每个有限样本或MSE结论；处理已外生时偏误可同为零。该Z与上节用于调整的预期暴露不是同一对象。

来源：[1271](https://www.lianxh.cn/details/1271.html)；[DiTraglia原博客](https://www.econometrics.blog/post/a-good-instrument-is-a-bad-control/) 模型与总体偏误推导。未逐图核查全部DAG，未运行模拟。

## 4. IV–OLS差距先拆目标和权重

同样本/控制下审计协变量权重、处理边际权重和被识别边际效应差异；不可观测效应异质时分解余项不能直接叫纯内生性偏误。基函数选择影响非线性近似；DID/RD专门实现不是一个选项创造设计。教程把rdd输出称DID、舍入差称分解失效等不能当一般定理。

来源：[1129](https://www.lianxh.cn/details/1129.html)；[Ishimaru v3](https://arxiv.org/html/2101.04346v3) 式4–5/分解/扩展；[作者help](http://fmwww.bc.edu/repec/bocode/i/ivolsdec.sthlp)、[FAQ](https://sites.google.com/view/ishimaru/home/ivolsdec)。未复现数值，发表版与v3未全文逐条比较。

## 5. Overid与内生性检验是诊断而非认证

阶条件、满秩条件与恰足/过度识别分开；DWH零假设为被检验变量外生。J考察同一参数下联合矩限制，不拒绝不证明每个工具有效，拒绝也不自动定位坏工具；异质工具可能不识别共同斜率。比较手工/自动检验前统一样本、控制、工具和VCE，不将不同样本的结果差归因于robust选项。

来源：[988](https://www.lianxh.cn/details/988.html)、1351；[官方后估计](https://www.stata.com/manuals/rivregresspostestimation.pdf?public=1) overid/endogenous。教程变量/样本不一致为静态发现，修正后的数值未执行。
