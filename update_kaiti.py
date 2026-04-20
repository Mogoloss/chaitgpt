import base64
import subprocess
import textwrap


def ps_here_string(text: str) -> str:
    return "@'\n" + text.rstrip() + "\n'@"


src = r"C:\Users\mgq56\Desktop\毕业论文\莫国庆开题报告.doc"
dst = r"C:\Users\mgq56\Desktop\毕业论文\莫国庆开题报告-按论文修改.doc"
new_title = "高荡村传统村落鸟类多样性"

section11 = """随着我国传统村落保护、生物多样性保护与乡村振兴战略的持续推进，传统村落生态资源调查逐渐成为区域生态保护研究的重要内容。国家和贵州省围绕传统村落保护及生物多样性保护先后出台了多项政策文件，为传统村落生态资源调查与评估提供了制度依据[1-4]。高荡村位于贵州省安顺市镇宁县，是保存较为完整的布依族传统村落之一，兼具农地、林地、居住地和人工绿地等多种生境类型，具有开展鸟类多样性调查的良好基础[10-11]。鸟类处于生态系统较高营养级，对栖息地结构变化、食物资源变化以及人为干扰反应敏感，常被作为评价区域生态环境质量和生境完整性的指示类群[5,12]。

国内关于鸟类群落的研究主要集中于自然保护区、森林、湿地和农田景观等区域，研究内容涉及群落结构、多样性格局、食性组成和生境利用等方面[5-7,12,16]。相关研究表明，不同生境类型在植被结构、食物资源和干扰强度上的差异，会显著影响鸟类物种组成和多样性水平[5-7]。近年来，随着传统村落保护工作的推进，学者开始关注传统聚落景观中的生物多样性，但针对传统村落尺度的鸟类本底调查仍然相对不足，尤其缺少将农地、林地、居住地和人工绿地等多种生境纳入同一调查框架进行比较分析的研究[10-11]。

国外关于鸟类多样性研究起步较早，相关研究已广泛应用于景观生态学、保护生物学和生境管理实践。已有研究指出，生境异质性、植被结构复杂度、食物资源丰度以及人为活动强度，是影响鸟类群落组成和多样性的重要因素[8-9]。因此，在高荡村这一传统村落景观中开展鸟类多样性研究，不仅能够补充传统村落生态调查资料，也有助于从微观尺度认识村落生境镶嵌格局对鸟类群落的影响，并为后续保护与管理提供依据[10-12]。"""

section12 = """理论意义：本研究以传统村落为研究单元，对高荡村鸟类的物种组成、群落结构、生境差异及食性特征进行分析，有助于丰富传统村落生态系统中鸟类群落研究的案例资料，拓展鸟类群落生态学在乡村聚落景观中的应用场景，为理解喀斯特地区传统村落生境异质性与鸟类多样性之间的关系提供基础依据[5,12,16]。

实践意义：通过调查高荡村鸟类资源现状，识别不同生境对鸟类多样性的支持作用及主要干扰因素，可为传统村落生态保护、旅游开发中的鸟类栖息地维护、生境优化及乡村振兴背景下的生态管理提供参考。同时，研究结果也可为贵州省传统村落生物多样性本底资料积累、后续监测与保护措施制定提供数据支撑[1-4,10-11]。"""

section21 = """本研究以贵州省安顺市镇宁县高荡村传统村落为研究区域，围绕鸟类多样性开展调查与分析，主要内容包括：
1. 调查高荡村鸟类物种组成、数量特征及群落基本结构，完成鸟类资源编目。
2. 比较农地、林地、居住地和人工绿地4种生境中鸟类多样性差异，分析不同生境的群落特征。
3. 统计鸟类的居留型、生态型、生活型、地理区系、保护等级及食性组成，揭示群落结构特征。
4. 结合调查结果分析影响高荡村鸟类多样性的主要因素，并提出相应的保护与管理建议。"""

