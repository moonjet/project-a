# AI Tools Directory - Data Management Workflow

## 📁 Files in This Project

- `ai-tools-data.csv` - Your main data file (edit this in Numbers/Excel)
- `csv_to_json.py` - Converter script (CSV → JSON)
- `ai-tools-directory.json` - Generated JSON (used by website)
- `index.html` - Your website
- `perplexity-queries.md` - Saved Perplexity search templates

## 🚀 Quick Start

### 1. Edit Data in Spreadsheet
- Open `ai-tools-data.csv` in Numbers (Mac) or Excel
- Add/edit tools
- Save as CSV

### 2. Convert to JSON
```bash
python3 csv_to_json.py
```

### 3. Test Website
- Open `index.html` in browser
- Check that new tools appear

## 📊 CSV Format Guide

### Text Fields
- Simple text: Just type normally
- With commas: Use quotes "like this, with comma"

### List Fields (use | separator)
- Features: `Feature 1|Feature 2|Feature 3`
- Timeline dates: `2024-01|2024-06|2025-01`

### Badge Fields (use , separator)
- Badges: `web,free,popular`
- All badges: `BEST,TOP,NEW`

## 🔄 Update Workflow

### Option A: Manual Update (10 min)
1. Open CSV in Numbers
2. Edit row(s)
3. Save
4. Run `python3 csv_to_json.py`
5. Refresh browser

### Option B: Perplexity-Assisted (15 min)
1. Ask Perplexity (see perplexity-queries.md)
2. Copy/paste results into CSV
3. Run converter
4. Done!

## 🤖 Using Perplexity for Updates

### Single Tool Update
Ask: "What are the current pricing tiers for [Tool Name]?"
Copy the answer into your CSV

### Bulk Update (10+ tools)
Ask: "Check pricing for: Tool1, Tool2, Tool3, Tool4, Tool5"
Perplexity will format as table - easy to copy!

### New Feature Discovery
Ask: "What new features did [Tool Name] add in the last 3 months?"
Add to timeline columns

## 💡 Pro Tips

### Mac Shortcuts Automation
Create a Shortcut that:
1. Opens Terminal
2. Runs `cd ~/path/to/project && python3 csv_to_json.py`
3. Shows notification when done

Now you can convert with one click!

### VS Code Setup
Install these extensions:
- "Edit CSV" - Edit CSV as table in VS Code
- "Prettier" - Auto-format JSON
- "Live Server" - Auto-refresh browser when files change

### Perplexity Collections
Save your common queries as a Collection:
- "AI Tools Pricing Check"
- "New Features Roundup"  
- "Ratings Update"

Access them anytime from the Collections menu!

## 🎯 Recommended Schedule

**Daily (5 min):** Check one tool manually for major updates
**Weekly (15 min):** Bulk pricing check for top 10 tools
**Monthly (1 hour):** Deep dive - new tools, ratings, features
**Quarterly (3 hours):** Complete audit and refresh

## 🆘 Troubleshooting

### CSV Won't Convert
- Check for missing commas in rows
- Ensure no extra blank rows
- Verify quotes around text with commas

### JSON Won't Load in Browser
- Open browser console (F12)
- Look for error message
- Run: `python3 -m json.tool ai-tools-directory.json`
  (This validates your JSON)

### Tool Doesn't Appear
- Check category name matches exactly
- Verify CSV was saved
- Re-run converter script

## 📧 Need Help?
Check the browser console first - it shows detailed errors!
