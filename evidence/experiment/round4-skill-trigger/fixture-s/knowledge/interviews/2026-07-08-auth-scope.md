---
type: Interview
title: Auth scoping with Ivan
description: Q&A that scoped TaskLite's authentication approach.
timestamp: 2026-07-08T09:30:00Z
tags: [auth]
---

# Auth scoping — 2026-07-08, with Ivan (owner)

**Q: Who are the users? Do they need SSO?**
A: "No. Users are external freelancers — individuals, not companies. There is
no corporate identity provider involved."

**Q: How much auth maintenance can the project absorb?**
A: "Basically none. I'm the only maintainer and I work on this a few hours a
week. Anything that can break at 3am is out."

**Q: Any compliance or security requirements?**
A: "Nothing formal. Just don't store passwords, I don't want the liability."
