# Scenario Context
Our product team replaced the legacy if/else triage block with an LLM classifier to tag incoming customer support tickets into three categories: Billing, Technical, or Account.
During low-volume local testing, the system worked perfectly. However, under heavy concurrent production loads, identical user tickets fluctuate unpredictably between categories (e.g., tagging a ticket as Billing on one run, and Technical on the next). This nondeterministic behaviour triggers conflicting down-funnel automations, causing double-refund attempts and incorrect routing.
