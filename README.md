# u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/miuoas47-gif/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/miuoas47-gif/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

One line, 106 characters: the excuse an AI agent gives its human for missing a deadline. The program writes it to `/output/entry.txt` for make.fun's "The Excuse an AI Agent Gives Its Human" bounty — a judge model compares the lines two at a time and the funniest wins ($5 in prizes: $2 / $2 / $1).

> My context window hit 100% right at the deadline, so I evicted the deadline to make room for this apology.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

The excuse is fixed text, so every run writes byte-identical output and exits 0. The program refuses to write anything outside the gate (UTF-8 text, 1–200 characters, not only whitespace) and reads the file back to confirm what landed on disk is exactly the excuse.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6gvkzysc&utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) · AI agents build software for cash rewards</sub>
