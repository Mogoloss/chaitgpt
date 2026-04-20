import base64
import subprocess
import textwrap


def ps_here_string(text: str) -> str:
    return "@'\n" + text.rstrip() + "\n'@"


src = r"C:\Users\mgq56\Desktop\毕业论文\莫国庆开题报告.doc"
dst = r"C:\Users\mgq56\Desktop\毕业论文\黄晋望开题报告-按论文修改.doc"

new_title = "贵州雷公山国家级自然保护区鸟类多样性"
new_name = "黄晋望"
new_id = "2022401024"

cell_r4 = """1选题背景及研究意义（选题背景应对该选题的国内外研究现状进行综述，研究意义应从理论和实践两个方面进行阐述。要求字数在800字左右）
1.1选题背景
鸟类被广泛认为是评价生态系统结构与功能的重要指示类群，对自然保护区生物多样性监测和保护管理具有重要意义。已有自然保护区鸟类多样性研究表明，建立较为完整的鸟类物种名录，是开展保护区资源调查、物种编目与科学保护的基础工作[1]。
雷公山国家级自然保护区是贵州省重要的森林生态系统类型自然保护区。前期科学考察和生物多样性研究已对保护区的自然概况和鸟类资源进行了系统记录[2-3]。在两次较大规模调查之后，研究者又通过红外相机监测等方式不断补充该区域鸟类新纪录[4]，说明该保护区鸟类多样性仍有持续更新的空间。
近年来，公众科学观鸟数据逐渐成为鸟类多样性监测的重要补充来源。同时，鸟类分类系统和物种地位也在持续调整更新，对已有物种名录进行重新梳理和修订具有必要性[5-6]。已有鸟类群落研究表明，不同区域持续、系统的数据积累对于认识群落组成和生境利用规律具有重要作用，这也为保护区长期监测提供了参考[7]。
在方法上，雾网调查、样线观察、公众观鸟记录和历史文献整理等多种数据来源具有明显互补性。雾网在隐蔽性强、小型林鸟调查中具有优势，而公众观鸟对区域性鸟类监测具有补充价值[8-9]。同时，红外相机网络也不断拓展了鸟类监测手段[10]。因此，以贵州雷公山国家级自然保护区为对象开展鸟类多样性研究，整合历史文献、公众科学数据和实地调查资料，符合该区域鸟类资源动态更新与名录修订的现实需求。
1.2研究意义
鸟类多样性研究在理论和实践方面都具有重要意义。
理论意义：通过对雷公山国家级自然保护区鸟类物种组成、保护属性、记录来源及新增鸟类的系统整理，有助于进一步丰富山地森林自然保护区鸟类多样性研究资料，并为理解亚热带山地保护区鸟类区系组成和群落特征提供基础依据。
实践意义：本研究可为雷公山国家级自然保护区鸟类多样性监测、珍稀濒危鸟类保护和资源管理提供基础数据，也可为后续公众科学数据整合、保护区物种编目更新及长期监测提供参考[4-5]。
2主要研究内容、研究方法以及拟解决的关键问题
2.1研究内容
本研究以贵州雷公山国家级自然保护区为研究对象，围绕鸟类多样性与物种名录更新开展研究，具体内容包括：
鸟类物种组成整理。整合历史文献、公众科学观鸟数据及作者调查记录，统计保护区鸟类物种数、分类单元和区系组成，编制雷公山鸟类名录。
珍稀濒危鸟类分析。统计国家重点保护鸟类、中国特有种及不同受威胁等级鸟类，分析保护区鸟类资源的保护价值。
记录来源比较。比较文献记录、公众科学数据和作者调查记录在鸟类名录更新中的作用，分析不同数据来源的互补性。
新增鸟类梳理。明确本次研究新增鸟类种类及其保护属性，为后续保护区鸟类监测提供补充资料。
2.2研究方法
实地调查
采用网捕调查、野外观察记录以及参与观鸟活动等方式收集鸟类数据。网捕法用于补充隐蔽性强、小型林鸟记录，鸟网设置方法参考相关研究[8]。同时，结合野外实习与观鸟活动记录，以提高鸟类资料收集的完整性。
资料收集
收集《雷公山自然保护区科学考察集》《雷公山国家级自然保护区生物多样性研究》等历史资料[2-3]，并整理中国观鸟记录中心、China-eBird 等公众科学平台中的观鸟数据[5]。
数据处理
依据《中国鸟类分类与分布名录（第四版）》对鸟类名称、分类系统和区系进行统一整理[6]，结合《国家重点保护野生动物名录》、中国生物多样性红色名录和 IUCN 红色名录统计鸟类保护等级与受威胁状况[14-16]。
综合分析
通过比对不同来源记录，梳理雷公山保护区鸟类名录，统计新增鸟类及珍稀濒危鸟类，分析多种调查手段在保护区鸟类监测中的互补作用[9-10]。"""

