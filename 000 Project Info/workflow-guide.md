# AI Tools Directory - Workflow Guide & Session Templates
**Last Updated:** January 6, 2026  
**Purpose:** How to work efficiently with this project across multiple sessions

---

## 🔄 Data Management Workflows

### Workflow 1: Manual Entry (Quick, 1-5 tools)
**Use When:** Adding just a few tools manually

```
1. Open ai-tools-template.csv in Numbers/Excel
2. Add tool row(s) with all details
3. Save as ai-tools-data.csv
4. Run: python3 csv_to_json.py
5. Refresh browser
```

**Time:** ~5 minutes per tool

---

### Workflow 2: Perplexity-Assisted Bulk Update (10+ tools)
**Use When:** Updating pricing, features, or discovering new tools

```
1. Open Perplexity
2. Use query from perplexity-queries.md:

   "Check current pricing for these AI tools:
   [Tool1, Tool2, Tool3, Tool4, Tool5]

   For each provide:
   - All pricing tiers (name and monthly price)
   - Key features per tier
   Format as a table for spreadsheet import."

3. Copy Perplexity's table response
4. Paste into spreadsheet (Numbers/Excel)
5. Clean up formatting if needed
6. Save CSV
7. Run: python3 csv_to_json.py
8. Refresh browser
```

**Time:** ~15 minutes for 10 tools

---

### Workflow 3: Discovering New Tools
**Use Perplexity to find emerging tools:**

```
Query: "What are the top 5 new AI [CATEGORY] tools 
launched in the last 3 months of 2026?

For each provide:
- Name and official website
- Brief description (1 sentence)
- Pricing structure
- Key differentiator
- User rating if available"

Then add to CSV manually.
```

**Time:** ~20 minutes to research and add 5 new tools

---

## 📅 Recommended Update Schedule

### Daily (5 minutes)
- Check 1-2 major tools for updates
- Update if pricing/features changed

### Weekly (15-20 minutes)
- Bulk pricing check for top 10-15 tools
- Add 1-2 new promising tools
- Test site in 2-3 different themes

### Monthly (1-2 hours)
- Deep dive on all tools (50+ tools)
- Refresh all ratings
- Discover 5-10 new tools
- Clean up any dead links
- Update timeline events

### Quarterly (3-4 hours)
- Complete audit of entire directory
- Remove discontinued tools
- Reorganize categories if needed
- Major feature additions to site
- Full design review

---

## 🛠️ Development Workflows

### Making CSS Changes
```
1. Save backup: cp index.html index-backup-YYYY-MM-DD.html
2. Edit CSS in <style> section
3. Refresh browser (Cmd+R on Mac)
4. If broken: restore backup
5. If working: commit/save
```

**Pro Tip:** Use browser DevTools to test CSS live first, then copy to file

---

### Adding New Features
```
1. Create new branch/backup
2. Test feature in isolation
3. Check in multiple themes
4. Test on mobile (Chrome DevTools)
5. Verify no regressions
6. Document changes
7. Merge/save
```

---

### Debugging Issues
```
1. Open browser console (F12)
2. Check for JavaScript errors
3. Use console.log() to debug
4. Check localStorage in Application tab
5. Test in incognito (fresh state)
```

**Common Issues:**
- Favorites not saving → Check localStorage
- Filters not working → Console.log activeCategory/activeBadges
- JSON not loading → Check file name spelling
- Styles broken → Check for CSS syntax errors

---

## 🤖 Perplexity Integration

### Saved Query Templates
**Location:** `perplexity-queries.md`

### Most Useful Queries

**1. Bulk Pricing Check**
```
"Check the current pricing (January 2026) for these AI tools:
[List of tools]

For each, provide:
- All pricing tiers (name and price/month)
- 3 key features per tier
- Any recent changes

Format as a table."
```

**2. New Features Discovery**
```
"What new features and updates did [TOOL NAME] release 
in the last 3 months?

Include:
- Version numbers and release dates
- Major new features
- Pricing changes if any
- New integrations"
```

**3. New Tool Research**
```
"What are the top 5 newest AI [CATEGORY] tools 
launched in Q1 2026?

For each:
- Official website URL
- One-sentence description
- Pricing model
- Key differentiator
- User ratings if available"
```

**4. Competitive Comparison**
```
"Compare [Tool A] vs [Tool B] vs [Tool C]:

- Current pricing (all tiers)
- Key features comparison
- User ratings
- Best use cases
- Recent updates

Format as comparison table."
```

---

## 💾 File Management Best Practices

### Version Control Strategy
```
project/
├── index.html                    # Current working version
├── index-2026-01-06-stable.html  # Last known good
├── index-2026-01-05-working.html # Previous working
├── backups/
│   ├── index-2026-01-04.html
│   └── index-2026-01-03.html
```

