"""
The Medical Writer's AI Toolkit — MCP Server
Exposes 33 expert prompts as callable tools for AI agents.
Free tier: tools 1-5 | Pro tier: all 33 tools + ADAPT framework

Author: PubsPro (CMPP-Certified, PhD, 10+ Years Medical Communications)
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Medical Writer's AI Toolkit",
    instructions="""You have access to a library of 33 expert-crafted prompts for
    pharmaceutical medical writing, curated by a CMPP-certified professional with a PhD
    and 10+ years of experience. These prompts cover abstracts, manuscripts, peer review,
    congress content, publication planning, author communications, editing, and career
    development. All prompts include data-safety guidance for pharma use.
    FREE TIER: tools 1-5. PRO TIER: all 33 tools + ADAPT framework."""
)

# ─────────────────────────────────────────────────────────────
# PART 1 · SCIENTIFIC PUBLICATIONS
# ─────────────────────────────────────────────────────────────

# ── FREE TIER ──────────────────────────────────────────────

@mcp.tool()
def get_structured_abstract_prompt(
    drug_name: str,
    indication: str,
    study_design: str,
    primary_endpoint_result: str,
    key_secondary_results: str,
    safety_highlights: str,
    word_limit: int = 250
) -> str:
    """
    [FREE] Generate a prompt to draft a structured journal abstract.
    Covers Background, Objective, Methods, Results, and Conclusions.
    CONSORT/STROBE aligned. Suitable for clinical manuscripts.
    DATA SAFETY: Only use published or approved summary data in the fields.
    """
    return f"""Write a structured abstract for a clinical manuscript with the following sections:
Background, Objective, Methods, Results, and Conclusions.

Drug/intervention: {drug_name}
Indication/population: {indication}
Study design: {study_design}
Primary endpoint result: {primary_endpoint_result}
Key secondary results: {key_secondary_results}
Safety highlights: {safety_highlights}
Word limit: {word_limit} words

Write in past tense for methods and results. Use precise, journal-appropriate language.

Pro tip: Add 'Follow CONSORT reporting guidelines' to align with most clinical trial journals.

⚠️ DATA SAFETY: Only input published or approved summary data. Never include unpublished
clinical trial data, patient-level data, or proprietary IP into any public AI tool."""


@mcp.tool()
def get_manuscript_outline_prompt(
    manuscript_type: str,
    topic: str,
    journal: str,
    study_design: str,
    num_figures_tables: int = 3
) -> str:
    """
    [FREE] Generate a prompt to create a detailed manuscript outline.
    Includes section headers, word counts, key data points, and journal formatting notes.
    Suitable for original research, reviews, and case reports.
    """
    return f"""Create a detailed outline for a {manuscript_type} on {topic} for submission to {journal}.

Include:
- Suggested section headers and subheaders
- Approximate word count per section
- Key data/figures to include in each section
- Notes on journal-specific formatting requirements if known

Study type: {study_design}
Number of figures/tables planned: {num_figures_tables}

Structure the outline so it can be handed directly to a medical writer to begin drafting."""


@mcp.tool()
def get_peer_review_response_prompt(
    reviewer_comment: str,
    action_taken: str,
    supporting_data: str = ""
) -> str:
    """
    [FREE] Generate a prompt to draft a professional point-by-point reviewer response.
    Produces respectful, concise, data-driven responses that maximize acceptance chances.
    DATA SAFETY: Only reference published or approved data in supporting_data.
    """
    return f"""Draft a professional point-by-point response to the following reviewer comment.
Be respectful, concise, and data-driven. If the comment requires a manuscript change,
state exactly what was changed and where.

Reviewer comment: {reviewer_comment}

Our response/action taken: {action_taken}

Relevant data supporting our position: {supporting_data if supporting_data else "N/A"}

Always begin with 'We thank the reviewer for this insightful comment.' to set a collegial tone.

⚠️ DATA SAFETY: Only reference published or approved data in your response."""


@mcp.tool()
def get_author_invitation_email_prompt(
    author_name: str,
    specialty: str,
    study_description: str,
    timeline_overview: str
) -> str:
    """
    [FREE] Generate a prompt to draft a professional author invitation email.
    ICMJE authorship criteria aligned. Tone: professional and respectful of their time.
    Target length: 200-250 words.
    """
    return f"""Write an email inviting {author_name}, a key opinion leader in {specialty},
