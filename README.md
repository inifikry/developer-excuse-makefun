[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![make.fun · rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/inifikry/developer-excuse-makefun/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![make.fun · reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/inifikry/developer-excuse-makefun/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

# Make the AI Judge Laugh: Developer Excuses

Entry for the make.fun bounty
`u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`.

## What it does

`main.py` writes one funny single-line excuse a developer gives when code
breaks in production to `/output/entry.txt`. The program is deterministic:
every run writes the exact same line.

## The line

> The bug only happens in production because that's the only place anyone actually uses my code.

94 characters, one line, no trailing newline. The joke turns on a twist a
developer recognises: the bug "only happens in production" not because
production is special, but because production is the only place where
anybody actually runs the code. It sounds like something a developer would
really say out loud, lands in a single sentence, and avoids the worn
excuses ("works on my machine", "it worked yesterday").

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
