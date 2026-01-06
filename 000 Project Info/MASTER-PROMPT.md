# AI Tools Directory - Master Session Prompt
**Version:** 1.0  
**Date:** January 6, 2026  
**Use:** Copy this prompt + upload files when starting any new AI chat session

---

## 🎯 Universal Session Starter

```
I'm working on an AI Tools Directory - a single-page web application for browsing and filtering AI tools.

════════════════════════════════════════════════════════════════

PROJECT OVERVIEW:
• Tech Stack: HTML/CSS/JavaScript (vanilla, no build tools)
• Styling: DaisyUI 4.6.0 + Tailwind CSS via CDN
• Data: JSON file (ai-tools-directory.json)
• Deployment: Static files only
• Status: Functional MVP with minor refinements needed

════════════════════════════════════════════════════════════════

CORE FEATURES:
✅ Tool cards with logo panels, pricing pills, corner badges
✅ Favorite system (localStorage, star icons)
✅ Category + badge filtering (multiple filters active)
✅ Tool detail modal (pricing tiers, timeline, features)
✅ Favorites modal (matches tool modal styling)
✅ Theme switcher (30+ DaisyUI themes)
✅ Responsive (mobile horizontal scroll, desktop 3-col grid)

════════════════════════════════════════════════════════════════

DESIGN SYSTEM HIGHLIGHTS:
• Consistent heights: All badges/buttons = 22px
• Flat design: Minimal shadows, semi-transparent backgrounds
• Color system: OKLCH with DaisyUI theme variables (works in all themes)
• CSS variables: Single source for dimensions (--corner-badge-height, etc.)
• Typography: Inter font, clear hierarchy
• Animations: Subtle (2px lifts, 0.2s transitions)

════════════════════════════════════════════════════════════════

FILES ATTACHED:
[ ] index.html - Main application file
[ ] ai-tools-directory.json - Data source
[ ] project-state.md - Complete project overview
[ ] design-decisions.md - CSS documentation & design principles
[ ] workflow-guide.md - Workflows, troubleshooting, templates

════════════════════════════════════════════════════════════════

CURRENT SESSION GOAL:
[Describe what you want to do - examples below]

Examples:
• "Fix button styling regression (should be flat, not DaisyUI default)"
• "Add text search functionality to filter tools by name/description"
• "Help me update pricing data for 10 tools using Perplexity"
• "Add a new category and 5 tools to the directory"
• "Debug why favorites aren't persisting in localStorage"
• "Improve mobile responsiveness for filter chips"

════════════════════════════════════════════════════════════════

SPECIFIC ISSUE (if applicable):
[Describe the problem in detail]

Expected behavior: [What should happen]
Current behavior: [What actually happens]
Steps to reproduce: [How to see the issue]
Appears in: [Which browsers/devices/themes]

════════════════════════════════════════════════════════════════

IMPORTANT CONTEXT:
• Review design-decisions.md for CSS patterns before suggesting changes
• All colors must use DaisyUI theme variables (oklch(var(--p)), etc.)
• Maintain 22px height for badges/buttons for consistency
• Test changes in both light and dark themes
• Keep code simple - no frameworks, no build tools
• Mobile-first approach for responsive changes

════════════════════════════════════════════════════════════════

PLEASE:
1. Review the attached documentation files first
2. [Specific request - analyze/fix/add/optimize]
3. Explain your approach before implementing
4. Provide complete code (not just snippets)
5. Note any design decisions or trade-offs

Let's keep this project simple, maintainable, and beautiful! 🚀
```

---

## 📋 Quick Context Variations

### For Bug Fixes
Add after "CURRENT SESSION GOAL":
```
BUG DETAILS:
• Component affected: [buttons/cards/modals/filters]
• When it started: [after what change]
• Working version: [filename if you have backup]
• Console errors: [any JavaScript errors]
• Screenshot: [if visual issue]
```

### For New Features
Add after "CURRENT SESSION GOAL":
```
FEATURE REQUIREMENTS:
• User story: As a [user], I want [feature] so that [benefit]
• Must-have: [core functionality]
• Nice-to-have: [optional enhancements]
• Design constraints: [must match existing style/work in all themes/etc]
• Performance: [should work with 50+ tools without lag]
```

### For Data Updates
Add after "CURRENT SESSION GOAL":
```
DATA TASK:
• Action: [add/update/remove] tools
• Count: [X tools in Y categories]
• Source: [manual research / Perplexity / API / other]
• Specific tools: [list if known]
• Need help with: [research/formatting/conversion]
```

### For Design Changes
Add after "CURRENT SESSION GOAL":
```
DESIGN CHANGE:
• Component: [which UI element]
• Current state: [how it looks now]
• Desired state: [how it should look]
• Reference: [design-decisions.md section or external example]
• Must maintain: [theme compatibility/responsive behavior/etc]
```

---

## 🎨 Design System Quick Reference

Include this if making visual changes:

```
KEY DESIGN CONSTRAINTS:
• Heights: All badges/buttons = 22px (--corner-badge-height)
• Radius: 12px for corners (--corner-radius)
• Colors: Only use oklch(var(--p/s/a/b1/bc)) - no hardcoded hex
• Shadows: Minimal, only on hover (0 1px 3px default)
• Transitions: 0.2s ease for consistency
• Hover effects: Small (2px lift, 3% scale max)
• Font sizes: 0.65rem-0.85rem for UI elements
• Mobile: Horizontal scroll, 85% card width
• Buttons: Flat style (no prominent shadows/borders)
```