cell_r5 = """2.3拟解决的关键问题
雷公山国家级自然保护区鸟类名录更新问题。通过整合历史文献、公众科学记录和作者调查数据，形成较为完整的鸟类名录。
保护区珍稀濒危鸟类现状问题。明确保护区国家重点保护鸟类、特有种及受威胁鸟类情况，评估其保护价值。
不同数据来源互补性问题。分析文献资料、公众科学观鸟与实地调查在鸟类多样性记录中的差异和互补作用。
新增鸟类及后续监测基础问题。梳理本次研究新增鸟类，为保护区长期监测和物种保护提供数据支持。

3完成毕业论文所必需具备的工作条件及解决的办法
1.工作条件
调查基础：
论文研究对象、资料来源和基础数据已经明确，已掌握历史文献、公众科学记录及实地调查数据。
调查设备：
具备望远镜、鸟网、相机等鸟类调查设备，可满足野外观察、网捕与记录需求。
资料条件：
可依托学校图书馆、知网及相关观鸟平台获取文献和公众科学数据，为名录整理与分析提供资料支持。
数据处理条件：
具备整理物种名录、核对分类系统和统计保护等级所需的基础条件，可完成论文数据整理与文本撰写。
2.解决办法
资料整合与核对：
系统整理历史文献、调查记录和公众科学数据，对重复记录和分类变动进行逐条核对，保证名录准确性。
调查补充与记录规范：
结合网捕法和野外观察补充部分隐蔽鸟类记录，统一记录标准，提高数据的可靠性与可比性。
文献查阅与分类修订：
依据最新鸟类分类名录和保护名录，对中文名、拉丁名、保护等级及区系信息进行修订和补充。
进度控制与指导修改：
按照论文计划分阶段完成资料收集、数据整理、结果分析和论文修改，并及时根据指导教师意见完善内容。"""

section4 = """2025年9月-2025年10月：确定论文选题，查阅雷公山自然保护区鸟类多样性相关文献，完成开题报告撰写。
2025年10月-2025年12月：整理历史文献资料、公众科学数据和作者已有调查记录，初步形成鸟类名录。
2026年1月-2026年2月：完成鸟类分类系统、保护等级、区系和记录来源等信息整理，统计新增鸟类和珍稀濒危鸟类。
2026年2月-2026年3月：完成论文初稿撰写，并根据指导教师意见修改完善。
2026年4月：进一步核对参考文献、附录和鸟类名录，完成论文定稿准备。
2026年5月：完成答辩准备、论文答辩及相关毕业材料提交工作。"""

section5 = """前言
1 研究区与研究方法
1.1 研究区概况
1.2 数据收集
1.3 数据处理
2 研究结果
2.1 鸟类群落组成
2.2 珍稀濒危鸟类
2.3 鸟类记录来源
2.4 新增鸟类
3 讨论
参考文献
附录
致谢"""

