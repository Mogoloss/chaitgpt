import copy
import shutil
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}
ET.register_namespace("w", W_NS)


def clear_paragraph(p):
    for r in list(p.findall("./w:r", NS)):
        p.remove(r)


def set_text(p, text):
    clear_paragraph(p)
    r = ET.SubElement(p, f"{{{W_NS}}}r")
    t = ET.SubElement(r, f"{{{W_NS}}}t")
    if text.startswith(" ") or text.endswith(" "):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def make_para(template, text):
    p = copy.deepcopy(template)
    set_text(p, text)
    return p


def main():
    desktop = Path(r"C:\Users\mgq56\Desktop")
    src = next(p for p in desktop.glob("龙正权_*结构优化版.docx") if not p.name.startswith("~$"))
    dst = desktop / "龙正权_大学生生物认知度与其生物课程成绩关系研究_附录排版版.docx"
    shutil.copy2(src, dst)

    with zipfile.ZipFile(dst, "r") as zin:
        xml = zin.read("word/document.xml")
        others = {n: zin.read(n) for n in zin.namelist() if n != "word/document.xml"}

    root = ET.fromstring(xml)
    body = root.find(".//w:body", NS)
    paras = body.findall("./w:p", NS)

    title_para = paras[161]     # 162
    normal_template = paras[163]  # 164

    appendix_lines = [
        "",
        "Q1  您的性别（单选）",
        "    A. 男",
        "    B. 女",
        "",
        "Q2  姓名：____________",
        "Q3  年级：____________",
        "",
        "Q4  你对生物知识感兴趣吗？（单选）",
        "    A. 非常感兴趣，经常主动学习相关知识",
        "    B. 比较感兴趣，偶尔会关注",
        "    C. 一般，没有特别的感觉",
        "    D. 不太感兴趣，几乎不关注",
        "",
        "Q5  您认为生物知识在日常生活中的应用广泛吗？（单选）",
        "    A. 非常广泛，很多方面都离不开",
        "    B. 比较广泛，部分领域有应用",
        "    C. 一般，只有少数情况能用到",
        "    D. 不太广泛，几乎没什么作用",
        "",
        "Q6  您对生物知识的总体了解程度如何？（单选）",
        "    A. 非常了解，能深入探讨专业内容",
        "    B. 比较了解，掌握常见生物知识",
        "    C. 一般，只知道一些基础常识",
        "    D. 不太了解，接触较少",
        "",
        "Q7  你知道地球上大约有多少种已知生物吗？（单选）",
        "    A. 100万-500万",
        "    B. 500万-1000万",
        "    C. 1000万-2000万",
        "    D. 不清楚",
        "",
        "Q8  你是否了解生物分类的基本等级？（单选）",
        "    A. 非常了解",
        "    B. 了解一些",
        "    C. 听说过，不太清楚",
        "    D. 完全不了解",
        "",
        "Q9  植物进行光合作用的主要场所是？（单选）",
        "    A. 叶绿体",
        "    B. 线粒体",
        "    C. 其他",
        "",
        "Q10  你在日常生活中会关注生物相关的新闻信息吗？（单选）",
        "    A. 经常关注",
        "    B. 偶尔关注",
        "    C. 很少关注",
        "    D. 从不关注",
        "",
        "Q11  你是否听说过基因编辑技术？（单选）",
        "    A. 非常了解",
        "    B. 了解一些",
        "    C. 听说过，不太清楚",
        "    D. 完全不知道",
        "",
        "Q12  对生物学基础概念（如细胞结构、遗传规律）的理解（单选）",
        "    A. 非常理解",
        "    B. 一般理解",
        "    C. 不太理解",
        "    D. 完全不懂",
        "",
        "Q13  你是否参加过与生物相关的科普活动？（单选）",
        "    A. 经常参加",
        "    B. 参加过几次",
        "    C. 很少参加",
        "    D. 从未参加",
        "",
        "Q14  对生物学科前沿领域（如基因编辑、生态保护）的关注度（单选）",
        "    A. 非常关注",
        "    B. 一般关注",
        "    C. 很少关注",
        "    D. 从不关注",
        "",
        "Q15  如果有机会，您愿意参加生物科普志愿者活动吗？（单选）",
        "    A. 非常愿意，很想为科普做贡献",
        "    B. 比较愿意，看时间和精力安排",
        "    C. 不确定，要视具体情况而定",
        "    D. 不太愿意，觉得自己能力有限",
        "",
        "Q16  你认为导致生物多样性减少的主要原因是什么？（多选）",
        "    A. 栖息地被破坏",
        "    B. 过度捕捞和狩猎",
        "    C. 环境污染",
        "    D. 气候变化",
        "",
        "Q17  你认为生物多样性的重要性体现在哪些方面？（多选）",
        "    A. 提供食物、药物和工业原料",
        "    B. 维持生态平衡",
        "    C. 促进文化和艺术发展",
        "    D. 提供旅游和娱乐资源",
        "",
        "Q18  你是否知道一些濒危生物？（多选）",
        "    A. 大熊猫",
        "    B. 东北虎",
        "    C. 白鳍豚",
        "    D. 朱鹮",
        "",
        "Q19  你主要通过哪些方式学习生物？（多选）",
        "    A. 课堂听讲",
        "    B. 教材自学",
        "    C. 网络资源",
        "    D. 实验操作",
        "",
        "Q20  大二专业课平均成绩：____________",
        "",
    ]

    # remove old appendix content and stray line before acknowledgements: paragraphs 163..182
    for para in paras[162:182]:
        body.remove(para)

    insert_at = list(body).index(title_para) + 1
    new_paras = [make_para(normal_template, line) for line in appendix_lines]
    for offset, para in enumerate(new_paras):
        body.insert(insert_at + offset, para)

    new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in others.items():
            zout.writestr(name, data)
        zout.writestr("word/document.xml", new_xml)

    print(dst)


if __name__ == "__main__":
    main()
