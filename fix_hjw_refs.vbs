Dim word, doc, cell, paras, i, txt, p
On Error Resume Next
Set word = CreateObject("Word.Application")
word.Visible = False
word.DisplayAlerts = 0
Set doc = word.Documents.Open("C:\Users\mgq56\Desktop\毕业论文\黄晋望开题报告-按论文修改.doc")
If Err.Number <> 0 Then
  WScript.Echo "OPEN_ERR:" & Err.Number
  WScript.Quit 1
End If
Set cell = doc.Tables.Item(2).Cell(3,1)
Set paras = cell.Range.Paragraphs
For i = 2 To paras.Count
  Set p = paras.Item(i).Range
  txt = p.Text
  txt = Replace(txt, Chr(13), "")
  txt = Replace(txt, Chr(7), "")
  If Trim(txt) <> "" Then
    p.Text = " " & Trim(txt) & vbCr
    p.ParagraphFormat.LeftIndent = 18
    p.ParagraphFormat.FirstLineIndent = 0
    p.ParagraphFormat.RightIndent = 0
    p.ParagraphFormat.SpaceBefore = 0
    p.ParagraphFormat.SpaceAfter = 0
    p.Font.Superscript = False
  End If
Next
doc.Save
doc.Close
word.Quit
WScript.Echo "OK"
