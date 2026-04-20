import shutil
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}
ET.register_namespace("w", W_NS)


def paragraph_text(p):
    return "".join((t.text or "") for t in p.findall(".//w:t", NS))


def set_paragraph_text(p, text):
    runs = p.findall("./w:r", NS)
    if not runs:
        r = ET.SubElement(p, f"{{{W_NS}}}r")
        t = ET.SubElement(r, f"{{{W_NS}}}t")
        if text.startswith(" ") or text.endswith(" "):
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t.text = text
        return

    first_t = None
    for r in runs:
        t = r.find("./w:t", NS)
        if t is not None:
            first_t = t
            break
    if first_t is None:
        first_t = ET.SubElement(runs[0], f"{{{W_NS}}}t")

    if text.startswith(" ") or text.endswith(" "):
        first_t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    first_t.text = text

    for r in runs:
        for child in list(r):
            if child.tag == f"{{{W_NS}}}t" and child is not first_t:
                r.remove(child)
        # remove drawing from caption/正文 replacement paragraphs
        for child in list(r):
            if child.tag in {
                f"{{{W_NS}}}drawing",
                f"{{{W_NS}}}object",
                f"{{{W_NS}}}pict",
            }:
                r.remove(child)

    # remove extra runs that became empty and have no formatting significance
    keep_seen = False
    for r in list(p):
        if r.tag != f"{{{W_NS}}}r":
            continue
        t = r.find("./w:t", NS)
        has_text = t is not None and (t.text or "") != ""
        if has_text and not keep_seen:
            keep_seen = True
            continue
        if r.find("./w:br", NS) is not None or r.find("./w:tab", NS) is not None:
            continue
        if not list(r) or all(child.tag == f"{{{W_NS}}}rPr" for child in list(r)):
            p.remove(r)
        elif not has_text and r.find("./w:t", NS) is None:
            p.remove(r)


def main():
    desktop = Path(r"C:\Users\mgq56\Desktop")
    preferred = [
        "龙正权_大学生生物认知度与其生物课程成绩关系研究_图文讨论修正版.docx",
        "龙正权_大学生生物认知度与其生物课程成绩关系研究_目录纯文本版.docx",
    ]
    src = None
    for name in preferred:
        candidate = desktop / name
        if candidate.exists():
            src = candidate
            break
    if src is None:
        src = next(p for p in desktop.glob("龙正权_*.docx") if not p.name.startswith("~$"))

    dst = desktop / "龙正权_大学生生物认知度与其生物课程成绩关系研究_结构优化版.docx"
    shutil.copy2(src, dst)

    with zipfile.ZipFile(dst, "r") as zin:
        xml_bytes = zin.read("word/document.xml")
        other_files = {name: zin.read(name) for name in zin.namelist() if name != "word/document.xml"}

    root = ET.fromstring(xml_bytes)
    body = root.find(".//w:body", NS)
    paragraphs = body.findall("./w:p", NS)

    def p(idx):
        return paragraphs[idx - 1]

    replacements = {
        117: "各因素与大二专业课平均成绩的相关性矩阵如图4及表2所示。四个认知因素维度均与大二专业课平均成绩呈显著正相关，其中个人因素与成绩的相关系数最高（r=0.805，p<0.001），教育因素次之（r=0.719，p<0.001），社会文化因素（r=0.505，p<0.001）与技术媒体因素（r=0.514，p<0.001）也均与成绩存在显著正相关关系。",
        120: "图4  各因素与大二专业课平均成绩相关性矩阵",
        121: "表2  各因素与大二专业课平均成绩相关性矩阵",
        124: "以四个认知因素维度为自变量、大二专业课平均成绩为因变量，进行多元线性回归分析，结果如图5及表3所示。回归模型整体显著（F=151.313，p<0.001），模型解释了成绩变异的83.6%（R²=0.836，调整R²=0.830），说明四维认知结构与大二专业课平均成绩之间存在较强统计关联。需要注意的是，较高的拟合度一方面可能与结果变量采用连续成绩有关，另一方面也可能受到同源自报数据的影响，因此不宜将模型解释力直接理解为现实中的因果效应强度。为避免对模型稳定性作过度解释，本研究进一步补充了共线性与残差诊断，结果见支撑表中的“共线性检验”与“回归诊断”工作表。",
        125: "从各预测变量的标准化回归系数来看，个人因素（β=0.580，p<0.001）与大二专业课平均成绩的统计关联最强，教育因素（β=0.384，p<0.001）次之，社会文化因素（β=0.144，p=0.001）也达到显著水平；技术媒体因素（β=0.039，p=0.398）在控制其他维度后未达显著水平。共线性检验显示各变量VIF仅为1.28—1.71，未见严重共线性；Durbin-Watson为2.015，残差独立性较好；Shapiro-Wilk检验p=0.5089，残差分布基本符合正态假设。Breusch-Pagan检验p=0.0480，提示模型可能存在轻微异方差风险，因此回归结果在解释时应保持审慎。",
        128: "图5  各因素对大二专业课平均成绩的回归系数（标准化β）",
        136: "本研究结果显示，大学生生物认知度与大二专业课平均成绩之间存在较清晰的层次差异。就描述统计而言，社会文化因素得分最高，说明学生对生物知识的现实应用价值、生物多样性保护及相关社会议题已有较强认同；而个人因素得分最低，则提示学生在基础概念理解、知识辨识与自我认知监控方面仍有进一步提升空间。",
        137: "从与成绩的关系看，个人因素始终是解释力最强的维度。无论在相关分析还是回归分析中，个人因素都表现出最突出的统计关联，说明学习兴趣、总体了解程度、客观知识辨识能力和基础概念理解与较好课程表现之间联系更为紧密。这一结果与元认知和自我调节学习理论较为一致，也提示成绩差异未必主要来自信息接触多少，而更可能与学生是否形成了较稳定的知识加工和自我监控能力有关。",
        138: "教育因素同样值得重视。课堂听讲覆盖率最高，而实验操作使用率相对偏低，说明当前学习方式仍以接受式学习为主。结合回归结果看，科普活动参与、基础技术了解以及学习渠道多样化与成绩之间存在显著正向关联，这意味着教学改进的重点不只是增加信息输入，还应增强实践参与和学习方式的丰富度。",
        141: "从理论角度看，本研究基于四维框架考察了大学生生物认知度与大二专业课平均成绩之间的统计关系，进一步说明个人认知因素和教育因素并非彼此割裂，而是共同构成影响学业表现的重要认知背景；社会文化因素虽不是最强预测维度，但也不是可以忽略的外围变量。",
        142: "在教学实践层面，本研究的启示主要集中在三个方面：一是把基础概念理解、知识辨析训练和学习反思活动放在更突出的位置，优先夯实个人认知基础；二是适当增加实验操作、案例分析和项目学习等实践性环节，改善学习活动过于单一的问题；三是引导学生把网络资源从信息获取工具进一步转化为服务理解、整合与反思的学习工具。上述建议是依据变量间关联提出的教学判断，不应直接视为严格的干预因果结论。",
    }

    for idx, text in replacements.items():
        set_paragraph_text(p(idx), text)

    # Remove figure 6 image paragraph and caption paragraph.
    for idx in sorted([137, 130, 129], reverse=True):
        body.remove(p(idx))
        paragraphs.pop(idx - 1)

    new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in other_files.items():
            zout.writestr(name, data)
        zout.writestr("word/document.xml", new_xml)

    print(dst)


if __name__ == "__main__":
    main()
