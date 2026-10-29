"""Automatic grading: last \\boxed{} of each answer, parsed to a number, vs the reference.

    python grade.py            # writes grades.json
    python grade.py --selftest # parses every reference answer in the pool
"""
import argparse
import json
import pathlib
import math
import re

import sympy

ROOT = pathlib.Path(__file__).parent


def last_boxed(text):
    i = text.rfind("\\boxed")
    while i != -1:
        j = text.find("{", i)
        if j == -1:
            return None
        depth, k = 0, j
        while k < len(text):
            depth += {"{": 1, "}": -1}.get(text[k], 0)
            if depth == 0:
                return text[j + 1:k]
            k += 1
        i = text.rfind("\\boxed", 0, i)
    return None


def to_number(s, exact=False):
    if s is None:
        return None
    s = s.strip().strip("$").replace("\\\\", "\\")  # doubled backslashes
    s = re.sub(r"^\\\{(.*)\\\}$", r"\1", s)  # a one-element set \{3\}
    s = re.split(r"\\approx|≈", s)[0].replace("°", "")  # "21\pi \approx 65.97", "80°"
    s = re.sub(r"\\text\{[^}]*\}|\\mathrm\{[^}]*\}|\^\\circ|\^\{\\circ\}|\\%|\\,|\\!|\\ |\\left|\\right", "", s)
    s = s.replace("\\dfrac", "\\frac").replace("\\tfrac", "\\frac").replace("\\cdot", "*").replace("\\times", "*")
    s = s.split("=")[-1]  # "x = 5", "AO = 65/3", "6^7 8^5 = 9172942848"
    s = re.sub(r"(?<=\d),(?=\d{3}\b)", "", s)  # thousands separators
    for _ in range(4):
        s = re.sub(r"\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"((\1)/(\2))", s)
        s = re.sub(r"\\frac\s*(\d)\s*(\d)", r"((\1)/(\2))", s)
        s = re.sub(r"\\frac\s*\{([^{}]*)\}\s*(\d)", r"((\1)/(\2))", s)
        s = re.sub(r"\\sqrt\s*\[([^]]*)\]\s*\{([^{}]*)\}", r"((\2)**(1/(\1)))", s)
        s = re.sub(r"\\sqrt\s*\{([^{}]*)\}", r"sqrt(\1)", s)
        s = re.sub(r"\\sqrt\s*(\d+)", r"sqrt(\1)", s)
    s = s.replace("\\pi", "pi").replace("{", "(").replace("}", ")").replace("^", "**")
    s = re.sub(r"(\d)\s*(pi|sqrt|\()", r"\1*\2", s)
    s = re.sub(r"\)\s*(\(|pi|sqrt|\d)", r")*\1", s)
    try:
        v = sympy.sympify(s, locals={"pi": sympy.pi, "sqrt": sympy.sqrt})
        if exact:
            return v
        return float(sympy.N(v, 30))
    except Exception:
        return None


def same(a, b, a_tex=None, b_tex=None):
    if a is not None and b is not None and math.isfinite(a) and math.isfinite(b):
        return abs(a - b) <= 1e-6 * max(1.0, abs(b))
    if a_tex is None or b_tex is None:  # huge values: compare exactly
        return False
    x, y = to_number(a_tex, exact=True), to_number(b_tex, exact=True)
    try:
        return x is not None and y is not None and sympy.simplify(x - y) == 0
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        bad = []
        for line in open(ROOT / "pool.jsonl"):
            it = json.loads(line)
            if to_number(it["answer"]) is None:
                bad.append((it["id"], it["answer"]))
        print("unparsed references:", bad or "none")
        return
    sel = {i["id"]: i for i in json.loads((ROOT / "selection.json").read_text())["items"]}
    grades = []
    for meta_path in sorted((ROOT / "runs").glob("*/*-meta.json")):
        meta = json.loads(meta_path.read_text())
        it = sel.get(meta["item"])
        if not it:
            continue
        ans = meta_path.with_name(meta_path.name.replace("-meta.json", "-answer.md")).read_text(encoding="utf-8")
        boxed = last_boxed(ans)
        got = to_number(boxed)
        ref = it["original_decimal"] if meta["version"] == "original" else it["variant_decimal"]
        ref_tex = it["original_answer"] if meta["version"] == "original" else it["variant_answer"]
        grades.append({"model": meta_path.parent.name, "item": meta["item"], "source": it["source"],
                       "version": meta["version"], "rep": meta["rep"], "stop_reason": meta["stop_reason"],
                       "truncated": "output token maximum" in ans,
                       "boxed": boxed, "parsed": got, "reference": ref if ref is None or math.isfinite(ref) else str(ref_tex), "correct": same(got, ref, boxed, ref_tex)})
    (ROOT / "grades.json").write_text(json.dumps(grades, indent=1), encoding="utf-8")
    print(f"{len(grades)} graded, {sum(g['boxed'] is None for g in grades)} without boxed, "
          f"{sum(g['boxed'] is not None and g['parsed'] is None for g in grades)} unparsed, "
          f"{sum(g['truncated'] for g in grades)} truncated")


if __name__ == "__main__":
    main()
