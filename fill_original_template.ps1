$sourcePath = 'C:\Users\mgq56\Desktop\罗智谦.doc'
$outputPath = 'C:\Users\mgq56\Desktop\罗智谦-按原模板填写.doc'

Copy-Item -LiteralPath $sourcePath -Destination $outputPath -Force

$lessonLines = @{
    4  = '课题：《沁园春·长沙》                                        课  型：诗歌鉴赏新授课'
    14 = '课题：《立在地球边上放号》                                        课  型：现代诗歌鉴赏课'
    24 = '课题：《红烛》                                        课  型：诗歌鉴赏课'
    34 = '课题：《百合花》                                        课  型：小说阅读课'
}

$recordCells = @(
    @{
        Table = 1
        Process = '教师先从时代背景和青年理想导入，组织学生反复诵读，指导字音与节奏；随后抓住“独立寒秋”“层林尽染”“万类霜天竞自由”等词句赏析上阕壮阔秋景，再围绕“问苍茫大地，谁主沉浮”分析下阕的时代担当，最后小结全词主旨并布置背诵作业。'
        Comment = '本节课思路清晰，朗读训练充分，能以问题链带动学生把握词作“上阕写景、下阕抒怀”的结构特点；景物赏析与情感探究结合较紧，较好体现了诗词教学的人文性，若能进一步增加学生自主表达时间，课堂效果会更好。'
    }
    @{
        Table = 2
        Process = '教师从五四新文化运动背景切入，先引导学生朗读诗歌、感受节奏与气势，再抓住“怒涌”“滚滚”“燃了起来”等词语分析诗歌的动态美和力量感；课堂重点讨论“立在地球边上”的想象视角及诗歌呼唤新世界的精神内核，最后完成主题总结与拓展阅读布置。'
        Comment = '本节课较好抓住了现代新诗重诵读、重感受的特点，时代背景介绍到位，便于学生理解作品中强烈的情感张力；问题设置有梯度，从语言到主题层层推进，如果板书能更突出“宏阔景象、激越情绪、创造精神”三条线索，会更利于整体把握。'
    }
    @{
        Table = 3
        Process = '课堂由“蜡烛的象征意义”导入，教师带领学生反复诵读，体会“红烛啊”反复呼告形成的节奏与情感；随后围绕“烧吧！烧吧！”“莫问收获，但问耕耘”等句分析红烛意象的象征意义，理解诗人自我燃烧、执着追求、勇于担当的精神。'
        Comment = '本节课情感目标落实较好，教师善于通过诵读带动理解，让学生在朗读中进入诗歌情境；对“红烛”象征意义和诗中奉献精神的分析较为准确，若能增加学生对重点诗节的自主赏析展示，课堂生成会更加充分。'
    }
    @{
        Table = 4
        Process = '教师以“战争题材是否只能写残酷”导入，随后组织学生梳理“借被子、送被子、盖被子”的情节线索，分析通讯员、新媳妇和“我”三个人物形象；课堂重点讨论“百合花被子”的象征意义，并从细节描写入手理解作品如何表现战争背景下的人性美和军民深情。'
        Comment = '本节课文本细读较扎实，教师能抓住人物、情节和物象展开分析，问题设置贴近学生思维；对“百合花”所象征的纯洁与温暖点拨准确，若能进一步联系战争背景展开主题提升，学生的理解会更深刻。'
    }
)

