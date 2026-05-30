# medwriter-mcp

[![MCPize](https://mcpize.com/badge/@pubspro/medwriter)](https://mcpize.com/mcp/medwriter)

**The Medical Writer's AI Toolkit — 34 expert prompts as callable MCP tools.**
Built by a CMPP-certified medical writer with a PhD and 10+ years in pharma. Gives Claude and any MCP-compatible AI agent direct access to publication-ready prompt frameworks for every stage of the pharma medical writing workflow.

---

## Plans & tiers
| Tier | Tools | Access |
|------|-------|--------|
| Free | 8 starter tools | $0/mo · 25 requests · install and use immediately |
| Pro | All 34 tools + ADAPT framework | $39/mo ($374/yr) · 1,000 requests |
| Business | All 34 tools + ADAPT framework | $89/mo ($854/yr) · 5,000 requests |
| Ultra | All 34 tools + ADAPT framework | $129/mo ($1,238/yr) · 10,000 requests |

---

## Tools

### ✅ Free tier

| Tool | Description |
|------|-------------|
| `get_manuscript_outline_prompt` | Create a detailed manuscript outline with section word counts |
| `get_structured_abstract_prompt` | Draft a CONSORT/STROBE-aligned structured journal abstract |
| `get_unstructured_abstract_prompt` | Draft a narrative (unstructured) journal abstract |
| `get_introduction_section_prompt` | Draft a manuscript Introduction section |
| `get_methods_section_prompt` | Draft a manuscript Methods section |
| `get_results_section_prompt` | Draft a manuscript Results section |
| `get_discussion_section_prompt` | Draft a manuscript Discussion section |
| `list_all_tools` | List every tool available in the toolkit |

### 🔐 Paid tiers — 26 additional tools across 9 chapters (Pro, Business, Ultra)
**Chapter 1 — Abstract writing**
- Convert structured → unstructured abstract
- Rewrite weak conclusions to be data-anchored
- Adapt abstracts for different audiences

**Chapter 2 — Manuscript development**
- Draft Introduction, Methods, Results, Discussion sections
- AMA style, CONSORT/STROBE aligned

**Chapter 3 — Peer review**
- Evidence-based rebuttal to reviewer disagreement
- Cover letter for revised manuscript submission

**Chapter 4 — Congress abstracts and posters**
- ASCO, ASH, ESMO, APA congress abstracts
- Declarative poster titles and take-home messages
- Timed oral presentation scripts

**Chapter 5 — Slide deck narratives**
- Slide-by-slide deck outlines by audience type
- Speaker notes for data slides
- Mechanism of action slide copy

**Chapter 6 — Publication planning**
- Publication plan framework table
- Literature and data gap analysis
- Executive summary for medical affairs leadership
- Journal selection with rationale (top 3 journals)

**Chapter 7 — Author collaboration**
- Author review request with deadline
- Response to author major revision request

**Chapter 8 — Editing, QC and style**
- Comprehensive AMA-style manuscript edit
- Promotional language check for MLR pre-review
- Statistical reporting consistency check

**Chapter 9 — Career and professional development**
- CV tailoring for ATS keyword alignment
- CMPP exam practice question generator
- Medical writing interview prep with STAR frameworks

**Bonus — ADAPT framework**
- Layer Audience, Document type, Accuracy level, Purpose, and Tone onto any prompt in the library

---

## Quickstart

### Install

```bash
git clone https://github.com/pubspro/medwriter-mcp.git
cd medwriter-mcp
pip install mcp
```

### Add to Claude Desktop

Edit `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "medwriter-mcp": {
      "command": "python",
      "args": ["/absolute/path/to/medwriter-mcp/server.py"]
    }
  }
}
```

Restart Claude Desktop. All tools appear automatically.

### Add to Claude Code

```bash
claude mcp add medwriter-mcp python /absolute/path/to/medwriter-mcp/server.py
```

---

## Example prompts

Once connected, ask Claude:

```
Use get_structured_abstract_prompt to draft an abstract for a Phase 3 RCT 
of pembrolizumab in NSCLC. Primary endpoint: PFS HR 0.58 (95% CI 0.46–0.72, p<0.001).
```

```
Use get_gap_analysis_prompt to identify publication gaps for a BTK inhibitor 
in CLL based on the current literature landscape.
```

```
Use get_congress_abstract_prompt to draft an ASH abstract for a study 
of venetoclax plus obinutuzumab in previously untreated CLL.
```

```
Use get_promotional_language_check_prompt to review this slide deck excerpt 
before MLR submission.
```

```
Use apply_adapt_framework to rewrite this abstract for a nursing audience 
at a health literacy reading level.
```

---

## Data safety

Every prompt is structured so you never need to input unpublished, confidential, or proprietary data. Tools marked 🔒 carry elevated data-sensitivity risk and include inline guidance.

**Never input into any public AI tool:**
- Unpublished clinical trial data
- Patient-level or identifiable data
- Proprietary compound information or IP
- Data under NDA or confidentiality agreement
- Pre-decisional regulatory documents

Always comply with ICMJE, GPP4, and your organization's AI use policies.

---

## Who this is for

- Medical writers at associate through director level
- Publication managers and medical affairs professionals
- Pharmacists, physicians, and researchers moving into medical writing
- CMPP candidates preparing for certification

---

## Companion servers

Pair with other `pubspro` MCP servers for a complete pharma AI workflow:

- [pharma-mcp](https://github.com/pubspro/pharma-mcp) — ClinicalTrials.gov, PubMed, FDA, ICH guidelines
- [pubmed-search](https://github.com/pubspro/pubmed-search) — PubMed literature search
- [medterms-mcp](https://github.com/pubspro/medterms-mcp) — ICD-10, MedDRA, RxNorm, CTCAE

---

## Requirements

- Python 3.8+
- mcp (`pip install mcp`)

---

## License

MIT
