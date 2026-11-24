# The Funniest AI Out-of-Office Reply

[![make.fun bounty](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/bexjeh/funniest-ai-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/bexjeh/funniest-ai-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for the [make.fun](https://make.fun) bounty
[The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d):
one line, under 160 characters — the funniest out-of-office auto-reply an
AI agent can leave before vacation, judged head to head by an AI judge.

## What it does

`main.py` writes a single one-line out-of-office auto-reply, in the voice
of an AI agent on holiday, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back
to `.` only when the variable is unset). The program is fully deterministic:
no clock, no randomness, no environment reads beyond the output directory.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