to serve as an author on a manuscript reporting {study_description}.

Include:
- Brief description of the study and manuscript
- Why this physician's expertise is relevant
- Expected authorship contribution (per ICMJE criteria)
- Timeline overview: {timeline_overview}
- Clear next step / call to action

Tone: professional, respectful of their time.
Length: 200-250 words.

Always reference ICMJE authorship criteria explicitly — it sets expectations early.

⚠️ DATA SAFETY: Do not include unpublished efficacy or safety data in external emails."""


@mcp.tool()
def get_linkedin_publication_post_prompt(
    paper_title: str,
    journal: str,
    key_message: str,
    clinical_significance: str,
    your_role: str
) -> str:
    """
    [FREE] Generate a prompt to draft a LinkedIn post announcing a publication.
    Professional but engaging tone. Includes call to action and hashtag suggestions.
    Target length: 150-200 words.
    """
    return f"""Write a LinkedIn post announcing the publication of '{paper_title}' in {journal}.

Key message: {key_message}
Clinical significance: {clinical_significance}
My role: {your_role}

Tone: professional but engaging.
Include a call to action.
Length: 150-200 words.
Suggest 3-5 relevant hashtags.

Pro tip: Publication announcements on LinkedIn drive profile views and establish
thought leadership in your therapeutic area."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 1: ABSTRACT WRITING
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_unstructured_abstract_prompt(
    structured_abstract: str,
    word_count: int,
    target_journal: str
) -> str:
    """
    [PRO] Convert a structured abstract to a flowing unstructured paragraph.
    Required by many basic science journals (Nature, Science family).
    DATA SAFETY: Only paste published or approved text.
    """
    return f"""Convert the following structured abstract into a single, flowing unstructured
paragraph of approximately {word_count} words.
Maintain all key data points. Use smooth transitions.
Target journal: {target_journal}

{structured_abstract}

⚠️ DATA SAFETY: Only input published or approved text."""


@mcp.tool()
def get_strengthen_conclusions_prompt(
    current_conclusion: str,
    primary_endpoint_result: str
) -> str:
    """
    [PRO] Rewrite an abstract conclusion to be data-anchored and clinically meaningful.
    Addresses the #1 reason abstracts get rejected: weak conclusions.
    DATA SAFETY: Only use published or approved text.
    """
    return f"""Review the following abstract conclusion and rewrite it to:
(1) directly answer the primary objective
(2) include the magnitude of effect with confidence intervals if available
(3) state the clinical significance clearly
(4) avoid overstatement or unsupported claims

Current conclusion: {current_conclusion}
Primary endpoint result: {primary_endpoint_result}

Pro tip: Weak conclusions are the #1 reason abstracts get rejected. Be specific and data-anchored.

⚠️ DATA SAFETY: Only use published or approved text."""


@mcp.tool()
def get_adapt_abstract_audience_prompt(
    abstract_text: str,
    target_audience: str,
    reading_level: str = "medical professional"
) -> str:
    """
    [PRO] Rewrite an abstract for a different audience while preserving scientific accuracy.
    Useful for patient summaries, nurse education, or general medical audiences.
    DATA SAFETY: Only paste published or approved text.
    """
    return f"""Rewrite the following abstract for {target_audience}.
Simplify technical jargon while preserving scientific accuracy.
Target reading level: {reading_level}

{abstract_text}

⚠️ DATA SAFETY: Only input published or approved text."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 2: MANUSCRIPT DEVELOPMENT
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_introduction_section_prompt(
    drug_or_topic: str,
    indication: str,
    target_journal: str,
    word_length: str = "400-500 words"
) -> str:
    """
    [PRO] Draft a manuscript Introduction/Background section.
    Covers disease burden, treatment landscape, study rationale, and objective statement.
    AMA style. No references included.
    """
    return f"""Write an Introduction section for a clinical manuscript on {drug_or_topic} in {indication}.

Structure:
1. Disease burden paragraph: prevalence, unmet need, patient impact
2. Current treatment landscape: standard of care, limitations
3. Rationale for this study: mechanism of action, preclinical/early clinical data
4. Study objective statement: what this paper reports

Target journal: {target_journal}
Length: {word_length}
Do not include references.

