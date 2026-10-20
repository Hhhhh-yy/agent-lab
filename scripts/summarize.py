# scripts/summarize.py
# 作用：data/clean 每个 txt -> 一句话摘要
import os
from pathlib import Path
from openai import OpenAI

CLEAN_DIR = Path("data/clean")
MAX_CHARS = 2000          # 只喂前 2000 字，控制费用
BASE_URL = "http://127.0.0.1:3065/v1"
# 模型名先用环境变量，方便你换
MODEL = os.environ.get("DS_MODEL", "")
PROMPT = "你用一句中文概括内容，不超过 40 字，不加解释。"


def get_client() -> OpenAI:
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        raise SystemExit("没读到 DEEPSEEK_API_KEY")
    return OpenAI(api_key=key, base_url=BASE_URL)


def summarize(client: OpenAI, text: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": text[:MAX_CHARS]},
        ],
        temperature=0.2,
    )
    # content 可能是 None，兜一下
    return (resp.choices[0].message.content or "").strip()


def main() -> None:
    if not MODEL:
        raise SystemExit("没设 DS_MODEL，先设模型名")
    client = get_client()
    for p in sorted(CLEAN_DIR.glob("*.txt")):
        if p.name.endswith(".summary.txt"):
            continue
        s = summarize(client, p.read_text(encoding="utf-8"))
        out = p.parent / (p.stem + ".summary.txt")
        out.write_text(s + "\n", encoding="utf-8")
        print(f"{p.name} -> {s}")


if __name__ == "__main__":
    main()