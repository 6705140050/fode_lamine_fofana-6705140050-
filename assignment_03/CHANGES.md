# Assignment 03 — CHANGES

**Name:** Fode Lamine Fofana  **Student ID:** 6705140050

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product stored as a bare tuple `("Laptop", 1200.0, "electronics")`, indexed by position | `Product` class with `name`, `price`, `category`; `PRODUCTS` tuples are wrapped into a catalog of `Product` objects | Classes / encapsulation | Ran `python Assignment_03.py` → PASS |
| 2 | Order stored as `(name, tier, [(product_index, qty), ...])`, unpacked with `it[0]`/`it[1]` | `OrderItem` (has-a `Product`) and `Order` (has-a `Customer`, has-many `OrderItem`) | Composition | PASS |
| 3 | Repeated `if t == "none"/"silver"/"gold"/"platinum"` chains for both discount and points | `Membership` base class + `Silver`/`Gold`/`Platinum` subclasses, each overriding `discount_rate()`; `points_multiplier` is a class attribute | Polymorphism / inheritance | PASS; deleted the old if/elif and re-ran |
| 4 | `calc()` computed totals **and** printed in the same function, using a `global TAXRATE` | `Order.subtotal()/discount()/tax()/total()/points()` are pure (return a number, no `print`); `Order.receipt()` is the only method that builds text; `global` removed entirely | Separation of calculation vs I/O | PASS; also manually diffed `Order.total()` output against the printed "Total:" line |
| 5 | Magic numbers scattered through `calc()` (`0.07`, `100`, `10`, `0.03`, `//10`) and no constructor validation | Named constants (`TAX_RATE`, `DISCOUNT_THRESHOLD`, `BULK_QTY_THRESHOLD`, `BULK_DISCOUNT_RATE`, `POINTS_DIVISOR`); `OrderItem`/`Product`/`Customer` constructors validate (`qty >= 1`, non-negative price, known tier) | Encapsulation, DRY | PASS; also tried `OrderItem(product, 0)` by hand to confirm it raises `ValueError` |

## 2 · Short reflection (4–6 sentences)

> Splitting calculation from printing made the biggest difference to how the code reads. In the original `calc()`, the totals and the receipt text were tangled together in one long function, so it was hard to tell which lines were "business logic" and which were just formatting. Moving `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` onto `Order` as pure methods that only return numbers, and pushing all the `print` statements into `receipt()`, made each piece easy to read and test on its own. Replacing the tier `if/elif` chains with a `Membership` class family was the second-biggest improvement — deciding the discount rate and points multiplier is now just a matter of picking the right subclass, instead of tracing four repeated conditionals in two different places. The part that forced me to slow down was moving tax logic onto `Product.tax_rate()`: it was tempting to just return `TAX_RATE` for every category, but that would have silently changed food items from tax-free to taxed, so I had to re-check the category check against the original `calc()` line by line before trusting it. Keeping the exact same rounding and string formatting (e.g. `str(round(sub, 2))`) also required care, since a cleaner-looking f-string with different formatting would have broken the self-test even though the math was correct.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Refactor the tier if/elif chains for discount and points into a class family" | `Membership` base class + `Silver`/`Gold`/`Platinum` subclasses, keyed by a `MEMBERSHIP_TIERS` dict instead of more if/elif | Accepted | Ran self-test → PASS |
| 2 | "Split calculation from printing, keep it returning the same numbers as the original `calc()`" | Pure methods `subtotal()/discount()/tax()/total()/points()` on `Order`, with `receipt()` doing only string building | Accepted | Ran self-test → PASS; hand-traced Bob's order (tier "none", 15 items) to confirm the 3% bulk discount still applied |
| 3 | "Let each Product decide its own tax instead of checking category in the totals loop" | `Product.tax_rate()` returning 0.0 for food, `TAX_RATE` otherwise | Accepted | Ran self-test → PASS |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
