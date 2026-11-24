# AnchorAudit-MRV

[![English](https://img.shields.io/badge/Lang-English-blue.svg)](./README.md)
[![Tiếng Việt](https://img.shields.io/badge/Lang-Ti%E1%BA%BFng%20Vi%E1%BB%87t-lightgrey.svg)](./README.vi.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Python](https://img.shields.io/badge/python-%E2%89%A53.10-blue.svg)

**Language:** **English** | [Tiếng Việt](./README.vi.md)

Experimental simulation and verification repository for the study:

> **Limits of Physical Auditing for Irrigation Logs and Conditions for Device Anchoring in Responsible Low-Emission Rice MRV**  
> Xuan Van Mai, Duc Minh Phuong Le\*, Tri Nguyen Dang, Khanh Duy Truong, Tuong Tri Nguyen\*  

## Scope

This repository reproduces all experimental tables and checks for a three-tier audit framework over alternate wetting and drying (AWD) irrigation logs using hourly ERA5 reanalysis meteorology across three Mekong Delta stations (Can Tho, Soc Trang, Ca Mau; 2024–2025):

1. **Tier 1 — Single-Configuration Baseline** ($\theta_0$, fixed gap threshold $\tau_0 = 5$ mm, physical plausibility filters $V_1, V_4, V_5$).
2. **Tier 2 — Robust Uncertainty-Set Detector** ($V_{\mathrm{rob}}(L) = \bigcap_{\theta \in \Theta} V_\theta(L)$ paired with elastic event-scaled tolerance $\tau(N_{\mathrm{event}})$ using $\sigma_{\mathrm{event}} = 7.67$ mm).
3. **Tier 3 — Device-Anchored Reconciliation** (directional multiset differences $\Delta^-, \Delta^+$ and maximum hourly depth deviation $\Delta_{\mathrm{depth}}$ against signed pump-controller records $\mathcal{G}$ as an internal consistency check).

## One-Command Reproduction

Requirements: Python $\ge$ 3.10 (`numpy`, `scipy`, `matplotlib`). No API keys are needed because cached ERA5 inputs and provenance files are included in `data/era5_multi/`.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.lock
bash reproduce_paper.sh
```

Runtime: approximately 1–2 minutes on a standard laptop.

## Paper Tables $\leftrightarrow$ Scripts & Outputs Mapping

| Paper Element | Reproduction Script | Reference Output File |
|---|---|---|
| Table 1 (Model & out-of-$\Theta$ parameters) | `src/log_filters.py`, `experiments/out_of_theta_probe.py` | — |
| Table 2 ($2\times 2$ ablation isolating $\Theta$ and $\tau$) | `experiments/robust_audit_eval.py --seeds 10` | `outputs/eval_theta_reduced_10seeds.csv` |
| Table 3 (False positives on $60$ honest logs) | `experiments/robust_audit_eval.py --seeds 10` | `outputs/eval_theta_reduced_10seeds.csv` |
| Table 4 (Paired $n_{\mathrm{dry}}$ dry-phase gains) | `experiments/robust_audit_eval.py --seeds 10` / `--full-theta --seeds 3` | `outputs/eval_theta_reduced_10seeds.csv`, `outputs/eval_theta_full_3seeds.csv` |
| Table 5 (Sensitivity across $d_{\mathrm{dry}}$ thresholds) | `experiments/sweep_dry_threshold.py` | `outputs/sweep_dry_threshold.csv` |
| Table 6 (Detection rates on $116$ modified logs) | `experiments/robust_audit_eval.py --seeds 10` | `outputs/eval_theta_reduced_10seeds.csv` |
| Out-of-$\Theta$ validation | `experiments/out_of_theta_probe.py`, `experiments/out_of_theta_fraud.py`, `experiments/make_out_of_theta_summary.py` | `outputs/_out_of_theta_summary.json` |

## Key Verified Results

- **False positives ($60$ noisy honest logs):** Single-config ($\tau_0$) flags $16/60$ ($26.7\%$); elastic allowance $\tau(N_{\mathrm{event}})$ alone lowers this to $5/60$ ($8.3\%$); robust intersection over $\Theta_{\mathrm{red}}$ lowers it to $3/60$ ($5.0\%$); device anchoring yields $0/60$ ($0/120$ total across ideal and noisy logs, reflecting internal consistency).
- **Timing-shift attack ($d_{\mathrm{dry}}=0.45$):** Mean dry-phase increase is $+0.61$ phases ($+12.5\%$) across all $23$ targeted logs and $+1.56$ phases ($4.78 \to 6.33$, $+32.6\%$) across $9$ hill-climb-modified logs; the robust detector misses $8/9$ at $d_{\mathrm{dry}}=0.45$ and $22/24$ pooled across $d_{\mathrm{dry}} \in \{0.05, 0.20, 0.45, 0.80, 0.95\}$.
- **Out-of-$\Theta$ validation ($42$ honest, $20$ timing-shift logs):** Honest false positives are $17/42$ ($40.5\%$, single-config), $1/42$ ($2.4\%$, elastic allowance), and $0/42$ ($0.0\%$, robust); timing-shift detection falls to $6/20$, $1/20$, and $0/20$, respectively.
- **Device-anchored reconciliation ($281$ audited logs under $\Theta_{\mathrm{red}}$):** Flags $116/116$ modified logs under any discrepancy ($107/107$ confirmed fraud cases after isolating $9$ omission cases as reconciliation errors) with $0/120$ honest false positives under uncompromised controller records.

## Repository Structure

```text
AnchorAudit-MRV/
├── README.md            # Primary English documentation
├── README.vi.md         # Vietnamese documentation (Bản tiếng Việt)
├── data/                # Cached ERA5 meteorology (Open-Meteo) with provenance
├── src/                 # FAO-56 water balance, filters V1/V4/V5, uncertainty set Θ
├── experiments/         # Evaluation, d_dry sensitivity sweeps, out-of-Θ scripts
├── tests/               # Physical invariant and filter unit tests
├── outputs/             # Reference CSV/JSON tables matched to paper results
├── reproduce_paper.sh   # One-command reproduction workflow
├── requirements.lock    # Pinned dependency versions
└── LICENSE              # MIT License
```

## Funding & Contact

This research was funded by Hue University under grant number **DHH2025-19-07**.

- Corresponding authors: `Ldmphuong@hueuni.edu.vn`; `ntuongtri@hueuni.edu.vn`.
