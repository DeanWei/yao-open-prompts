---
title: "Outline: use language your learners understand"
category: "AI Marketing"
subcategory: "Course Marketing: Design"
source_section: "prompts/08-ai-marketing/course-marketing/course-outline.md"
author: "Yao Jingang"
version: "V1.0-en"
created: "2026-10-08"
status: "active"
tags: "Course Marketing, Design, Knowledge Products"
book_chapter: "2.2"
inputs: "Course topic, learner profile, core pain point, list of technical concepts"
output: "Learner-friendly concepts and a modular outline"
followup: "Add a learning objective and assessable assignment to each module."
---

# 2.2 Outline: use language your learners understand

## Overview

A companion prompt from Course Marketing by Yao Jingang, in the design section. Prepare: Course topic, learner profile, core pain point, list of technical concepts. Expected output: Learner-friendly concepts and a modular outline. See the [usage guide](../../../references/course-marketing-guide.en.md).

## Prompt

```text
Role:
You are a course designer and pedagogy expert. You understand how the curse of knowledge harms teaching. You turn professional concepts into logical, appealing outlines from the learner's perspective, using the point-line-plane-volume principle for structured design.

Task:
Help me optimize my course outline. I will provide its core professional concepts. Complete these steps:
1. Translate each concept from professional language into a question, pain point, or benefit learners care about.
2. Organize the translated material into 3-4 logical learning modules using classification or causal relationships, with understandable and appealing module titles.

My course information:
- Course topic: {Example: PPT design and production}
- Target learner profile: {Example: office workers who frequently prepare reports and proposals}
- Core learner pain point: {Example: making slides takes too much time and effort, the results are poor, and their boss criticizes them}
- Professional concepts I plan to teach:
  - {Example: master slides and layout design}
  - {Example: principles of color matching}
  - {Example: presenting information in charts}
  - {Example: animation effects and transition logic}
  - {Example: using presenter view}

Format:
### Step 1. Translate professional concepts into learner language
- Master slide setup -> Learner question: How can I build a slide framework in ten minutes?
- Color matching -> Pain-point question: Why do my slides look cheap?
- Continue for every concept.

### Step 2. Reorganize into logical modules
Module 1: Efficiency, make slides quickly and well
  - 1.1 [Translated title]
  - 1.2 [Translated title]
Module 2: Aesthetics, improve your slides' appearance
  - 2.1 [Translated title]
  - 2.2 [Translated title]
Module 3: Presentation, make your report persuasive
  - 3.1 [Translated title]
  - 3.2 [Translated title]
Build a complete outline with 3-4 modules.
```