section22 = """实地调查：采用样点法开展鸟类调查[5,12]。于2025年10月2日至4日，在7:00-11:00和15:00-18:30两个时间段，对高荡村农地、林地、居住地和人工绿地4种生境进行调查。每种生境设置6个样点，共24个样点；每个样点观察10 min，记录样点半径100 m范围内看到或听到的鸟类种类与数量，并同步记录栖息地特征。

仪器与记录：调查过程中使用双筒望远镜进行观察，使用相机拍照留存影像资料，并结合地图软件记录样点经纬度和海拔信息。

数据处理：依据《中国鸟类分类与分布名录》等资料对调查记录的鸟类进行分类整理，并统计居留型、地理区系、保护等级和中国特有种等信息[13-15]。

数据分析：采用Shannon-Wiener指数分析不同生境的alpha多样性，采用Sorenson相似性系数比较不同生境间的beta多样性；同时从食性组成、生境分布和优势种等方面分析高荡村鸟类群落结构特征[5-7,12]。"""

section23 = """1. 高荡村传统村落鸟类资源本底及群落结构特征，即区域内鸟类的物种组成、数量特征、保护属性和食性结构。
2. 不同生境中鸟类多样性的差异，即农地、林地、居住地和人工绿地在鸟类丰富度、多样性指数及群落相似性上的变化。
3. 影响高荡村鸟类多样性的主要因素，即生境异质性、植被条件、地形结构及人为干扰对鸟类分布的综合影响。
4. 如何在传统村落保护与旅游开发背景下提出针对性的鸟类保护建议，实现生态保护与村落发展的协调统一。"""

section3 = """1. 工作条件
调查基础：论文研究区域、调查对象与基础资料已经明确，已具备鸟类调查记录、样点信息、照片资料及相关文献基础。
调查设备：需要望远镜、相机、记录表、地图定位软件等，用于鸟类观察、拍摄与样点信息记录。
资料条件：可依托学校图书馆、中国知网等数据库获取鸟类多样性、传统村落保护及生态学相关文献。
数据处理条件：可利用Excel、SPSS等软件进行数据整理、统计分析和图表绘制。

2. 解决办法
在野外调查阶段，合理安排调查时间，尽量选择鸟类活动较频繁的早晚时段开展观察，提高调查记录的完整性。
在资料整理阶段，结合鸟类分类名录和相关文献，对调查数据进行规范核对，确保物种名称、保护等级和区系信息准确。
在分析与写作阶段，通过请教指导教师、查阅文献和反复校核数据等方式解决研究过程中出现的问题，保证论文分析与结论的科学性。"""

section4 = """2025年9月-2025年10月：确定论文选题，查阅传统村落与鸟类多样性相关文献，完成开题报告撰写。
2025年10月：开展高荡村鸟类野外调查，完成样点布设、鸟类观察记录及生境信息收集。
2025年11月-2025年12月：整理野外调查资料，统计鸟类名录、数量、生境分布及相关生态学属性。
2026年1月-2026年2月：完成数据分析，计算不同生境鸟类多样性指数和群落相似性，形成论文初稿。
2026年3月：根据指导教师意见修改论文，完善结果分析、讨论与参考文献。
2026年4月-2026年5月：完成论文定稿、答辩准备及毕业论文答辩相关工作。"""

section5 = """摘要
Abstract
1 背景
1.1 政策背景
1.2 调查区域地理位置及生态背景
2 野外调查
2.1 调查目的
2.2 调查任务
2.3 调查范围
2.4 前期工作
2.5 调查方法
2.6 数据处理
3 调查结果
3.1 鸟类群落特征
3.2 鸟类分类目的组成
3.3 鸟类分类科的组成
3.4 鸟类种的数量占比
3.5 不同生境鸟类多样性指数
3.6 鸟类食性分析
4 讨论
4.1 影响高荡村鸟类多样性的因素
参考文献
附录
致谢"""