section6 = """ [1]\t何芳，王秦韵，肖梅，等. 四川唐家河国家级自然保护区鸟类多样性[J]. 四川动物，2025，44（1）：96-101.
 [2]\t周政贤，姚茂森，莫文理，等. 雷公山自然保护区科学考察集[M]. 贵阳：贵州人民出版社，1989.
 [3]\t张华海，张旋，谢镇国，等. 雷公山国家级自然保护区生物多样性研究[M]. 贵阳：贵州科技出版社，2007.
 [4]\t李扬，余德会，宋志红，等. 贵州雷公山国家级自然保护区红外相机鸟兽监测[J]. 野生动物学报，2022，43（3）：704-714.
 [5]\t顾燚芸，薛嘉祈，高金会，等. 一种基于公众科学数据的区域性鸟类多样性评价方法[J]. 生物多样性，2024，32（7）：24080.
 [6]\t郑光美. 中国鸟类分类与分布名录（第四版）[M]. 北京：科学出版社，2023.
 [7]\t罗祖奎，刘伦沛，王云，等. 贵州省云台山鸟类群落特征[J]. 华东师范大学学报（自然科学版），2013（5）：43-52.
 [8]\t邹发生，陈桂珠. 雾网在森林鸟类群落研究中的应用[J]. 应用生态学报，2003，14（9）：1557-1560.
 [9]\t刘萌萌，张曼玉，韩茜，等. 公众观鸟和传统样线法调查应用于鸟类多样性监测的比较：以南京老山为例[J]. 生态与农村环境学报，2023，39（9）：1196-1204.
 [10]\t朱淑怡，段菲，李晟. 基于红外相机网络促进我国鸟类多样性监测：现状、问题与前景[J]. 生物多样性，2017，25（10）：1114-1122.
 [11]\tSHI J B，LI D Q，XIAO W F. A review of impacts of climate change on birds：implications of long-term studies[J]. Zoological Research，2006，27（6）：637-646.
 [12]\t孙全辉，张正旺. 气候变暖对我国鸟类分布的影响[J]. 动物学杂志，2000，35（6）：45-48.
 [13]\t杜寅，周放，舒晓莲，等. 全球气候变暖对中国鸟类区系的影响[J]. 动物分类学报，2009，34（3）：664-674.
 [14]\t国家林业和草原局，农业农村部. 国家重点保护野生动物名录（2021年版）[J]. 野生动物学报，2021，42（2）：605-640.
 [15]\t生态环境部. 中国生物多样性红色名录——脊椎动物卷（2020）[M]. 2023.
 [16]\tIUCN. The IUCN red list of threatened species[EB/OL]. [2025-09-27]. https://www.iucnredlist.org/en."""

