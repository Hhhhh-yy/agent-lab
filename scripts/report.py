# scripts/report.py
# 作用：统计 data/clean -> 写 data/report.json -> 读回来核对
import json
from collections import Counter
from pathlib import Path

CLEAN_DIR = Path("data/clean")
REPORT = Path("data/report.json")


def top_bigrams(text: str, k: int = 5) -> list[list]:
    """中文没空格，先按 2 字一组粗切，只为演示统计这件事"""
    grams = [text[i:i + 2] for i in range(len(text) - 1)]
    return [[g, c] for g, c in Counter(grams).most_common(k)]


def main() -> None:
    items = []
    for p in sorted(CLEAN_DIR.glob("*.txt")):
        if p.name.endswith(".summary.txt"):
            continue
        text = p.read_text(encoding="utf-8")
        items.append({
            "file": p.name,
            "lines": len(text.splitlines()),
            "chars": len(text),
            "top_bigrams": top_bigrams(text),
        })

    report = {
        "file_count": len(items),
        "total_chars": sum(i["chars"] for i in items),
        "files": items,
    }
    REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),  # 中文不转义，便于肉眼读
        encoding="utf-8",
    )

    back = json.loads(REPORT.read_text(encoding="utf-8"))  # 读回来验证能解析
    print(f"文件数={back['file_count']} 总字符={back['total_chars']}")
    for i in back["files"]:
        print(f"  {i['file']}: {i['lines']} 行 / {i['chars']} 字符")


if __name__ == "__main__":
    main()