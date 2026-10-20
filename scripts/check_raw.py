# scripts/inspect.py
# 作用：只读不写。报告每个 txt 的编码、行数、首末行
from pathlib import Path

RAW_DIR = Path("data/raw")   # 相对路径，以"你运行命令时所在目录"为准


def decode_file(path: Path) -> tuple[str, str]:
    """先按 utf-8 解，失败再按 gbk 解；返回(编码名, 文本)"""
    raw = path.read_bytes()        # 拿原始字节，先不解码
    for enc in ("utf-8", "gbk"):   # 两个最常见的编码依次试
        try:
            return enc, raw.decode(enc)
        except UnicodeDecodeError:  # 这个编码解不了 -> 换下一个
            continue
    return "unknown", ""            # 两个都不行，交给人看


def main() -> None:
    files = sorted(RAW_DIR.glob("*.txt"))
    print(f"共找到 {len(files)} 个 txt")
    for p in files:
        enc, text = decode_file(p)
        lines = text.splitlines()
        head = lines[0][:30] if lines else "(空文件)"
        tail = lines[-1][:30] if lines else ""
        print(f"{p.name} | 编码={enc} | 行数={len(lines)} | 字符={len(text)}")
        print(f"    首行: {head}")
        print(f"    末行: {tail}")


if __name__ == "__main__":   # 只有直接运行这个文件时才执行 main
    main()