$planTables = @(
    @{
        Table = 5
        Title = '《沁园春·长沙》'
        Method = '诵读法、问题引导法、合作探究法、点拨归纳法'
        Type = '诗歌鉴赏新授课'
        Goal = '1. 了解词作背景和体裁特点，准确诵读并背诵全词。2. 把握典型意象与上下阕结构，体会壮阔秋景和青春情怀。3. 理解“谁主沉浮”所体现的时代责任意识。'
        KeyPoint = '重点是分析意象特点和情景交融手法；难点是把握词人由自然秋景上升到时代思考的情感逻辑。'
        Process1 = '导入新课，简介背景；初读正音，整体感知；赏析上阕写景，把握“看”字统领的意象群；赏析下阕抒怀，理解“问苍茫大地，谁主沉浮”的思想内涵；最后总结主旨并布置背诵和赏析作业。'
        Process2 = '一是由“悲秋”传统导入，突出本词秋景的昂扬壮美；二是通过诵读和问题探究理解景物描写与人物精神的关系；三是联系“同学少年”“中流击水”等句体会青年革命者胸怀天下的担当。'
        Board = '《沁园春·长沙》 上阕写景：万山、层林、漫江、百舸、鹰、鱼；下阕抒怀：同学少年、谁主沉浮、中流击水；主旨：青春理想与时代担当。'
    }
    @{
        Table = 6
        Title = '《立在地球边上放号》'
        Method = '诵读法、情境教学法、合作讨论法、比较赏析法'
        Type = '现代诗歌鉴赏课'
        Goal = '1. 了解郭沫若及《女神》的创作背景。2. 反复诵读诗歌，把握宏阔意象、强烈节奏和喷薄情感。3. 理解诗歌表现的破旧立新和呼唤新世界的精神力量。'
        KeyPoint = '重点是品味动词、呼告和反复手法；难点是理解诗人宏大想象背后的时代意义与青年精神。'
        Process1 = '先介绍五四时代背景，随后通过教师范读和学生朗读感知诗歌气势；再抓住“怒涌”“滚滚”“燃了起来”等词赏析语言特点，讨论“立在地球边上”的想象视角和“放号”的象征含义，最后归纳主题。'
        Process2 = '课堂突出朗读体验与时代联系，引导学生认识本诗以强烈节奏和宏阔景象表现对旧世界的冲决、对新生力量的礼赞，并安排朗诵和短评写作作为课后巩固。'
        Board = '《立在地球边上放号》 视角：立在地球边上；语言：怒涌、滚滚、燃烧；主题：破坏旧世界，呼唤新生力量。'
    }
    @{
        Table = 7
        Title = '《红烛》'
        Method = '诵读法、点拨法、合作探究法、赏析法'
        Type = '诗歌鉴赏课'
        Goal = '1. 理解“红烛”这一核心意象的象征意义。2. 学习从反复、呼告、象征等角度赏析新诗语言。3. 感受诗人自我燃烧、无私奉献的理想人格与责任意识。'
        KeyPoint = '重点是理解“红烛”意象与诗人精神追求之间的关系；难点是把握“流泪”与“发光”、“痛苦”与“奉献”的复杂情感。'
        Process1 = '由蜡烛的象征意义导入，简介闻一多及背景；通过反复诵读体会“红烛啊”的呼告节奏；围绕“烧吧！烧吧！”“莫问收获，但问耕耘”等句分析红烛意象，理解诗人的理想追求与奉献精神。'
        Process2 = '在合作探究中引导学生认识诗人并非单纯赞美牺牲，而是在追问生命价值，强调在痛苦中坚守理想、照亮他人；结尾进行课堂总结并布置诗节赏析练笔。'
        Board = '《红烛》 意象：红烛；特点：燃烧、流泪、发光；精神：自我奉献、执着追求、勇于担当。'
    }
    @{
        Table = 8
        Title = '《百合花》'
        Method = '情境导入法、文本细读法、合作探究法、讨论归纳法'
        Type = '小说阅读课'
        Goal = '1. 梳理小说情节，把握人物关系和叙述线索。2. 通过典型细节分析通讯员、新媳妇和“我”的人物形象。3. 理解“百合花被子”的象征意义，体会战争环境下的人性美与军民情谊。'
        KeyPoint = '重点是通过细节描写分析人物形象与主题思想；难点是理解小说如何以小见大，在平凡故事中表现崇高情感。'
        Process1 = '先以“战争文学是否只能写残酷”导入，再梳理“借被子、送被子、盖被子”的情节；接着分析通讯员、新媳妇和“我”的形象，重点讨论百合花被子的线索作用和象征意义，理解作品的人性美。'
        Process2 = '课堂通过细节品读突出小说语言清新细腻、情感含蓄真挚的特点，引导学生认识作品在战争背景下写出普通人物的纯洁与崇高，并布置人物赏析短文作为作业。'
        Board = '《百合花》 情节：借被子、送被子、盖被子；人物：通讯员、新媳妇、“我”；物象：百合花被子；主题：战争中的人性美与军民情。'
    }
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($outputPath)

foreach ($index in $lessonLines.Keys) {
    $doc.Paragraphs.Item($index).Range.Text = $lessonLines[$index] + "`r"
}

foreach ($item in $recordCells) {
    $table = $doc.Tables.Item($item.Table)
    $table.Cell(2,1).Select()
    $word.Selection.TypeText($item.Process)
    $table.Cell(2,2).Select()
    $word.Selection.TypeText($item.Comment)
}

foreach ($item in $planTables) {
    $table = $doc.Tables.Item($item.Table)
    $table.Cell(1,2).Select()
    $word.Selection.TypeText($item.Title)
    $table.Cell(2,2).Select()
    $word.Selection.TypeText($item.Method)
    $table.Cell(2,4).Select()
    $word.Selection.TypeText($item.Type)
    $table.Cell(3,2).Select()
    $word.Selection.TypeText($item.Goal)
    $table.Cell(4,2).Select()
    $word.Selection.TypeText($item.KeyPoint)
    $table.Cell(5,2).Select()
    $word.Selection.TypeText($item.Process1)
    $table.Cell(6,1).Select()
    $word.Selection.TypeText('教学内容及过程：')
    $word.Selection.TypeParagraph()
    $word.Selection.TypeText($item.Process2)
    $table.Cell(7,1).Select()
    $word.Selection.TypeText('板书设计：')
    $word.Selection.TypeParagraph()
    $word.Selection.TypeText($item.Board)
}

$doc.Save()
$doc.Close()
$word.Quit()

Get-Item -LiteralPath $outputPath | Format-List FullName,Length,LastWriteTime