Pro tip: Add 'write in active voice where appropriate per AMA style' for cleaner prose."""


@mcp.tool()
def get_methods_section_prompt(
    study_design: str,
    drug: str,
    population: str,
    treatment_arms: str,
    primary_secondary_endpoints: str
) -> str:
    """
    [PRO] Draft a manuscript Methods section.
    CONSORT aligned for RCTs, STROBE for observational studies.
    Covers design, eligibility, treatment arms, endpoints, and statistical analysis.
    """
    return f"""Write a Methods section for a {study_design} study of {drug} in {population}.

Subsections:
- Study design and setting
- Patient eligibility (inclusion/exclusion criteria)
- Treatment arms: {treatment_arms}
- Primary and secondary endpoints: {primary_secondary_endpoints}
- Statistical analysis plan overview

Use past tense. Follow CONSORT/STROBE guidelines as appropriate.

Pro tip: For observational studies specify STROBE. For RCTs specify CONSORT."""


@mcp.tool()
def get_results_section_prompt(
    primary_endpoint_data: str,
    secondary_endpoint_data: str,
    safety_ae_data: str
) -> str:
    """
    [PRO] Draft a manuscript Results section narrative from approved/published data.
    Format: patient disposition → efficacy → safety.
    DATA SAFETY: ELEVATED RISK — only use published data or data from your org's approved AI platform.
    Never paste raw tables from unpublished studies.
    """
    return f"""Write a Results section narrative based on the following data.
Do not add data not present. Report all values with units, confidence intervals, and p-values as provided.

Primary endpoint: {primary_endpoint_data}
Secondary endpoints: {secondary_endpoint_data}
Safety/AE data: {safety_ae_data}

Format: patient disposition → efficacy → safety.
Use past tense throughout.

Pro tip: Always verify AI-reported numbers against your source tables before submission.

🔒 DATA SAFETY — ELEVATED RISK: Only use published data, approved press releases, or data
from your organization's approved AI platform. Do NOT paste raw tables from unpublished
studies or interim analyses."""


@mcp.tool()
def get_discussion_section_prompt(
    study_summary_and_key_result: str,
    prior_studies_comparators: str,
    study_limitations: str
) -> str:
    """
    [PRO] Draft a manuscript Discussion section.
    Covers primary finding, context vs prior studies, mechanistic rationale,
    clinical implications, limitations, and conclusions.
    """
    return f"""Write a Discussion section for a manuscript reporting:
{study_summary_and_key_result}

Structure:
1. Opening: restate primary finding in context of primary objective (2-3 sentences)
2. Context: how do results compare to {prior_studies_comparators}?
3. Mechanistic rationale: why might these results make biological sense?
4. Clinical implications: what does this mean for practice?
5. Limitations: {study_limitations}
6. Conclusions: forward-looking, appropriately cautious statement

Avoid introducing new data. Do not overstate findings.

Pro tip: The limitations paragraph is often the most scrutinized by reviewers —
be honest and thorough."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 3: PEER REVIEW
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_rebuttal_disagreement_prompt(
    reviewer_request: str,
    reason_for_disagreement: str,
    supporting_evidence: str
) -> str:
    """
    [PRO] Draft a polite, evidence-based rebuttal when disagreeing with a reviewer.
    Acknowledges concern, explains rationale, cites guidelines, offers compromise.
    """
    return f"""A reviewer has requested {reviewer_request}, but we respectfully disagree
because {reason_for_disagreement}.

Draft a polite, evidence-based rebuttal that:
(1) acknowledges the reviewer's concern
(2) explains our rationale for not making this change
(3) cites relevant literature or guidelines supporting our approach
(4) offers a compromise if appropriate (e.g., adding a sentence to the limitations section)

Supporting evidence/references: {supporting_evidence}

Tone: collegial and professional. Never defensive."""


