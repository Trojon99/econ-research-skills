# 样本、变换、合并与同语义性能审计

基于六篇连享会文字全文及官方/开发者文档的定向核验记录。示例静态审阅，不是Stata执行或计时复现；允许探索处理规则，但原数据不动，保留字段/规则/退出原因与结果版本。

## 1. 样本链与缺失语义

分阶段报行数、实体数、各变量非缺失N、可加权N、权重和、退出原因和模型e(sample)。数值缺失大于有限数，`if x`和`x>0`可含缺失；`x!=.`不排除扩展缺失。组合逻辑右侧常数不继承左侧比较；采用明确括号、完整比较或inlist，对0、边界、负值、系统/扩展缺失做小测试。e(sample)是当前命令的样本，应立即保存，不是万能删缺失标志。

来源：[1375](https://www.lianxh.cn/details/1375.html)、[1749](https://www.lianxh.cn/details/1749.html)；[Stata逻辑FAQ](https://www.stata.com/support/faqs/data-management/true-and-false/)、[operators](https://www.stata.com/help.cgi?operators)、[missing](https://www.stata.com/help.cgi?missing)、[programming functions](https://www.stata.com/manuals/fnprogrammingfunctions.pdf) e(sample)。全部为文档语义，目标模型实际删样本需执行核验。

## 2. 缩尾先证明同一任务再比较速度

保护原变量与阈值非缺失：上尾替换不能只写x>qhi；min/max忽略缺失参数，数学clip式不自动保留Stata缺失。记录分位点的样本/组键/算法/权重、阈值、改写量、原缺失与组缺失。全样本与分组缩尾不是同一计时任务；N/均值/SD一致不证明逐行相同。用含极小组、并列边界和扩展缺失的测试，按容差逐行比较后才计时。

来源：1749；[数学函数手册](https://www.stata.com/manuals/fnmathematicalfunctions.pdf) min/max、[gtools作者文档](https://gtools.readthedocs.io/en/latest/usage/gstats_winsor/)选项。模拟year/year_index及冲击条件静态发现不认证计时表；winsor2/gstats源码等价和速度未实测。数值winsor、trim与event-time binning是不同操作，不互称缩尾。

## 3. 格式标准化不是实体链接

`format`只改显示；tostring可按格式生成字符串但需先验整数性、码本、长度、精度与缺失。固定长度截取可能制造碰撞，长ID丢精度不能补零恢复。保留源键和标准键，检查一对多映射及单位/时间有效期；数值缺失转成文本点号不是合法ID。merge前核验唯一键与基数，解释全部_merge状态；不为绕过报错改m:m或立即只留匹配掩盖选择。

来源：[1748](https://www.lianxh.cn/details/1748.html)；[tostring](https://www.stata.com/help.cgi?tostring)、[merge](https://www.stata.com/help.cgi?merge)、[types](https://www.stata.com/help.cgi?data_types)。未核验任何真实跨库链接关系。

## 4. 加权摘要同时留原始分母

collapse默认变量各自可用样本，cw才共同完整案例。count/sum含义依权重类型，带权count不能一律叫行数；rawsum忽略权重大小但零权重仍排除，因此带权rawsum非缺失flag不等于全样本原始N。需要两个口径时分别建立未加权样本账与加权摘要，再按组键合并；明确无效/缺失权重和调查设计，不为兼容快命令把pweight任意改aweight。

来源：[1537](https://www.lianxh.cn/details/1537.html)；[collapse官方手册](https://www.stata.com/manuals/dcollapse.pdf) weights/rawsum/cw、[weights](https://www.stata.com/help.cgi?weight)。本轮额外回查官方manual；未测试gcollapse/fcollapse等价。

## 5. 变换与工程复现边界

ln需正值，ln1p只是数值精度改进并不扩大1+x的定义域。先区分真实零、缺失误码、测量下限与合法负净额；删除零改变条件总体，IHS系数受单位尺度影响，PPML不是任意负结果处理法。跨模型比较先对齐原尺度对象和共同样本。

来源：[1234](https://www.lianxh.cn/details/1234.html)；[数学函数](https://www.stata.com/manuals/fnmathematicalfunctions.pdf)、[Poisson官方](https://www.stata.com/manuals/rpoisson.pdf)。iOLS理论/SE及优越性原源未核，不提升为规则。

`version`不锁第三方文件，adopath改变解析顺序；保存包来源、文件hash、依赖/插件/平台并用which核验。cwd不自动是master所在目录，capture不证明目录可写。compress保持精度与手动recast不同；collapse fast改变Break恢复保障，不证明更准。

来源：[1739](https://www.lianxh.cn/details/1739.html)、1537；官方[version](https://www.stata.com/help.cgi?version)、[adopath](https://www.stata.com/help.cgi?adopath)、[compress](https://www.stata.com/help.cgi?compress)、[preserve](https://www.stata.com/help.cgi?preserve)。要求真实raw→结果链执行和语义断言，不把教学auto模板当项目复现成功。
