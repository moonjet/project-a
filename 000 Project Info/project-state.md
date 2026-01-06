# AI Tools Directory - Project State
**Last Updated:** January 6, 2026  
**Status:** Functional MVP with minor styling refinement needed

---

## 📦 Project Overview

A modern, responsive web directory for AI tools featuring:
- **Frontend:** Pure HTML/CSS/JavaScript (no build tools required)
- **Styling:** DaisyUI 4.6.0 + Tailwind CSS
- **Data:** JSON-based (easy to update)
- **Features:** Filtering, favorites, themes, modals
- **Deployment:** Static files (works anywhere - GitHub Pages, Netlify, etc.)

---

## 📁 File Structure

```
project/
├── index.html                      # Main application file (single page)
├── ai-tools-directory.json         # Data source (12 tools, 2 categories)
├── themes.css                      # Optional custom theme overrides
├── csv_to_json.py                  # Utility: Convert CSV to JSON
├── ai-tools-template.csv           # Template for spreadsheet editing
├── patch_favorites_modal.py        # Utility: Apply styling fixes
├── perplexity-queries.md           # Saved search templates
└── README-workflow.md              # Data management guide
```

---

## ✅ Working Features

### Core Functionality
- ✅ **Tool Cards**: Display with logo, description, pricing pills, corner badges
- ✅ **Filtering**: Category filters + badge filters (recommended, new, popular, etc.)
- ✅ **Search/Filter Combo**: Multiple filters can be active simultaneously
- ✅ **Clear Filters**: One-click reset to show all tools
- ✅ **Result Count**: Shows filtered result count dynamically

### Favorites System
- ✅ **Star Toggle**: Click star on any card to favorite/unfavorite
- ✅ **Persistent Storage**: Favorites saved to localStorage
- ✅ **Favorites Modal**: Popup showing all favorited tools
- ✅ **Badge Counter**: Shows count in navbar (hidden when 0)
- ✅ **Sync Across Views**: Star state updates everywhere instantly

### Modal Popups
- ✅ **Tool Details Modal**: Shows pricing tiers, timeline, features
- ✅ **Favorites Modal**: Shows all favorited tools in grid layout
- ✅ **Gradient Headers**: Both modals have matching styled headers
- ✅ **Scrollable Content**: Long content scrolls inside modal
- ✅ **Responsive**: Modals work on mobile and desktop

### Theme System
- ✅ **30+ Themes**: Full DaisyUI theme collection
- ✅ **Theme Switcher**: Dropdown in navbar with color preview dots
- ✅ **Persistent**: Theme choice saved to localStorage
- ✅ **Smooth Transitions**: Theme changes apply instantly

### Responsive Design
- ✅ **Mobile**: Horizontal scroll for tool cards (swipe-friendly)
- ✅ **Tablet**: 2-column grid layout
- ✅ **Desktop**: 3-column grid layout
- ✅ **Sticky Elements**: Navbar and filters stay visible on scroll

### Data Management
- ✅ **CSV Workflow**: Edit in spreadsheet → Convert to JSON → Deploy
- ✅ **Python Converter**: Automated CSV to JSON conversion
- ✅ **Validation**: JSON is validated during conversion
- ✅ **Perplexity Integration**: Templates for AI-assisted updates

---

## ⚠️ Known Issues & Refinements Needed

### Minor Styling Issues (Current)
1. **Button Regression**: Some buttons reverted from flat style to default DaisyUI style
   - Affected: Possibly navbar buttons, modal action buttons
   - Original design: Flatter, more minimal appearance
   - Current: May have more prominent shadows/borders

2. **Theme Dropdown Styling**: May need consistency check

### Not Implemented Yet
- ❌ **Search Bar**: No text search functionality (only filters)
- ❌ **Sorting**: No sort by rating, name, or date added
- ❌ **Tool Comparison**: No side-by-side comparison view
- ❌ **Export Favorites**: No way to export/share favorite list
- ❌ **Deep Linking**: No URL parameters for sharing filtered views
- ❌ **Analytics**: No usage tracking

---

## 🎨 Design Decisions

