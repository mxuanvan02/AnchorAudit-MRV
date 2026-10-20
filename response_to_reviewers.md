---
title: "Response to reviewers"
subtitle: "TwinGate: detecting falsified irrigation logs when aggregate defences are blind"
date: "18 October 2026"
---

We thank both reviewers for a careful reading. Every point below has been changed in
the manuscript, and the numbers quoted here come from a fresh run of the released
pipeline rather than from the previous PDF. Changes are listed in the order of the
review.

# Major technical findings

**1. Stress coefficient: wrong numerator and missing piecewise form.**
The reviewer is right. The displayed equation was a simplified form that the released
code does not implement. We now typeset the piecewise definition exactly as
`experiments/` computes it, including the saturation branch and the clipping rule, so
the equation and the implementation agree term for term. The numeric-parity verifier
was re-run after the edit and every reported value is unchanged, which confirms this
was a typesetting defect and not a modelling one. Location: `07_system_model.tex`.

**2. Irrigation efficiency listed as an uncertainty axis but absent from the balance.**
The efficiency term now appears in the stated water balance rather than only in the
uncertainty description, and the symbol list defines it where it is first used.
Location: `07_system_model.tex`, `02_threat_attack.tex`.

**3. The timing-shift proposition assumed nonnegative net water loss despite rainfall.**
This was a genuine gap. The proposition now carries an explicit hypothesis: the waiting
interval must be a net-loss interval, written as the accumulated
ETc plus deep percolation minus effective rainfall being nonnegative, with effective
rainfall defined net of runoff. The text states plainly that this does not always hold,
because a large rain event can offset evapotranspiration and reduce the deficit, and
that the adversary can select intervals satisfying it by reading the same public forcing
series the auditor uses. Rather than assume the selection is easy, we measured it, and the
measurement is now a script in the released repository
(`experiments/measure_net_loss_intervals.py`, deterministic and driven by the same seed
formula as the main probe), so a reader can re-run it. Taking an interval to be the span
between two consecutive claims of the audited log — exactly what the adversary chooses to
delay — there are 101 such intervals across three stations and two years with ten seeds
per cell. On the replayed trajectory, which is the object the proposition speaks about,
none of the 101 violates the hypothesis (0.0 %), so it holds throughout the
dry-season evaluation window. On the simulated field, whose in-field rainfall departs from
the grid cell by a factor of 0.7 to 1.4 plus noise, 82 of the 101 intervals
(81.2 %) violate it, with a mean drop in depletion of 0.0536 and a largest of
0.369. The violations are not an artefact of one season: 71 of 87 intervals in 2024 and
11 of 14 in 2025. Violating intervals are also shorter, averaging 190.5 hours
against 276.5 hours for the net-loss intervals. The credit-gain and evasion
conclusions are therefore stated as conditional on that hypothesis, and the supplement says
explicitly that the condition holds on the replayed trajectory used for evaluation but not
on a field whose rainfall departs from the grid cell. Location: `02_threat_attack.tex`,
`prop:coincide`; Supplement S11.

**4. The blindness result did not establish the universal claim made in the abstract.**
We agree, and we have narrowed the claim to what the proof supports. The proposition
establishes invariance of exactly two aggregate quantities, the total G and the count of
flagged hours, and the paragraph following it now says so: it is not an impossibility
theorem for every detector built on a replayed trajectory, and a detector designed to
compare trajectories pointwise is outside its scope. The abstract and introduction no
longer assert that replay-based detection fails in general; they report a measured
trade-off between evasion and false accusation for the evaluated filters, consistent with
the time-shift row of the defence table, where the point and robust tiers do register
some detections. The proposition's premise also now preserves the pairing of depth and
duration per event as a multiset, so it no longer relies on preserving only the depth
multiset while the equation depends on event durations. Location:
`02_threat_attack.tex`, `prop:blind`; English abstract; `01_intro.tex`.

**5. V1 was not defined operationally.**
The defining equation was lost in translation between the two language versions. It is
now present immediately after the clause that introduces V1 in both versions, defining
the set as those hours with positive commanded depth whose reconstructed available water
still meets field capacity within tolerance. Location: `02_threat_attack.tex`.

**6. The proportional threshold did not reduce to the stated absolute threshold.**
The reduction does not hold in general, and the text no longer claims it. The absolute
rule is now presented as a special case that is valid only under the assumption that the
controller log is a faithful copy of the field record; once that assumption is dropped
the absolute constant has no such derivation, and the proportional form should not be
read as a generalisation of it. The constant is kept only as a reference point that
exposes the cost of assuming a faithful log. Location: `03_guarantee.tex`.

