# 空间均衡：通勤、反演和贸易实验

## 数量口径先于模型拟合
通勤联合份额按全部居住地—工作地组合加总为1；条件工作选择份额是在给定居住地内加总为1。前者乘总工人数，后者乘相应居住地人数，才能得到可比流量。明确矩阵两轴、行列身份和国内/跨区流量；居民数与工作地就业是不同加总。Monte基础模型固定总工人且每人一单位劳动：地方岗位反应可来自迁移和跨区通勤，不能直接解释成全经济净增岗位。居住地收入还需对工作地工资按条件通勤权重平均。

## 给定参数反演与行为识别分开
Redding 2016 §2.7 Proposition 3是在已给定模型参数、贸易成本参数化及人口/工资/土地下，归一化后恢复生产率和amenity。它不是行为参数全部识别的定理，也不是任意扩展模型的均衡唯一性。逐参数列变异/矩、规范化和排除；反演所用人口的再拟合不得当独立验证。开放/封闭人口、土地收益归属与移动摩擦另写。

该基础模型中跨地点相等的是条件期望效用，不必是实际收入或个体实现效用。只改变贸易成本时，福利须同时包含本地贸易份额与人口重配，并保留固定土地/其他基本面/总人口、Fréchet偏好及租金归属假设。不能把人口项孤立解释成迁入必降低福利，也不把另一模型的房东闭合拼接进来。

## ge_gravity2：先估计冲击，再解GE
所查作者help/ado版本输入theta为正贸易弹性、psi非负；partial为对数局部效应，内部转换为exp(partial)，无冲击用0。不能混淆负的回归贸易成本系数、弹性正值、百分比和成本倍数。这个命令求价格固定点，不执行PPML参数估计；先行系数的识别和政策不变性仍须单独论证。所查接口为tol()/max_iter()，不能从二手标题推断有tc()/solver(yotov)/tolerance()或内置IV。

先声明赤字闭合、名义归一化、何物外生：默认固定名义赤字、multiplicative与universal不是普遍同一实验。通用价格/贸易映射不等于通用福利；c_hat情形不提供同样福利。多因素、非恒弹性、内生赤字、关税收入以及多部门/排放扩展都要独立证明兼容性。财政关税收入不是冰山资源损失。

## 计算验收
所读ado按crit>tol且未达max_iter继续，退出后外层仍会打印solved；保存e(crit)、e(n_iter)并独立核预算、清算、份额加总及经济可行性。by调用的返回量可能不同，先查版本。保持出口/进口身份方阵、非负无缺失和正的国内对角；程序缺失转零或国内冲击归零的容错不是数据核验。这里是静态源码判断，未执行求解器或制造失败日志。西班牙示例的新旧冲击差分方向冲突尚未解决，不发布其政策数值模板。

### 原源与阅读边界

- [Commuting, migration, and local employment elasticities](https://www.princeton.edu/~erossi/CMLEE.pdf)：§I.D 式(10)–(14), pp.3863–3864。版本/范围：AER 108(12), 2018, 3855–3890；作者站PDF文本检索副本；仅相关段落/静态文档核查，非全证明或软件运行。
- [Goods trade, factor mobility and welfare](https://www.princeton.edu/~reddings/pubpapers/GoodsTradeFactorMobilJIE2016.pdf)：§2.7 Proposition 3, p.153；§2.4式(9)–(14)、§2.9式(24)–(30), pp.151,153–154。版本/范围：JIE 101 (2016) 148–167；作者站PDF文本检索副本；仅相关段落/静态文档核查，非全证明或软件运行。
- [ge_gravity2: a command for solving universal gravity models](https://rolf-campos.github.io/publication/sj-2025-ge_gravity2/sj-2025-ge_gravity2.pdf)：§2.4、§2.9、§3.1, pp.7–8,13–14；§1末段、§2.3、§2.5–2.8, pp.2,7–13。版本/范围：作者稿标注August 23, 2025；非声称逐页核对期刊排版；仅相关段落/静态文档核查，非全证明或软件运行。
- [ge_gravity2 author help, ado and examples](https://github.com/rolf-campos/ge_gravity2)：ado L17–20、L170–172、L274–275；help Elasticities；help Other options；ado L397–407；ado L168–174、L329–376、L431–435。版本/范围：help v1.0 25Mar2024；ado v3.0 April2024；Git blob help=a0943564413b0bd1ea1ec6ad66bc6febbec25a43, ado=4dcbf78753f8c05fd9c15234d62935c6f8237c66, examples=d2278082f7a6e1b377f5a5efaaff423afd2dce24；仅相关段落/静态文档核查，非全证明或软件运行。

二手阅读背景：[1970](https://www.lianxh.cn/details/1970.html)、[1971](https://www.lianxh.cn/details/1971.html)、[1965](https://www.lianxh.cn/details/1965.html)、[1966](https://www.lianxh.cn/details/1966.html)、[1961](https://www.lianxh.cn/details/1961.html)、[1755](https://www.lianxh.cn/details/1755.html)、[1625](https://www.lianxh.cn/details/1625.html)、[1531](https://www.lianxh.cn/details/1531.html)。这些是相应组文字正文阅读记录；不是所有图片已读。相关组图像未完整查看；本次只审报告、逐条台账及承重原源选段，不重新爬取文章、重做全部证明或运行来源程序。