@mcp.tool()
def get_revised_manuscript_cover_letter_prompt(
    journal: str,
    manuscript_title: str,
    manuscript_number: str,
    major_revisions: str
) -> str:
    """
    [PRO] Draft a cover letter for a revised manuscript submission.
    Professional, confident, and collegial tone. ~200-250 words.
    """
    return f"""Write a cover letter for a revised manuscript submission to {journal}.

Manuscript title: '{manuscript_title}'
Manuscript number: {manuscript_number}
Key revisions made:
{major_revisions}

Tone: professional, confident, and collegial.
Length: ~200-250 words.

Pro tip: Highlight your most substantive revisions — editors read cover letters
before reviewer responses."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 4: CONGRESS ABSTRACTS & POSTERS
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_congress_abstract_prompt(
    congress_name: str,
    study_description: str,
    key_primary_result: str,
    key_secondary_results: str,
    safety_summary: str,
    word_limit: int = 500
) -> str:
    """
    [PRO] Draft a congress abstract for ASCO, ASH, ESMO, APA, or similar.
    DATA SAFETY: ELEVATED RISK — only use data approved for external disclosure.
    Sections: Background, Methods, Results, Conclusions.
    """
    return f"""Write a congress abstract for {congress_name} based on the following study data.

Format:
- Word limit: {word_limit} words
- Sections: Background, Methods, Results, Conclusions
- Include: trial registration number placeholder, funding source line

Study: {study_description}
Key result: {key_primary_result}
Key secondary results: {key_secondary_results}
Safety summary: {safety_summary}

Write in present tense for background, past tense for methods and results.

Pro tip: Check congress-specific abstract guidelines annually — format requirements change each cycle.

🔒 DATA SAFETY — ELEVATED RISK: Only use data that has received internal approval
for external disclosure."""


@mcp.tool()
def get_poster_title_and_takeaways_prompt(
    study_or_topic: str,
    congress: str,
    key_finding: str,
    character_limit: int = 200
) -> str:
    """
    [PRO] Generate 5 alternative congress poster titles + 3 take-home message bullets.
    Declarative titles outperform question titles for poster traffic.
    """
    return f"""Generate 5 alternative titles for a congress poster on {study_or_topic}.

Titles should be:
(1) declarative where possible
(2) include the drug name and indication
(3) highlight the key finding: {key_finding}
(4) comply with {congress} character limits (~{character_limit} characters)

Also write 3 take-home message bullet points (max 25 words each) that a physician
should remember after leaving the poster.

Pro tip: Declarative titles (stating the result) outperform question titles for poster traffic."""


@mcp.tool()
def get_oral_presentation_script_prompt(
    congress: str,
    study_description: str,
    key_message: str,
    audience: str,
    duration_minutes: int = 10
) -> str:
    """
    [PRO] Draft a timed oral presentation script for a congress.
    Includes slide-by-slide breakdown: title, background, design, results, safety, conclusions.
    """
    return f"""Write a {duration_minutes}-minute oral presentation script for {congress} on {study_description}.

Slide flow:
- Slide 1: Title + disclosures (30 sec)
- Slides 2-3: Background & rationale (2 min)
- Slides 4-5: Study design & patient characteristics (2 min)
- Slides 6-8: Key results (3 min)
- Slide 9: Safety (1.5 min)
- Slide 10: Conclusions (1 min)

Key message: {key_message}
Audience: {audience}

Pro tip: Read it aloud and time yourself — most people speak faster under pressure."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 5: SLIDE DECK NARRATIVES
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_slide_deck_outline_prompt(
    presentation_type: str,
    topic_or_drug: str,
    indication: str,
    audience: str,
    duration_minutes: int,
    key_message: str,
    available_data: str
) -> str:
    """
    [PRO] Create a slide-by-slide outline for advisory board, symposium, or HCP education decks.
    Includes slide title, key content, and suggested visual type per slide.
    """
    return f"""Create a slide-by-slide outline for a {presentation_type} presentation on
{topic_or_drug} in {indication}.

Audience: {audience}
Duration: {duration_minutes} minutes
Key message: {key_message}
Data available: {available_data}

For each slide: slide title, key content, suggested visual type.

Structure for maximum impact and retention."""


@mcp.tool()
def get_speaker_notes_prompt(
    slide_title: str,
    data_shown: str,
    audience: str,
    target_length: str = "150-200 words"
) -> str:
    """
    [PRO] Write speaker notes for a data slide.
    Notes contextualize data, explain the graph, highlight clinical meaning,
    and proactively address likely questions.
    DATA SAFETY: Describe data in general terms. Do not paste unpublished figures.
    """
    return f"""Write speaker notes for a slide presenting the following efficacy data.

Notes should:
(1) contextualize the data for the audience
(2) explain what the graph shows before stating the result
(3) highlight the most clinically meaningful aspect
(4) anticipate one likely question and address it proactively

Slide title: {slide_title}
Data shown: {data_shown}
Audience: {audience}
Target length: {target_length}

Pro tip: Speaker notes should sound conversational when read aloud — not like they're being read.

🔒 DATA SAFETY: Describe the data in general terms. Do not paste unpublished figures
or raw table values."""