---

## 🔍 Common Issue Patterns

### Button Styling Regression
```
SYMPTOM: Buttons look like default DaisyUI (shadows, borders)
CAUSE: Using .btn class or lost custom button CSS
SOLUTION: Use .btn-visit / .btn-more with custom flat styles
REFERENCE: design-decisions.md → "Button System" section
```

### Theme Compatibility Issue
```
SYMPTOM: Colors look wrong in certain themes
CAUSE: Hardcoded colors instead of theme variables
SOLUTION: Replace hex/rgb with oklch(var(--token))
REFERENCE: design-decisions.md → "Color System" section
```

### Filter Not Working
```
SYMPTOM: Clicking filter doesn't filter tools
CAUSE: Category name mismatch or badge name mismatch
SOLUTION: Verify exact string match (case-sensitive)
CHECK: Console.log activeCategory and activeBadges
```

### Modal Won't Open
```
SYMPTOM: Clicking "More" does nothing
CAUSE: JavaScript error or tool not found
CHECK: Browser console for errors
VERIFY: toolsData loaded, tool exists in category
```

---

## 📚 Documentation Map

**Need to know...**
- **What exists?** → `project-state.md`
- **How it's styled?** → `design-decisions.md`
- **How to update data?** → `workflow-guide.md` → "Data Management"
- **How to fix bugs?** → `workflow-guide.md` → "Troubleshooting"
- **Original design intent?** → `design-decisions.md` → specific component
- **How to start next session?** → This file!

---

## 💾 Files Checklist

Before starting new session, attach:

**Required (for any session):**
- [ ] `index.html` (current working version)
- [ ] `project-state.md` (project overview)
- [ ] `design-decisions.md` (CSS reference)

**Recommended (depending on task):**
- [ ] `ai-tools-directory.json` (if working with data)
- [ ] `workflow-guide.md` (if need workflows/troubleshooting)
- [ ] `perplexity-queries.md` (if doing research)
- [ ] Previous working version (if fixing regression)

**Optional:**
- [ ] `ai-tools-data.csv` (if using CSV workflow)
- [ ] `themes.css` (if customizing themes)
- [ ] Screenshots (if visual issue)

---

## ⚡ Quick Start Examples

### Example 1: Fix Button Regression
```
[Use Master Prompt above]

CURRENT SESSION GOAL:
Fix button styling - they should be flat but currently look like 
default DaisyUI buttons with shadows and prominent borders.

SPECIFIC ISSUE:
• Expected: Flat buttons with minimal border, semi-transparent background
• Current: Buttons have box-shadow and solid borders
• Component: .btn-visit and .btn-more
• Reference: design-decisions.md → "Button System" → "Original Flat Design"

PLEASE:
1. Review the original flat button design in design-decisions.md
2. Identify which CSS changed (compare to original)
3. Provide complete updated CSS for .btn-visit and .btn-more
4. Ensure hover states are also flat (scale, no shadow)
```

### Example 2: Add Search Feature
```
[Use Master Prompt above]

CURRENT SESSION GOAL:
Add a text search input to filter tools by name or description.

FEATURE REQUIREMENTS:
• Search bar above category filters
• Live filtering as user types
• Works with existing category/badge filters (AND logic)
• Shows result count
• Clears with "Clear All" button
• Mobile-friendly input
• Must match existing filter chip styling

PLEASE:
1. Design the search input component (consistent with filters)
2. Add JavaScript search logic
3. Integrate with renderTools() function
4. Update clearAllFilters() to include search
5. Test that it works with 50+ tools
```

### Example 3: Update Data via Perplexity
```
[Use Master Prompt above]

CURRENT SESSION GOAL:
Update pricing data for 10 AI tools using Perplexity research.

DATA TASK:
• Tools to update: [List 10 tools]
• Need: Current pricing tiers (name, price, key features)
• Method: Guide me through Perplexity queries
• Output: Updated CSV or JSON

PLEASE:
1. Provide optimized Perplexity query for bulk pricing check
2. Show me how to format the response for CSV
3. Help update the CSV/JSON with new data
4. Validate the JSON before I deploy
```

---

## 🎯 Success Criteria

A good session should:
- ✅ Achieve the stated goal
- ✅ Maintain design consistency
- ✅ Work in all themes (light/dark minimum)
- ✅ Be mobile-responsive
- ✅ Have no JavaScript errors
- ✅ Be documented (if new feature)
- ✅ Include testing steps

---

## 🔄 End of Session Checklist

Before ending session:
- [ ] Save working version with date: `index-YYYY-MM-DD-stable.html`
- [ ] Test in 2-3 different themes
- [ ] Test on mobile (Chrome DevTools)
- [ ] Check browser console (no errors)
- [ ] Update `project-state.md` if features changed
- [ ] Note any new issues discovered
- [ ] Thank your AI assistant! 😊

---

## 📞 Emergency Recovery

If something breaks badly:
1. Restore last backup: `index-[date]-stable.html`
2. Start new session with:
   - Broken file
   - Last working backup
   - This master prompt
   - Specific error description
3. Ask for diff comparison to identify what broke

---

**This master prompt is your safety net. Use it every time you start a new chat about this project!** 🛟

═══════════════════════════════════════════════════════════════════

**Pro Tip:** Bookmark this file or keep it in a "Templates" folder for quick access!