### Key Design Principles
1. **Compact & Information-Dense**: Show max info in minimal space
2. **Consistent Heights**: All badges/pills use 22px height
3. **Visual Hierarchy**: Corner badges → Title → Description → Pricing
4. **Subtle Interactions**: Hover effects are gentle, not jarring
5. **Theme-Aware**: All colors use CSS variables (adapt to any theme)

### Component Sizes (CSS Variables)
```css
--corner-badge-height: 22px
--corner-btn-height: 22px
--pricing-pill-height: 22px (matches badge)
--corner-radius: 12px
```

### Color Strategy
- Uses DaisyUI color tokens (oklch variables)
- Adapts to light/dark themes automatically
- Category headers color-coded (primary, info, accent, secondary)

---

## 📊 Data Structure

### JSON Format
```json
{
  "categories": [
    {
      "name": "Category Name",
      "description": "Optional description",
      "colorScheme": "primary|info|accent|secondary",
      "tools": [
        {
          "name": "Tool Name",
          "url": "https://...",
          "description": "Brief description",
          "badges": ["web", "free", "recommended"],
          "rating": 4.8,
          "thumbnail": "https://...",
          "cornerBadge": "POPULAR",
          "allBadges": ["FAST", "POPULAR"],
          "pricing": "Free/$20/$200",
          "pricingTiers": [...],
          "timeline": [...]
        }
      ]
    }
  ]
}
```

### CSV Format
- Uses pipe `|` separator for lists (features, timeline items)
- One tool per row
- Easy to edit in Numbers/Excel/Google Sheets

---

## 🔄 Typical Workflow

### Adding New Tools
1. Open `ai-tools-data.csv` in spreadsheet app
2. Add row with tool details
3. Run: `python3 csv_to_json.py`
4. Refresh browser to see changes

### Updating Pricing (with Perplexity)
1. Ask Perplexity: "Check current pricing for [Tool1, Tool2, Tool3]"
2. Copy/paste results into spreadsheet
3. Convert CSV to JSON
4. Deploy

### Applying Fixes
1. Save current working `index.html`
2. Run patch script if available
3. Test in browser
4. Commit if working

---

## 🚀 Deployment

### Works On
- ✅ GitHub Pages
- ✅ Netlify
- ✅ Vercel
- ✅ Any static hosting
- ✅ Local file system

### Requirements
- Just serve the folder as static files
- No build process
- No server-side code
- No dependencies to install

---

## 🔧 Development Tools

### Required
- Web browser (Chrome, Firefox, Safari)
- Text editor (VS Code recommended)
- Python 3 (for CSV conversion)

### Recommended VS Code Extensions
- "Edit CSV" by janisdd (edit CSV as table)
- "Prettier" (auto-format HTML/JSON)
- "Live Server" (auto-refresh on save)

### Mac-Specific Tools
- Numbers (spreadsheet editing)
- Shortcuts app (automate conversion)

---

## 📈 Future Enhancements

### Priority 1 (High Value)
- Text search functionality
- Sort options (rating, name, newest)
- Deep linking (shareable filtered URLs)

### Priority 2 (Nice to Have)
- Tool comparison view
- Export favorites as JSON/CSV
- Import tools from various APIs
- User-submitted tools (requires backend)

### Priority 3 (Advanced)
- Analytics dashboard
- Admin panel for editing
- Multi-language support
- Community ratings/reviews

---

## 💡 Tips for Next Developer

1. **Don't modify `index.html` directly for data changes** - use the CSV workflow
2. **CSS variables are your friend** - change one variable, everything updates
3. **Test in multiple themes** - some colors may look bad in certain themes
4. **localStorage is fragile** - favorites will reset if user clears browser data
5. **Mobile first** - test on mobile, especially the horizontal scroll
6. **Keep it simple** - no build tools means easy to debug and deploy

---

## 📞 Quick Reference

### Useful Perplexity Queries
- "Check current pricing for [tools list]"
- "What new features did [tool] release recently?"
- "What are the top 5 new AI [category] tools in 2026?"

### Common Tasks
- **Add tool**: Edit CSV → Convert → Refresh
- **Fix favorites**: Check localStorage in DevTools
- **Debug filters**: Console.log activeCategory and activeBadges
- **Test themes**: Open theme dropdown, try dark/light themes

---

**Next Steps:** See `design-decisions.md` for detailed CSS documentation