### When to Create Backup
- ✅ Before major CSS changes
- ✅ Before adding new features
- ✅ After completing working milestone
- ✅ Before applying patches/fixes
- ✅ End of each work session

### Naming Convention
```
index-YYYY-MM-DD-descriptor.html

Examples:
- index-2026-01-06-stable.html        (Known good)
- index-2026-01-06-button-fix.html    (Feature branch)
- index-2026-01-05-pre-modal.html     (Before change)
```

---

## 📚 Starting a New Chat Session

### What to Upload
1. **Current working files:**
   - `index.html`
   - `ai-tools-directory.json`

2. **Documentation:**
   - `project-state.md`
   - `design-decisions.md`
   - This file (`workflow-guide.md`)

3. **Optional:**
   - `ai-tools-data.csv` (if working on data)
   - `perplexity-queries.md` (if doing research)

---

### Session Starter Template - General

```
I'm working on an AI Tools Directory web app. Current status:

**Tech Stack:**
- HTML/CSS/JavaScript (no build tools)
- DaisyUI 4.6.0 + Tailwind CSS
- JSON data source

**Working Features:**
- Tool cards with pricing pills, corner badges, favorites
- Category + badge filters
- Tool detail modals with pricing tiers & timelines
- Favorites modal (matches tool modal styling)
- 30+ theme switcher
- Responsive design (mobile horizontal scroll)

**Files Attached:**
- index.html (main app)
- ai-tools-directory.json (data)
- project-state.md (complete overview)
- design-decisions.md (CSS documentation)

**Current Goal:**
[Describe what you want to do]

**Specific Issue (if any):**
[Describe the problem]

Please review the attached documentation first, then help me with: [specific task]
```

---

### Session Starter Template - Bug Fix

```
AI Tools Directory - Bug Fix Session

**Issue:**
[Specific problem - e.g., "Buttons reverted to non-flat style"]

**Expected Behavior:**
[What should happen - e.g., "Buttons should be flat with minimal borders"]

**Current Behavior:**
[What's actually happening - e.g., "Buttons have shadows and prominent styling"]

**Files Attached:**
- index.html (current working version)
- design-decisions.md (shows original button design on page X)

**Context:**
- Last working version: index-2026-01-06-working.html
- Issue appeared after: [what changed]
- Affects: [which components]

**Please:**
1. Review the original design in design-decisions.md
2. Identify what changed
3. Provide a surgical fix (minimal changes)
```

---

### Session Starter Template - New Feature

```
AI Tools Directory - Adding New Feature

**Feature Request:**
[What you want to add - e.g., "Add text search functionality"]

**Current Capabilities:**
- Category filtering
- Badge filtering
- Click-to-filter from badges

**Proposed Implementation:**
[Your ideas if any]

**Files Attached:**
- index.html (current working)
- project-state.md (overview)
- design-decisions.md (for design consistency)

**Design Requirements:**
- Must work in all themes
- Mobile-friendly
- Consistent with existing filter chips
- Performance: no lag on 50+ tools

**Please help me:**
1. Design the UI component
2. Implement the search logic
3. Integrate with existing filters
4. Test plan
```

---

### Session Starter Template - Data Update

```
AI Tools Directory - Data Update Session

**Goal:**
[e.g., "Add 10 new AI coding tools" or "Update pricing for all tools"]

**Current Data:**
- X categories
- Y total tools
- Last updated: [date]

**Files Attached:**
- ai-tools-directory.json (current data)
- ai-tools-data.csv (if using CSV workflow)

**Task:**
Help me [use Perplexity to research / format data / convert CSV to JSON]

**Specific Tools:**
[List if known, or ask for discovery help]
```

---

## 🎯 Quick Reference Commands

### Python Commands
```bash
# Convert CSV to JSON
python3 csv_to_json.py

# Validate JSON
python3 -m json.tool ai-tools-directory.json

# Apply patch
python3 patch_favorites_modal.py
```

### Browser DevTools
```javascript
// Check favorites in console
JSON.parse(localStorage.getItem('favorites'))

// Clear favorites
localStorage.removeItem('favorites')

// Check current theme
localStorage.getItem('theme')

// Force theme
localStorage.setItem('theme', 'dark')
document.documentElement.setAttribute('data-theme', 'dark')

// Count visible tools
document.querySelectorAll('.tool-card').length

// Check active filters
console.log(activeCategory, activeBadges)
```

### VS Code Shortcuts (Mac)
```
Cmd+P           - Quick file open
Cmd+Shift+F     - Search in all files
Cmd+/           - Comment/uncomment
Cmd+Shift+L     - Select all occurrences
Option+Shift+F  - Format document (with Prettier)
```