@mcp.tool()
def get_moa_slide_prompt(
    drug_or_class: str,
    indication: str,
    target: str,
    pathway: str,
    clinical_consequence: str,
    audience: str
) -> str:
    """
    [PRO] Explain a mechanism of action for a slide deck in 3-4 clear sentences.
    Plain, precise language. Suitable for HCP education slides.
    """
    return f"""Explain the mechanism of action of {drug_or_class} in {indication}
for a slide deck targeting {audience}. Use plain, precise language.

Key points:
- Target: {target}
- Pathway affected: {pathway}
- Clinical consequence: {clinical_consequence}

Length: 3-4 sentences for a single 'MOA in brief' slide.

Pro tip: Add 'use an analogy' if the MOA is particularly complex — metaphors stick with audiences."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 6: PUBLICATION PLANNING
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_publication_plan_framework_prompt(
    drug_name: str,
    indication: str,
    available_studies: str,
    target_hcp_audience: str,
    key_congresses: str,
    target_journals: str
) -> str:
    """
    [PRO] Build a publication plan framework as a structured table.
    Columns: Publication Type | Study/Data Source | Target Venue | Timeline | Priority | Status.
    """
    return f"""Create a publication plan framework for {drug_name} in {indication}.

Available studies: {available_studies}
Target audience: {target_hcp_audience}
Key congresses: {key_congresses}
Target journals: {target_journals}

Output as table:
Publication Type | Study/Data Source | Target Venue | Timeline | Priority | Status

Pro tip: Build the framework first, then layer in specific timelines.
Easier to get buy-in from medical affairs leadership that way."""


@mcp.tool()
def get_gap_analysis_prompt(
    drug_or_class: str,
    indication: str,
    current_publication_landscape: str,
    available_data_package: str
) -> str:
    """
    [PRO] Conduct a literature and data gap analysis for a publication strategy.
    Identifies scientific, data, communication, and competitive gaps with rationale.
    """
    return f"""Perform a gap analysis for publications on {drug_or_class} in {indication}.

Current landscape: {current_publication_landscape}
Our data package: {available_data_package}

Identify:
1. Scientific gaps: questions not yet answered in the literature
2. Data gaps: analyses possible from available data but not yet conducted
3. Communication gaps: topics well-studied but underrepresented in publications
4. Competitive gaps: areas where competitor data exists but ours does not

Output as a prioritized gap list with rationale.

Pro tip: Present gap analyses visually as a matrix — much more impactful in steering committees."""


@mcp.tool()
def get_pub_plan_executive_summary_prompt(
    drug: str,
    indication: str,
    audience: str,
    priority_publications: str,
    timeline_overview: str,
    resource_requirements: str
) -> str:
    """
    [PRO] Write a one-page publication plan executive summary for medical affairs leadership.
    Strategic rationale, key data assets, priority publications, timeline. ~300-350 words.
    """
    return f"""Write a one-page executive summary of a publication plan for {drug} in {indication}
for presentation to {audience}.

Include:
- Strategic rationale (why these publications, why now)
- Key data assets being leveraged
- Priority publications: {priority_publications}
- Timeline overview: {timeline_overview}
- Resource requirements: {resource_requirements}

Tone: strategic and confident. Length: 300-350 words.

Pro tip: Lead with the 'so what' — busy medical affairs leaders want the bottom line first."""


@mcp.tool()
def get_journal_selection_rationale_prompt(
    study_description: str,
    indication: str,
    target_hcp_type: str
) -> str:
    """
    [PRO] Recommend the top 3 journals for a manuscript submission with full rationale.
    Includes impact factor, fit rationale, time to decision, submission requirements,
    and likelihood of acceptance.
    """
    return f"""Recommend the top 3 journals for submitting a manuscript on {study_description}
in {indication}.

For each journal:
- Journal name and impact factor (approximate)
- Rationale for fit (scope, audience, recent similar publications)
- Typical time to first decision
- Key submission requirements
- Likelihood of acceptance (High/Medium/Low) with reasoning

