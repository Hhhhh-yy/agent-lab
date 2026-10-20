# scripts/clean.py
# 作用：data/raw -> 去脏行 -> 统一 utf-8 存到 data/clean
from pathlib import Path

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")


def is_dirty(line: str) -> bool:
    """命中任意一条就丢：空行、页码行、内部资料标记"""
    s = line.strip()
    if not s:
        return True
    if "页" in s and ("第" in s or "/" in s):   # 形如"第 3 页 / 共 9 页"
        return True
    return any(k in s for k in ("内部资料", "机密", "==="))


def load_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8", "gbk"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return ""


# scripts/clean.py  只贴改动的部分
# 作用：先把字面 nn 还原成换行，再做行级清洗

def is_dirty(line: str) -> bool:
    """命中任意一条就丢：空行、页码行、页眉标题行"""
    s = line.strip()
    if not s:
        return True
    if "页" in s and ("第" in s or "/" in s):
        return True
    if "测试文档" in s:      # 页眉：第 N 篇测试文档
        return True
    return any(k in s for k in ("内部资料", "机密", "==="))


def clean_text(text: str) -> str:
    text = text.replace("nn", "\n")   # 归一化：把字面 n 还原成真换行
    kept = [ln.strip() for ln in text.splitlines() if not is_dirty(ln)]
    return "\n".join(kept) + "\n"


def main() -> None:
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)  # 目录不在就建，已存在不报错
    for p in sorted(RAW_DIR.glob("*.txt")):
        before = len(load_text(p).splitlines())
        out = CLEAN_DIR / p.name          # 同名文件，换目录
        out.write_text(clean_text(load_text(p)), encoding="utf-8")
        after = len(out.read_text(encoding="utf-8").splitlines())
        print(f"{p.name}: {before} 行 -> {after} 行")


if __name__ == "__main__":
    main()