section6 = """[1]\t陈勤昌，王兆峰，王武林. 乡村振兴背景下湘西地区传统村落活态性特征及提升路径[J]. World Regional Studies，2026，35（1）.
[2]\t环境保护部. 中国生物多样性保护战略与行动计划（2011-2030年）[R]. 2010.
[3]\t贵州省生态环境厅. 贵州省生物多样性保护战略与行动计划（2016-2026）[R]. 2015.
[4]\t王成，彭翔，易子，等. 贵州高荡村千年布依古寨的石头之谜[J]. 城市地理，2024（3）：98-103.
[5]\t毛炜. 文化生态视角下传统村落公共空间重塑: 以贵州省安顺市镇宁县高荡村为例[D]. 贵州师范大学，2024.
[6]\t罗祖奎，刘伦沛，王云，等. 贵州省云台山鸟类群落特征[J]. 华东师范大学学报（自然科学版），2013（5）：43-52.
[7]\t楼利高，刘家武，舒实，等. 湖北沙湖湿地自然保护区秋季鸟类物种多样性[J]. 林业调查规划，2008（5）：44-47.
[8]\t代开兴. 大理洱海流域农田景观冬季鸟类多样性组成及时空分布格局研究[D]. 大理大学，2025.
[9]\t罗祖奎，刘文，李振吉，等. 贵州草海冬季鸟类群落特征[J]. 华东师范大学学报（自然科学版），2012（4）：102-111.
[10]\t张岚岚，孙建伟，邓玲玲，等. 中国传统村落的多尺度时空格局特征及影响因素[J]. Research of Soil & Water Conservation，2025，32（2）.
[11]\tProenca V M，Pereira H M，Guilherme J，et al. Plant and bird diversity in natural forests and in native and exotic plantations in NW Portugal[J]. Acta Oecologica，2010，36（2）：219-226.
[12]\tClout M N，Gaze P D. Effects of plantation forestry on birds in New Zealand[J]. Journal of Applied Ecology，1984，21：795-815.
[13]\t罗祖奎，岳峰，吴法清，等. 湖北沙湖冬季鸟类群落特征[J]. 生态学杂志，2009，28（7）：1361-1367.
[14]\t郑光美. 中国鸟类分类与分布名录[M]. 北京：科学出版社，2023.
[15]\t国家林业和草原局，农业农村部. 国家重点保护野生动物名录（2021年版）[J]. 野生动物学报，2021，42（2）：605-640.
[16]\t钱燕文. 中国鸟类图鉴[M]. 郑州：河南科学技术出版社，1995."""

cell_r4 = """1选题背景及研究意义（选题背景应对该选题的国内外研究现状进行综述，研究意义应从理论和实践两个方面进行阐述。要求字数在800字左右）
1.1选题背景
随着我国传统村落保护、生物多样性保护与乡村振兴战略的持续推进，传统村落生态资源调查逐渐成为区域生态保护研究的重要内容。传统村落保护与发展研究为此类调查工作的开展提供了现实背景[1]。国家和贵州省先后发布生物多样性保护相关政策文件，为传统村落生态资源调查与评估提供了制度依据[2-3]。
高荡村位于贵州省安顺市镇宁县，是保存较为完整的布依族传统村落之一[4]。相关研究表明，该村具有较为鲜明的传统聚落景观和文化生态特征[5]。同时，高荡村兼具农地、林地、居住地和人工绿地等多种生境类型，具备开展鸟类多样性调查的良好基础。鸟类处于生态系统较高营养级，对栖息地结构变化以及人为干扰反应敏感，常被作为评价区域生态环境质量和生境完整性的指示类群[6]。
国内关于鸟类群落的研究主要集中于自然保护区、森林、湿地和农田景观等区域[7]。农田景观中的鸟类多样性研究表明，生境类型和土地利用方式会显著影响鸟类群落组成[8]。已有研究还指出，不同生境在植被结构、食物资源和干扰强度上的差异，会进一步影响鸟类多样性格局[9]。相比之下，围绕传统村落这一复合景观单元开展鸟类多样性综合比较的研究仍相对有限，这也说明在高荡村开展相关调查具有一定补充意义[10]。
国外关于鸟类多样性研究起步较早，相关研究已广泛应用于景观生态学、保护生物学和生境管理实践。已有研究指出，生境异质性、植被结构复杂度和人为活动强度，是影响鸟类群落组成和多样性的重要因素[11-12]。因此，在高荡村这一传统村落景观中开展鸟类多样性研究，不仅能够补充传统村落生态调查资料，也有助于从微观尺度认识村落生境镶嵌格局对鸟类群落的影响。
1.2研究意义
鸟类多样性研究在理论和实践方面具有重要意义。
理论意义：本研究以传统村落为研究单元，对高荡村鸟类的物种组成、群落结构、生境差异及食性特征进行分析，有助于丰富传统村落生态系统中鸟类群落研究的案例资料，也有助于拓展鸟类群落生态学在乡村聚落景观中的应用场景[7]。
实践意义：通过调查高荡村鸟类资源现状，识别不同生境对鸟类多样性的支持作用及主要干扰因素，可为传统村落生态保护、旅游开发中的鸟类栖息地维护和生境优化提供参考，也可为后续监测与保护措施制定提供数据支撑[2-3]。
2主要研究内容、研究方法以及拟解决的关键问题
2.1研究内容
本研究以贵州省安顺市镇宁县高荡村传统村落为研究区域，围绕鸟类多样性开展调查与分析，具体研究内容包括：
鸟类资源编目与群落特征分析。调查高荡村鸟类物种组成、数量特征及群落基本结构，掌握区域鸟类资源现状。
不同生境鸟类多样性比较。比较农地、林地、居住地和人工绿地4种生境中鸟类多样性差异，分析不同生境的群落特征。
鸟类生态属性统计。统计鸟类的居留型、生态型、生活型、地理区系、保护等级及食性组成，揭示群落结构特征。
保护与管理建议。结合调查结果分析影响高荡村鸟类多样性的主要因素，并提出相应的保护与管理建议。
2.2研究方法
实地调查
采用样点法开展鸟类调查[7]。于2025年10月2日至4日，在7:00-11:00和15:00-18:30两个时间段，对高荡村农地、林地、居住地和人工绿地4种生境进行调查。
每种生境设置6个样点，共24个样点；每个样点观察10 min，记录样点半径100 m范围内看到或听到的鸟类种类与数量，并同步记录栖息地特征和样点位置信息。
数据分析
依据《中国鸟类分类与分布名录》等资料对调查记录的鸟类进行分类整理[14]，并结合国家重点保护野生动物名录统计保护等级信息[15]，结合鸟类图鉴核对食性等生态属性[16]。
采用Shannon-Wiener指数分析不同生境的alpha多样性，采用Sorenson相似性系数比较不同生境间的beta多样性；同时从食性组成、生境分布和优势种等方面分析高荡村鸟类群落结构特征。"""