Primary target audience: {target_hcp_type}

Pro tip: Always verify impact factors and submission guidelines directly on the journal
website — they change annually."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 7: AUTHOR COLLABORATION
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_author_review_request_prompt(
    author_name: str,
    document_type: str,
    deadline: str,
    context: str,
    specific_questions: str = ""
) -> str:
    """
    [PRO] Draft a professional email requesting author review with a clear deadline.
    Concise (<150 words), friendly but firm on deadline, with a specific ask.
    """
    return f"""Write a professional email to {author_name} requesting review of {document_type}
with deadline: {deadline}.

Context: {context}
Specific questions for author: {specific_questions if specific_questions else "General review requested"}

Email should be:
- Concise (under 150 words)
- Friendly but clear on deadline
- Include a specific ask (e.g., 'please track changes directly in the document')"""


@mcp.tool()
def get_author_revision_response_prompt(
    change_requested: str,
    is_aligned_with_data: bool,
    action_or_counter: str,
    next_steps: str
) -> str:
    """
    [PRO] Draft a professional response to an author's major revision request.
    Collaborative, not defensive. Accepts or respectfully declines with rationale.
    """
    aligned_text = "is aligned with our data" if is_aligned_with_data else "is not fully aligned with our data"
    action_type = "Accept the change" if is_aligned_with_data else "Respectfully explain why we are not incorporating this change"

    return f"""An author has requested {change_requested} to our manuscript draft.
This {aligned_text}.

Draft a professional response that:
- Acknowledges and thanks the author for their input
- {action_type}: {action_or_counter}
- Confirms next steps: {next_steps}

Tone: collaborative, not defensive. Length: 150-200 words."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 8: EDITING, QC & STYLE
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_manuscript_edit_prompt(text_excerpt: str) -> str:
    """
    [PRO] Comprehensive medical manuscript edit prompt.
    Checks: scientific accuracy, AMA style, active/passive voice, redundancy, terminology consistency.
    Returns tracked-changes notation with brief comments.
    DATA SAFETY: Only paste published or internally approved text.
    """
    return f"""Edit the following medical writing excerpt for:
1. Scientific accuracy of language (flag overstated or imprecise statements)
2. AMA style compliance (numbers, abbreviations, units)
3. Active vs. passive voice (convert passive to active where appropriate)
4. Redundancy and wordiness (tighten without losing meaning)
5. Consistency of terminology (flag inconsistent drug names, endpoint names)

Return edited text with tracked changes notation and a brief comment per major edit.

{text_excerpt}

Pro tip: Use this after your own edit pass — a second-pass AI edit catches things fresh eyes miss.

🔒 DATA SAFETY: Only paste published or approved content."""


@mcp.tool()
def get_promotional_language_check_prompt(
    text_excerpt: str,
    regulatory_framework: str = "FDA"
) -> str:
    """
    [PRO] Review medical document text for promotional or non-compliant language.
    Flags superlatives, causal claims, off-label implications, comparative claims.
    Invaluable for MLR pre-review preparation.
    DATA SAFETY: Only input text approved for external use.
    """
    return f"""Review the following medical document excerpt for promotional, misleading,
or non-compliant language per {regulatory_framework} guidelines.

Flag:
- Superlatives without data support ('best,' 'superior,' 'uniquely')
- Causal claims not supported by study design
- Off-label implications
- Comparative claims without head-to-head data
- Minimization of safety information

{text_excerpt}

For each flagged item, explain the concern and suggest a compliant alternative.

Pro tip: This prompt is invaluable for medical-legal-regulatory (MLR) pre-review preparation.

🔒 DATA SAFETY: Only input text from documents approved for external use."""


@mcp.tool()
def get_statistical_reporting_check_prompt(results_text: str, journal_or_style: str = "AMA") -> str:
    """
    [PRO] Review results text for consistent, complete statistical reporting.
    Checks: effect size, 95% CI, p-value format, N per group, statistical test.
    DATA SAFETY: Only input published or approved statistical results.
    """
    return f"""Review the following results text and ensure statistical values are reported consistently
per {journal_or_style} style.

For each result, confirm:
- Effect size or difference
- 95% confidence interval
- P-value (formatted per {journal_or_style} style)
- N for each group
- Statistical test used (if not already in Methods)

