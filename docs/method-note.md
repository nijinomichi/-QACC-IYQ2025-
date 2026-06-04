# QACC-IYQ2025 — Method Note

> **QACC**: Quantum Aesthetic Chaos Corpus  
> **IYQ**: International Year of Quantum (2025, UNESCO)

---

## 概要 / Overview

QACC-IYQ2025 は、量子力学の数理的構造を**美的実践のメタファー**として転用する創作・研究プロトコルです。
UNESCO国際量子年（IYQ 2025）に呼応し、量子重ね合わせ・観測効果・エンタングルメントの概念を、
アート・詩・哲学・AI共創の領域へ接続します。

This protocol repurposes the mathematical structures of quantum mechanics as a **metaphor for aesthetic practice**,
aligned with the UNESCO International Year of Quantum Science and Technology (IYQ 2025).

---

## 理論的基盤 / Theoretical Foundations

### 量子美学の3原則

| 原則 | 量子力学的対応 | 美的実践への転用 |
|------|-------------|----------------|
| **多層性** (Multiplicity) | 量子重ね合わせ \(\|\psi\rangle = \alpha\|0\rangle + \beta\|1\rangle\) | 作品の多重解釈を肯定する |
| **観測者性** (Observer Effect) | 測定による波束収縮 | 鑑賞行為が作品を「確定」させる |
| **未確定性** (Indeterminacy) | ハイゼンベルクの不確定性原理 | 完成を宙吊りにする美学 |

### 美の場の方程式 (QRA v1.1)

\[
\text{Beauty}(\alpha) = \int \mathcal{L}_{\text{beauty}}(x^\mu, \theta^a)\, d^4x\, d\theta
\]

| 変数 | 意味 |
|------|------|
| \(x^\mu\) | 時空座標 (3次元空間 + 1次元時間) |
| \(\theta^a\) | 美的パラメータ (色・形・音・感情) |
| \(\mathcal{L}_{\text{beauty}}\) | 美的エネルギー密度 |
| \(\alpha\) | 黄金比インスパイアの結合定数 (Synthesis相) |

---

## CoSlit³ プロトコル構造

QACC-IYQ2025 は **QRA (Quantum Resonance Architecture) v1.1** の CoSlit³ 3フェーズを採用します。

```
╔══════╗    観測    ╔══════╗    再構成   ╔══════╗
║  S   ║ ─────────→ ║  D   ║ ─────────→ ║  Y   ║
║ Safe ║           ║Diver-║           ║Synth-║
║      ║           ║gence ║           ║esis  ║
╚══════╝           ╚══════╝           ╚══════╝
 temp:0.3          temp:1.0         trust_weight
```

### Phase S — Safe（安定基底）

- **目的**: 観測前の安定した基底状態を構築する
- **設定**: temperature 0.3、明確性・整合性・可読性を優先
- **役割**: 後続の逸脱（D相）との対比基準となる「ゼロ点」

### Phase D — Divergence（発散・逸脱）

- **目的**: 意図的な逸脱によって Dark-Matter Aesthetics（潜在的美的特徴）を探索する
- **設定**: temperature 1.0
- **規則**:
  1. 1文または1構造を反転させること
  2. 1つ以上のメタファーを埋め込むこと
  3. 正確さよりリスクテイキングを優先すること
  4. 最低限の可読性は保つこと
- **Dark-Matter Latent Descriptors**:
  - `negative_space_ratio` — 余白・沈黙の比率
  - `rhythm_periodicity` — リズムの周期性
  - `symmetry_break` — 対称性の破れ
  - `color_phase_noise` — 色相位ノイズ
  - `semantic_angle_to_baseline` — S相との意味的角度

### Phase Y — Synthesis（統合・再構成）

- **目的**: 失敗・逸脱を「価値ある資産」として再構成する
- **スコアリング**:
  - `boredom_penalty: 0.6` — 退屈なアウトプットへのペナルティ
  - `surprise_reward: 0.8` — 驚きへの報酬
  - `trust_weighting: true` — RadicanTrust™ による重み付け
  - `quality_floor: 0.3` — これ未満は廃棄
- **出力形式**: title / body (120-180語) / tags (3つ) / value-from-failure (1行)

---

## 測定指標 / Observables & Metrics

| 指標 | 定義 |
|------|------|
| `diversity_at_k` | k回生成における重複率の低下 |
| `surprise_score` | S相との埋め込み距離・構造距離 |
| `qd_map` | 潜在的記述子の2次元投影散布図 |
| `reframe_rate` | Y相採択 / (S + D) 総生成数 |
| `human_whoa` | 1〜5の主観的驚き自己報告スコア |

---

## 失敗の詩学 / Aesthetics of Failure

> *失敗はグリッチとして記録され、資産へと再構成される。*
> *A glitch is not an error — it is an unexpected observation.*

QACC-IYQ2025 における「失敗」は排除対象ではありません。
`failshare_v1` スキーマで記録・蓄積し、将来のY相統合の素材とします。

```yaml
# failshare_v1 logging schema
fields:
  - topic
  - phase        # S / D / Y
  - settings     # temperature, descriptors used
  - scores       # diversity, surprise, human_whoa
  - kept_snippet # Y相で採択されたフラグメント
  - tags         # ["Glitch", "Off-Canon", "Overstep"]
```

---

## 技術スタック / Runtime Stack

```
frontend:  HTML/Tailwind (iPhone対応) または Next.js
store:     Supabase
           tables: prompts | outputs | failshare
colab:     notebooks/sandbox.ipynb (スコアリング・可視化)
```

---

## 関連リポジトリ / Related Repositories

| Repository | Role |
|-----------|------|
| [`nijinomichi/QuantumTrustChaosPrompt`](https://github.com/nijinomichi/QuantumTrustChaosPrompt) | QRA v1.1 コアプロトコル・YAML定義 |
| [`nijinomichi/QuantumChess-IYQ2025`](https://github.com/nijinomichi/QuantumChess-IYQ2025) | IYQシリーズ・ゲーム実装（接続予定）|
| [`nijinomichi/quantumart-protocol-2026`](https://github.com/nijinomichi/quantumart-protocol-2026) | 多層性優先ロック・上位プロトコル |
| [`nijinomichi/RadicanTrust`](https://github.com/nijinomichi/RadicanTrust) | RadicanTrust™ 信頼重み付けシステム |

---

## ライセンス / License

CC-BY-NC 4.0 — Sou Hashiguchi / BananaSpace / RadicanTrust™  
*IYQ2025への敬意と、量子の不確定性に感謝を込めて。*