---

## 🔍 Troubleshooting Guide

### Issue: JSON won't load
```
1. Check spelling: ai-tools-directory.json
2. Validate JSON: python3 -m json.tool ai-tools-directory.json
3. Check browser console for 404 error
4. Ensure file is in same directory as index.html
```

### Issue: Favorites not persisting
```
1. Check localStorage in browser (F12 → Application → Local Storage)
2. Try incognito mode (fresh state)
3. Check for JavaScript errors in console
4. Verify toggleFavorite() function exists
```

### Issue: Filters not working
```
1. Console.log activeCategory and activeBadges
2. Check if renderTools() is called after filter change
3. Verify category names match exactly (case-sensitive)
4. Check badge names in JSON match filter chip data-badge
```

### Issue: Modal won't open
```
1. Check for JavaScript errors
2. Verify tool exists in toolsData
3. Try: document.getElementById('toolModal').showModal()
4. Check if modal HTML exists in DOM
```

### Issue: Theme not saving
```
1. Check localStorage: localStorage.getItem('theme')
2. Try: changeTheme('dark') in console
3. Check if initializeThemeDropdown() runs on load
4. Verify theme name is valid DaisyUI theme
```

### Issue: Styles look broken
```
1. Check if DaisyUI/Tailwind CDN loaded (Network tab)
2. Verify data-theme attribute: document.documentElement.getAttribute('data-theme')
3. Check for CSS syntax errors (missing brackets, semicolons)
4. Try different theme (might be theme-specific issue)
```

---

## 📊 Project Metrics Tracking

### Suggested Metrics to Track
```markdown
## Directory Stats

**Last Updated:** 2026-01-06

### Content
- Total tools: 12
- Categories: 2
- Avg tools per category: 6

### Coverage
- With pricing data: 12 (100%)
- With timelines: 12 (100%)
- With ratings: 12 (100%)
- Free options: 12 (100%)

### Updates
- Last content update: 2026-01-06
- Last pricing check: 2026-01-06
- Last design update: 2026-01-06
```

---

## 🎓 Learning Resources

### Understanding the Code
1. **DaisyUI Docs**: https://daisyui.com/
2. **Tailwind Docs**: https://tailwindcss.com/
3. **OKLCH Colors**: https://oklch.com/
4. **CSS Variables**: MDN Web Docs
5. **LocalStorage API**: MDN Web Docs

### Design Inspiration
- **Tools Directories**: Product Hunt, Futurepedia
- **Card Designs**: Dribbble, Behance
- **Modal Patterns**: UI Garage

---

## 💡 Pro Tips

### Working with Perplexity
1. **Save queries as Collections** - reuse easily
2. **Ask for tables** - easier to copy to spreadsheet
3. **Batch requests** - check 5-10 tools at once
4. **Be specific** - "January 2026 pricing" not just "pricing"
5. **Request formats** - "format as CSV" or "format as table"

### CSS Efficiency
1. **Change variables first** - one change, many effects
2. **Use DevTools live editing** - test before committing
3. **Keep backups** - easy to undo experiments
4. **Comment your changes** - explain why, not what
5. **Test in dark theme** - catches hardcoded colors

### Data Management
1. **CSV is truth** - JSON is generated
2. **Version control CSV too** - track content changes
3. **Validate before deploy** - run json.tool
4. **Keep URLs updated** - check for redirects
5. **Document sources** - where you got the data

---

## 🚀 Next Steps Checklist

Before ending any session:
- [ ] Save working files with dated filename
- [ ] Update project-state.md if needed
- [ ] Note any issues discovered
- [ ] Commit/backup to safe location
- [ ] Clear browser cache if testing
- [ ] Document any new findings

Before starting next session:
- [ ] Load latest working files
- [ ] Read project-state.md for current status
- [ ] Check design-decisions.md for relevant patterns
- [ ] Prepare specific goal/question
- [ ] Have backup files ready

---

## 📞 Getting Unstuck

If you're stuck on something:

1. **Check documentation first**
   - project-state.md for what exists
   - design-decisions.md for how it's styled
   - This file for workflows

2. **Isolate the problem**
   - What worked last?
   - What changed?
   - Can you reproduce it?

3. **Start new chat with:**
   - All documentation files
   - Current broken file
   - Previous working file (if you have it)
   - Specific error message or behavior

4. **Describe clearly:**
   - Expected behavior
   - Actual behavior
   - Steps to reproduce
   - What you've tried

---

**Remember:** This project is designed to be simple and maintainable. If something feels overly complex, there's probably a simpler way!

---

**Master Prompt on Next Page** →