cell_r5 = """2.3拟解决的关键问题
高荡村传统村落鸟类资源本底及群落结构特征。明确区域内鸟类的物种组成、数量特征、保护属性和食性结构。
不同生境中鸟类多样性的差异。分析农地、林地、居住地和人工绿地在鸟类丰富度、多样性指数及群落相似性上的变化。
影响高荡村鸟类多样性的主要因素。探讨生境异质性、植被条件、地形结构及人为干扰对鸟类分布的综合影响。
传统村落保护背景下的鸟类保护建议。结合研究结果提出生态保护与村落发展相协调的管理建议。

3完成毕业论文所必需具备的工作条件及解决的办法
1.工作条件
调查基础：
论文研究区域、调查对象与基础资料已经明确，已具备鸟类调查记录、样点信息、照片资料及相关文献基础。
调查设备：
需配备望远镜、相机、记录表和地图定位软件等，用于鸟类观察、拍摄与样点信息记录。
文献资源：
可依托学校图书馆、中国知网等数据库获取鸟类多样性、传统村落保护及生态学相关文献。
时间安排：
已具备论文写作与资料整理时间基础，可按计划推进数据整理、分析与论文撰写。
团队合作：
在指导教师指导下完成选题论证、资料整理和论文写作，必要时可请教相关老师与同学协助。

2.解决办法
设备准备与资料整理：
提前检查调查设备和照片资料，统一整理样点记录、鸟类名录及原始数据，保证后续分析顺利开展。
文献获取与信息核对：
通过学校数据库和相关文献资料核对鸟类分类、保护等级和区系信息，保证资料引用准确规范。
时间管理与进度控制：
根据论文进度安排分阶段完成数据整理、结果分析和论文修改，确保按时完成毕业论文各环节任务。
请教指导与反复修改：
在分析与写作阶段及时向指导教师请教，根据反馈反复修改完善，保证论文内容与结论的科学性。"""

