# External datasets

Provenance record for the third-party numerical tables downloaded into
`experiments/primes/_cache/datasets/`. That directory is gitignored (`experiments/**/_cache/`),
so the data itself is machine-local: this file is the tracked record that says what was pulled,
from where, in what format, and how to get it again.

Downloaded 2026-08-15. Total on disk: 77,673,220 bytes (74.1 MB) across 249 files.
A per-file checksum manifest is written at `_cache/datasets/SHA256SUMS` (regenerate with the
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

---

## 1. Scope and layout

```
experiments/primes/_cache/
├── odlyzko/                 pre-existing: zeros1, zeros3, zeros4, zeros5 (see section 2)
└── datasets/                everything in this document
    ├── SHA256SUMS           per-file manifest, 249 entries
    ├── odlyzko/             zeros2, zeros6, zeros6.gz
    ├── lmfdb/               high-precision zeta zeros, Platt sample, Dirichlet L zeros
    ├── lmfdb_maass/         level-1 Maass cusp form spectral parameters (see section 17)
    ├── tos/                 Oliveira e Silva: primes/, gaps/, twin_gaps/, goldbach/, apc/, zeta/
    ├── oeis/                14 b-files
    ├── gaps_records/        maximal and first-occurrence prime gap tables
    └── misc/                Gourdon reference material
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

**LMFDB rate limiting, the one real trap.** `www.lmfdb.org` sits behind Google reCAPTCHA Enterprise
bot management. When it throttles, it returns **HTTP 200** with an HTML reCAPTCHA challenge body
instead of the requested data. A script that checks only the status code will happily write that
challenge page to disk as if it were a dataset. Always check `Content-Type` and grep the body for
`recaptcha` or `<!doctype` before trusting a response. Throttle to well under 1 request per second
and never issue concurrent requests. `beta.lmfdb.org` has no such defense once the `human=1` cookie
is set.

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
