---
id: web-system-architecture
status: proposal
date: 2026-08-28
course_slot: 1
---

# Course 1 Proposal

## Course Name

Basic Fundamentals of Web System Architecture
Working title: *How a Web System Works: From Click to Database and Back*

## Target Learner

A salesperson with no technical background who needs to understand web development and system architecture at an
overview level. Students and career-switchers are served by three optional labs, not a second track.

## Why This Course

- **Reuse — the strongest reason.** The mental models here (server, API, database, request and response, how the
  pieces fit together) are the ones later courses assume a learner already has. Most of what we write for this
  course gets reused rather than rewritten.
- **It gives learners the basic model first.** More specific technical or tool-focused courses land better once
  someone can picture what a request does and where data lives.
- **It fits the learner profile we have.** Overview level, for someone who will never write code.
- **It works within current platform limits.** Nothing here waits on a platform change.

**Progression.** Course 1 provides foundation knowledge the rest of the curriculum can build on. Later courses can
assume the learner understands how a request reaches a server, where data lives, and what an API is, and spend
their time on their own subject.

## Course Goal

A correct mental model of how a web system works: what runs on their machine and what does not, what travels in a
request and why it takes time, where data lives and what it costs to change it, and how APIs and third-party
services fit in. Conversant and correctly modelled, not able to build.

## Course Structure

4 weeks · about 2–3 hours a week · 4 sections · 20 lessons — 13 Lectures, 4 Quizzes, 3 optional Labs.

| Section | Covers | Lessons |
|---|---|---|
| S1 · The Two Machines | the client/server split and the trust boundary | 3 lectures, 1 quiz, 1 optional lab |
| S2 · The Round Trip | what travels in a request, and why it is slow | 3 lectures, 1 quiz, 1 optional lab |
| S3 · Where the Data Lives | state, sessions, and the cost of changing data | 3 lectures, 1 quiz, 1 optional lab |
| S4 · The Pieces Around It | APIs, third-party services, and AI | 4 lectures, 1 cumulative quiz |

## Lesson 13 Sample

Lesson 13 is one generated sample lesson, used to test whether the current knowledge base can produce publishable
beginner content. It is not finished course material.

The scenario is "Can you just add a field?" — a client asks for a new database field and assumes it is a small
text change. The lesson explains why changing database structure affects more than one value.

The independent review of this sample is still pending.

## What We Deliberately Are Not Teaching

| Not taught | Why |
|---|---|
| HTML, CSS, JavaScript syntax | Architecture course; this learner will never write any |
| Any framework, cloud provider or pricing | Vocabulary churn; dates the course within a quarter |
| SQL syntax | We model a query without teaching one, and SQL cannot run on the platform |
| git, environments, local setup | Developer culture, not a need for this learner |
| DNS, TCP, anything below HTTP | One layer below the useful abstraction |
| Security beyond the trust boundary | Partial coverage is worse than none |
| Prompt engineering | Lesson 19 is about what AI changes architecturally |

The charter carries the full list, including deployment and HTTPS detail.

## Platform Fit

- A lesson is exactly one type: lecture, quiz, or lab. A lecture cannot contain a question.
- Labs run as JavaScript only, graded by exact printed output. Free learners get 10 runs a day, so the labs are
  small and optional.
- Quizzes are single-answer multiple choice with no field to explain a wrong answer, so the wrong answers carry the
  teaching. The pass mark is a count of correct questions, not a percentage.
- Diagrams are mermaid text and render in the learner app, so no image hosting is needed.

## Current Status

**Content and functional validation complete; final knowledge-base cleanup in progress.** All 20 lessons are
written and seeded. Functional browser smoke testing passed, the responsive Lab layout issues were fixed and
verified, and the learner-facing content review is complete with its priority gating fixes applied. The quiz
assessment blockers — the predictable correct-answer position and the learner answer-key API leak — are fixed, and
both publish blockers were verified on the deployed server. The Lesson 13 comparison was completed and its feedback
already drove the gating and content changes.

**Remaining after this cleanup** — the knowledge-base alignment in this pass (charter and platform-note
corrections, the candidate-list trim, and the open Q7 teaching-sequence decision, which awaits an owner statement),
then the §9 human sign-off on the L1/L2 opinion notes, and moving this proposal out of `proposal` status once that
sign-off lands.

## Open Questions

1. Course order. It affects how soon the knowledge base pays for itself.
2. Which candidate notes get cut. One overlaps a teaching note we already wrote.
3. Two platform limits shape what we can assess: labs are JavaScript-only, and there is no field to explain a
   wrong quiz answer.
4. Whether to wait for the Lesson 13 review before generating more lessons, or start S3 in parallel.
