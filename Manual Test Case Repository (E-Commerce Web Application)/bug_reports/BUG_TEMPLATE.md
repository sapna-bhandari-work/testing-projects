# Bug Report Template

**Repository:** Manual E-Commerce Testing — SauceDemo
**Template Version:** 1.0
**Last Updated:** [Date]

---

## How to Use This Template

1. Copy the template block below for each new defect found.
2. Assign a Bug ID following the convention: `BUG_[MODULE]_[3-digit number]`
   - Modules: `LOGIN`, `BROWSE`, `CART`, `CHECKOUT`
   - Example: `BUG_LOGIN_001`, `BUG_CART_003`
3. Fill in all mandatory fields. Leave `Attachments` as a placeholder if screenshots are not yet available.
4. **Severity** and **Priority** are independent assessments:
   - **Severity** = Impact of the bug on system functionality (Critical / Major / Minor / Trivial)
   - **Priority** = Urgency of fixing the bug relative to business and release needs (High / Medium / Low)
5. Update the **Status** field as the bug progresses through its lifecycle.

---

## Severity Definitions

| Severity Level | Description |
|----------------|-------------|
| **Critical**   | The defect causes a complete breakdown of a core feature or prevents users from completing a key workflow. No workaround exists. |
| **Major**      | The defect significantly impairs functionality but a workaround may exist. Affects a primary user flow. |
| **Minor**      | The defect causes a limited or cosmetic issue. Core functionality is not impaired. |
| **Trivial**    | The defect is a cosmetic or typographical issue with negligible functional impact. |

## Priority Definitions

| Priority Level | Description |
|----------------|-------------|
| **High**       | Must be fixed before the next release. Business-critical or customer-facing impact. |
| **Medium**     | Should be fixed in the upcoming sprint / release cycle. |
| **Low**        | Can be deferred to a future release without significant impact. |

## Bug Status Lifecycle

`New` → `Open` → `In Progress` → `Fixed` → `Ready for Retest` → `Closed` / `Rejected` / `Deferred`

---

## Bug Report Template

```
---

## BUG_[MODULE]_[XXX] — [Short Bug Title]

| Field                | Value |
|----------------------|-------|
| **Bug ID**           | BUG_[MODULE]_[XXX] |
| **Title**            | [Concise description of the defect — what is wrong] |
| **Module**           | [Login / Product Browsing / Shopping Cart / Checkout] |
| **Severity**         | [Critical / Major / Minor / Trivial] |
| **Priority**         | [High / Medium / Low] |
| **Environment**      | Browser: [Chrome / Firefox / etc.] vXX | OS: [Windows 11 / macOS] | URL: https://www.saucedemo.com |
| **Test Case Ref.**   | [TC_MODULE_XXX or N/A if found exploratorily] |
| **Reported By**      | [QA Engineer Name] |
| **Date Reported**    | [YYYY-MM-DD] |
| **Status**           | [New / Open / In Progress / Fixed / Ready for Retest / Closed / Rejected] |

### Steps to Reproduce

1. [First step — be specific enough that anyone can reproduce]
2. [Second step]
3. [Continue as needed...]

### Expected Result

[What should happen based on requirements or standard behaviour]

### Actual Result

[What actually happened — be specific, quote exact UI text or error messages where relevant]

### Attachments

- [ ] Screenshot — [filename or "N/A"]
- [ ] Screen recording — [filename or "N/A"]
- [ ] Console log / browser network log — [filename or "N/A"]

### Additional Notes

[Any relevant context: frequency of occurrence (always / intermittent), related bugs,
workaround if known, impact on other test cases, etc.]

---
```

---

*End of BUG_TEMPLATE.md*