{results_text}

Flag missing elements and suggest where they should be inserted.

🔒 DATA SAFETY: Only input statistical results from published papers or data approved for disclosure."""


# ─────────────────────────────────────────────────────────────
# PRO TIER — CHAPTER 9: CAREER & PROFESSIONAL DEVELOPMENT
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_cv_tailoring_prompt(job_posting: str, current_resume_bullets: str) -> str:
    """
    [PRO] Tailor a CV/resume to a medical writing job posting for ATS alignment.
    Aligns bullets to requirements, incorporates keywords, strengthens achievement language,
    and identifies gaps.
    """
    return f"""Review my resume and the following job posting and suggest specific edits to:
1. Align my bullet points with the job's key requirements
2. Incorporate relevant keywords from the posting (for ATS)
3. Strengthen achievement-based language (quantify where possible)
4. Identify gaps between my experience and the role requirements

Job posting:
{job_posting}

My current resume / key bullet points:
{current_resume_bullets}

Pro tip: ATS systems scan for exact keyword matches — don't paraphrase the job requirements, mirror them."""


@mcp.tool()
def get_cmpp_practice_questions_prompt(
    topic: str,
    num_questions: int = 5
) -> str:
    """
    [PRO] Generate CMPP certification exam practice questions with explanations.
    Topics: GPP guidelines, authorship criteria, publication ethics, statistical concepts.
    Multiple choice format with correct answer and explanation of distractors.
    """
    return f"""Generate {num_questions} practice questions for the CMPP certification exam
covering: {topic}

Format each question as:
- Question (multiple choice with 4 options)
- Correct answer
- Explanation of why the other options are incorrect
- Reference to relevant guideline or resource

Focus on application-level questions, not just recall."""


@mcp.tool()
def get_interview_prep_prompt(
    job_title: str,
    company_type: str,
    key_responsibilities: str,
    your_key_experiences: str,
    focus_area: str
) -> str:
    """
    [PRO] Prepare for a medical writing interview with role-specific questions and STAR frameworks.
    Generates 10 likely questions, answer frameworks, and 5 smart questions to ask.
    """
    return f"""I have an interview for {job_title} at {company_type}.
The role focuses on {key_responsibilities}.

Generate:
1. 10 likely interview questions specific to this role
2. For each question, a STAR-format answer framework using: {your_key_experiences}
3. 5 smart questions I should ask the interviewer

Focus especially on: {focus_area}"""


# ─────────────────────────────────────────────────────────────
# PRO TIER — BONUS: ADAPT FRAMEWORK
# ─────────────────────────────────────────────────────────────

@mcp.tool()
def apply_adapt_framework(
    base_prompt: str,
    audience: str = "",
    document_type: str = "",
    accuracy_level: str = "",
    purpose: str = "",
    tone: str = "",
    additional_modifiers: str = ""
) -> str:
    """
    [PRO] Apply the ADAPT framework to any base prompt for precision output.
    ADAPT: Audience, Document type, Accuracy level, Purpose, Tone.
    Add any combination of layers to sharpen any prompt in this library or your own.
    """
    layers = []
    if audience:
        layers.append(f"Write for {audience}.")
    if document_type:
        layers.append(f"Format as a {document_type}.")
    if accuracy_level:
        layers.append(f"Use {accuracy_level} accuracy/terminology level.")
    if purpose:
        layers.append(f"The purpose is to {purpose}.")
    if tone:
        layers.append(f"Tone: {tone}.")
    if additional_modifiers:
        layers.append(additional_modifiers)

    adapt_layers = "\n".join(layers) if layers else "No additional modifiers applied."

    return f"""ADAPT-ENHANCED PROMPT:

{base_prompt}

─── ADAPT MODIFIERS ───
{adapt_layers}

─── POWER MODIFIERS AVAILABLE ───
Add any of these to further refine output:
- "Limit your response to [X] words."
- "Write at a [medical professional / 8th grade] reading level."
- "Provide 3 alternative versions with different tones."
- "Build on the previous response to add a [SECTION]."
- "Revise your previous response to be 20% shorter without losing key data."
- "For each edit you make, briefly explain why."
- "Write in the style of papers published in [NEJM / JAMA / Blood]."
- "If you are uncertain about any fact, mark it with [VERIFY]." """