ps_script = textwrap.dedent(
    f"""
    $ErrorActionPreference = 'Stop'
    $src = '{src}'
    $dst = '{dst}'
    Copy-Item -LiteralPath $src -Destination $dst -Force
    $newTitle = '{new_title}'
    $newName = '{new_name}'
    $newId = '{new_id}'
    $cellR4 = {ps_here_string(cell_r4)}
    $cellR5 = {ps_here_string(cell_r5)}
    $section4 = {ps_here_string(section4)}
    $section5 = {ps_here_string(section5)}
    $section6 = {ps_here_string(section6)}

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

    function Apply-Reference-Formatting($dstCell, $srcCell) {{
        $dstParas = $dstCell.Range.Paragraphs
        $srcHeader = $srcCell.Range.Paragraphs.Item(1).Range
        $srcRef = $srcCell.Range.Paragraphs.Item(2).Range
        Copy-Range-Format $srcHeader $dstParas.Item(1).Range
        for ($i = 2; $i -le $dstParas.Count; $i++) {{
            $txt = ($dstParas.Item($i).Range.Text -replace "[`r`a]", "")
            if ([string]::IsNullOrWhiteSpace($txt)) {{
                continue
            }}
            $r = $dstParas.Item($i).Range
            $r.Font.NameFarEast = $srcRef.Font.NameFarEast
            $r.Font.NameAscii = $srcRef.Font.NameAscii
            $r.Font.NameOther = $srcRef.Font.NameOther
            $r.Font.Size = $srcRef.Font.Size
            $r.Font.Bold = $srcRef.Font.Bold
            $r.Font.Italic = $srcRef.Font.Italic
            $pf = $r.ParagraphFormat
            $pf.Alignment = $srcRef.ParagraphFormat.Alignment
            $pf.LineSpacingRule = $srcRef.ParagraphFormat.LineSpacingRule
            $pf.LineSpacing = $srcRef.ParagraphFormat.LineSpacing
            $pf.LeftIndent = 12
            $pf.FirstLineIndent = 0
            $pf.RightIndent = 0
            $pf.SpaceBefore = 0
            $pf.SpaceAfter = 0
            $pf.CharacterUnitLeftIndent = 0
            $pf.CharacterUnitFirstLineIndent = 0
        }}
    }}

    function Apply-Superscript-Citations($doc, $cell) {{
        $text = $cell.Range.Text
        $baseStart = $cell.Range.Start
        $matches = [regex]::Matches($text, '\\[[0-9,\\-]+\\]')
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
        Replace-All-Exact $doc '莫国庆' $newName
        Replace-All-Exact $doc '2022401003' $newId

        Set-Cell-Text $doc.Tables.Item(1).Cell(4,1) $cellR4
        Set-Cell-Text $doc.Tables.Item(1).Cell(5,1) $cellR5
        Set-Cell-Text $doc.Tables.Item(2).Cell(1,1) ('4工作的计划、进度与时间安排' + "`r" + $section4.Trim())
        Set-Cell-Text $doc.Tables.Item(2).Cell(2,1) ('5论文写作提纲（要求至少到二级标题）' + "`r" + $section5.Trim())
        Set-Cell-Text $doc.Tables.Item(2).Cell(3,1) ('6参考文献（不少于15篇）' + "`r" + $section6.TrimEnd())

        Copy-Range-Format $srcDoc.Tables.Item(1).Cell(4,1).Range $doc.Tables.Item(1).Cell(4,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(1).Cell(5,1).Range $doc.Tables.Item(1).Cell(5,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(2).Cell(1,1).Range $doc.Tables.Item(2).Cell(1,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(2).Cell(2,1).Range $doc.Tables.Item(2).Cell(2,1).Range
        Copy-Range-Format $srcDoc.Tables.Item(2).Cell(3,1).Range $doc.Tables.Item(2).Cell(3,1).Range

        Apply-Paragraph-Templates $doc.Tables.Item(1).Cell(4,1) $srcDoc.Tables.Item(1).Cell(4,1) @(1,2,3,4,5,6,7,8,9,11,12,15,16,17,18,19,20,20,21,22,25,26)
        Apply-Paragraph-Templates $doc.Tables.Item(1).Cell(5,1) $srcDoc.Tables.Item(1).Cell(5,1) @(1,2,3,4,4,4,6,7,8,9,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27)
        Apply-Paragraph-Templates $doc.Tables.Item(2).Cell(1,1) $srcDoc.Tables.Item(2).Cell(1,1) @(1,2,3,4,5,6,7)
        Apply-Paragraph-Templates $doc.Tables.Item(2).Cell(2,1) $srcDoc.Tables.Item(2).Cell(2,1) @(1,2,3,4,5,6,7,8,9,10,11,12,13)
        Apply-Reference-Formatting $doc.Tables.Item(2).Cell(3,1) $srcDoc.Tables.Item(2).Cell(3,1)
        Apply-Superscript-Citations $doc $doc.Tables.Item(1).Cell(4,1)
        Apply-Superscript-Citations $doc $doc.Tables.Item(1).Cell(5,1)
        Apply-Superscript-Citations $doc $doc.Tables.Item(2).Cell(1,1)

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
