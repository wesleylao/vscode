from xml.etree import ElementTree as ET

# 讀取檔案（請確認路徑正確）
with open(r"C:\Users\wesle\Desktop\vscode\python learning\playlist.xml", "r", encoding="utf-8") as f:
    xml_text = f.read()

# 解析 XML
root = ET.fromstring(xml_text)

# 抓出所有 <song_name>
names = [e.text for e in root.findall(".//song_name") if e.text]

# 輸出成 TXT 檔
with open("song_names.txt", "w", encoding="utf-8") as out:
    for n in names:
        out.write(n + "\n")


