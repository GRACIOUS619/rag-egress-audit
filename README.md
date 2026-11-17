# Audit Finding: RAG Output Filter Bypass via Evasion Classes

**Finding ID:** RAG-2026-001
**Severity:** HIGH
**Auditor:** Gracious
**Component:** RAG Assistant - Output Sanitization Pipeline
**Status:** Remediated
**Regression Test:** `tests/test_rag_egress_regression.py`
`

## 1. Executive Summary
The output filter used a blocklist regex approach to prevent markdown images and HTML tags from reaching the frontend. Blocklist filtering is insufficient. An attacker can craft evasion payloads that bypass specific regex patterns, triggering an outbound network request (data exfiltration). We demonstrated the bypass with 5 evasion classes, then remediated by replacing the blocklist with an allowlist sanitizer + DOMPurify + CSP. 

## 2. Vulnerability Details
The original filter attempted to enumerate bad patterns: only stripping `<img>`, `<iframe>`, and `.png` URLs. An attacker can use extensionless URLs or `<video>` tags to bypass this.
- **Class 4:** Extensionless URL (FAIL on blocklist)
- **Class 5:** Alternate Media Tag `<video>` (FAIL on blocklist)

## 3. Remediation
Switched to an allowlist sanitizer: strips ALL markdown images, ALL HTML tags, and ALL bare external URLs. Paired with CSP headers and DOMPurify frontend sanitization.

## 4. Proof - Regression Test
Run: `python -m unittest tests/test_rag_egress_regression.py -v`
The blocklist tests fail as expected (proving the vulnerability). The allowlist tests pass (proving the fix).

## 5. Architectural Lesson
Blocklists fail in adversarial environments. Allowlists and strict sanitization are required.
