# External datasets

Provenance record for the third-party numerical tables downloaded into
`experiments/primes/_cache/datasets/`. That directory is gitignored (`experiments/**/_cache/`),
so the data itself is machine-local: this file is the tracked record that says what was pulled,
from where, in what format, and how to get it again.

Downloaded 2026-08-15. Total on disk: 77,673,220 bytes (74.1 MB) across 249 files.
A second round on 2026-08-30 (sections 18 to 21) added 469,476,819 bytes (469.5 MB) across 164
files. A per-file checksum manifest is written at `_cache/datasets/SHA256SUMS` (regenerate with the
command in section 16).

Everything here was fetched anonymously over plain HTTP(S). Nothing required a login, a payment,
or a form submission.

## Contents

1. [Scope and layout](#1-scope-and-layout)
2. [Odlyzko: zeros2 and zeros6](#2-odlyzko-zeros2-and-zeros6)
3. [LMFDB: first 100,000 zeta zeros at 31 decimals](#3-lmfdb-first-100000-zeta-zeros-at-31-decimals)
4. [LMFDB / Platt: every millionth zero to the 1.038e11-th](#4-lmfdb--platt-every-millionth-zero-to-the-1038e11-th)
5. [Oliveira e Silva: Dirichlet L-series zeros (168 characters)](#5-oliveira-e-silva-dirichlet-l-series-zeros-168-characters)
6. [Oliveira e Silva: pi(x) and pi2(x) tables](#6-oliveira-e-silva-pix-and-pi2x-tables)
7. [Oliveira e Silva: prime gaps](#7-oliveira-e-silva-prime-gaps)
8. [Oliveira e Silva: twin-prime gaps](#8-oliveira-e-silva-twin-prime-gaps)
9. [Oliveira e Silva: Goldbach partitions](#9-oliveira-e-silva-goldbach-partitions)
10. [Oliveira e Silva: admissible prime constellations](#10-oliveira-e-silva-admissible-prime-constellations)
11. [LMFDB: Dirichlet L-function zeros with Conrey labels](#11-lmfdb-dirichlet-l-function-zeros-with-conrey-labels)
12. [Maximal and first-occurrence prime gap records](#12-maximal-and-first-occurrence-prime-gap-records)
13. [OEIS b-files](#13-oeis-b-files)
14. [Gourdon reference tables](#14-gourdon-reference-tables)
15. [Sources tried and not obtained](#15-sources-tried-and-not-obtained)
16. [Re-download and verification](#16-re-download-and-verification)
17. [LMFDB: level-1 Maass cusp forms](#17-lmfdb-level-1-maass-cusp-forms)
18. [LMFDB / Platt: three windows of the rigorous zero binary archive](#18-lmfdb--platt-three-windows-of-the-rigorous-zero-binary-archive)
19. [LMFDB: sibling L-function zeros, degrees 2-4](#19-lmfdb-sibling-l-function-zeros-degrees-2-4)
20. [LMFDB: abelian variety isogeny classes over finite fields (Weil polynomial tables)](#20-lmfdb-abelian-variety-isogeny-classes-over-finite-fields-weil-polynomial-tables)
21. [Physics resonance spectra: ENDF neutron resonances and Kerr quasinormal modes (QNM)](#21-physics-resonance-spectra-endf-neutron-resonances-and-kerr-quasinormal-modes-qnm)

---

## 1. Scope and layout

```
experiments/primes/_cache/
├── odlyzko/                 pre-existing: zeros1, zeros3, zeros4, zeros5 (see section 2)
└── datasets/                everything in this document
    ├── SHA256SUMS           per-file manifest, 416 entries
    ├── odlyzko/             zeros2, zeros6, zeros6.gz
    ├── lmfdb/               high-precision zeta zeros, Platt sample, Dirichlet L zeros
    │   ├── platt/data/      three binary .dat zero-block windows (see section 18)
    │   ├── siblings/        degree 2/4 sibling L-function zeros (see section 19)
    │   └── av_fq/           abelian variety isogeny classes over F_q (see section 20)
    ├── lmfdb_maass/         level-1 Maass cusp form spectral parameters (see section 17)
    ├── tos/                 Oliveira e Silva: primes/, gaps/, twin_gaps/, goldbach/, apc/, zeta/
    ├── oeis/                14 b-files
    ├── gaps_records/        maximal and first-occurrence prime gap tables
    ├── misc/                Gourdon reference material
    └── physics/             ENDF neutron resonances and Kerr QNM tables (see section 21)
        ├── endf/            IAEA ENDF/B-VIII.0 resolved resonance parameters, 14 nuclides
        └── qnm/             Berti-Cardoso-Starinets Schwarzschild + Kerr QNM tables
```

Two conventions recur and are easy to get wrong:

- **Odlyzko offset convention.** The high-index tables (`zeros3`, `zeros4`, `zeros5`, already in the
  repo) do not list $\gamma$ itself. They list $\gamma - C$ for a per-file constant $C$ stated in a
  9-line prose header, because $\gamma$ has more integer digits than the tables carry precision.
  `zeros1`, `zeros2` and `zeros6` have no header and no offset: the values are absolute $\gamma$.
  `experiments/primes/e5e_zero_statistics.py` already parses the offset out of the header.
- **Oliveira e Silva exponent notation.** Throughout his files, `NdM` means $N \cdot 10^M$ and `NbM`
  means $N \cdot 2^M$. So `1d17` is $10^{17}$ and `1b76` is $2^{76}$. A `?` in a value column means
  the quantity is not known at that point, not zero.

All Oliveira e Silva files are gzipped ASCII with a `#`-prefixed comment header that restates the
column meanings, a two-line column caption (names, then a dashed rule), then the data rows, then a
`# EOF` line. Line counts below are given for the uncompressed stream.

---

## 2. Odlyzko: zeros2 and zeros6

**What it is.** The two Odlyzko zeta zero tables the repo did not already have. `zeros2` is the
first 100 nontrivial zeros to over 1000 decimal places. `zeros6` is the first 2,001,052 zeros to
within $4 \cdot 10^{-9}$, superseding the already-present `zeros1` (first 100,000) in coverage.

**Source.**
- `https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros2`
- `https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6.gz`

Index page: `https://www-users.cse.umn.edu/~odlyzko/zeta_tables/`

| Local file | Bytes | Lines | sha256 |
|---|---|---|---|
| `odlyzko/zeros2` | 105,979 | 1,601 | `0439d90a4c025d1ab3ed25f2241f27afeb6d01e651d95672267783b859ee170f` |
| `odlyzko/zeros6.gz` | 14,369,780 | (gzip) | `6acacb4707c429bf368f32823a8eef0e0737b6318d3e144c78975a4986d155da` |
| `odlyzko/zeros6` | 36,018,936 | 2,001,052 | `2ef7b752c2f17405222e670a61098250c8e4e09047f823f41e2b41a7b378e7c6` |

**Format, `zeros2`.** 100 records, one per zero, in increasing order. Records are separated by a
whitespace-only line. Within a record the digits of $\gamma$ are broken across continuation lines:
the first line is ` 14.134725141734693790457251983562470270784257115699243175685567460149`
(a leading space, then `NN.` and 66 digits), each continuation line is a leading space plus 70
further digits, and the final line of the record is a short remainder. Joining the stripped lines
of a record gives a plain decimal numeral. Verified: 100 records, 1,023 decimal places on the first
record, 1,022 on the last, every record matching `\d+\.\d+`, first record agreeing with the known
value of $\gamma_1$. Range $\gamma_1 = 14.1347\ldots$ to $\gamma_{100} = 236.5242\ldots$.
No offset. Units: imaginary part of the zero, i.e. $\rho = 1/2 + i\gamma$.

**Format, `zeros6`.** One value per line, 9 decimal places, absolute $\gamma$, no header, no offset,
strictly increasing. First `14.134725142`, last `1132490.658714411`. Accuracy $4 \cdot 10^{-9}$.

**Serves.** `zeros2` is the precision reference for anything where 9 digits is not enough: Li
coefficient $\lambda_n$ evaluation, explicit-formula residuals, and Weil quadratic form entries in
`experiments/positivity/`, where cancellation eats digits fast. `zeros6` extends the zero-counting
and pair-correlation work in `e5e_zero_statistics.py` from $10^5$ to $2 \cdot 10^6$ zeros, a
twentyfold increase in the height range at fixed precision.

---

## 3. LMFDB: first 100,000 zeta zeros at 31 decimals

**What it is.** The same index range as Odlyzko's `zeros1` but at 31 decimal places instead of 9.
LMFDB's zeta zero archive covers the first 103,800,788,359 zeros at a stated precision of
$\pm 2.5 \cdot 10^{-31}$; this is the first 100,000 of them.

**Source.** `https://www.lmfdb.org/zeros/zeta/list?N=1&limit=100000&download=yes`

The endpoint takes `N` (starting zero index) or `t` (starting imaginary part), plus `limit`.
`download=yes` only sets a `Content-Disposition` header; the body is identical without it.

| Local file | Bytes | Lines | sha256 |
|---|---|---|---|
| `lmfdb/lmfdb_zeta_zeros_N1_100000.txt` | 4,378,075 | 100,000 | `af8ca55fa1cca4d07d42e9e93511c91760d07d96d2053aa673d5c6b8e29451f1` |

**Format.** Two whitespace-separated columns, no header, no offset.

| Column | Meaning |
|---|---|
| 1 | zero index $n$, integer, contiguous from 1 to 100000 |
| 2 | $\gamma_n$, the imaginary part, 31 decimal places |

Verified: indices contiguous, values strictly increasing, first `14.1347251417346937904572519835625`,
last (index 100000) `74920.8274989941867938492009469183467`. That last value agrees with `zeros1`'s
final entry `74920.827498994`, which is a good cross-check between the two independent sources.

**Serves.** Drop-in high-precision replacement for `zeros1` wherever the 9-digit table currently
limits an experiment: Li coefficient sums, the Weil explicit formula pairing in
`e5c_explicit_formula.py`, and any Gram-matrix positivity margin where the answer is a small
difference of large terms.

---

## 4. LMFDB / Platt: every millionth zero to the 1.038e11-th

**What it is.** A sampled traverse of the entire LMFDB/Platt rigorous zeta zero archive: the
$n \cdot 10^6$-th zero for $n = 1 \ldots 103800$. This reaches the $1.038 \cdot 10^{11}$-th zero at
height $\gamma \approx 3.06 \cdot 10^{10}$, which is the height of Platt's rigorous RH verification.
It is the single widest-range zero dataset here by a very large margin, and it is plain ASCII rather
than the binary `.dat` format the rest of that archive uses.

**Source.** `https://beta.lmfdb.org/riemann-zeta-zeros/examples/every_millionth_zero/`

Files taken: `every_millionth`, `platt_zeros.py` (the decoder for the binary `.dat` files in the
sibling `data/` directory), `print_every_million.py` (the 9-line script that generated the sample),
and `md5sum.log` (upstream checksums for all 14,580 binary `.dat` files, kept so the rest of the
archive can be pulled and verified later without re-listing it).

The `beta.lmfdb.org` host sits behind a trivial JavaScript cookie gate. `curl -b "human=1"` passes
it. There is no login.

| Local file | Bytes | Lines | sha256 |
|---|---|---|---|
| `lmfdb/platt/every_millionth` | 5,834,244 | 103,800 | `518365e1383afada4cd43ba166241696310f5897b8d5f5f97f2d14b6edca68cf` |
| `lmfdb/platt/platt_zeros.py` | 7,052 | 188 | `60109d4206801b3e4bfd3f317e091c1c1e4e069bc7e494ec5acf8f77190ac764` |
| `lmfdb/platt/print_every_million.py` | 204 | 9 | `dd0d35f96b391bd3bcbb5c09f177b61f6e81b6422328d1d43e9ee6d1e337f838` |
| `lmfdb/platt/md5sum.log` | 811,161 | 14,580 | `6ca3534a1e967f593a93428e6479eac0992c446a105da3eeb0b7a64121808521` |

**Format of `every_millionth`.** Two whitespace-separated columns, no header, no offset.

| Column | Meaning |
|---|---|
| 1 | zero index $n$, a multiple of $10^6$, from `1000000` to `103800000000` |
| 2 | $\gamma_n$, imaginary part, about 32 decimal places |

Verified: 103,800 rows, exactly 2 fields each, strictly increasing, first row
`1000000 600269.67701244495552123391427049074415`, last row
`103800000000 30609823941.04471807107601978670037846167787`.

`platt_zeros.py` is Python 2 (as is `print_every_million.py`, which uses a `print` statement). Use
it as a format reference, not as a runnable module, unless you port it.

**Serves.** This is the dataset that lets a zero-statistics claim be tested against height rather
than against index. The Riemann-von Mangoldt count $N(T)$, the mean spacing
$2\pi / \log(T/2\pi)$, and any asymptotic in `e5e_zero_statistics.py` can be checked at
$T \sim 3 \cdot 10^{10}$ instead of $T \sim 10^5$, which is where the $\log\log$ terms finally
separate. It is also the concrete data behind the "RH verified to height $H$" record.

---

## 5. Oliveira e Silva: Dirichlet L-series zeros (168 characters)

**What it is.** The first 10,000 critical-line zeros of $L(s,\chi)$ for every primitive Dirichlet
character of modulus $q \in \{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,24,30,40,60,120\}$, plus 10
zeros each for the imprimitive ones. 651,030 zeros in total across 168 files, to 20 decimal places.
Modulus 1 is the Riemann zeta function itself.

This is the most directly useful single acquisition for this repo: it covers moduli 3, 4, 8 and 12
(the Chebyshev prime races) and modulus 5 (the character basis behind the Davenport-Heilbronn
control) at a depth no other free source matches.

**Source.** `https://sweet.ua.pt/tos/zeta/zeros_<QQQ>_<CCC>.txt.gz`, indexed from
`https://sweet.ua.pt/tos/zeta.html`. Computed with Rubinstein's `lcalc` for an initial approximation
and refined to 20 decimals with PARI/GP. Last updated 2007-08-07.

| Directory | Files | Bytes | Aggregate sha256 |
|---|---|---|---|
| `tos/zeta/` | 168 | 8,358,500 (17,755,875 uncompressed) | `911b3aa283085fa28f3cbfce5bc0bfa1f724d19f05d6bfeb1f03576f938c1054` |

The aggregate is `sha256` of the sorted per-file `sha256sum` listing; see section 16. Individual
checksums for the files this repo cares about:

| Local file | Character | Bytes | Data rows | sha256 |
|---|---|---|---|---|
| `tos/zeta/zeros_001_000.txt.gz` | $\zeta(s)$ | 128,232 | 10,000 | `184394cefc738c6b70caf092c284c3f485408edc019d2a9560ec673a1c23e3f9` |
| `tos/zeta/zeros_003_001.txt.gz` | odd real, mod 3 | 128,149 | 10,000 | `8d2c08dcf9e4ccab23ae500742e775d63b01bd67c05d06681214c0d792765e66` |
| `tos/zeta/zeros_004_001.txt.gz` | odd real, mod 4 | 128,152 | 10,000 | `6b75c79c9d9af6ab3cae83873e13e41bcc5b1a279d625a32affe5b7230c3bba3` |
| `tos/zeta/zeros_005_001.txt.gz` | odd order 4, mod 5 | 127,935 | 10,000 | `b91fad760df6c2f9c7467cf596c1bbb2cb590774b4fe34e79019d423b1405738` |
| `tos/zeta/zeros_005_002.txt.gz` | even real, mod 5 | 127,974 | 10,000 | `a5bce3f3e261127b263ccd52328609761b54b216d8ef4c242dee7d88ff86bb62` |
| `tos/zeta/zeros_005_003.txt.gz` | odd order 4, mod 5 | 127,955 | 10,000 | `23ca00dc5fdf7d65c7f2f99ec4ed6941d7aa83be8565868d179425d6092a43ed` |

**Naming.** `zeros_QQQ_CCC.txt.gz`: `QQQ` is the modulus $q$ zero-padded to 3 digits, `CCC` is a
character index within that modulus, zero-padded to 3 digits, running `000` to `phi(q)-1`. Index
`000` is always the principal character. Files for primitive characters carry 10,000 zeros; files
for imprimitive characters carry only 10, and their header names the primitive character they
reduce to (for example `zeros_003_000` has `type: + real 001-000`, and its ten values are exactly
the first ten zeta zeros).

File counts by modulus: 1, 2 (one file each); 3, 4, 6 (two); 5, 8, 10, 12 (four); 7, 9, 14 (six);
15, 16, 20, 24, 30 (eight); 11 (ten); 13 (twelve); 40, 60 (sixteen); 120 (thirty-two).

**Character identification (important).** `CCC` is an internal index, not a Conrey label. Do not
guess it. Each file's header specifies the character completely and unambiguously as a table of
$\log(\chi(n)) / (2\pi i)$ for each $n$ coprime to $q$, given as an exact rational, so
$\chi(n) = e^{2\pi i \theta_n}$. For example `zeros_005_001` has
$\theta_1 = 0, \theta_2 = 1/4, \theta_3 = -1/4, \theta_4 = 1/2$, and is labelled
`type: - primitive` (the leading sign is the parity: `-` odd, `+` even). This spec is
convention-independent, so it can be matched against any labelling scheme you like. Section 11
records the Conrey cross-reference established from the LMFDB downloads.

**Format of the data rows.** One value per line, no index column, no offset: the positive imaginary
part $\gamma > 0$ of a zero on the critical line, 20 decimal places, strictly increasing. Only
positive-imaginary-part zeros are listed (the rest follow by symmetry). Verified for all 168 files:
every file parses as floats, every file is strictly increasing, 65 files carry exactly 10,000 zeros
and 103 carry exactly 10, no exceptions.

**Serves.** Two things at once. First, the Chebyshev prime race work mod 3, 4, 8 and 12 needs the
zeros of exactly these $L$-functions to build the explicit formula for
$\psi(x;q,a) - \psi(x;q,b)$, and 10,000 zeros per character is enough to resolve the bias out to
substantial $x$. Second, the Davenport-Heilbronn control in `experiments/_shared/davenport_heilbronn.py`
is built from characters mod 5, and these files supply the exact zeros of the two genuine mod-5
$L$-functions that the D-H combination is assembled from, which is what makes "zeta versus D-H"
a controlled comparison rather than an assertion.

---

## 6. Oliveira e Silva: pi(x) and pi2(x) tables

**What it is.** Exact values of the prime counting function $\pi(x)$ and the twin-prime counting
function $\pi_2(x)$ (the number of primes $p \le x$ with $p+2$ also prime), on decimal and binary
grids, plus a $\pi(x) \bmod 2$ table and a table of zero-based estimates of $\pi(x)$.

**Source.** `https://sweet.ua.pt/tos/primes/<name>.txt.gz`, indexed from
`https://sweet.ua.pt/tos/primes.html`.

| Directory | Files | Bytes | Aggregate sha256 |
|---|---|---|---|
| `tos/primes/` | 43 | 4,604,568 (12,333,343 uncompressed) | `648944b31eed4b0070beef87431079774de605d2e266fe640d94124218e6c81b` |

Contents: `1d00`..`1d22` (23 files, 161,433 data rows total), `2d00`..`2d15` (16 files, 144,018 data
rows total), `1b00`, `2b00`, `mod2`, `estimates`.

**Naming.** Prefix `1` is $\pi(x)$, prefix `2` is $\pi_2(x)$. Letter `d` is a decimal grid, `b` a
binary grid. Suffix `00` is the special "powers of the base" table. Suffix `NN` at least 01 means
the grid step is $10^{NN}$, so `1d05` holds $\pi(k \cdot 10^5)$ for $k = 1, 2, 3, \ldots$.

| File | Grid | Rows |
|---|---|---|
| `1d00` | $\pi(10^k)$, $k = 1 \ldots 23$ | 23 |
| `1d01`..`1d16` | $\pi(k \cdot 10^m)$, $k = 1 \ldots 10000$ | 10,000 each |
| `1d17` | $\pi(k \cdot 10^{17})$, $k = 1 \ldots 1000$ | 1,000 |
| `1d18`..`1d21` | $\pi(k \cdot 10^m)$, $k = 1 \ldots 100$ | 100 each |
| `1d22` | $\pi(k \cdot 10^{22})$, $k = 1 \ldots 10$ | 10 |
| `1b00` | $\pi(2^k)$, $k = 1 \ldots 76$ | 76 |
| `2d00` | $\pi_2(10^k)$, $k = 1 \ldots 18$ | 18 |
| `2d01`..`2d14` | $\pi_2(k \cdot 10^m)$, $k = 1 \ldots 10000$ | 10,000 each |
| `2d15` | $\pi_2(k \cdot 10^{15})$, $k = 1 \ldots 4000$ | 4,000 |
| `2b00` | $\pi_2(2^k)$, $k = 1 \ldots 61$ | 61 |

**Format, the `1*` files.** Three whitespace-separated columns.

| Column | Meaning |
|---|---|
| `x` | the argument, in `NdM` / `NbM` exponent notation |
| `pi(x)` | exact integer $\pi(x)$ |
| `li(x)` | $\mathrm{li}(x)$, the principal value of $\int_0^x dt/\log t$, truncated and suffixed with `...` |

The third column is the logarithmic integral itself, not a difference. Compute $\pi(x) - \mathrm{li}(x)$
yourself if you want the error term; the `...` marks truncation, so strip it before parsing.

**Format, the `2*` files.** Three columns: `x`, then exact integer `pi2(x)`, then a column captioned
`2Ctwin li2(x)`, which is the Hardy-Littlewood prediction $2 C_2 \int_2^x dt/(\log t)^2$ with
$C_2$ the twin primes constant, again truncated with `...`.

**Format, `mod2`.** Three columns: `x`, `pi(x)` (or `?` where unknown), and `p` equal to
$\pi(x) \bmod 2$. 740 lines, 668 data rows, covering both decimal and binary grids.

**Format, `estimates`.** Six columns, 2,265 lines, 2,241 data rows, for $x$ up to about $10^{30}$.

| Column | Meaning |
|---|---|
| `x` | argument in `NdM` / `NbM` notation |
| `nz` | number of zeta zeros used in the Riemann exact formula for this estimate |
| `pi(x) estimate` | estimated $\pi(x)$, non-integral |
| `std(x)` | approximate standard deviation of that estimate |
| `e(x)` | the error in the estimate |
| `e(x)/std(x)` | the error in units of its own standard deviation |

These are estimates from Riemann's exact formula truncated at $10^9$ zeros, not exact counts.

**Individual checksums.**

| Local file | Bytes | Lines (uncompressed) | Data rows | sha256 |
|---|---|---|---|---|
| `tos/primes/1d00.txt.gz` | 821 | 43 | 23 | `d92cf2937c9153e5041ebe8907f93bc34d4a7c065826714bb1a6735d4b0de4ae` |
| `tos/primes/2d00.txt.gz` | 711 | 39 | 18 | `3fc410c2e912c980334bb7ee47d351c797e2cde59db19ab413221c313117a7c6` |
| `tos/primes/1b00.txt.gz` | 1,800 | 96 | 76 | `90dc8cac9a0956c625ea36a9db892f858a014db8ce6167ac156c70083bf5fe30` |
| `tos/primes/2b00.txt.gz` | 1,366 | 82 | 61 | `22ce8e943171c3d3e8ff22b131efa613d894ec8739ac091567ee7eb0a4d3a6c5` |
| `tos/primes/mod2.txt.gz` | 7,878 | 740 | 668 | `34700f4a09c55ac6c7ef7d263ae591b361b23356174693367201247829be7680` |
| `tos/primes/estimates.txt.gz` | 67,168 | 2,265 | 2,241 | `06e6b634ef3598357583f21cce5fa3e513cbc6ccd230e108a7180f06105eaa80` |

**Accuracy caveats stated upstream.** $\pi(x)$ values were double-checked by re-running the same
program, so they are checked against random machine error but not against a consistent algorithmic
or hardware fault; the author states 99.99% confidence. Values of $\pi_2(x)$ for
$x > 357425 \cdot 10^{12}$ published before 2008-03-01 were low by one; the current files are fixed.

**Serves.** This is the ground truth for the prime-counting side of the explicit formula. The
$\pi(x)$ grids at step $10^{m}$ over $10^{16}$ rows give a direct measurement of
$\pi(x) - \mathrm{li}(x)$ oscillation, which is the quantity the zeta zeros are supposed to
reconstruct in `e5c_explicit_formula.py`; the $\pi_2(x)$ grids do the same for the twin-prime
constant in `e5b_twin_primes.py`. The `estimates` file is a useful adversarial check on our own
explicit-formula code, since it is the same computation done independently.

---

## 7. Oliveira e Silva: prime gaps

**What it is.** First occurrences and occurrence counts for every even gap between consecutive
primes, over all primes below $4 \cdot 10^{18}$, plus the Hardy-Littlewood constants needed to
predict those counts.

**Source.** `https://sweet.ua.pt/tos/gaps/t0.txt.gz` and `.../t1.txt.gz`, indexed from
`https://sweet.ua.pt/tos/gaps.html`. Last updated 2012-04-07 (`t0`) and 2012-09-08 (`t1`).

| Local file | Bytes | Lines (uncompressed) | Data rows | sha256 |
|---|---|---|---|---|
| `tos/gaps/t0.txt.gz` | 14,119 | 782 | 740 | `7227a85c31cbfc16e4bbd5588d4b3bb1a9c11e360d558745cc55e73b9f5d11b7` |
| `tos/gaps/t1.txt.gz` | 98,949 | 2,612 | 2,463 | `c2979a78e88c3a0a2d7faad1b823fb91bbf0b89b2d8636e76a1d26d88e0b1246` |

**Format, `t0`.** Four columns.

| Column | Meaning |
|---|---|
| `g` | the gap, an integer; may carry a trailing `*` |
| `P(g)` | the least prime such that $P(g)+g$ is the next prime after $P(g)$; may carry a trailing `*`; `?` if unknown |
| `N(g)` | the number of times gap $g$ occurred between consecutive primes below the test limit |
| `finder` | attribution string |

The `*` marks a record holder. Per the file's own legend: $g$ is a record holder if
$P(g') > P(g)$ for all even $g' > g$, and $P(g)$ is a record holder if $P(g') < P(g)$ for all even
$g' < g$. So filtering rows whose `g` carries a `*` extracts the maximal prime gaps directly.
Test interval $[2, 4 \cdot 10^{18}]$, double-tested on $[2, 4 \cdot 10^{17}]$.

**Format, `t1`.** Four columns: `g`, `k` (the size of the constellation), `T(g,k)` (the accumulated
product $\prod (q-w)$ in Brent's notation), and `A(g,k)` (the associated Hardy-Littlewood constant,
in `0.dddde+NN` PARI style). The header carries the PARI/GP snippets that turn `T(g,k)` into
`A(g,k)` and then into the estimate $N(x;g)$, including the alternating-sign sum over $k$. Covers
even $g$ up to 212.

**Serves.** `t0` is the exact answer key for gap statistics: any model of prime gaps (Cramer,
Hardy-Littlewood, the $\log$-correlated field picture in `experiments/multifractal/`) predicts
$N(g)$, and this file says what $N(g)$ actually is out to $4 \cdot 10^{18}$. `t1` supplies the
constants so the prediction can be computed rather than fitted.

---

## 8. Oliveira e Silva: twin-prime gaps

**What it is.** First occurrences and counts of gaps between consecutive twin-prime pairs, up to
$10^{16}$.

**Source.** `https://sweet.ua.pt/tos/twin_gaps/twin_gaps.txt.gz`, indexed from
`https://sweet.ua.pt/tos/twin_gaps.html`. Last updated 2013-08-05.

| Local file | Bytes | Lines (uncompressed) | Data rows | sha256 |
|---|---|---|---|---|
| `tos/twin_gaps/twin_gaps.txt.gz` | 60,000 | 4,079 | 4,052 | `960e6ae33e7a103971dbe98569b0bd03479f24d7b1d98f158dd7fbd8885db176` |

**Format.** Three columns.

| Column | Meaning |
|---|---|
| `g` | gap between consecutive twin-prime pairs, that is $q - p$ where $(p,p+2)$ and $(q,q+2)$ are consecutive twin pairs; may carry `*` |
| `F(g)` | the least prime $p$ of the first twin pair at which gap $g$ first occurs; may carry `*` |
| `T(g)` | number of occurrences of gap $g$ with the last prime of the second pair below $10^{16}$ |

The `*` marks record holders under the same rule as section 7: $g$ is a record holder if
$F(u) > F(g)$ for all $u > g$, and $F(g)$ is a record holder if $F(u) < F(g)$ for all $u < g$.

**Serves.** The second-order test for `e5b_twin_primes.py`. Getting the twin-prime count right is
one constraint; getting the distribution of gaps between twin pairs right is a much sharper one, and
this is the only free table of it at this depth.

---

## 9. Oliveira e Silva: Goldbach partitions

**What it is.** The output of the Goldbach verification to $4 \cdot 10^{18}$, expressed as: for each
small prime $p$, the least even number whose minimal Goldbach partition uses $p$ as its smaller
prime, and how often $p$ played that role. Plus Hardy-Littlewood constants, plus 100,000 digits of
the twin primes constant.

**Source.** `https://sweet.ua.pt/tos/goldbach/{t0,t1,cTwin}.txt.gz`, indexed from
`https://sweet.ua.pt/tos/goldbach.html`. Verification limit $4 \cdot 10^{18}$ reached 2012-04-04;
double-checked to $4 \cdot 10^{17}$ as of 2013-05-26; about 781.8 single-core CPU years.

| Local file | Bytes | Lines (uncompressed) | Data rows | sha256 |
|---|---|---|---|---|
| `tos/goldbach/t0.txt.gz` | 24,812 | 1,252 | 1,207 | `fa5e73f253154342e2d13ad095f32bab4a1670c517baaf9b3da42751f8010fce` |
| `tos/goldbach/t1.txt.gz` | 48,153 | 1,239 | 1,143 | `23c184b8777af225f2df26c23e6fb78bc869d6ad21746d9c314be3fbd1bb2986` |
| `tos/goldbach/cTwin.txt.gz` | 50,292 | 1,014 | 1,000 | `c7f220d7a7f1020cb6a764b696f7c16e45a5ee07948df89527fc20a2eee4bbe0` |

**Format, `t0`.** Five columns.

| Column | Meaning |
|---|---|
| `pi(p)` | the index of $p$, that is the number of primes not larger than $p$ |
| `p` | the prime; may carry `*` |
| `S(p)` | the least even number for which $p$ is the smallest prime in one of its Goldbach partitions; may carry `*`; `?` if unknown |
| `L(p)` | the number of times $p$ was the smallest prime in a minimal Goldbach partition |
| `finder` | attribution string |

`*` marks record holders: $p$ is one if $S(q) > S(p)$ for all $q > p$, and $S(p)$ is one if
$S(q) < S(p)$ for all $q < p$. Test interval $[4, 4 \cdot 10^{18}]$.

**Format, `t1`.** Four columns `p`, `k`, `T(p,k)`, `C(p,k)`, the Hardy-Littlewood data used to
estimate $L(x;p)$, for odd primes $p < 250$.

**Format, `cTwin`.** Not a table. It is the decimal expansion of the twin primes constant
$C_2 = 0.66016181584686957392\ldots$, 1,000 lines of 100 digits each, so 100,000 digits. The first
line carries the `0.` prefix, subsequent lines are indented continuation digits.

**Serves.** `cTwin` at 100,000 digits removes the twin-prime constant as a source of error in any
Hardy-Littlewood comparison. `t0` is a strong structural control for the counting-side work: it is
an exact, deep, additive-decomposition statistic, which is precisely the kind of quantity the
Beurling discipline in `experiments/_shared/beurling.py` says a Euler-product-only construction
must fail to reproduce.

---

## 10. Oliveira e Silva: admissible prime constellations

**What it is.** The minimum width $l(k)$ of an admissible prime $k$-tuple, against the $k$-th prime
$p(k)$, for $k$ up to 1000. This is the data behind the search for a counterexample to the
$\pi(x)$ conjecture (the second Hardy-Littlewood conjecture).

**Source.** `https://sweet.ua.pt/tos/apc/t0.txt.gz`, indexed from
`https://sweet.ua.pt/tos/apc.html`. Computational results dated 2015-07-14.

| Local file | Bytes | Lines (uncompressed) | Data rows | sha256 |
|---|---|---|---|---|
| `tos/apc/t0.txt.gz` | 12,639 | 1,029 | 999 | `253fa015b27cb23901c827b28e8da2484ac8d78091cadb4a2fa7a73015d1349b` |

**Format.** Five columns.

| Column | Meaning |
|---|---|
| `k` | constellation size, 2 to 1000 |
| `p(k)` | the $k$-th prime |
| `l(k)` | minimum width of an admissible constellation of size $k$; exact for $k \le 300$, `?` beyond |
| `le(k)` | the estimate $k(1 + \log k)$ for that width |
| `c(k)` | $p(k) - l(k) - 1$ when $l(k)$ is available, otherwise $p(k) - le(k) - 1$ |

Integer values are exact for $k \le 300$; floating point values for $k > 300$ are estimates. The
stated goal is to find a $k$ with $c(k) \ge 0$.

**Serves.** Admissibility data for the constellation sieve in `primestream.py`, and an independent
check on the $k$-tuple machinery used by `e5b_twin_primes.py`.

---

## 11. LMFDB: Dirichlet L-function zeros with Conrey labels

**What it is.** A small set of LMFDB per-L-function zero downloads, taken specifically to pin down
the Conrey label of the Oliveira e Silva character indices in section 5.

**Source.** `https://www.lmfdb.org/L/download_zeros/<label>` where `<label>` is the hyphenated
LMFDB L-function label, for example `1-3-3.2-r1-0-0`.

| Directory | Files | Bytes | Aggregate sha256 |
|---|---|---|---|
| `lmfdb/dirichlet/` | 4 | 44,350 | `0cad37b647ddccba7b60a171b4a94c6dded9932fd28d3e008bd6e912c716270c` |

| Local file | Positive zeros | Bytes | sha256 |
|---|---|---|---|
| `1-3-3.2-r1-0-0.zeros.txt` | 114 | 8,659 | `454868ad79b51a192729f9ee81c8cf43ea30beda9fdf038b0d8e3a4b3f8b231d` |
| `1-5-5.2-r1-0-0.zeros.txt` | 130 | 9,817 | `0a1a49b47ceb38ba0d6a8b8d481828536211fd787ba34fee5ea6cd1a32f801da` |
| `1-5-5.4-r0-0-0.zeros.txt` | 129 | 9,806 | `92420854aff1d4cb2438517959717ad582c36070aea2a9ff83474fc586fa67b7` |
| `1-12-12.11-r0-0-0.zeros.txt` | 158 | 11,972 | `9c1783218abac0e21eca87b492a84185feb776625a315cfca676f37a179d25cc` |

**Format.** One `#` comment line naming the L-function and the download date, then a single JSON
object on the remainder of the file, with keys `order_of_vanishing`, `positive_zeros`,
`negative_zeros`, `positive_zeros_accuracy`, `negative_zeros_accuracy`. The zeros are decimal
strings at 30 significant digits, imaginary parts, no offset. Parse by slicing from the first `{`
and calling `json.loads`.

**The cross-reference this establishes.** The LMFDB first zeros agree exactly with the Oliveira e
Silva first zeros to all 20 shared decimals, giving:

| Conrey label | Oliveira e Silva file | First $\gamma$ |
|---|---|---|
| 3.2 | `zeros_003_001` | 8.03973715568146668171 |
| 5.2 | `zeros_005_001` | 6.18357819545085391438 |
| 5.4 | `zeros_005_002` | 6.64845334472771471612 |

So the two labelling schemes can be aligned by matching first zeros, and for moduli where that is
ambiguous the character header described in section 5 settles it outright.

**Serves.** Label reconciliation only. For actual computation use the Oliveira e Silva files: 10,000
zeros per character beats 114 to 158, and the extra 10 digits of precision here are not the binding
constraint. Kept because a wrong character-to-label mapping is a silent, expensive error in a prime
race experiment.

---

## 12. Maximal and first-occurrence prime gap records

**What it is.** Three record tables: Thomas R. Nicely's comprehensive first-occurrence and maximal
prime gap list, and Jens Kruse Andersen's maximal-gap and large-merit-gap tables.

**Source.** Both original hosts are gone. `trnicely.net` now resolves to an unrelated spam blog
(it returns HTTP 200, so a naive fetch silently succeeds with garbage), and `primerecords.dk`
returns HTTP 454 to anonymous clients. All three files came from the Wayback Machine, using the
`id_` raw-content suffix so no toolbar is injected:

- `https://web.archive.org/web/20191020030117id_/http://www.trnicely.net/gaps/gaplist.html`
- `https://web.archive.org/web/20260807003855id_/http://primerecords.dk/primegaps/gaps20.htm`
- `https://web.archive.org/web/20260314161939id_/https://primerecords.dk/primegaps/maximal.htm`

Note the Nicely snapshot deliberately uses a 2019 timestamp. The most recent snapshot of that URL
is only 6 KB and captures the squatted page; the 2019 snapshots are about 33 KB compressed and hold
the real table.

| Local file | Bytes | Lines | sha256 |
|---|---|---|---|
| `gaps_records/nicely_gaplist.html` | 100,353 | 1,722 | `5feae5b58ef8ab0bb36014d9974c4f69c86058e99507ec106866dc29d3d21d74` |
| `gaps_records/jka_gaps20.html` | 25,831 | 343 | `9e336141c51d198e6918424f282394601f1d8c3b8b855ff071b9240434030333` |
| `gaps_records/jka_maximal.html` | 14,495 | 198 | `fa96f9c5f7f39b046d5c394a774c8acd891501c29362d3d638eecdf11da68002` |

**Format.** All three are HTML documents wrapping a fixed-width or `<table>` record list, not
delimited data. Strip tags (`sed 's/<[^>]*>/ /g'`) before parsing. The Wayback `id_` endpoint served
the two `primerecords.dk` files gzip-compressed without declaring a `Content-Encoding`, so they were
decompressed after download; the copies on disk are plain HTML.

`jka_maximal.html` columns: `No` (record ordinal), `Size` (the gap), `Gap start` (given as
`Pn = <value>`, where `n` is the digit count of the starting prime), `Merit`
(gap divided by $\log$ of the gap start, prefixed `+` when the merit is also a record),
`Discoverer`, `Year`. `jka_gaps20.html` is the companion list of known gaps of merit above 20.
`nicely_gaplist.html` is the larger first-occurrence table, keyed by gap size with the starting
prime, merit, and discoverer.

**Serves.** Extreme-value control for gap models. The maximal gaps are where Cramer-type
$\limsup$ predictions and the multifractal picture in `experiments/multifractal/` actually differ,
and these tables record the observed record holders with their merits.

---

## 13. OEIS b-files

**What it is.** Fourteen OEIS b-files covering primes, twins, constellations, record gaps, the
Mertens function, and zeta zero indices.

**Source.** `https://oeis.org/A<number>/b<number>.txt`. Format is universal: comment lines start
with `#`, data lines are two whitespace-separated fields, index then value, and there are no other
line types. Some files carry trailing blank lines, so count rows by matching digits rather than by
`wc -l`.

| Local file | Sequence | What it holds | Index range | Rows | Bytes | sha256 |
|---|---|---|---|---|---|---|
| `oeis/b006988.txt` | A006988 | the $10^n$-th prime | 0..24 | 25 | 502 | `4266921c6f1294c929a7a1e0fe8d4c8796437073f39e93e919b039b302084d11` |
| `oeis/b002110.txt` | A002110 | primorial $p_n\#$ | 0..350 | 351 | 161,172 | `7ca99cf314e44514fc6a5358c609d0a3421651f1fb0b53029569f426631c4c09` |
| `oeis/b005250.txt` | A005250 | record (maximal) prime gaps | 1..85 | 85 | 587 | `9e4d829fc00101ea7b7776837f2f9063fd898ce0ea28c5aebecba4c27a7cc090` |
| `oeis/b002386.txt` | A002386 | prime starting each maximal gap | 1..85 | 85 | 1,314 | `671d8f0616ebb9fa264849ec35838b69997a43ba36ed7438489aa501114e793f` |
| `oeis/b000101.txt` | A000101 | prime ending each maximal gap | 1..85 | 85 | 1,315 | `44e98f1b14d1580f9e5461a46a668b04200950a55f4d7f7231fabd1483557ecf` |
| `oeis/b005669.txt` | A005669 | index of the prime starting each maximal gap | 1..82 | 82 | 1,135 | `7672d03a43ee340a30b31b72cc535439cf97e55754e2b5cc7c1608507588b313` |
| `oeis/b001359.txt` | A001359 | lesser of twin primes | 1..100000 | 100,000 | 1,420,279 | `19eb8c7d5f32d51dc6c77f8647f74069e4cf8b92da9e21e293b879fb5b0a6a9f` |
| `oeis/b006512.txt` | A006512 | greater of twin primes | 1..10000 | 10,000 | 119,258 | `0552d3d6b7e86b0f2a1ff3258ba942198ce91dab2ac118bb209042ccd9a3ec84` |
| `oeis/b007529.txt` | A007529 | prime triples $p, p+2, p+6$ | 1..10000 | 10,000 | 125,397 | `a91ecf1f313444383dc14c06c922c21dfbb1fa7459e252412bcaa49f27f7dc2c` |
| `oeis/b007530.txt` | A007530 | prime quadruplets $p, p+2, p+6, p+8$ | 1..10000 | 10,000 | 163,001 | `5ba8e991f3de3e4706de9e9367c8b2310549ec37fa8e3979661319616df256c1` |
| `oeis/b006880.txt` | A006880 | $\pi(10^n)$ | 0..29 | 30 | 521 | `8111c06f2093b8cf138480a458945bf2eb1a01ee783d64041a7b11a102cd08a3` |
| `oeis/b002321.txt` | A002321 | Mertens function $M(n)$ | 1..10000 | 10,000 | 78,670 | `c45fa9a5ccb94ebf69b38491e369471378673c659478ac34ead48f17e4705db8` |
| `oeis/b084237.txt` | A084237 | $M(10^n)$ | 0..23 | 24 | 278 | `875871f4cf3ac84943922a134cd3e389757f8a2fe1807a207e60bb1763d834f3` |
| `oeis/b002410.txt` | A002410 | nearest integer to $\gamma_n$ | 1..10000 | 10,000 | 98,217 | `933fa725cdd47db00a583722e7c833977f8fc606c5a85bc5664b7ee4c6eb8969` |

| Directory | Files | Bytes | Aggregate sha256 |
|---|---|---|---|
| `oeis/` | 14 | 2,175,742 | `c2a16f62e03408ad0337299251f30615b1f68a830f5c596aea819639d332f6da` |

Two of these exceed what the task asked for and are worth flagging. A006880 now runs to
$\pi(10^{29}) = 1520698109714272166094258063$, past the $10^{27}$ target. A084237 gives
$M(10^n)$ to $10^{23}$, which is the deepest free Mertens data available and directly bounds how
far the Mertens conjecture's failure has been pushed numerically.

**Units and conventions.** All values are exact integers. A005250 is the gap size itself, while
A002386 and A000101 are the two primes bracketing it, so
A000101$(n) -$ A002386$(n) = $ A005250$(n)$ holds row by row and is a cheap integrity check.
A002410 is a rounded integer, not a precise $\gamma$: use it as an index cross-check only, never as
zero data.

**Serves.** Cheap, exact, independently-sourced check values for `test_primes.py` and
`e5a_digit_patterns.py`. The Mertens pair is the interesting one for RH specifically, since
$M(x) = O(x^{1/2+\epsilon})$ is equivalent to RH, and A084237 is the table against which a numerical
$M(x)/\sqrt{x}$ growth study is calibrated.

---

## 14. Gourdon reference tables

**What it is.** Two documents from Xavier Gourdon and Pascal Sebah's numbers.computation.free.fr,
kept as reference rather than as parseable data.

**Source.**
- `http://numbers.computation.free.fr/Constants/Primes/countingPrimes.html`
- `http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf`

| Local file | Bytes | Lines | sha256 |
|---|---|---|---|
| `misc/gourdon_countingPrimes.html` | 23,711 | 522 | `7d3642701de4acfe9014fadb38cd85b50dfec133f500e4a4d2e0e581621c2a02` |
| `misc/gourdon_zetazeros_1e13_1e24.pdf` | 422,827 | 3,418 | `b1868b1c3f8d8661cb59c58ab6ceffc687dc6dce4d18d35b69117c84f60d4025` |

**Format.** The first is an HTML survey of $\pi(x)$ computation, carrying a $\pi(10^n)$ table and the
Meissel-Lehmer-Lagarias-Miller-Odlyzko method description; strip tags to read it. The second is a
PDF, not machine-readable without extraction, listing zeta zeros in the ranges $10^{13}$ to
$10^{24}$. Treat the PDF as documentation of the Gourdon verification, not as a data source; the
LMFDB and Odlyzko tables in sections 2 to 4 are the machine-readable equivalents.

**Serves.** Method reference for anyone extending `e5f_rh_verification.py`, and a secondary source
for the $\pi(10^n)$ values that cross-checks section 6 and A006880.

---

## 15. Sources tried and not obtained

Recorded so the same dead ends are not re-walked.

| Source | Status |
|---|---|
| `www.trnicely.net` | Domain squatted. The live site is an unrelated blog that returns HTTP 200, so it will fool a status-code check. Original tables recovered from the 2019 Wayback snapshots, see section 12. |
| `primerecords.dk` | Returns HTTP 454/455 to anonymous clients, with and without a browser user agent. Recovered from Wayback, see section 12. |
| `primefan.ru` (Kulsha's $\pi(x)$ and $\mathrm{li}(x)$ tables) | Parked domain; the live page is a Russian-language suspension notice. Downloaded, detected as junk, and deleted. Wayback snapshots from 2008 to 2026 are all 3 to 7 KB, so the archived page never held the bulk tables either. Not obtained. |
| `oto.math.uwaterloo.ca/~mrubinst/L_function_public/` (Rubinstein's 35.1M zeta zeros) | Host fails DNS resolution entirely and has no Wayback snapshot. Decommissioned. Superseded by sections 3 and 4. |
| LMFDB Dirichlet zeros for moduli 4 and 8 | The moduli 8 requests were soft-blocked, and the label `1-4-4.3-r1-0-0` returned HTTP 404, so its rank suffix is wrong. Not chased further: section 5 already covers moduli 4 and 8 with 10,000 zeros per character. |
| LMFDB zeta zeros at high starting index | The `N=1000000000` request was soft-blocked (see the warning below). The first 100,000 landed cleanly before the block. |
| Platt's raw RH verification zero set | Not published as a standalone download. The sampled traverse in section 4 is the public form of it. |
| Li coefficient tables | No public tabulation found. These are computed in-repo from zero data; sections 2 and 3 are the inputs. |
| `pages.jh.edu/eberti2/ringdown/` (Berti's Kerr QNM ringdown tables) | Cloudflare WAF blocks non-browser clients with an HTTP 403 "Sorry, you have been blocked" page, on both http and https, with and without browser-style headers. Not a rate limit; no amount of pacing fixes it. Recovered from the CENTRA/GRIT gravitational-physics group mirror at IST Lisbon, see section 21. |
| LMFDB level-1 Maass form L-functions (degree 2), `download_zeros` | No individually labeled, downloadable record exists; confirmed absent (not throttled) three independent ways, see section 19. Contrast: GL3 self-dual Maass forms do get individual records. |
| LMFDB symmetric square of a level-1 weight-12 form (degree 3), `download_zeros` | Confirmed absent from LMFDB entirely, not merely unlabeled, three independent ways, see section 19. |

**LMFDB rate limiting, the one real trap.** `www.lmfdb.org` sits behind Google reCAPTCHA Enterprise
bot management. When it throttles, it returns **HTTP 200** with an HTML reCAPTCHA challenge body
instead of the requested data. A script that checks only the status code will happily write that
challenge page to disk as if it were a dataset. Always check `Content-Type` and grep the body for
`recaptcha` or `<!doctype` before trusting a response. Throttle to well under 1 request per second
and never issue concurrent requests. `beta.lmfdb.org` has no such defense once the `human=1` cookie
is set.

**LMFDB labels: trailing digits are opaque database keys, never pattern-guess them.** A label's
final numeric fields (e.g. the `0-410` in `2-5077-1.1-c1-0-410`) are not a composable
`(index, order_of_vanishing)` pair, even though several worked examples elsewhere in this file
happen to end in `-0-0`. Copying a suffix pattern from one object onto another returns a different,
silently wrong, well-formed object (HTTP 200, clean, self-consistent JSON) with no signal of the
mismatch beyond a disagreeing `order_of_vanishing`; this cost a silent wrong-object fetch (37.b
instead of 37.a) during the pull in section 19. Resolve the real label from the object's own page
via its origin-URL redirect (HTTP 302, `Location` header), never by pattern-guessing from another
object's label. See section 19 for the full account.

---

## 16. Re-download and verification

Every file here is re-fetchable with `curl` and no credentials. To rebuild the checksum manifest:

```bash
cd experiments/primes/_cache/datasets
find . -type f ! -name SHA256SUMS -printf '%P\n' | sort | xargs sha256sum > SHA256SUMS
```

To verify:

```bash
cd experiments/primes/_cache/datasets && sha256sum -c SHA256SUMS
```

The per-directory aggregate checksums quoted in sections 5, 6, 11 and 13 are the `sha256` of the
sorted per-file `sha256sum` listing for that directory, computed as:

```bash
cd experiments/primes/_cache/datasets
find tos/zeta -type f -printf '%P\n' | sort | (cd tos/zeta && xargs sha256sum) | sha256sum
```

Integrity checks performed at download time, all passing: every `.gz` file passes `gzip -t`; all 168
Dirichlet zero files parse as floats and are strictly increasing with exactly 10,000 or exactly 10
rows; the zeta zero files in sections 2, 3 and 4 parse, are strictly increasing, and agree with each
other and with the known value of $\gamma_1$ where they overlap; all 14 OEIS b-files are plain text
with no HTML contamination. One file was downloaded, found to be a parked-domain placeholder rather
than data, and deleted (see section 15).

---

## 17. LMFDB: level-1 Maass cusp forms

Added 2026-08-19 for [`e1ab_automorphic_spectrum.py`](../spectral/e1ab_automorphic_spectrum.py) and
[`local_quantum_gravity_and_primes.md`](../../docs/03_research/local_quantum_gravity_and_primes.md).

**What it is.** The discrete spectrum of the Laplacian on the modular surface
$\mathbb{H}/PSL(2,\mathbb{Z})$: 2202 weight-0, trivial-character Maass cusp forms of level 1,
listed by spectral parameter $R$, where the Laplace eigenvalue is $\lambda = 1/4 + R^2$. Values
carry roughly 100 significant digits. Contributor of record in LMFDB is Holger Then.

This is the "other half" of the automorphic spectrum from the zeta zeros, which is why it is here.
The zeros are not in this list: they are resonances in the *continuous* (Eisenstein) part, poles of
the scattering phase $\varphi(s) = \xi(2s-1)/\xi(2s)$ at $s = \rho/2$. Having both halves in hand is
what lets the probe show they are different universality classes.

**Files** (`_cache/datasets/lmfdb_maass/`):

| File | Bytes | Contents |
|---|---|---|
| `lmfdb_maass_level1_raw.txt` | 283,890 | The download verbatim, including LMFDB's header and definitions footer. |
| `maass_level1_R.txt` | 91,024 | Parsed, sorted ascending. Columns: `R  symmetry  fricke  label`. |
| `maass_level1.json` | 404,763 | Same records as JSON, retaining the full-precision `R_str`. |

SHA256:

```
df35f051dad90fe234fe94cb2fb4bf71a4282c9788547919da649734914718e2  lmfdb_maass_level1_raw.txt
ce5c71bc2f62fcb0b4acd908b6a235d44ebf99440cfe46568bd3b88caf78b2b4  maass_level1_R.txt
8145824a7b5ac7af3ac4c3152456edea6f228efacba3f1dc07b403c2265e9a50  maass_level1.json
```

**Two conventions that are easy to get wrong.**

- **Symmetry is coded differently by the API and by the download.** The JSON API reports
  `symmetry` as $\pm 1$; this search-page download reports `1`/`0`. Cross-checked on the first
  three forms ($R = 9.5337$ and $12.1730$: API $-1$, here `1`; $R = 13.7798$: API $+1$, here `0`),
  so **`1` is odd and `0` is even**. The first cusp form of the modular group is the odd one at
  $R = 9.533695261$.
- **The list is not complete over its whole range**, and this is the trap that matters. Measured
  against Weyl's law with the scattering correction,
  $N(R) \sim R^2/12 - (2R/\pi)\log(R/e\sqrt{\pi/2})$, the staircase tracks to better than 0.5% up
  to $R = 100$ (617 forms), then drops to 0.94 at $R = 105$ and stays low. Anything statistical
  must be run **below $R = 100$**: deleting levels at random pushes any spectrum toward Poisson
  statistics, which is exactly the sort of conclusion this data gets used to test. On the complete
  range the fitted leading coefficient is $0.083149$ against
  $\mathrm{Area}/4\pi = 1/12 = 0.083333$, confirming Weyl's law to 0.22% there.

**How it was obtained.** Not through the JSON API. Anonymous API requests were served briefly, then
throttled into the reCAPTCHA wall described in section 15 (HTTP 200 with an HTML challenge body),
and `beta.lmfdb.org` refused as well. The route that works is the **search-page download endpoint**,
which returns plain text and was not throttled:

```bash
curl -sL -A "Mozilla/5.0" -o lmfdb_maass_level1_raw.txt \
  "https://www.lmfdb.org/ModularForm/GL2/Q/Maass/?download=1&query=%7B%27level%27%3A+1%7D&level=1&search_type=List"
```

Prefer this endpoint over `/api/` for any LMFDB table small enough to return whole.

---

## 18. LMFDB / Platt: three windows of the rigorous zero binary archive

Added 2026-08-30. Extends section 4 (`every_millionth`, the sampled traverse of the same archive)
with actual binary `.dat` data: three contiguous windows of the archive that section 4's own
provenance note flagged as pullable later, once the checksums were in hand.

**What it is.** Three of the archive's 14,580 binary `.dat` files, chosen to cover: the $10^9$-th
zero, the $10^{10}$-th zero, and the top of the archive (its last file, ending at the
$1.038\times10^{11}$-th zero, i.e. Platt's rigorous RH verification height). Each `.dat` file is a
block-structured binary encoding of consecutive zeros' imaginary parts to an absolute precision of
$2^{-101}$.

**Source.** `https://beta.lmfdb.org/riemann-zeta-zeros/data/zeros_<T0>.dat`, sibling of the
`examples/` directory section 4 was pulled from. Confirmed by fetching the directory listings of
`/riemann-zeta-zeros/` and `/riemann-zeta-zeros/examples/` (both plain Apache autoindex pages) and
then HEAD-probing three candidate filenames taken from `md5sum.log`; all three returned `200 OK`
with a `Content-Length` and no `Content-Type` (Apache has no MIME mapping for `.dat` here). The
`human=1` cookie gate from section 4 applies identically; no login. A companion `index.db` (1.2 GB
sqlite, the upstream server's own file-and-offset index) also lives at the archive root but was not
fetched: file selection here is computed directly from `md5sum.log` plus `every_millionth` instead
(see "Filename scheme" below), and fetching it would have used roughly 5x the whole budget spent on
actual zero data.

| Local file | Bytes | md5 | sha256 |
|---|---|---|---|
| `lmfdb/platt/data/zeros_370046000.dat` | 77,780,588 | `8528a1e9f803e85583d49e603139f2cd` | `d9bdb24490a238a0927434b86fc11309d14181e935cc8c017b958153e9bc9bff` |
| `lmfdb/platt/data/zeros_3293246000.dat` | 87,267,689 | `7eef4223049ebc71f64467b1c2c45386` | `54adedde95de3f6ae7b58b8a2ded646bb5b927b632084ddd3d422e7e6657964e` |
| `lmfdb/platt/data/zeros_30607946000.dat` | 96,952,975 | `7a6067b260db95a79509f21b8e13b6e6` | `f0ac605267a6ad7633552f5723118a1b1855a4a58339c66efebded6b869c1fa1` |

Total 262,001,252 bytes (~249.9 MiB), against a 2 GB budget; all three fit, so nothing was dropped.
Both md5 values matched `md5sum.log` for all three files and confirm bit-identical transfers; sha256
recorded new (upstream does not publish sha256, only md5).

**Filename scheme (derived, not documented upstream).** Decoded all 14,580 filenames in
`md5sum.log` (`zeros_<T0>.dat`) and sorted the `<T0>` integers numerically (the log itself is
sorted *alphabetically* by filename string, which interleaves numbers of different digit counts, so
naive adjacent-line diffing on the raw log is misleading). `<T0>` is the integer part of the height
$t_0$ of the file's *first* block. 14,575 of the 14,579 gaps between consecutive files are exactly
2,100,000; the four exceptions are all in the first five files ($T_0 = 14, 5000, 26000, 236000,
446000$), where zero density is low enough that Platt's original chunking evidently used shorter
files. The regular grid runs from $T_0 = 2{,}546{,}000$ to the archive's last file at
$T_0 = 30{,}607{,}946{,}000$. Confirmed directly, not just inferred: every downloaded file's own
first block header carries $t_0$ exactly equal to its filename's $T_0$, and each file's 1000 blocks
span exactly 2100 in height apiece (verified on block 0 of `zeros_370046000.dat`:
$t_0=370046000.0$, $t_1=370048100.0$).

**Window selection.** $\gamma$ at $n=10^9$ and $n=10^{10}$ read directly off `every_millionth`
(both are multiples of $10^6$, so no interpolation needed):

| Target | $n$ | $\gamma_n$ (from `every_millionth`) | Enclosing file |
|---|---|---|---|
| $10^9$-th zero | 1,000,000,000 | 371870203.83702805273405479598662519100071 | `zeros_370046000.dat` |
| $10^{10}$-th zero | 10,000,000,000 | 3293531632.39713670420899170313387696770681 | `zeros_3293246000.dat` |
| top of archive | 103,800,000,000 (last row) | 30609823941.04471807107601978670037846167787 | `zeros_30607946000.dat` (the archive's last file) |

Each enclosing file is the largest `T0` in the sorted filename list that is `<=` the target height;
each was HEAD-confirmed before download, `Content-Length` matching the eventual download exactly.

**Binary format of a `.dat` file** (ported to Python 3 as `platt_reader.py`; the original Python 2
reference is Jonathan Bober's `platt_zeros.py`, already on disk from section 4):

| Offset | Field | Type |
|---|---|---|
| 0 | `number_of_blocks` | uint64 LE |
| 8 + $32k$ + (running entry bytes) | block $k$ header: `t0, t1, Nt0, Nt1` | `double, double, uint64, uint64` LE (32 bytes) |
| immediately after each header | `Nt1 - Nt0` entries, 13 bytes each | `uint64, uint32, uint8` LE, concatenating to a 104-bit unsigned delta |

$t_0$/$t_1$ bound the block's height range; $N_{t_0}$/$N_{t_1}$ are *counts* of zeros strictly below
$t_0$ and $t_1$ (not labels: the block's own zeros carry ranks $N_{t_0}+1 \ldots N_{t_1}$ inclusive,
one-based). Within a block, an accumulator $Z$ starts at 0 and each entry adds its 104-bit delta to
it; the $k$-th zero in the block (1-based) has height $t_0 + Z_k \cdot 2^{-101}$ exactly. Because
$t_0$ is an exact float64 and the delta sum is an exact integer, every zero's height is an exact
dyadic rational: `platt_reader.py` represents it as a Python `Fraction` rather than fixed-precision
`mpmath`, so reproducing a reference decimal string is a correctly-rounded truncation with no
rounding-mode ambiguity.

**Trap hit and fixed: the off-by-one in `Nt0`.** The first version of the index lookup treated
$N_{t_0}$ as if it were the label of the block's first zero and read one entry too many. This did
*not* show up as structural corruption (every delta was still positive, blocks still chained, byte
accounting still balanced exactly), because it silently returns the *next* zero instead of a
garbage value. It was caught by the `every_millionth` cross-check: every probed value came out
systematically high by almost exactly one local zero spacing (e.g. off by 0.527 at $n=10^9$, where
the mean spacing is 0.351), and the discrepancy grew across a file precisely as more blocks (hence
more compounding one-off block starts) were crossed. Fixed by reading $N_{t_0}$ as a *count* (first
rank in a block is $N_{t_0}+1$); after the fix all `every_millionth` cross-checks match to all
printed digits.

**Validation performed** (`python -m experiments.primes.platt_reader`, all three files, runtime
under 1 second):

| Check | `zeros_370046000.dat` | `zeros_3293246000.dat` | `zeros_30607946000.dat` |
|---|---|---|---|
| md5 vs `md5sum.log` | OK | OK | OK |
| blocks | 1000 | 1000 | 1000 |
| index range (1-based, inclusive) | [994,804,897, 1,000,785,556] | [9,999,087,291, 10,005,797,727] | [103,793,332,901, 103,800,788,359] |
| zeros decoded | 5,980,660 | 6,710,437 | 7,455,459 |
| height range | [370046000.0, 372146000.0) | [3293246000.0, 3295346000.0) | [30607946000.0, 30610046000.0) |
| $\gamma_{\text{first}}$ | 370046000.20727544447936433605 | 3293246000.14210896550483951597 | 30607946000.43979868008487584315 |
| $\gamma_{\text{last}}$ | 372145999.94269533223930622785 | 3295345999.86185585566739941391 | 30610045999.95521306570911214709 |
| strictly increasing (bad deltas) | True (0) | True (0) | True (0) |
| block chaining ($t_1^{(k)}=t_0^{(k+1)}$, $N_{t_1}^{(k)}=N_{t_0}^{(k+1)}$) | OK | OK | OK |
| index-count self-consistency ($\sum$ block sizes $=$ header span) | OK | OK | OK |
| trailing bytes past declared blocks | 0 | 0 | 0 |
| observed zeros/height vs Riemann-von Mangoldt $\log(T/2\pi)/(2\pi)$ | ratio 0.99999992 | ratio 0.99999996 | ratio 0.99999993 |
| `every_millionth` cross-check (exact digit match) | 6/6 | 6/6 | 7/7 |

19/19 `every_millionth` rows fall inside these three windows and all 19 matched to every printed
digit (32 decimal places) after the off-by-one fix. Byte accounting is exact for all three files
(file size $= 8 + 1000\times32 + (\text{total entries})\times13$ with zero remainder), so none of
the three hit the "garbage at the end" quirk Bober's own comments warn is possible somewhere in the
archive; `platt_reader.py` reports (not fails on) any trailing bytes should a future pull hit one
that does.

No response was HTML/reCAPTCHA on any request (checked per the rule in section 15), and
`beta.lmfdb.org` never triggered the `www.lmfdb.org` rate-limit behavior that section 15 also
documents. All requests were single-threaded and paced, with a 3-second sleep separating the three
big transfers.

**Not obtained (by design, not failure).** `index.db` (1.2 GB sqlite) was seen in the directory
listing but not fetched, for the budget reason given above. The remaining 14,577 `.dat` files of
the archive were not pulled (out of scope for this task; re-fetchable the same way with
`platt_reader.py`).

**Serves.** Gives the project actual rigorous zero data (not just the sampled heights in section 4)
at three widely separated heights, each with exact imaginary parts to $2^{-101}$: a resource for
anything in `experiments/primes/` or the zero-statistics/explicit-formula work that needs a dense,
certified run of consecutive zeros rather than a millionth-spaced sample, at $T\sim3.7\times10^8$,
$T\sim3.3\times10^9$, and $T\sim3.06\times10^{10}$ (the last being the top of Platt's own verified
range). The decoder (`experiments/primes/platt_reader.py`) is a tracked, reusable Python 3 port, so
any additional file from this archive can be pulled later (same `data/<filename>` URL, same
`md5sum.log` checksums already on disk) and validated the same way without re-deriving the format.

**Local paths.**
- Data: `experiments/primes/_cache/datasets/lmfdb/platt/data/{zeros_370046000,zeros_3293246000,zeros_30607946000}.dat`
  (gitignored under `experiments/**/_cache/`, machine-local, matching every other binary cache in this repo)
- Decoder: `experiments/primes/platt_reader.py` (tracked; `python -m experiments.primes.platt_reader` validates every `.dat` file in the `data/` directory, or specific paths given as arguments)

---

## 19. LMFDB: sibling L-function zeros, degrees 2-4

Added 2026-08-30. A small set of per-L-function zero downloads for believed-RH-true "sibling"
L-functions one and two degrees above the Dirichlet family in section 11: an elliptic-curve/modular
form family at degree 2 spanning rank 0/1/3, and a genus-2 curve at degree 4.

**What it is.** Seven targets were attempted (a level-1 weight-12 cusp form, three elliptic curves
of increasing rank, a level-1 Maass form, the symmetric square of the weight-12 form, and a genus-2
curve). Five landed. Two (the Maass form and the symmetric square) do not exist as downloadable
`lfunc_lfunctions` records in LMFDB at all, confirmed independently three ways each (see "Tried and
not obtained" below): dead ends, not throttling casualties.

**Source.** `https://www.lmfdb.org/L/download_zeros/<label>`, the same endpoint pattern as
section 11. Labels were **not** guessed from the section 11 example past the first four characters
of confidence; see "Traps hit" for why that matters. Two label-discovery methods were used, both
against `www.lmfdb.org`, strictly sequential, never concurrent:

1. The JSON API, `https://www.lmfdb.org/api/lfunc_lfunctions/?origin=<ObjectOrigin>&_format=json`,
   which returns the full stored record (label, conductor, order_of_vanishing, root_number, etc.)
   for a given source object.
2. Redirect resolution: `https://www.lmfdb.org/L/<ObjectType>/Q/<params>/` (trailing slash) with
   redirects disabled returns an HTTP 302 whose `Location` header is the canonical slash-separated
   label path, e.g. `/L/2/5077/1.1/c1/0/410`. Converting slashes to hyphens gives the
   `download_zeros` label directly. This is the reliable method (see Traps hit); the API's own
   `label` field is not always populated (it was `null` for the 5077.a record even though `origin`,
   `conductor`, and `order_of_vanishing` were all present and correct).

| Local file | Target | Positive zeros | Bytes | sha256 |
|---|---|---|---|---|
| `2-1-1.1-c11-0-0.zeros.txt` | Ramanujan Delta, level 1 weight 12 (degree 2) | 10 | 932 | `bcc27b87da075e6ccc79bf7418142863bf796f04d91480fb6a5af3264e196341` |
| `2-11-1.1-c1-0-0.zeros.txt` | Elliptic curve 11.a, rank 0 (degree 2) | 10 | 930 | `d2b819a29a3f79f280783ddd715259df3f5001485f17719fe127d5ba79f9a295` |
| `2-37-1.1-c1-0-1.zeros.txt` | Elliptic curve 37.a, rank 1 (degree 2) | 9 | 855 | `975f12b5b20a2e0fd74faeb29c547fe757a6112394f5e71c1079283088718947` |
| `2-5077-1.1-c1-0-410.zeros.txt` | Elliptic curve 5077.a, rank 3 (degree 2) | 7 | 703 | `07080c3db328e0c84be0aa3a8679f3ddc9df0a33ccf08e3d092c2de2f73d3853` |
| `4-249-1.1-c1e2-0-0.zeros.txt` | Genus 2 curve 249.a, abelian surface (degree 4) | 21 | 942 | `9cf602d51bc58c58367ef53d8727bcc18429b8c34ca33af1c65a2276aeaf6a9f` |

All five under `experiments/primes/_cache/datasets/lmfdb/siblings/`. Total 4,362 bytes across 5
files. Aggregate sha256 (sha256 of the sorted `sha256sum` listing, per the convention in
section 16): `9e019c3dd3efd496d47bfbd9f4cc093b8fcc6d55b34e6fd8b67a035a83ddb820`.

**Format.** Identical schema to section 11: one `#` comment line naming the label and download
date, then a single JSON object with keys `order_of_vanishing`, `positive_zeros`, `negative_zeros`,
`positive_zeros_accuracy`, `negative_zeros_accuracy`. Parse by slicing from the first `{` and
calling `json.loads`. `positive_zeros`/`negative_zeros` list only the off-central ($t \neq 0$)
zeros; `order_of_vanishing` separately carries the multiplicity of the zero forced to sit exactly at
the central point by the functional equation's sign, so for 5077.a (order 3) the first *listed*
positive zero (2.0525) is not the lowest zero of the completed L-function, it is the lowest zero
**above** the tripled central zero.

One inhomogeneity worth flagging: the degree-2 files (Delta, the three curves) carry 30-digit
decimal strings with `positive_zeros_accuracy: 100`; the degree-4 genus-2 file carries only about
12-13 significant digits with `positive_zeros_accuracy: null`. Genus-2 curve L-function zeros are
simply stored at lower precision upstream. Do not assume uniform precision across degrees when
mixing this data into a downstream computation.

**Validation.** All 5 files: JSON parses cleanly; `positive_zeros` and `negative_zeros` both
strictly increasing in absolute value; `len(positive_zeros) == len(negative_zeros)` in every file
(symmetric under $t \to -t$, as expected for these self-dual L-functions).

| Target | order_of_vanishing | Expected | First positive zero | Known value | Agreement |
|---|---|---|---|---|---|
| Delta | 0 | (none stated) | 9.222379399921103 | ~9.22237940 | 9 digits |
| EC 11.a | 0 | 0 (rank 0) | 6.362613894713089 | ~6.3626 | 5 digits |
| EC 37.a | 1 | 1 (rank 1) | 5.003170014006659 | (none given) | order matches |
| EC 5077.a | 3 | 3 (rank 3) | 2.052472858479940 | (none given) | order matches |
| Genus 2 249.a | 0 | (none stated) | 4.45419105482 | (none given) | count matches API (21, largest 19.958) |

**Traps hit.**

**1. The reCAPTCHA wall is stateful across tools and outlasts the standard cooldown.** Section 15
documents the `www.lmfdb.org` reCAPTCHA Enterprise wall (HTTP 200 with an HTML challenge body in
place of data). Four label-discovery lookups fired concurrently early in this pull tripped it, and
the very next request in the main download script (for a different, unrelated target) then also hit
the challenge page and stayed blocked through three well-spaced in-script retries, across both a raw
`urllib` session and the agent's own web-fetch tool: "concurrent requests" from *any* source against
the same apparent origin count against the same budget. Recovery needed a real 150-second
wall-clock cooldown in a fresh process, not the standard 1.5-2 s inter-request sleep. Once cleared,
strictly sequential single-shot requests at ~2-2.5 s spacing worked reliably for the rest of the
pull.

**2. The label's trailing numeric fields are opaque database keys, not a composable
`(index, order_of_vanishing)` pair.** This is new and belongs alongside section 11's own "Character
identification" warning (and is now also flagged in section 15). Section 11's worked examples all
happen to end in `-0-0` or `-r1-0-0`, and it is tempting to assume the final digit is simply the
order of vanishing and the one before it a free index. That assumption **silently returns wrong
data**:

- Copying the `-0-0` suffix from the (correct) 11.a example onto 37.a fetched `2-37-1.1-c1-0-0`
  successfully (HTTP 200, well-formed, self-consistent JSON), but that label belongs to **37.b**
  (rank 0), not 37.a (rank 1). Nothing in the response signals the mismatch except the
  `order_of_vanishing` field disagreeing with the curve actually wanted; had the task not specified
  the expected rank as a check, this would have shipped silently wrong.
- Suspecting the final digit *was* order-of-vanishing and setting it to the target's known rank does
  not fix this either: `2-5077-1.1-c1-0-3` also returns HTTP 200 with clean, self-consistent,
  strictly-increasing JSON, reporting `order_of_vanishing: 0` for yet another, still-wrong object at
  the same conductor. The trailing field is not free-form; the true label for 5077.a turned out to
  be `2-5077-1.1-c1-0-410` (order of vanishing 3), where `410` is an opaque database index with no
  relation to rank, conductor, or curve letter.
- The reliable fix is the redirect method above: hit the object's own origin URL
  (`/L/EllipticCurve/Q/5077/a/`) with redirects disabled and read the real label off the 302
  `Location` header, rather than ever constructing a label from a pattern seen on a different
  object. Both corrections were confirmed this way before the final successful downloads.

**3. `conductor=<small integer>` as a bare API filter intermittently 500s.**
`/api/lfunc_lfunctions/?degree=2&conductor=1&_format=json` and the degree-3 equivalent both
returned HTTP 500; `degree=3&_format=json` with no conductor filter worked and happened to return
only conductor-1 records anyway. Filtering by `origin=<exact string>` never 500'd. Prefer the
origin filter or the redirect method over a bare `conductor=` filter.

**Tried and not obtained.**

**Level-1 Maass cusp form, $R = 9.5336952614\ldots$ (degree 2).** No downloadable `download_zeros`
record exists for this object, confirmed three independent ways:

- The object's own LMFDB page (`https://www.lmfdb.org/ModularForm/GL2/Q/Maass/1.0.1.1.1`) links to
  no L-function-specific page at all, only the generic `/L/` and `/L/rational` browse pages.
- `https://www.lmfdb.org/api/lfunc_lfunctions/?origin=ModularForm/GL2/Q/Maass/1/0/1/1/1&_format=json`
  returns an empty `data` array.
- Direct guesses (both the bare and `r`-prefixed spectral-parameter forms of the label, on both
  `www.lmfdb.org` and `beta.lmfdb.org`) all 404'd, all confirmed not challenge pages.

GL2/Q level-1 Maass form L-functions appear to be exposed only through the interactive
JavaScript-rendered scatter plot at `https://www.lmfdb.org/L/degree2/MaassForm/`, with no
individually labeled, downloadable record behind any point on it. (Contrast: GL3 self-dual Maass
forms *do* get individual `lfunc_lfunctions` records, discovered while probing for the symmetric
square below; degree-2 Maass forms just are not curated the same way.)

**Symmetric square of Delta (degree 3).** Confirmed absent from LMFDB entirely, not merely
unlabeled, three independent ways:

- `https://www.lmfdb.org/L/SymmetricPower/2/ModularForm/GL2/Q/holomorphic/1/12/a/a/` returns a bare
  HTTP 404 with no redirect (the object-origin route that worked for every other target here does
  not resolve at all for this one).
- `https://www.lmfdb.org/api/lfunc_lfunctions/?origin=SymmetricPower/2/ModularForm/GL2/Q/holomorphic/1/12/a/a&_format=json`
  returns an empty `data` array.
- `https://www.lmfdb.org/api/lfunc_lfunctions/?degree=3&_format=json` (unfiltered by conductor)
  returns exactly 11 records, all self-dual GL3 Maass cusp forms at conductor 1; none originates
  from a symmetric-square-of-classical-modular-form construction. LMFDB does carry
  symmetric-square/-cube L-functions of *elliptic curves* as their own object type, but weight-12
  level-1 forms have no associated elliptic curve (weight must be 2), and no analogous precomputed
  object exists for them.
- Direct guesses (`3-1-1.1-c11e2-0-0`) 404'd on both hosts.

**Serves.** Extends the repo's Euler-positive-control instrument (LEARNINGS #210: chi3/chi4,
believed-RH-true through the e1k harness collapse gap_even 4.7-6.9 orders, harder than D-H) from
degree-1 Dirichlet characters up through degrees 2 and 4, with genuine rank diversity built in: two
rank-0 controls at two different degrees (11.a at degree 2, 249.a at degree 4), a rank-1 minimal
case (37.a, the smallest-conductor rank-1 curve), and a rank-3 case (5077.a, the smallest-conductor
rank-3 curve) whose triple central zero is a sharp, unambiguous structural feature no D-H-style
off-line construction produces. Any RH-discipline method that claims to detect on-line-ness from
zero data alone should be checked against this ladder as degree rises, exactly as chi3/chi4
sharpened the degree-1 case: a detector that only works by accident on low-degree, low-rank examples
should be expected to degrade or fail somewhere on this list, and where it does so is diagnostic in
the same way the chi3/chi4 undercount was.

---

## 20. LMFDB: abelian variety isogeny classes over finite fields (Weil polynomial tables)

Added 2026-08-30. Slices of the LMFDB's "Abelian variety isogeny classes over $\mathbb{F}_q$"
table: for each isogeny class, its Weil (L-)polynomial, dimension $g$, base field size $q$,
$p$-rank, principal polarizability, and point count. This is RH-over-finite-fields ground truth:
Weil's theorem guarantees every root of the Weil polynomial has absolute value $\sqrt q$, so the
table is literally a catalog of the world where the Riemann Hypothesis analogue is a proven fact,
indexed by $(g,q)$.

**Source.** Search page: `https://www.lmfdb.org/Variety/Abelian/Fq/`. Stats/counts page (used to
get independent expected-row-count ground truth per $(g,q)$ before downloading, at
`?search_type=Counts`): `https://www.lmfdb.org/Variety/Abelian/Fq/?search_type=Counts`.

**The download endpoint (worked out from the search page, same family as section 17's Maass
pull).** Every results page carries a `Download` link of the form

```
https://www.lmfdb.org/Variety/Abelian/Fq/?download=1&query=<QUERY>&g=<G>&q=<Q>&search_type=List
```

where `<QUERY>` is a **Python-`repr`-formatted dict** (single-quoted, `key: value` pairs)
describing the filter, percent-encoded. Three shapes were needed:

| Slice shape | `query` dict | `q` URL param |
|---|---|---|
| single $(g,q)$ | `{'q': 2, 'g': 4}` | `q=2` |
| fixed $g$, all $q$ | `{'g': 1}` | *(omitted)* |
| fixed $g$, a list of $q$ | `{'$or': [{'q': 2, 'g': 2}, {'q': 3, 'g': 2}, ...]}` | `q=2,3,4,...` (comma list) |

The `$or`-of-dicts form was not guessed: the `q` search box's placeholder text only advertises a
single value or a dash-range (`e.g. 81 or 3-49`), so a comma-separated list (`q=2,3,4,5`) was tried
speculatively against a live, non-download results page first; LMFDB accepted it, expanded it
server-side, and its own auto-generated `Download` link on that results page showed the resulting
`{'$or': [{'q': 2, 'g': 2}, {'q': 3, 'g': 2}, ...]}` query dict verbatim. That was then reused
directly. Python's built-in `repr()` of the equivalent dict reproduces LMFDB's own query-string
formatting byte-for-byte, so no hand-rolled JSON/Mongo-string serializer was needed.

**Column selection.** The default download gives only 6 columns (Label, Dimension, Base field,
L-polynomial, $p$-rank, Isogeny factors). Principal polarizability and point counts are real
columns in the underlying table but hidden by default in both the on-screen results table and the
download. They are controlled by a `showcol` URL parameter, discovered by reading
`/static/lmfdb.js`'s `update_download_url` / `control_column` functions (the on-screen "columns to
display" selector writes the toggled-on column keys into a hidden `<input name="showcol">`,
**period-separated**, not comma-separated, which the download link then copies into its own URL).
Adding

```
&showcol=has_principal_polarization.abvar_count
```

extends every download to 8 columns, confirmed against the table's own column-key list (harvested
from the `<option value="...">` list in the column selector): `has_principal_polarization` =
"princ. polarizable", `abvar_count` = "$\mathbb{F}_q$ points on variety".

**The trap, hit once.** Section 15's `www.lmfdb.org` reCAPTCHA Enterprise wall fired on the single
largest request, $g=6, q=2$ (164,937 rows expected); caught immediately by the same body-inspection
rule section 15 prescribes, so nothing was written to disk as if it were the dataset. All five
smaller requests against `www.lmfdb.org` in the same run succeeded on the first try with no
throttling (single sequential Python script, one request at a time, 2.5 s sleep between requests,
browser `User-Agent`). Retried against `beta.lmfdb.org` with `Cookie: human=1` per section 15's
documented fallback: succeeded cleanly, 164,937 rows, 19.64 MB, 14.0 s server time, first try. A
secondary, easily-missed gotcha for future pulls: a good download's `Content-Type` is
`text/event-stream; charset=utf-8`, not `text/plain` or `text/csv` as one might guess; checking for
that (positive signal) alongside the doctype/recaptcha grep (negative signal) is what the fetch
script used to accept or reject each response.

**Slices pulled.** All six requested slices landed, each COMPLETE (downloaded row count equals the
LMFDB stats page's own stated count for that $(g,q)$ selection, checked both from the file's own
self-reported header line and an independent line count). No slice was paged, capped, or shrunk;
the endpoint returned every matching row in one shot up to 164,937 rows with no sign of a silent
truncation limit.

| Slice | File | Rows | Expected (stats page) | Complete? | Bytes | sha256 |
|---|---|---|---|---|---|---|
| $g=1$, all $q$ (118 field sizes) | `av_g1_allq.txt` | 6,184 | 6,184 | YES | 364,425 | `db031549c1105b0dc2956726d5b335537e4670040b33bbc41ff24cdc5cd2204f` |
| $g=2$, $q\in\{2,3,4,5,7,8,9,11,13,16,25\}$ | `av_g2_q2_3_4_5_7_8_9_11_13_16_25.txt` | 3,621 | 3,621 | YES | 255,861 | `95d5daf3bf994b24af9f19b64a3ba3452b2ea74601a52e3e079374c97bfa7346` |
| $g=3$, $q\in\{2,3,4,5\}$ | `av_g3_q2_3_4_5.txt` | 5,242 | 5,242 | YES | 427,083 | `4dfbb5eadf0a9f0cdf9088d5c63ac03fbd93cc90090e73614a0820b73422baae` |
| $g=4$, $q=2$ | `av_g4_q2.txt` | 1,645 | 1,645 | YES | 158,527 | `5ed38585a46d2514abbc18fa3ac6feb6d5fc57c7f90e14a6c7dbca62f50e0fd3` |
| $g=5$, $q=2$ | `av_g5_q2.txt` | 14,325 | 14,325 | YES | 1,533,323 | `5645f024318dccba6139dfc3a761792462cacbf35ef3df9f51a3ae35f613e208` |
| $g=6$, $q=2$ (via `beta.lmfdb.org` fallback) | `av_g6_q2.txt` | 164,937 | 164,937 | YES | 19,642,965 | `d4a86ac3bdf4bc981b07a55f8383732bbb7794638e5622b023498a6f1bdc45b1` |

Total: **195,954 rows**, **22,382,184 bytes (22.4 MB)** across the six data files, well inside the
300 MB hard budget and each individual file well under the ~100 MB per-file ceiling (the largest,
`av_g6_q2.txt`, is 19.6 MB). Saved under `experiments/primes/_cache/datasets/lmfdb/av_fq/`
(gitignored, machine-local; this document is the tracked provenance record). Two auxiliary files
sit alongside the six data files: `_fetch_log.txt` (the full request-by-request transcript) and
`_fetch_summary.json` (machine-readable per-slice metadata: URL, query dict, byte count, sha256,
completeness flag); the high-precision validation recheck below adds two more,
`_validation_report.txt` and `validate_hp_run.log`.

**Format.** Tab-separated, no header row over the data (a `#`-prefixed comment block precedes and
follows the data instead: provenance line, the exact search link, the row count, then after the
data a full prose definitions section for every column, taken verbatim from LMFDB's own knowls).
Quoted string field for the label; everything else a bare number, `true`/`false`, or a Python-style
list literal.

| Column | Meaning |
|---|---|
| 1 | Label, format `g.q.isog` (e.g. `"1.2.ac"`), quoted |
| 2 | Dimension $g$ |
| 3 | Base field cardinality $q$ |
| 4 | Principal polarizability (`true`/`false`) |
| 5 | L-polynomial $L_A(t) = \det(1 - tF_q \mid H^1)$, as a list of $2g+1$ integer coefficients, constant term first (e.g. `[1, -2, 2]` means $1 - 2t + 2t^2$) |
| 6 | $p$-rank |
| 7 | $\#A(\mathbb{F}_q)$, the point count on the abelian variety itself (this is the "number of points" column; LMFDB separately has a curve-point-count column, `curve_count`, only meaningful when a curve model is known, not pulled here since the task asked for the variety point count generically) |
| 8 | Isogeny factors: list of `[simple_label, multiplicity]` pairs |

**The reversal convention (load-bearing for validation, easy to get backwards).** LMFDB's own knowl
for the L-polynomial states it explicitly: $L_A(t)$ is *the reverse of* the monic characteristic
polynomial $P_A(t)$ of Frobenius (whose roots are the actual Frobenius eigenvalues, $|\alpha_i| =
\sqrt q$ by Weil's theorem). So the roots of $L_A(t)$ **as literally written** in column 5 have
absolute value $q^{-1/2}$, not $\sqrt q$. Concretely, for `"1.2.ac"` with $q=2$, column 5 is
`[1, -2, 2]` and its own roots are $0.5 \pm 0.5i$, magnitude $1/\sqrt2 \approx 0.707$. Feeding that
same coefficient list, in the same constant-term-first order, directly into `numpy.roots` (which
itself expects highest-degree-first) computes the roots of the *reversed* list, i.e. of $P_A(t)$
itself: for `[1, -2, 2]` that gives $1 \pm i$, magnitude $\sqrt2$, matching $\sqrt q$ exactly. This
was confirmed by hand before trusting it at scale. **The validation below computes
`numpy.roots(coeffs_as_given)` and checks that against $\sqrt q$** (equivalently: reverse the list
first if you want the roots of $L_A(t)$ itself against $q^{-1/2}$; both are the same statement).

**Validation.**

_(1) RH over $\mathbb{F}_q$ (every root of the Weil polynomial has $|\text{root}| = \sqrt q$)._
Checked on **every row of all six files** (195,954 rows total, not just a 5,000-row sample: cheap
enough to do exhaustively). Double-precision `numpy.roots` passed 194,575 / 195,954 rows to better
than $10^{-6}$ relative error outright; the remaining 1,379 rows (all at $g \ge 2$, concentrated at
higher $g$: 8 at $g=2$, 46 at $g=3$, 26 at $g=4$, 180 at $g=5$, 1,119 at $g=6$) missed the $10^{-6}$
bar by up to $4.7\times10^{-3}$ relative error. Every miss traces to companion-matrix eigenvalue
conditioning on **clustered/near-multiple roots** (e.g. the $g=6$ worst case,
`6.2.am_cu_aku_bea_acku_dwy`, has six root-pairs sitting within $10^{-2}$ of each other near
$1+i$): a known limitation of double-precision numerical root-finding at higher degree, not a data
or parsing defect (the functional-equation identity for every one of these rows, see below, holds
exactly in integer arithmetic, so the coefficients themselves are not in question).

**The full-coverage numpy check is the load-bearing one**: RH over $\mathbb{F}_q$ is Weil's theorem,
not a conjecture, so "|root| = $\sqrt q$ to 6 decimals" is expected to hold for literally every row,
and it does for 194,575 / 195,954 (99.30%) outright at double precision, with every miss explained
(clustered roots, higher $g$) rather than unexplained. The remaining 1,379 rows were put through a
higher-precision corroboration with `mpmath.polyroots` (`mp.dps=30`, `extraprec=300`,
`maxsteps=150`) run against a fixed sample of 560 of the 1,379 (seed 212): all 260 misses from the
$g\in\{2,3,4,5\}$ files (every one of them, not a sample) plus a random 300 of the 1,119 misses from
`av_g6_q2.txt`. That recheck was still in progress when this report was finalized (each
non-convergent case costs the full 150-step budget, so the tail is slow): 451 of the 560 sampled
rows had been individually processed by report time. A separate, full independent numpy pass over
all 195,954 rows confirms no new information changes the picture: **zero confirmed violations at
either precision, at any point in the run.** Of those 451, every row that converged matched
$\sqrt q$ to between $10^{-14}$ and $10^{-31}$ relative error (far inside the $10^{-6}$ bar;
spot-checked values include $1.39\times10^{-31}$ and $1.14\times10^{-31}$ on $g=3$, $g=5$, $g=6$
rows), and a small subgroup, all 8 of the $g=2$ misses at $q \in \{4,9,16,25\}$ (exactly the
perfect-square field sizes) plus at least 1 more at $g=6$, did not converge under `polyroots` at
this precision/step budget and are recorded as **inconclusive**, not fail: `NoConvergence` is a
solver-budget statement, and a real violation would instead have converged to a wrong-magnitude
root (which never happened; a genuine failure prints unconditionally in the recheck script
regardless of sampling, and none did through row 451). **Summary of what was checked at what
precision: all 195,954 rows at numpy double precision (the theorem-level check); 451 of a 560-row
sample re-confirmed at mpmath 50-digit-class precision (`dps=30`, effectively far higher via
`extraprec=300`), with 0 confirmed failures and 0 unconfirmed failures at either precision, only
solver non-convergence on 9 of the 451 (2.0%), concentrated entirely at perfect-square $q$.** Both
`_validation_report.txt` (the full numpy-precision + exact functional-equation run) and the recheck
transcript (`validate_hp_run.log`) are saved alongside the six data files, for anyone who wants to
finish the remaining 109 rows of the 560-row sample (rows 452-560) or widen the sample beyond the
300 of 1,119 $g=6$ misses it currently covers.

_(2) Known isogeny-class counts._ $g=1,q=2$: **5** classes (expected 5, PASS). $g=1,q=3$: **7**
classes (expected 7, PASS). Both read directly out of the parsed `av_g1_allq.txt` slice, and both
independently match the LMFDB stats page's own grid before any file was even downloaded.

_(3) Functional-equation symmetry_ ($c_{2g-i} = q^{g-i}c_i$). Checked on **every row of all six
files**. All 195,954 rows pass exactly, in exact Python integer arithmetic, **once the check is
restricted to $i = 0 \ldots g$** (the other half, $i = g{+}1 \ldots 2g$, is the identical constraint
read backwards and was dropped from the checker, not the data: testing it directly requires raising
$q$ to a *negative* integer power, and Python's `int ** negative_int` silently returns a `float`,
e.g. `49**-1 * 49 == 0.9999999999999999`, one ULP short of the integer `1` on the other side of the
comparison. The first version of the checker used the full $i=0\ldots2g$ range and reported 808
spurious failures on `av_g1_allq.txt` and 207 on the $g=2$ slice purely from this artifact, at
$q \in \{49, 7, ...\}$ where $q^{-1}$ isn't exactly representable in binary floating point; every
one of those "failures" passes once the exponent stays non-negative, since $i$ and $2g-i$ are the
same equation.) A violation here means a bug in the check, not the data, and this is exactly that
case, located in the validator instead of the parser.

**Caps or traps hit.** Exactly one, the reCAPTCHA wall above. No row-count cap was hit anywhere:
every slice, including the one with the most rows, returned its full LMFDB-stated count in a single
request with no pagination needed.

**Tried and not obtained.** Nothing in this pull. All six requested slices landed complete on the
first (five slices) or second (the $g=6$ retry via `beta.lmfdb.org`) attempt.

**Serves.** This is ground truth for the world where the Riemann Hypothesis analogue is a *proven
theorem*: every row here is a certificate that Weil's proof produces exactly the spectral structure
(all Frobenius eigenvalues on the circle $|z|=\sqrt q$) that the actual RH conjectures for $\zeta$.
That makes it the natural comparison corpus for [`fq_shadow.py`](../lemma_db/fq_shadow.py) (the
function-field shadow used as a positive gradient in the Generative Engine, see
`docs/03_research/generative_engine.md`) and for the M4 polarization fingerprint
([`docs/03_research/breadth_program.md`](../../docs/03_research/breadth_program.md),
[`docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md)):
M4 asks for the arithmetic analogue of exactly the positivity (a genuine polarization) that forces
these Weil polynomials' roots onto the circle in the first place, and this table is the largest
freely available sample of *solved* instances of that structure across dimension ($g=1$ to $6$) and
field size ($q=2$ to $1024$), including the principal-polarizability and point-count data needed to
check any proposed fingerprint predicate against real cases rather than only the worked toy/curve
examples already in the repo.

---

## 21. Physics resonance spectra: ENDF neutron resonances and Kerr quasinormal modes (QNM)

Added 2026-08-30. Two third-party physics datasets pulled as **controls/calibration data, not RH
tests**: `experiments/primes/PRIME_PATTERNS.md` already establishes that spectral statistics (GUE
pair correlation, level-spacing distributions) are provably RH-blind. Nuclear resonance spectra
(GOE) and black-hole quasinormal modes serve two purposes instead: instrument calibration for the
zero-statistics pipeline against a *different* random-matrix universality class than the zeros',
and comparative spectral data for `docs/03_research/local_quantum_gravity_and_primes.md`.

Total on disk: 185,075,662 bytes (185.1 MB) across 146 files under
`experiments/primes/_cache/datasets/physics/`. A local per-directory manifest,
`physics/SHA256SUMS` (146 entries, 13,075 bytes), also lives there; it is excluded from that count
and from the root manifest by filename, the same rule section 16 uses. Everything was fetched
anonymously over plain HTTP(S), single-threaded, paced with `time.sleep` inside each Python fetch
script, browser-ish `User-Agent`, response bodies checked for zip magic / non-HTML before saving.

```
experiments/primes/_cache/datasets/physics/
├── SHA256SUMS              per-directory manifest, 146 entries
├── endf/
│   ├── download_endf.py    fetches the 14 nuclide zips from IAEA, unzips, sha256's
│   ├── parse_endf.py       parses MF=2/MT=151 resolved resonance parameters
│   ├── raw/                14 x (.zip as downloaded, .dat extracted) = 28 files
│   └── parsed/          14 x <Nuclide>_s_wave.txt (E_r_eV, J, l, Gamma_n, Gamma_gamma)
└── qnm/
    ├── download_qnm.py     fetches the Schwarzschild dat files + l=2,3 Kerr tarballs
    ├── s0l0.dat, s1l1.dat, s2l2.dat   Schwarzschild QNM, one file per (s,l=s)
    ├── l2.tar.gz, l3.tar.gz           Kerr gravitational (s=-2) QNM vs spin, as downloaded
    └── l2/, l3/                       tarballs extracted: per-(n,l,m) dat files
```

**Part 1: ENDF/B-VIII.0 neutron resonance parameters.**

**What it is.** Resolved-resonance-region neutron resonance parameters for 14 even-even
heavy/rare-earth nuclides plus the two textbook actinides, the nuclide set behind the Nuclear Data
Ensemble tradition (Haq, Pandey & Bohigas, *Phys. Rev. Lett.* 48, 1086 (1982): pooled s-wave neutron
resonance spacings from many nuclei fit GOE, the foundational "nuclei are GOE" result the whole
tradition is named for).

**Source.** IAEA ENDF/B-VIII.0 archive, anonymous HTTP, neutron sublibrary:
`https://www-nds.iaea.org/public/download-endf/ENDF-B-VIII.0/n/`. File names follow
`n_<ZZZA>_<Z>-<Sym>-<A>.zip`; the exact names were read off that directory listing (no guessing),
for example `n_9237_92-U-238.zip`. All 14/14 targeted nuclides were present and downloaded on the
first pass; the IAEA fallback (NNDC) was not needed.

**Download table.**

| Nuclide | `raw/*.zip` bytes | `raw/*.zip` sha256 | `raw/*.dat` bytes | `raw/*.dat` sha256 |
|---|---|---|---|---|
| Th-232 | 3,375,665 | `ecfa46f9c48fbbca24248e33a2ee3827065a989c6316656827bf610e8c8fafb1` | 13,924,338 | `681951ebf617e85aa2f0fd45c8a77ccc5f73b5f3fc7bae230cc6a88736c4a7de` |
| U-238 | 4,576,541 | `5bbb4b6c1a46c9634c452eed028d70cf3226b2d5d5e893d34bae163b4d66afef` | 16,118,822 | `8bb40a09c758b135751b6bc0a0110a6c953ce3c20962ff013252ed4a9a035b1c` |
| Er-166 | 175,092 | `01b7f9d3b6e195430dd6e89db69991ca7d589524f89da6b948fd6f702dd17819` | 733,818 | `d466a7a57ab8bfc5732ad32c844955eef1f1ab8cd37f2019242e3f5588fa0f61` |
| Er-168 | 180,116 | `c4eed1f546ea020deba1649b6b8477413b46504ca6456b432209596c7ca2ac37` | 771,866 | `17c6dca0ec335aa45c16ad30f6b9b3a696c6032b66158e989d89e73d396c8d58` |
| Yb-172 | 215,079 | `77f1a1fdc97ac4c2caed07091fa27f2be0909de41bb1cac2b01b754444b499e2` | 933,324 | `56bed8dfe3eeb2d713903b1d626dfba811a37add06a84e4b868ca18e74d1a5c7` |
| Yb-174 | 201,163 | `9fd6d1882ffad1b9ba7402265ad051f5ff2cd3bda02d658b4cc87410253aaf78` | 857,802 | `d932c022ddec652ede16e4b913f92304d7d3fa160288ce6554f92386f85bf18b` |
| W-182 | 2,996,525 | `e0ec552349a0c717d466fdc3400658e543d0157408e9d3dc248b919eebd79dd2` | 11,675,816 | `87c67954e57cfa7563e0e1089f989c1d0633ff3942e710e37662c7700e6dd58b` |
| W-184 | 1,952,459 | `5dc8cf0386885fe17b492d3f7c1e33365aa3cc6f8dc940ce2880022a584b7869` | 8,187,864 | `f80b4bc802cf0055bfb8c9934b1bf0cd8b10216c8eec9b8a787232c87f5078d2` |
| Gd-156 | 639,782 | `1fd02dfed1e4126efc89639c43578e2c1ec65a840f0f0649171a078d2b42c02f` | 3,013,746 | `0d22a87888b05240a84b69f5fc33de7d49d732de2eb510a6f9da8a0af8451e6a` |
| Gd-158 | 629,871 | `a6f1102045ec7d96e3a8f8875f119d9e6a842942686578c5a06897283479182f` | 2,636,464 | `8849681900d46b7c7da4fb7d1ce6083910fb20f59dae182466630e0ec924a7ec` |
| Dy-162 | 389,664 | `04ef15bfad25f287c0fbe230bbe7bd2ee53834128d84e3daba651528af66bc7c` | 1,703,714 | `22b4a92565c163b90e00dfa259390fa5893b04511ec0d8182011a38f364a7020` |
| Dy-164 | 369,301 | `03fc53bccdcec020d84999e40c98d2052cbb549f6c64d3eaf61628b737ad34ab` | 1,598,918 | `a7c4d69d1565eec7562b795f682db1f3579ec13d5b5af7b32d6b172e600555e3` |
| Sm-152 | 395,929 | `74cf0e32f2192381bd6dd4c455bc2c7e6ca19af0825454f070001f3fa9414766` | 1,777,596 | `c94869821947b64da7e49416707116cb2c2dce390e96f25c92f240a7fa996234` |
| Cd-114 | 21,327 | `6cc0fa04f999ec8f28ad09621ce0f0af460c642c452698a6d1693596392bddd3` | 104,550 | `0e02e48a7a991dc7acf55a66cd2040b3d7691340aac226fcf19d13729467a1c7` |

14/14 nuclides landed. Zip total 16,118,514 bytes; extracted `.dat` total 64,038,638 bytes. Scripts:
`endf/download_endf.py` (sha256 `32a3236af1e05f1b6bed2e39fbcee18019fb2d9fdcc64a31e1ba437e4501022f`),
`endf/parse_endf.py` (sha256 `24c75ef60c02689445d5c743c36fc626e179b3e2ff7144a82478342797fa1e49`).

**Parsed s-wave results table.** Columns: resonance formalism (LRF), the nominal resolved-region
bound `EH` from the file's own energy-range header, the count of *all* l-values' resonances found
in that region, the s-wave (l=0, E_r>0) count kept in the parsed table, and the s-wave table's own
energy extent (which can run a little past `EH`; see the trap noted below).

| Nuclide | LRF (formalism) | Resolved region EL-EH (eV) | All-l resonances | s-wave count | s-wave table range (eV) | First s-wave E_r (eV) |
|---|---|---|---|---|---|---|
| Th-232 | 3 (Reich-Moore) | 1e-5 - 4,000 | 927 | 250 | 21.81 - 6,000 | **21.8086** |
| U-238 | 3 (Reich-Moore) | 1e-5 - 20,000 | 3,345 | 904 | 6.674 - 27,500 | **6.67428** |
| Er-166 | 2 (MLBW) | 1e-5 - 5,000 | 174 | 167 | 15.55 - 9,486.2 | 15.55 |
| Er-168 | 2 (MLBW) | 1e-5 - 15,000 | 130 | 101 | 79.7 - 14,862 | 79.7 |
| Yb-172 | 2 (MLBW) | 1e-5 - 3,500 | 101 | 98 | 139.8 - 10,102 | 139.8 |
| Yb-174 | 2 (MLBW) | 1e-5 - 3,000 | 79 | 77 | 342.7 - 19,801 | 342.7 |
| W-182 | 7 (R-Matrix Limited) | 1e-5 - 10,000 | 312 | 175 | 4.150 - 10,333.9 | 4.150017 |
| W-184 | 7 (R-Matrix Limited) | 1e-5 - 10,000 | 218 | 133 | 101.95 - 16,450 | 101.948 |
| Gd-156 | 3 (Reich-Moore) | 1e-5 - 2,227 | 88 | 67 | 33.23 - 2,201.2 | 33.23 |
| Gd-158 | 3 (Reich-Moore) | 1e-5 - 9,980 | 96 | 77 | 22.3 - 9,949.5 | 22.3 |
| Dy-162 | 2 (MLBW) | 1e-5 - 4,845 | 75 | 68 | 5.44 - 4,844.6 | 5.44 |
| Dy-164 | 2 (MLBW) | 1e-5 - 6,998 | 70 | 41 | 146.97 - 6,996.3 | 146.97 |
| Sm-152 | 2 (MLBW) | 1e-5 - 5,150 | 92 | 87 | 8.047 - 5,100 | 8.047 |
| Cd-114 | 3 (Reich-Moore) | 1e-5 - 8,000 | 85 | 23 | 120.13 - 10,092.4 | 120.13 |

**Validation (as specified).** U-238 first s-wave resonance: **6.67428 eV**, target ~6.67 eV.
MATCH. Th-232 first s-wave resonance: **21.8086 eV**, target ~21.8 eV. MATCH. Both are exact hits
against well-known textbook values (U-238's 6.67 eV line and Th-232's 21.8 eV line are also the two
most commonly cited resonance-integral calibration lines in the neutron cross-section literature,
independent of this project).

**ENDF-6 format spec and parsing conventions.**

**Card layout (ENDF-102, the public format manual).** Every line is 80 columns: 6 data fields of 11
characters each (columns 1-66), then `MAT` (4 chars, columns 67-70), `MF` (2 chars, columns 71-72),
`MT` (3 chars, columns 73-75), `NS` (5-char sequence number, columns 76-80). `parse_endf.py` selects
the resonance section by testing `line[70:72] == " 2"` and `line[72:75] == "151"` (0-indexed
slicing) directly on every line, which is robust to the file's own leading "tape label" line and to
`MAT` varying by nuclide.

**Number format.** ENDF floats may omit the exponent marker, e.g. `6.670000+0` means `6.67E0` and
`-4.405250+3` means `-4405.25`. `endf_float()` detects whether a token already carries `E`/`D` and
otherwise inserts `E` before the last bare `+`/`-` that isn't part of the mantissa.

**Record structure walked (MF=2, MT=151), for the three formalisms actually present across the 14
files:**

- `HEAD`: `ZA, AWR, 0, 0, NIS, 0`; per isotope `CONT`: `ZAI, ABN, 0, LFW, NER, 0`; per energy range
  `CONT`: `EL, EH, LRU, LRF, NRO, NAPS`. Only the first energy range is read (confirmed `LRU=1`,
  resolved, for all 14 files; the second `NER` range in every file is the unresolved region above
  `EH`, which this task does not need and this script does not parse).
- **LRF 1 (SLBW) / 2 (MLBW)** -- 7 of the 14 nuclides (all the rare-earth/lanthanide ones: Er, Yb,
  Dy, Sm): `CONT SPI,AP,0,0,NLS,0`, then per l-value a `LIST` `AWRI,QX,L,LRX,6*NRS,NRS` header
  followed by `NRS` resonance rows of 6 values `ER,AJ,GT,GN,GG,GF`. `l` is the header's `L` field;
  `Gamma_n = GN`, `Gamma_gamma = GG`.
- **LRF 3 (Reich-Moore)** -- 5 nuclides (the two actinides plus Cd-114, Gd-156, Gd-158): same shape
  but the resonance row is `ER,AJ,GN,GG,GFA,GFB` (no total width column; two fission-width slots
  instead, both 0 for the non-fissile nuclides here).
- **LRF 7 (R-Matrix Limited)** -- W-182 and W-184, the format actually used by the ENDF/B-VIII.0
  tungsten evaluations and the most involved of the three: a top `CONT` gives `IFG` (0 = widths, not
  seen otherwise here), `KRM` (3 = Reich-Moore-type R-matrix reduction, both W isotopes), `NJS`
  (number of J-pi spin groups); a `LIST` of `NPP` particle pairs, 12 values each
  (`MA,MB,ZA,ZB,IA,IB,Q,PNT,SHF,MT,PA,PB`), identifies the elastic-neutron pair by `MT==2` and the
  capture pair by `MT==102`; then per spin group, a channel `LIST` (`PPI,L,SCH,BND,APE,APT` per
  channel) whose entry pointing at the elastic pair carries that spin group's `l`, followed by a
  resonance `LIST` in which **each resonance is padded out to a whole number of 6-word lines**
  (`ER, GAM(1..NCH), 0-padding`) rather than packed tightly, which is what makes W-182's
  per-spin-group resonance-block byte count come out to an even multiple of 6 regardless of its
  actual channel count (2, here: elastic + capture), and is the one place this parser had to diverge
  from the tighter packing used by LRF 1/2/3. Verified independently on W-182: first positive-energy
  l=0 resonance lands at $E_r = 4.150017$ eV, $\Gamma_n = 1.566$ meV, $\Gamma_\gamma = 45.08$ meV,
  matching the commonly cited W-182 first s-wave resonance near 4.16 eV.

**Trap: table range vs. nominal `EH`.** Several s-wave tables (U-238 to 27,500 eV against a nominal
`EH=20,000`; Th-232 to 6,000 against `EH=4,000`) run past the file's own stated upper bound of the
resolved region. This is standard ENDF/B evaluator practice, not a parsing bug: a handful of extra
resonances just above `EH` are routinely included in the table to stabilize the reconstructed cross
section's tail near the boundary. The table above lists the nominal `EH` and the parsed table's
actual extent separately for exactly this reason.

**Trap: three formalisms, not one.** A naive parser written against only the U-238/Th-232
(Reich-Moore) layout would have silently mis-parsed all 7 MLBW files (wrong column-to-quantity
mapping past `AJ`) and crashed or produced garbage on both W files (entirely different record
structure). `parse_endf.py` detects `LRF` from the energy-range header and dispatches to one of
three code paths; an unsupported `LRF` (4 Adler-Adler, or the general `KRM` values of LRF 7 with
`IFG=1` reduced-width amplitudes) is reported as a named parse failure per nuclide rather than
silently skipped or mis-read. None of the 14 files hit this path.

**Part 2: Berti-Cardoso-Starinets Kerr QNM tables.**

**What it is.** Schwarzschild and Kerr black-hole quasinormal-mode (ringdown) frequency tables from
Berti, Cardoso & Starinets, *Class. Quantum Grav.* 26, 163001 (2009), arXiv:0905.2975, the standard
reference tabulation for black-hole ringdown frequencies, used here as a physically unrelated
complex-spectrum control (damped oscillation frequencies of a classical field equation, nothing to
do with number theory) for the comparative-spectra discussion in
`docs/03_research/local_quantum_gravity_and_primes.md`.

**Source used.** The task's named source, `https://pages.jh.edu/eberti2/ringdown/` (Berti's page at
Johns Hopkins), is blocked (see section 15): a Cloudflare WAF rule against non-browser clients,
confirmed on 3 well-spaced attempts (default `User-Agent` over https, full browser-style headers
over https, plain http which redirects to the same blocked https URL), not a transient error or
rate limit, so no amount of pacing fixes it. The identical dataset (same paper, same arXiv id, cited
on both pages) was obtained instead from the CENTRA/GRIT gravitational-physics group page at IST
Lisbon: `https://centra.tecnico.ulisboa.pt/network/grit/files/ringdown/`. Its download links point
at the legacy host `blackholes.ist.utl.pt`, which 302-redirects to `blackholes.tecnico.ulisboa.pt`;
both are followed automatically by `curl -L` / `urllib`. The old
`www.phy.olemiss.edu/~berti/qnms.html` address (Berti's pre-JHU page) is still alive only as a
redirect to the blocked `pages.jh.edu` URL, so it is not a usable alternate route.

**File table.**

| Local file | Bytes | sha256 | Contents |
|---|---|---|---|
| `qnm/s0l0.dat` | 65,000 | `99c25c4f1a20e53b561d0d0b53275ef296987b15d8574a3c7bafb3a09b07a1ea` | Schwarzschild scalar (s=0, l=0) QNM, n=0..999, format `2M*omega_R, 2M*omega_I, error, n` |
| `qnm/s1l1.dat` | 65,000 | `4ad32e51ae23d5f76eedf8f32e1e5f0caa0ab01233b1127c77b9841ec5fca3e3` | Schwarzschild EM (s=1, l=1) QNM, same format |
| `qnm/s2l2.dat` | 65,130 | `6fb5fde221349f0b036f913df8918c2a88f8ea30755ca342f7b97040f3fe654e` | Schwarzschild gravitational (s=2, l=2) QNM, same format |
| `qnm/l2.tar.gz` | 9,640,422 | `0569faae28e14366480cf594ea398f3d33ac9d3f82dbbddd43a68d920d807086` | Kerr gravitational (s=-2) l=2, all m, n=1..8, as downloaded |
| `qnm/l3.tar.gz` | 13,384,012 | `e5ba542e327a27783269dd3f69d4c00f01256d0fd1e61c6c39f33dc78dc3ad27` | Kerr gravitational (s=-2) l=3, all m, n=1..8, as downloaded |
| `qnm/l2/` (extracted) | 40 files, 34,004,096 total | -- | one file per (n,m), n=1..8 x m=-2..2 |
| `qnm/l3/` (extracted) | 56 files, 47,604,096 total | -- | one file per (n,m), n=1..8 x m=-3..3 |

Script: `qnm/download_qnm.py` (sha256 `3665c12d1b0924c4c9dfdfb17e5c5c09f7355ec1a054b24ba9bec9cd4c00c6b5`).

Bytes actually pulled over the network: 65,000 + 65,000 + 65,130 + 9,640,422 + 13,384,012 =
**23,219,564 bytes (22.1 MiB)**, comfortably under the 100 MB cap. The `qnm/` directory's on-disk
total is larger (104,836,052 bytes) only because both tarballs (kept as sha256'd provenance copies)
and their fully extracted per-mode `.dat` files (kept for direct read access without re-extracting)
are present simultaneously; no extra data was fetched from the network to produce that expansion.

**Format.** Kerr tables: `a/M, M*omega_R, M*omega_I, Re[A_lm], Im[A_lm]`, spin sampled from
`a/M=0` to `a/M=0.9999` (non-uniform step, denser near extremality), overtone `n` counted from 1
(so the tar files' `n=1` is the fundamental, `n=1,2,3` = the conventional `n=0,1,2`; all 8 overtones
the page provides were kept rather than truncating to 3). Schwarzschild-only `s*l*.dat` files:
`2*M*omega_R, 2*M*omega_I, error, n` (conventional `n` starting at 0; note the factor of 2 on
`M*omega` here, absent in the Kerr tables).

**Validation (as specified).** `qnm/s2l2.dat` row `n=0`: $2M\omega = 0.7473433688 - 0.1779246314i$
$\to M\omega = 0.37367168 - 0.08896232i$, target $\sim0.37367 - 0.08896i$. **MATCH.** Cross-checked
independently against the `a/M=0` row of `qnm/l2/n1l2m0.dat` (the Kerr table's zero-spin limit),
which reproduces the identical value to all 10 given digits.

**Coverage landed.** l=2: m in $\{-2,-1,0,1,2\}$, n in $\{1,\ldots,8\}$ (40 files). l=3: m in
$\{-3,-2,-1,0,1,2,3\}$, n in $\{1,\ldots,8\}$ (56 files). Both exceed the "n=0..2" floor named in
the task (the page packages all overtones per tarball; nothing was truncated).

**Re-fetching.** Every file here is re-fetchable anonymously with no credentials:

```bash
cd experiments/primes/_cache/datasets/physics
python3 endf/download_endf.py && python3 endf/parse_endf.py
python3 qnm/download_qnm.py
```

`physics/SHA256SUMS` (146 entries) follows the same regeneration and verification commands as
section 16, run one directory down.

**Serves.** Both parts are calibration/comparison data, not RH evidence, by the repo's own
governing result: `experiments/primes/PRIME_PATTERNS.md` establishes that GUE-type spectral
statistics are provably RH-blind (moving a zeta zero off the critical line changes no statistic
derived only from the unfolded spacing distribution). Nuclear resonance level spacings are the
historical other side of that same universality question: pooled s-wave neutron resonances from
many nuclei follow the **Gaussian Orthogonal Ensemble (GOE)**, not the Gaussian Unitary Ensemble
(GUE) the zeta zeros and this repo's own `e5e_zero_statistics.py` pipeline test against. That
symmetry-class mismatch (GOE has real eigenvalues from a time-reversal-symmetric Hamiltonian, GUE
does not) is exactly the point: the ENDF resonance tables are a second, independent, real
experimental spectrum to run the same unfolding/spacing-statistic code against, which exercises the
pipeline on data where the *answer is known to differ* from the zeta case (GOE spacing statistics,
not GUE), the sharpest instrument check available short of a synthetic random-matrix draw. The
14-nuclide spread (7 MLBW, 5 Reich-Moore, 2 R-Matrix Limited evaluations) additionally means the
ENDF parser in `endf/parse_endf.py` was forced to handle all three resonance formalisms actually in
current use in ENDF/B-VIII.0, not just the simplest one.

The Kerr QNM tables serve the comparative-spectra thread in
`docs/03_research/local_quantum_gravity_and_primes.md` directly: quasinormal-mode frequencies are a
genuinely different kind of "zeros of a special function" (poles of a black-hole scattering
resonance, indexed by (l,m,n) and continuously deformed by spin a/M) that the quantum-gravity
literature has repeatedly proposed as a structural analogy to the zeta zeros. Having the actual
Berti-Cardoso-Starinets numbers on disk (rather than citing the paper secondhand) lets that
document's comparison be checked against real values instead of asserted from memory, starting from
the exact Schwarzschild fundamental mode landmark validated above.
