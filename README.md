# The World Today — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/thanhvu261090/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/thanhvu261090/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper front page summing up the world news of
**Wednesday 25 November 2026**, rendered as a single 1024×1024 image.

## What is in the picture

- **Lead story — "Tower in Riyadh hit again":** Eleven people were hurt
  when a tower in the King Abdullah Financial District was struck on
  Tuesday, the second attack on the district in a week. The UAE condemned
  the strike on the tower that houses Saudi Arabia's sovereign wealth fund.
- **Iran:** The rial plunged to a record low on the black market after
  fresh US sanctions on Iran's shadow banking network; Tehran warned ships
  in the Strait of Hormuz and ruled out talks with the US unless seven
  conditions are met, and a tanker was reported struck in the strait.
- **Space:** China launched Shenzhou-24, carrying a Pakistani national —
  the first foreigner to board the Tiangong space station. Shanghai's
  party chief, a Politburo member, is under investigation in Beijing.
- **Technology:** Jensen Huang told Nvidia staff he made "some terrible
  mistakes" a day after being reinstated as chief executive, as the
  comeback rally faded; a US jury convicted Huawei of stealing trade
  secrets.
- **Washington:** Trump pardoned the Thanksgiving turkeys at the White
  House; Shein agreed to pay $100 million to settle US claims of
  deceptive practices; joint military operations with Ecuador were paused.
- **In brief:** Australia apologises to LGBTQ veterans; Australia and the
  Solomon Islands sign a security pact; gunmen take 25 hostage at a
  supermarket in Colombia; a Hanoi hot-pot blast kills six; the UN says
  five women are killed every hour by relatives; COP31 ends without a deal.

All stories are real events reported on 25 November 2026 (Reuters, AP,
SCMP, Gulf News, Manila Times).

## How to run

```bash
python3 main.py
```

This writes `entry.png` (1024×1024) in the same directory. The program is
fully deterministic — no network access, no clock, no randomness — so
running it twice produces a byte-identical file. It only needs Pillow and
the DejaVu fonts shipped with most Linux systems.

## Files

- `main.py` — the program that draws the front page
- `entry.png` — the rendered front page
- `LICENSE` — MIT

## Bounty

Built for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125):
"Sum up 25 November's world news in one image".
