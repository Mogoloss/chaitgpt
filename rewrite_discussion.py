import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}
ET.register_namespace("w", W_NS)


def set_paragraph_text(p, text):
    runs = p.findall("./w:r", NS)
    first_r = None
    first_t = None
    for r in runs:
        t = r.find("./w:t", NS)
        if t is not None:
            first_r = r
            first_t = t
            break
    if first_t is None:
        first_r = ET.SubElement(p, f"{{{W_NS}}}r")
        first_t = ET.SubElement(first_r, f"{{{W_NS}}}t")
    if text.startswith(" ") or text.endswith(" "):
        first_t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    first_t.text = text
    for r in list(p.findall("./w:r", NS)):
        for child in list(r):
            if child.tag == f"{{{W_NS}}}t" and not (r is first_r and child is first_t):
                r.remove(child)
            elif child.tag in {
                f"{{{W_NS}}}drawing",
                f"{{{W_NS}}}object",
                f"{{{W_NS}}}pict",
            }:
                r.remove(child)


path = Path(r"C:\Users\mgq56\Desktop\discussion_work.docx")

with zipfile.ZipFile(path, "r") as zin:
    xml = zin.read("word/document.xml")
    others = {n: zin.read(n) for n in zin.namelist() if n != "word/document.xml"}

root = ET.fromstring(xml)
body = root.find(".//w:body", NS)
paras = body.findall("./w:p", NS)

updates = {
    131: "5.1 主要研究发现",
    132: "结合第四章的描述统计、相关分析和回归分析结果可以看出，大学生生物认知度与大二专业课平均成绩之间确实存在较明确的对应关系，但这种对应并不是四个维度平均用力。先看总体得分，社会文化因素最高，为76.56%，个人因素最低，为60.75%。这说明受访学生对生物知识的现实价值、生态保护和社会议题并不陌生，态度层面的认同感相对较强；真正拉开差距的，反而是基础概念理解、知识辨识和自我判断这些更贴近学习过程本身的内容。",
    133: "从与成绩的关系看，个人因素是最值得重视的一项。在相关分析中，个人因素与大二专业课平均成绩的相关系数最高（r=0.805，p<0.001）；在回归分析中，它的标准化回归系数也最大（β=0.580，p<0.001）。教育因素同样表现突出，相关系数为0.719，回归系数为0.384，均达到显著水平。这个结果说明，学生最后呈现出来的成绩差异，很大程度上还是落在两类更具体的东西上：一类是对知识本身有没有真正理解，另一类是有没有在较好的学习支持和学习方式中把这种理解稳定下来。",
    134: "再结合学习方式的结果来看，课堂听讲的使用率最高，为94.35%，网络资源为76.61%，教材自学为70.16%，实验操作只有51.61%。这一分布说明，学生目前的学习重心仍然偏向接受式输入，实践性学习相对不足。与此同时，技术媒体因素虽然在相关分析中与成绩呈显著正相关（r=0.514，p<0.001），但进入回归模型后并未表现出独立显著作用（β=0.039，p=0.398）。换句话说，单纯“接触到信息”并不等于真正学会，网络资源更像是一种辅助条件，只有和个人理解能力、教育支持条件结合起来，才更可能转化为较稳定的课程表现。",
    135: "5.2 理论与实践意义",
    136: "从理论上说，本研究的意义不在于提出一个很新的概念，而在于把生物认知度拆开来看后，发现不同维度和成绩的关系并不一样。社会文化因素得分最高，却不是回归中最有解释力的变量；个人因素得分不高，却和成绩联系最紧。这一点提醒我们，认知并不是一个笼统的整体，它既包含态度认同，也包含知识理解和学习调节，而真正更贴近学业表现的，往往是后者。这个发现与前人关于元认知、自我调节学习的结论是能够互相印证的。",
    137: "从实践上看，前面的结果至少给出三点比较具体的启示。第一，教学中不能只停留在让学生“知道一点”，还要把基础概念理解、知识辨析和学习反思做扎实，因为这些内容与成绩的联系最直接。第二，实验操作和实践性学习的比重可以适当提高。图2已经说明，实验操作的使用率明显低于课堂听讲，如果长期停留在听和记的层面，学生对知识的掌握就容易停在表面。第三，网络资源可以继续用，但重点不应放在“看得多不多”，而应放在“能不能把看到的信息转化为自己的理解”。这些建议都只是依据统计关联提出的教学判断，不能直接当作严格的因果结论。",
    138: "5.3 研究局限与展望",
    139: "本研究也有比较明显的边界。样本只来自同一院校，外部推广需要谨慎；成绩数据来自学生自报，而不是直接提取自教务系统，这会带来一定测量误差；认知指标和成绩又是在同一时间点收集的，因此相关结果更容易反映同步变化，而不是先后影响关系。另外，回归诊断中Breusch-Pagan检验p=0.0480，提示模型存在轻微异方差风险，这也意味着结果虽然总体稳定，但在解释时仍应保留必要的审慎。",
    140: "后续研究可以从几个更扎实的方向继续推进：一是扩大样本来源，把不同地区、不同层次高校的生物学专业学生纳入比较；二是尽量引入教务系统成绩、课程考核成绩或客观测验成绩，减少同源数据偏差；三是把横截面数据进一步延伸为纵向跟踪，看看认知变化和成绩变化是否具有持续对应关系；四是结合访谈、学习日志等材料，补足问卷数据难以呈现的学习过程细节。这样做之后，关于生物认知度与课程成绩之间的关系，才能解释得更完整，也更有说服力。",
}

for idx, text in updates.items():
    set_paragraph_text(paras[idx - 1], text)

new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
    for n, d in others.items():
        zout.writestr(n, d)
    zout.writestr("word/document.xml", new_xml)

print("done")