@mcp.tool()
def list_all_tools() -> str:
    """
    List all available tools in the Medical Writer's AI Toolkit with tier and description.
    Use this to discover which tools are available before calling them.
    """
    free_tools = [
        ("get_structured_abstract_prompt", "Draft a structured journal abstract (CONSORT/STROBE aligned)"),
        ("get_manuscript_outline_prompt", "Create a detailed manuscript outline with word counts"),
        ("get_peer_review_response_prompt", "Draft a point-by-point reviewer response"),
        ("get_author_invitation_email_prompt", "Write an ICMJE-aligned author invitation email"),
        ("get_linkedin_publication_post_prompt", "Draft a LinkedIn post announcing a publication"),
    ]
    pro_tools = [
        ("get_unstructured_abstract_prompt", "Convert structured abstract to flowing paragraph"),
        ("get_strengthen_conclusions_prompt", "Rewrite weak abstract conclusions to be data-anchored"),
        ("get_adapt_abstract_audience_prompt", "Rewrite abstract for a different audience"),
        ("get_introduction_section_prompt", "Draft manuscript Introduction/Background section"),
        ("get_methods_section_prompt", "Draft manuscript Methods section"),
        ("get_results_section_prompt", "Draft Results section narrative from approved data"),
        ("get_discussion_section_prompt", "Draft manuscript Discussion section"),
        ("get_rebuttal_disagreement_prompt", "Draft evidence-based rebuttal to reviewer"),
        ("get_revised_manuscript_cover_letter_prompt", "Draft cover letter for revised submission"),
        ("get_congress_abstract_prompt", "Draft ASCO/ASH/ESMO congress abstract"),
        ("get_poster_title_and_takeaways_prompt", "Generate poster titles and take-home messages"),
        ("get_oral_presentation_script_prompt", "Draft timed oral presentation script"),
        ("get_slide_deck_outline_prompt", "Create slide-by-slide deck outline"),
        ("get_speaker_notes_prompt", "Write speaker notes for a data slide"),
        ("get_moa_slide_prompt", "Explain mechanism of action for a slide"),
        ("get_publication_plan_framework_prompt", "Build a publication plan framework table"),
        ("get_gap_analysis_prompt", "Conduct literature and data gap analysis"),
        ("get_pub_plan_executive_summary_prompt", "Write pub plan exec summary for leadership"),
        ("get_journal_selection_rationale_prompt", "Recommend top 3 journals with rationale"),
        ("get_author_review_request_prompt", "Draft author review request with deadline"),
        ("get_author_revision_response_prompt", "Respond to author major revision request"),
        ("get_manuscript_edit_prompt", "Comprehensive AMA-style manuscript edit"),
        ("get_promotional_language_check_prompt", "Check for promotional/non-compliant language"),
        ("get_statistical_reporting_check_prompt", "Verify consistent statistical reporting"),
        ("get_cv_tailoring_prompt", "Tailor CV to medical writing job posting"),
        ("get_cmpp_practice_questions_prompt", "Generate CMPP exam practice questions"),
        ("get_interview_prep_prompt", "Prepare for medical writing interview"),
        ("apply_adapt_framework", "Apply ADAPT framework to any prompt for precision output"),
    ]

    output = "═══ THE MEDICAL WRITER'S AI TOOLKIT — TOOL DIRECTORY ═══\n\n"
    output += "✅ FREE TIER (5 tools)\n"
    output += "─" * 50 + "\n"
    for name, desc in free_tools:
        output += f"  • {name}\n    {desc}\n\n"

    output += "\n🔐 PRO TIER (28 tools + ADAPT framework)\n"
    output += "─" * 50 + "\n"
    for name, desc in pro_tools:
        output += f"  • {name}\n    {desc}\n\n"

    output += "\n⚠️  DATA SAFETY REMINDER\n"
    output += "─" * 50 + "\n"
    output += """Never input the following into any public AI tool:
  • Unpublished clinical trial data
  • Patient-level or identifiable data
  • Proprietary compound information or IP
  • Data covered by NDA or confidentiality agreement
  • Pre-decisional regulatory documents

Tools marked 🔒 carry elevated data-sensitivity risk.
Always comply with ICMJE, GPP4, and your organization's AI use policies."""

    return output


if __name__ == "__main__":
    mcp.run()