ps_script = textwrap.dedent(
    f"""
    $ErrorActionPreference = 'Stop'
    $src = '{src}'
    $dst = '{dst}'
    if (-not (Test-Path -LiteralPath $dst)) {{
        Copy-Item -LiteralPath $src -Destination $dst -Force
    }}
    $newTitle = '{new_title}'
    $cellR4 = {ps_here_string(cell_r4)}
    $cellR5 = {ps_here_string(cell_r5)}
    $section4 = {ps_here_string(section4)}
    $section5 = {ps_here_string(section5)}
    $section6 = {ps_here_string(section6)}

    function Find-Range($doc, $text) {{
        $range = $doc.Content
        $find = $range.Find
        $find.ClearFormatting() | Out-Null
        $find.Text = $text
        $find.Forward = $true
        $find.Wrap = 0
        $found = $find.Execute()
        if (-not $found) {{
            throw "未找到文本: $text"
        }}
        return $range
    }}

    function Replace-All-Exact($doc, $oldText, $newText) {{
        $searchRange = $doc.Range(0, $doc.Content.End)
        while ($true) {{
            $find = $searchRange.Find
            $find.ClearFormatting() | Out-Null
            $find.Text = $oldText
            $find.Forward = $true
            $find.Wrap = 0
            $found = $find.Execute()
            if (-not $found) {{
                break
            }}
            $match = $doc.Range($searchRange.Start, $searchRange.End)
            $match.Text = $newText
            $searchRange = $doc.Range($match.End, $doc.Content.End)
        }}
    }}

    function Set-Cell-Text($cell, $text) {{
        $range = $cell.Range
        $range.End = $range.End - 1
        $range.Text = $text
    }}

    function Copy-Range-Format($srcRange, $dstRange) {{
        $dstRange.Font.NameFarEast = $srcRange.Font.NameFarEast
        $dstRange.Font.NameAscii = $srcRange.Font.NameAscii
        $dstRange.Font.NameOther = $srcRange.Font.NameOther
        $dstRange.Font.Size = $srcRange.Font.Size
        $dstRange.Font.Bold = $srcRange.Font.Bold
        $dstRange.Font.Italic = $srcRange.Font.Italic
        $dstRange.Font.Underline = $srcRange.Font.Underline
        $dstRange.ParagraphFormat.Alignment = $srcRange.ParagraphFormat.Alignment
        $dstRange.ParagraphFormat.LeftIndent = $srcRange.ParagraphFormat.LeftIndent
        $dstRange.ParagraphFormat.RightIndent = $srcRange.ParagraphFormat.RightIndent
        $dstRange.ParagraphFormat.FirstLineIndent = $srcRange.ParagraphFormat.FirstLineIndent
        $dstRange.ParagraphFormat.SpaceBefore = $srcRange.ParagraphFormat.SpaceBefore
        $dstRange.ParagraphFormat.SpaceAfter = $srcRange.ParagraphFormat.SpaceAfter
        $dstRange.ParagraphFormat.LineSpacingRule = $srcRange.ParagraphFormat.LineSpacingRule
        $dstRange.ParagraphFormat.LineSpacing = $srcRange.ParagraphFormat.LineSpacing
        $dstRange.ParagraphFormat.CharacterUnitFirstLineIndent = $srcRange.ParagraphFormat.CharacterUnitFirstLineIndent
    }}

    function Apply-Paragraph-Templates($dstCell, $srcCell, $templateIndexes) {{
        $dstParas = $dstCell.Range.Paragraphs
        for ($i = 1; $i -le $dstParas.Count; $i++) {{
            $txt = ($dstParas.Item($i).Range.Text -replace "[`r`a]", "")
            if ([string]::IsNullOrWhiteSpace($txt)) {{
                continue
            }}
            $templateIndex = $templateIndexes[[Math]::Min($i - 1, $templateIndexes.Count - 1)]
            $srcPara = $srcCell.Range.Paragraphs.Item($templateIndex)
            Copy-Range-Format $srcPara.Range $dstParas.Item($i).Range
        }}
    }}

    function Set-Reference-Paragraph-Visible($cell) {{
        $paras = $cell.Range.Paragraphs
        for ($i = 2; $i -le $paras.Count; $i++) {{
            $txt = ($paras.Item($i).Range.Text -replace "[`r`a]", "")
            if ([string]::IsNullOrWhiteSpace($txt)) {{
                continue
            }}
            $pf = $paras.Item($i).Range.ParagraphFormat
            $pf.LeftIndent = 0
            $pf.FirstLineIndent = 0
            $pf.RightIndent = 0
            $pf.SpaceBefore = 0
            $pf.SpaceAfter = 0
            $pf.CharacterUnitLeftIndent = 0
            $pf.CharacterUnitFirstLineIndent = 0
            $paras.Item($i).Range.Font.Superscript = $false
        }}
    }}

    function Apply-Superscript-Citations($cell) {{
        $text = $cell.Range.Text
        $baseStart = $cell.Range.Start
        $matches = [regex]::Matches($text, '\[[0-9,\-]+\]')
        foreach ($m in $matches) {{
            $hit = $doc.Range($baseStart + $m.Index, $baseStart + $m.Index + $m.Length)
            $hit.Font.Superscript = $true
        }}
    }}

    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0

    try {{
        $srcDoc = $word.Documents.Open($src, $false, $true)
        $doc = $word.Documents.Open($dst)

        Replace-All-Exact $doc '黎平县东风林场人工林与天然林鸟类群落结构差异' $newTitle
        Set-Cell-Text $doc.Tables.Item(1).Cell(4,1) $cellR4
        Set-Cell-Text $doc.Tables.Item(1).Cell(5,1) $cellR5
        Set-Cell-Text $doc.Tables.Item(2).Cell(1,1) ('4工作的计划、进度与时间安排' + "`r" + $section4.Trim())
        Set-Cell-Text $doc.Tables.Item(2).Cell(2,1) ('5论文写作提纲（要求至少到二级标题）' + "`r" + $section5.Trim())
        Set-Cell-Text $doc.Tables.Item(2).Cell(3,1) ('6参考文献（不少于15篇）' + "`r" + $section6.Trim())

        Copy-Range-Format $srcDoc.Tables.Item(1).Cell(4,1).Range $doc.Tables.Item(1).Cell(4,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(1).Cell(5,1).Range $doc.Tables.Item(1).Cell(5,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(2).Cell(1,1).Range $doc.Tables.Item(2).Cell(1,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(2).Cell(2,1).Range $doc.Tables.Item(2).Cell(2,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(2).Cell(3,1).Range $doc.Tables.Item(2).Cell(3,1).Range

        Apply-Paragraph-Templates $doc.Tables.Item(1).Cell(4,1) $srcDoc.Tables.Item(1).Cell(4,1) @(1,2,3,4,5,6,7,8,9,11,12,15,16,17,18,19,20,20,21,22,23,24,25,26,25,27)
        Apply-Paragraph-Templates $doc.Tables.Item(1).Cell(5,1) $srcDoc.Tables.Item(1).Cell(5,1) @(1,2,3,4,4,4,6,7,8,9,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,29,30,32,33)
        Apply-Paragraph-Templates $doc.Tables.Item(2).Cell(1,1) $srcDoc.Tables.Item(2).Cell(1,1) @(1,2,3,4,5,6,7)
        Apply-Paragraph-Templates $doc.Tables.Item(2).Cell(2,1) $srcDoc.Tables.Item(2).Cell(2,1) @(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27)
        Apply-Paragraph-Templates $doc.Tables.Item(2).Cell(3,1) $srcDoc.Tables.Item(2).Cell(3,1) @(1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)
        Set-Reference-Paragraph-Visible $doc.Tables.Item(2).Cell(3,1)
        Apply-Superscript-Citations $doc.Tables.Item(1).Cell(4,1)
        Apply-Superscript-Citations $doc.Tables.Item(1).Cell(5,1)
        Apply-Superscript-Citations $doc.Tables.Item(2).Cell(1,1)

        $doc.Save()
        $doc.Close()
        $srcDoc.Close()
    }}
    finally {{
        if ($word) {{
            $word.Quit()
        }}
    }}

    Write-Output $dst
    """
)

encoded = base64.b64encode(ps_script.encode("utf-16le")).decode("ascii")
result = subprocess.run(
    ["powershell", "-NoProfile", "-EncodedCommand", encoded],
    capture_output=True,
    text=True,
    encoding="utf-8",
)

print(result.stdout)
if result.returncode != 0:
    print(result.stderr)
    raise SystemExit(result.returncode)
