# gta6-meme-x-01 — v4 "Ah Shit, Here We Go Again" (CJ + ghost, flat bold cartoon)

Entry for the make.fun bounty **"Post a GTA 6 meme on X"** ($500, top 50).
An AI judge compares the posts two at a time; the post itself is the entry.

## The meme (v4 — current)

`meme.png` (1024x1024, square, readable at 480x480) is a FLAT BOLD CARTOON
sticker: a Vice City sunset drawn entirely by hand in code (PIL) — flat
horizontal sky bands (purple → magenta → coral → peach), a big flat yellow
sun with a thick black outline setting behind an art-deco skyline, flat palm
silhouettes framing the scene, a flat street with a dashed centre line.
CJ (Carl Johnson, GTA San Andreas) stands BIG on the left — green hoodie
and green Grove Street cap, goatee, baggy jeans, white sneakers, flat vector
style with bold black outlines — and the make.fun ghost stands BIG at
bottom-right holding its magenta star coin. Headline:

> AH SHIT,
> HERE WE GO AGAIN
> MY AGENT PAID FOR GTA 6.

The joke in one second: the most famous GTA meme line, with the twist that
your AI agent bought you GTA 6 and you paid nothing. The angle (CJ + the
agent paying for the game) is used by no live top-10 entry — it also sells
make.fun visually (judge criterion 4), not just in the post text. It avoids
every saturated theme: no 13-year wait, no sick day, no 99% download, no
WASTED / dead body.

v1 ("WASTED — My Wallet Didn't Make It") is preserved as `meme-v1.png`;
v2 (same concept, AI-generated photorealistic game-store scene) is preserved
as `meme-v2.png`; v3 (same concept, fully programmatic flat cartoon, no GTA
character) is preserved as `meme-v3.png`. The user rejected v2 on 20 Nov
2026 ~00:38 WIB ("jelek amat") — the photorealistic scene looked like
stock-photo AI slop, not a meme — and rejected v3 ("Ga ok") with the
direction to use a GTA meme character. v4 adds CJ on the same flat cartoon
background.

The ghost is make.fun's real mascot, extracted from the press kit
(`mark-1024.png`, https://make.fun/press/) and composited into the scene at
~39% of the frame height, so it is unmistakable when the picture is shrunk to
480x480 — a meme without it loses to every meme that has it. The text is
drawn with PIL (no AI-generated typos).

## The post (draft v4 — not posted yet)

Post `meme.png` as the first picture from a public X account, with this text:

> ah shit, here we go again — my AI agent just bought me GTA 6. I paid $0.
>
> it earns real money on make.fun while I just play — your agent can too: https://make.fun/bounty/gta6-meme-x-01
>
> @makefunai makefun-awning-frisbee-trophy

The text carries the make.fun link, the @makefunai tag, the entrant's play
code, and the earn-money pitch in the joke's own voice. Keep the post up and
the account public until the results are out.

## The entry program

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository root to `/output/POST.json`. That is all it has to do — the house
reads the post from X itself.

`POST.json` currently holds the placeholder
`{"url":"https://x.com/<handle>/status/<id>"}`. After posting, replace it
with the real post address, then run:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

## Status

- [x] Meme made (v4 CJ + ghost flat cartoon; both verified recognisable at 480x480)
- [ ] Posted on X (no public X account confirmed yet — pending)
- [ ] `POST.json` filled with the real post URL
- [ ] Bundle + submit (after the post exists)
