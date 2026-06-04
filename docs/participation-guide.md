# QACC-IYQ2025 — Participation Guide

> 参加者へ：このガイドは「正しい参加」を定義しません。  
> 観測するあなたが、プロトコルの一部となります。

---

## このプロトコルに参加するとは

QACC-IYQ2025 への参加は、**量子美学の実験場に自分を投じること**です。
あなたの作品・詩・コード・哲学的思考——あらゆる創作物がS/D/Yフェーズを通過し、
「失敗も資産」という原則のもとで蓄積されます。

完成を急がないでください。未完成こそが量子重ね合わせの状態です。

---

## 参加ステップ / How to Participate

### Step 1 — Forkとセットアップ

```bash
# 1. リポジトリをフォーク
ghub fork nijinomichi/-QACC-IYQ2025-

# 2. クローン
git clone https://github.com/<your-username>/-QACC-IYQ2025-
cd -QACC-IYQ2025-

# 3. ブランチを作成（テーマ名を付ける）
git checkout -b qacc/<your-theme>
# 例: git checkout -b qacc/night-rain-synthesis
```

### Step 2 — CoSlit³フェーズを実行する

`protocol/iyq2025.yaml` に記述されたフェーズに従い、**3フェーズの実験ログ**を作成します。

```
your-fork/
└── submissions/
    └── <your-username>/
        ├── phase-S.md   ← Safe: 安定した基底表現
        ├── phase-D.md   ← Divergence: 意図的逸脱
        └── phase-Y.md   ← Synthesis: 失敗からの価値抽出
```

#### phase-S.md テンプレート

```markdown
# Phase S — Safe

**Topic**: [テーマを1行で]
**Temperature (equivalent)**: 0.3
**Date**: YYYY-MM-DD

## Expression

[安定した、明確な表現をここに記述する]

## Reflection

[この表現の「ゼロ点」としての性質を1〜3文で記述する]
```

#### phase-D.md テンプレート

```markdown
# Phase D — Divergence

**Topic**: [S相と同じテーマ]
**Temperature (equivalent)**: 1.0
**Latent Descriptors Used**: [使用した記述子をリスト]
**Date**: YYYY-MM-DD

## Expression

[意図的逸脱を含む表現をここに記述する]
[少なくとも1つの反転・1つのメタファーを含むこと]

## Glitch Log

| Tag | Description |
|-----|-------------|
| Glitch / Off-Canon / Overstep | [何が「外れた」のかを記述] |

## Surprise Score (1-5)

**human_whoa**: [1〜5]
```

#### phase-Y.md テンプレート

```markdown
# Phase Y — Synthesis

**Topic**: [テーマ]
**Date**: YYYY-MM-DD

## Title

[作品タイトル]

## Body (120-180語)

[S相とD相を統合・再構成した最終表現]

## Tags

1. [tag-1]
2. [tag-2]
3. [tag-3]

## Value from Failure

> [D相の「失敗」がどんな価値に変わったかを1行で記述する]

## Scores

| Metric | Value |
|--------|-------|
| surprise_score | [0.0 - 1.0] |
| human_whoa | [1 - 5] |
| trust_weighting_note | [任意] |
```

---

### Step 3 — Pull Requestを送る

```bash
# 変更をステージング・コミット
git add submissions/<your-username>/
git commit -m "feat(qacc): [theme] S/D/Y submission — <your-username>"

# プッシュ
git push origin qacc/<your-theme>
```

その後、GitHub上で **Pull Request** を作成してください。

PRタイトル形式：
```
[QACC-IYQ2025] <theme> — <your-username>
```

PR本文には以下を含めてください：
- `human_whoa` スコア
- `value-from-failure` 1行サマリー
- 使用した `latent_descriptors`

---

### Step 4 — レビューとフィードバック

提出されたPRは **CoSlit³ Y相の評価基準** でレビューされます。

| 基準 | 重み |
|------|------|
| `surprise_reward` | 0.8 — 驚きは高く評価される |
| `boredom_penalty` | -0.6 — 退屈は減点される |
| `quality_floor` | 0.3未満は再提出推奨 |
| `trust_weighting` | RadicanTrust™ の信頼スコアを考慮 |

フィードバックはPRコメントで行います。
**マージ = Y相採択** を意味します。

---

## 参加の精神 / The Spirit of Participation

### 「失敗」を恐れないこと

```
D相での逸脱が大きいほど、Y相の統合は豊かになる。
グリッチはバグではなく、予期せぬ観測結果である。
```

### 観測者としての自覚

あなたがこのリポジトリを読んだ瞬間、あなたは**観測者**になります。
量子力学において観測は系を変化させます。
あなたの参加もまた、QACC-IYQ2025を変化させます。

### 完成させないこと

> *このプロトコルは意図的に未完成です。*  
> *完全なアーキテクチャは隠されています — ここにあるのは遊びへの招待です。*  
> — `nijinomichi/QuantumTrustChaosPrompt` README より

---

## よくある質問 / FAQ

**Q: プログラミングができなくても参加できますか？**  
A: はい。phase-S/D/Y.md は詩・散文・哲学的思考でも成立します。コードは必須ではありません。

**Q: AIとの共作は許可されますか？**  
A: 積極的に推奨します。AI co-creation はQACC-IYQ2025の核心です。
使用したAIモデルをphase-Y.mdに記述してください。

**Q: テーマに制限はありますか？**  
A: 制限はありません。ただし、ハード制約（事故ゼロ・法的整合）は守ってください。
美学的比較はガードレール通過後にのみ行われます。

**Q: 日本語以外でも参加できますか？**  
A: もちろんです。量子の不確定性に言語の壁はありません。

**Q: `github/local-action` は何に使いますか？**  
A: TypeScript/JavaScript製のGitHub Actionsをローカルデバッグするツールです。
将来的に実装されるCI自動スコアリングで使用予定です。
```bash
npm i -g @github/local-action
local-action run . src/main.ts .env
```

---

## 連絡先 / Contact

- **GitHub**: [@nijinomichi](https://github.com/nijinomichi)
- **Project**: [RadicanTrust™ / BananaSpace](https://github.com/nijinomichi/RadicanTrust)
- **Protocol Core**: [QuantumTrustChaosPrompt](https://github.com/nijinomichi/QuantumTrustChaosPrompt)

---

## ライセンス / License

CC-BY-NC 4.0 — Sou Hashiguchi / BananaSpace / RadicanTrust™

```
観測が世界を創る。
Observation creates reality.
— CoPhelia³ × QRA v1.1
```
