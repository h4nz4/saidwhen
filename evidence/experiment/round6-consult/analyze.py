"""Round-6 analysis: per-session token economy + exact Mann-Whitney U.

Usage: python analyze.py
Reads c*.events.jsonl from both arms' worktrees, prints the per-session
table, per-prompt and pooled stats, and the pre-registered one-sided
Mann-Whitney test (treatment < control) on the billable proxy
(uncached input + output tokens). Stdlib only.
"""
import json
import glob
import os
import statistics
from functools import lru_cache

WORKTREES = {
    'control': r'E:\PROJEKTI\saidwhen-r5-control',
    'treatment': r'E:\PROJEKTI\saidwhen-r5-treatment',
}


def sessions(arm):
    base = os.path.join(WORKTREES[arm], 'evidence', 'experiment', 'round6-consult', 'runs')
    out = []
    for f in sorted(glob.glob(os.path.join(base, f'{arm}-*', 'c*.events.jsonl'))):
        run = os.path.basename(os.path.dirname(f))
        prompt = os.path.basename(f).split('.')[0]
        inp = cached = outp = 0
        for line in open(f, encoding='utf-8-sig'):
            try:
                ev = json.loads(line.strip())
            except (json.JSONDecodeError, ValueError):
                continue
            if ev.get('type') == 'turn.completed':
                u = ev.get('usage', {})
                inp += u.get('input_tokens', 0)
                cached += u.get('cached_input_tokens', 0)
                outp += u.get('output_tokens', 0)
        out.append({'run': run, 'prompt': prompt, 'input': inp, 'cached': cached,
                    'output': outp, 'billable': (inp - cached) + outp})
    return out


@lru_cache(maxsize=None)
def _count(m, n, u):
    # number of arrangements of m treatment / n control obs with U statistic <= u
    if u < 0:
        return 0
    if m == 0 or n == 0:
        return 1
    return _count(m - 1, n, u - n) + _count(m, n - 1, u)


def mann_whitney_exact_p(treat, ctrl):
    """One-sided exact p for H1: treatment < control.

    U counts (t < c) pairs, so LARGE U supports H1; the p-value is the
    upper tail P(U >= u), computed via the symmetric lower tail
    P(U <= m*n - u). (Bug fix 2026-07-08, disclosed in results.md: the
    originally registered implementation used the lower tail of the same
    statistic, i.e. the wrong direction for the registered hypothesis.)"""
    u = sum(1 for t in treat for c in ctrl if t < c) + 0.5 * sum(
        1 for t in treat for c in ctrl if t == c)
    m, n = len(treat), len(ctrl)
    from math import comb, floor
    total = comb(m + n, m)
    return u, _count(m, n, floor(m * n - u)) / total


def fmt(v):
    return f'{v:,.0f}'


def main():
    data = {arm: sessions(arm) for arm in WORKTREES}
    for arm in data:
        print(f'\n== {arm} ({len(data[arm])} sessions)')
        for s in data[arm]:
            print(f"  {s['run']:14} {s['prompt']}  in={fmt(s['input']):>12} "
                  f"cached={fmt(s['cached']):>12} out={fmt(s['output']):>9} "
                  f"billable={fmt(s['billable']):>9}")
    print('\n== per-prompt billable means (treatment vs control)')
    for p in ('c1', 'c2', 'c3'):
        t = [s['billable'] for s in data['treatment'] if s['prompt'] == p]
        c = [s['billable'] for s in data['control'] if s['prompt'] == p]
        if t and c:
            dm = 100 * (statistics.mean(t) - statistics.mean(c)) / statistics.mean(c)
            print(f'  {p}: treatment {fmt(statistics.mean(t))} vs control {fmt(statistics.mean(c))} ({dm:+.0f}%)')
    t = [s['billable'] for s in data['treatment']]
    c = [s['billable'] for s in data['control']]
    if t and c:
        print('\n== pooled billable proxy (uncached input + output)')
        print(f'  treatment: mean {fmt(statistics.mean(t))}  median {fmt(statistics.median(t))}')
        print(f'  control:   mean {fmt(statistics.mean(c))}  median {fmt(statistics.median(c))}')
        u, p = mann_whitney_exact_p(t, c)
        print(f'  Mann-Whitney U = {u}, one-sided exact p (treatment < control) = {p:.5f}')
        holds = (statistics.mean(t) < statistics.mean(c)
                 and statistics.median(t) < statistics.median(c) and p < 0.05)
        print(f'  pre-registered economy claim: {"HOLDS" if holds else "does NOT hold"}')


if __name__ == '__main__':
    main()