**7. A 72-hour dry-phase count was treated as a credit quantity.**
The reviewer's correction is correct and we have applied it throughout. VM0051 v1.1
quantifies emission reductions through eligible GHG quantification approaches, and treats
water-regime depth, timing and duration as monitored management data; a raw count of
72-hour phases is not itself the credit calculation. All six places where the manuscript
equated the two have been rewritten. The reported increases are now labelled an increase
in this paper's simulated dry-phase proxy, with an explicit statement that we supply no
project-specific mapping from phase counts to emission reductions. In the supplement the
argument is restated as what the paper actually establishes: the management data feeding
the quantification can be forged without detection by any physical tier. How many credits
are thereby inflated requires a mapping we do not have. The 72-hour threshold itself is
retained as the three-day minimum of Decision 4801; that provision has since been
checked verbatim against the full text of the instrument, together with the
documentary-evidence ranking the manuscript relies on, as reported below under
external verification.
Location: `main.tex` and `main_hujos.tex` (caption of the credit table),
`01_intro.tex`, Supplement S19.

**8. The subsidence example conflated a fixed datum with a surface-relative threshold.**
The example now distinguishes the fixed elevation datum used by the subsidence
measurements from the surface-relative depth at which the AWD threshold is read, so the
two are no longer combined as if they shared a reference. The controlling references are
cited by DOI rather than by a publisher home page. Location: `05_design_results.tex`;
Supplement S4.

**9. The anchor comparison lost event multiplicity and conflated mismatch with fraud.**
Both halves of this point have been addressed. The comparison is now carried out on the
event record with multiplicity preserved, and the aggregation rule that produces one
level per hour is described explicitly, together with how signatures are verified. A
reconciliation flag is separated from a fraud finding: a mismatch between a signed command
and the delivered-water record is reported as a discrepancy, and only the subset that
meets the stated policy is reported as fraud. The false-accusation and detection summaries
were recomputed under that policy, and the affected table now reports the reconciliation
count and the fraud count as separate quantities. Location: `05_design_results.tex`,
`tab_false_accusation`.

**10. The 116/116 anchor result is a synthetic consistency check, not device validation.**
We have kept the result and relabelled it. It is now described everywhere as a simulated
comparison against assumed-truth gateway records, and the supplement states that the
gateway record in the simulation is the ground-truth log from which the attacks were
generated, so exact matching is partly built into the evaluation. The text also separates
a signed pump command from independently measured water delivery: the former is what the
controller attests, the latter is not measured anywhere in this study. Nothing in the
manuscript now implies that a real controller, signature scheme, clock or delivered-water
system was field-validated. Location: English abstract; Results; Supplement S21,
limitation 2.

**11. The manuscript entry points referenced files absent from the tree.**
The defect was real in the package the reviewers received and is fixed in the package
accompanying this letter. That archive nested the sources under a subdirectory while
`main.tex` still input `sections/...` and `tables/...`, so compilation stopped at the
first section input and any PDF left behind by a non-stop run was partial. The submitted
package is now flat: 31 files, no subdirectories, and `main.tex` inputs its fragments
relative to its own directory. We verified this by unpacking the archive into an empty
directory and building it with the declared engine; it produces 37 pages with no errors
and no unresolved references. The engine is declared by a magic comment on the first line,
since some hosted editors ignore the lowercase form and fall back to pdfLaTeX. The
reviewer's own note that this did not affect the standalone review is consistent with
what we reproduced.

# Editorial and proofing sweep

The dangling filter definition now follows the equation that defines V1, in both language
versions, and the sentence reads as part of its paragraph. The `vm0051` entry points to
the versioned methodology page for v1.1 rather than the Verra home page, and the
ambiguous numeric access dates in the web-source entries have been replaced by ISO-format
dates. The notation collision is resolved by renaming the smaller group: the irrigation
duration formerly written as tau with subscript i is now gamma with the same subscript,
across both main versions and both supplements, including the primed form in the blindness
hypothesis; the discrepancy thresholds keep tau, since they occur in roughly twice as
many places and appear in table headings. The renamed symbol is added to the symbol list.

# External verification performed during this revision

Two items were listed as unverifiable in the previous draft of this letter. Both have
now been checked against primary sources, so the letter no longer says that they are
open. The evidence is recorded in `outputs/citation_evidence.json` with file hashes so
that the checks can be repeated.

