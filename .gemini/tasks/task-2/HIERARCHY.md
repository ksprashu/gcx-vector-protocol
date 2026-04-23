# Proposed Priority Hierarchy

Based on the Gemini CLI policy engine parsing of TOML files (calculating final priority as `tier_base + (toml_priority / 1000)`), the TOML `priority` value can range from 0 to 999.

To standardize rule priority assignments within any given tier, the following standard priority levels are proposed:

- **Explicit Denies (Highest precedence within tier):** `priority = 600`
- **Explicit Allows (High precedence):** `priority = 500`
- **Conditional / Contextual Rules:** `priority = 300`
- **Catch-alls / Fallbacks (Lowest precedence):** `priority = 100`

### Justification
The policy engine ensures that tier bases (Admin = 5, User = 4, Extension = 2, Default = 1) override local TOML priorities. However, within a single tier, the TOML priority value (0-999) dictates precedence. By assigning Explicit Denies a higher priority (600) than Explicit Allows (500), we ensure a "deny override" security posture, making explicit restrictions harder to bypass. Catch-alls are assigned a low priority (100) so they can be easily overridden by more specific allow or deny rules.
