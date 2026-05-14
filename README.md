# Scenario Context
Our product team replaced the legacy if/else triage block with an LLM classifier to tag incoming customer support tickets into three categories: Billing, Technical, or Account.
During low-volume local testing, the system worked perfectly. However, under heavy concurrent production loads, identical user tickets fluctuate unpredictably between categories (e.g., tagging a ticket as Billing on one run, and Technical on the next). This nondeterministic behaviour triggers conflicting down-funnel automations, causing double-refund attempts and incorrect routing.

## The Task
   1. Run test_instability.py to observe the drift and see how the model outputs conversational fluff or fluctuates between categories.
   2. Refactor the triage_ticket endpoint in app_unstable.py to achieve absolute, reproducible determinism.
   3. Fix the system so that the test suite passes consistently across continuous test runs.