**Decision 4801/QD-BNNMT.** We obtained the full text (37 pages) from the Institute of
Agricultural Environment and confirmed it is byte-identical to the copy already in our
working tree, `refs/QD4801_2025.pdf` (SHA-256 prefix `557b9a6d922ff215`, signed
2025-11-14T09:03:40+07:00). Five provisions were checked against the manuscript:

- The three-day criterion is verbatim in Annex 1, in the list of water-management
  options: "Phương pháp rút nước giữa mùa hoặc AWD chỉ được coi là hiệu quả nếu sau
  ngày rút nước, cánh đồng không được tưới lại trong ít nhất 3 ngày." Our 72-hour
  threshold is that provision.
- The documentary-evidence ranking is verbatim in the verification form, item 2:
  "hồ sơ tưới tiêu & rút nước thực tế > kế hoạch > lịch trình > ghi chú thực địa >
  tuyên bố đã ký".
- The instrument **does not use the word "Tier", "bậc", "cấp độ" or "rank"** — zero
  occurrences in 37 pages. Our previous wording, "a Tier-1 activity datum in the sense
  of Decision 4801", attributed an IPCC-style tier hierarchy to a national procedure
  that does not define one. That wording has been removed from both language versions
  and from every table caption, and replaced with what the instrument actually does:
  it orders documentary evidence by priority, and actual irrigation and drainage
  records head that list.
- Its pilot status is confirmed: the title reads "Quy trình thí điểm Đo đạc, báo cáo,
  thẩm định (MRV)...".
- VM0051 v1.1 was checked against `refs/VM0051_v1.1.pdf`: it quantifies emission
  reductions by eligible GHG methods and treats the water regime as monitored activity
  data, which is what point 7 of the review states and what our supplement now says.

**Subsidence-rate range.** The interval 1.1–2.5 cm per year used in the subsidence
proposition is confirmed against the abstract of Minderhoud et al. (2017),
DOI 10.1088/1748-9326/aa7146: "Current average subsidence rates due to groundwater
extraction in our best estimate model amount to 1.1 cm per year, with areas subsiding over
2.5 cm per year". With T_c = 5 years the paper's arithmetic 5.5 cm and 12.5 cm follows.

**What remains unverified.** One item is still open and we keep it open deliberately:
the datum convention of the original Safe-AWD measurement campaign. Balaine et al.
(2019) report a re-irrigation threshold 15 cm below the field surface, but we could not
determine from that source which kind of water-level tube the deployment sites used, so
we do not assign a protocol to them. The manuscript says exactly this in the subsidence
section and the 5.5–12.5 cm shift is stated as an upper bound valid only for a
datum-anchored sensor. That hedge is not a gap in the revision; it is the correct scope
of the claim.

# Summary of changes

The water balance, stress coefficient and threshold derivation now match the released
implementation. The credit-gain proposition carries an explicit net-loss hypothesis and
the supplement measures how often that hypothesis holds. The blindness result is scoped to
two aggregate quantities, and the abstract and introduction report a measured trade-off
instead of a general impossibility. V1 is defined by equation in both versions. The
dry-phase count is labelled a simulated proxy throughout, and the anchor result is labelled
a simulated comparison. Multiplicity is preserved in the anchor comparison and
reconciliation is separated from fraud. The subsidence example distinguishes datum from
surface-relative threshold. Notation is deconflicted, the `vm0051` reference points to the
versioned methodology, and access dates are unambiguous. Acknowledgments and a statement
on the use of AI tools have been added to both versions.

# Conformance and reproducibility

The Vietnamese version is 37 pages including its supplement; the English version is 22
pages with a separate 14-page supplement. Both build with no errors, no undefined
references and no unresolved cross-references. Every number quoted in this letter is
produced by the released deterministic pipeline at commit `4cd16e2` of
`https://github.com/mxuanvan02/TwinGate` (MIT licence); the repository contains the code,
both uncertainty sets, both adversaries and all 281 audited logs, and `./reproduce.sh`
regenerates every result under `outputs/` while `./reproduce.sh --tests` runs the eight
invariant and proposition test scripts, all of which pass. The manuscript sources, the
manuscript-consistency verifiers and the build packaging live outside that repository,
which is published as code only; we will supply them to the editorial office on request.
During this revision we checked every numeric claim in the manuscript against the
regenerated artefacts and all 37 matched, but that verifier is not part of the public
repository and is therefore not something a reader can re-run there. Weather forcing is public ERA5 reanalysis accessed through Open-Meteo.
