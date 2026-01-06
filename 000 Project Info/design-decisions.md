# AI Tools Directory - Design System & CSS Documentation
**Last Updated:** January 6, 2026  
**Purpose:** Complete reference for all design decisions and CSS techniques

---

## 🎨 Design Philosophy

### Core Principles
1. **Compact Information Density** - Maximum info in minimum space
2. **Consistent Sizing** - All similar elements share exact dimensions
3. **Subtle Elegance** - Professional without being flashy
4. **Theme Adaptability** - Works perfectly in all 30+ DaisyUI themes
5. **Mobile-First Responsive** - Optimized for touch and small screens

### Visual Hierarchy
```
Corner Badge (top-left) → Logo Panel → Title → Description → Pricing Pills → Action Buttons
```

---

## 📐 CSS Architecture

### Technology Stack
- **Tailwind CSS**: Utility-first classes via CDN
- **DaisyUI 4.6.0**: Component library built on Tailwind
- **CSS Custom Properties**: For consistent sizing/spacing
- **OKLCH Colors**: Modern color space with DaisyUI tokens

### File Organization
```css
<style> in index.html contains:
1. CSS Variables (:root)
2. Global Styles (body, typography)
3. Layout Components (navbar, footer)
4. Filter System Styles
5. Card Components
6. Modal Styles
7. Utility Classes
```

---

## 🔧 CSS Variables Reference

### Core Sizing Variables
```css
:root {
    /* Badge & Button Heights - ALL 22px for consistency */
    --corner-badge-height: 22px;        /* Top-left corner badges */
    --corner-btn-height: 22px;          /* Visit/More buttons */
    --pricing-pill-height: 22px;        /* Implied, uses badge height */

    /* Badge Dimensions */
    --corner-badge-min-width: 54px;     /* Minimum badge width */
    --corner-badge-max-width: 120px;    /* Maximum before truncate */
    --corner-badge-padding: 0 0.6rem;   /* Horizontal padding */
    --corner-badge-font-size: 0.65rem;  /* ~10.4px */

    /* Button Dimensions */
    --corner-btn-width: 52px;           /* "More" button width */
    --corner-btn-padding: 0.25rem;      /* Button padding */
    --visit-btn-min-width: 120px;       /* "Visit" button minimum */
    --visit-btn-max-width: 320px;       /* "Visit" button maximum */

    /* Border Radius */
    --corner-radius: 12px;              /* Consistent rounded corners */

    /* Logo Panel */
    --logo-panel-width: 26%;            /* Left side of tool card */

    /* Animations */
    --animation-speed-fast: 0.2s;       /* Quick transitions */
}
```

### Why These Values?
- **22px height**: Visible but not dominant, same as filter chips
- **12px radius**: Modern, not too rounded (not 16px, not 8px)
- **26% logo panel**: Shows logo clearly without dominating card
- **0.65rem font**: Readable on all screens, fits in 22px height

---

## 🎴 Component Design Details

### Tool Card Anatomy
```
┌─────────────────────────────────────────┐
│ [BADGE]  26% Logo Panel    Top-Right ★ │
│          (Flex column)                  │
│          Logo (centered)                │
│          [Visit Button] ───────────────┤
│ Title (bold, 1.125rem)         74%     │
│ Description (0.875rem, gray)   Content │
│ [Pricing Pills 22px]           Panel   │
│                       [More Button]    │
└─────────────────────────────────────────┘
```

### Design Decisions for Cards
1. **Logo Panel Separation**: 26% creates strong visual anchor
2. **Visit Button at Bottom of Logo Panel**: Natural "go to site" action
3. **Pricing After Description**: Logical reading order
4. **More Button Bottom-Right**: Expected action button position
5. **Favorite Star Top-Right**: Standard favorite icon placement

### Card Styling
```css
.tool-card {
    min-height: 180px;                    /* Consistent card height */
    background: linear-gradient(...);     /* Subtle gradient */
    border: 1px solid oklch(...);         /* Theme-aware border */
    box-shadow: 0 1px 3px oklch(...);     /* Minimal shadow */
    transition: all 0.2s ease;            /* Smooth hover */
}

.tool-card:hover {
    transform: translateY(-2px);          /* Lift effect */
    box-shadow: 0 4px 12px oklch(...);    /* Enhanced shadow */
}
```

**Why these choices?**
- **180px min-height**: Accommodates 3 pricing tiers + text
- **Subtle gradient**: Depth without distraction
- **2px lift on hover**: Feels interactive, not jarring
- **oklch() colors**: Consistent across all themes

---

## 🏷️ Badge System

### Corner Badges (Top-Left)
```css
.corner-badge {
    position: absolute;
    top: -2px;                            /* Extends beyond card edge */
    left: -2px;
    border-bottom-right-radius: 12px;     /* Only bottom-right curved */
    height: 22px;
    min-width: 54px;
    max-width: 120px;
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;               /* Slight spacing */
    cursor: pointer;                      /* Clickable to filter */
}
```

**Badge Color Mapping:**
- `badge-popular` / `badge-best`: Red (--er)
- `badge-new`: Yellow (--wa)
- `badge-fast`: Blue (--in)
- `badge-value`: Purple (--s)

**Why clickable?** Quick way to filter by that badge type

### Pricing Pills (Horizontal Bar)
```css
.pricing-pills {
    display: flex;
    gap: 0;                               /* No gap between pills */
    height: 22px;                         /* Matches badge height */
    margin-top: 0.5rem;
}

.pricing-pill {
    flex: 1;                              /* Equal width distribution */
    font-size: 0.65rem;
    font-weight: 700;
    /* First child: left rounded corners */
    /* Last child: right rounded corners */
    /* Middle children: no rounding (seamless bar) */
}
```

**Color Scheme:**
- `free`: Green (--su)
- `tier-1`: Primary (--p)
- `tier-2`: Secondary (--s)
- `tier-3`: Accent (--a)

**Why this design?**
- **No gaps**: Creates unified pricing bar visual
- **Flexible**: Adapts to 1-4 pricing tiers automatically
- **Color progression**: Free (green) → Paid (primary → secondary → accent)

---

## 🎯 Button System

### Original Flat Design (Before Regression)
```css
.btn-visit, .btn-more {
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 0.7rem;
    border: 1px solid oklch(var(--bc) / 0.1);     /* Subtle border */
    background: oklch(var(--b3) / 0.8);           /* Flat background */
    color: oklch(var(--bc));
    transition: all 0.2s ease;
}

/* Hover: Subtle scale + background change (NOT shadow) */
.btn-visit:hover, .btn-more:hover {
    transform: scale(1.03);
    background: oklch(var(--b3));                 /* Slightly more opaque */
}
```

**Key Characteristics of Flat Design:**
- ✅ No box-shadow
- ✅ Minimal border (10% opacity)
- ✅ Semi-transparent background
- ✅ Hover = scale + background opacity (not shadow)

**What to AVOID (DaisyUI defaults):**
- ❌ `.btn` class (adds shadows, padding, borders)
- ❌ `.btn-primary` (too prominent)
- ❌ Default DaisyUI button hover (adds shadows)

### Button Positioning
```css
.btn-visit {
    /* Positioned at bottom of 26% logo panel */
    border-top-right-radius: 12px;        /* Matches corner radius */
    border-bottom-left-radius: 0.5rem;
    height: 22px;
    min-width: 120px;
}

.btn-more {
    /* Positioned at bottom-right of card */
    border-top-left-radius: 12px;
    border-bottom-right-radius: 0.5rem;
    width: 52px;
    height: 22px;
}
```

**Why asymmetric rounding?** Creates visual flow and fits card corners

---

## 🌈 Color System

### Using OKLCH with DaisyUI
```css
/* Basic usage */
background: oklch(var(--b1));              /* Base background */
color: oklch(var(--bc));                   /* Base content (text) */
border: 1px solid oklch(var(--bc) / 0.1); /* Border at 10% opacity */

/* Computed color manipulation */
background: oklch(from oklch(var(--b1)) calc(l * 0.97) c h);
/* Darkens base by 3% - creates subtle gradients */
```

### DaisyUI Color Tokens
- `--b1`, `--b2`, `--b3`: Background layers (b1 lightest)
- `--bc`: Base content (text on background)
- `--p`, `--pc`: Primary color and its content
- `--s`, `--sc`: Secondary color and its content
- `--a`, `--ac`: Accent color and its content
- `--n`, `--nc`: Neutral color and its content
- `--in`, `--su`, `--wa`, `--er`: Info, Success, Warning, Error

### Category Color Mapping
```css
.category-header.color-primary h2 { color: oklch(var(--p) / 0.85); }
.category-header.color-info h2 { color: oklch(var(--in) / 0.85); }
.category-header.color-accent h2 { color: oklch(var(--a) / 0.85); }
.category-header.color-secondary h2 { color: oklch(var(--s) / 0.85); }
```

**Why 0.85 opacity?** Softer than full opacity, better hierarchy

---

## 🔍 Filter System Design

### Filter Chips (Categories)
```css
.filter-chip {
    padding: 0.35rem 0.85rem;
    border-radius: 0.5rem;               /* More rounded than cards */
    font-size: 0.8rem;
    border: 2px solid oklch(var(--bc) / 0.1);
    background: oklch(var(--b2) / 0.5); /* Semi-transparent */
    transition: all 0.2s ease;
}

.filter-chip.active {
    background: oklch(var(--p));         /* Solid primary */
    color: oklch(var(--pc));
    border-color: oklch(var(--p));
}
```

**Design Logic:**
- Inactive: Subtle, transparent
- Active: Bold, solid color
- Clear visual feedback

### Badge Filters (Secondary)
```css
.badge-chip {
    /* Smaller than category chips */
    padding: 0.3rem 0.65rem;
    border-radius: 0.4rem;
    font-size: 0.72rem;                  /* Slightly smaller */
    border: 1.5px solid ...;             /* Thinner border */
}

.badge-chip.active {
    background: oklch(var(--s));         /* Secondary (not primary) */
}
```

**Why secondary color?** Visual distinction from category filters

---

## 🪟 Modal Design

### Modal Structure
```
┌─────────────────────────────────────────┐
│ [Header - Gradient Background]         │ ← 1rem padding
│ Logo | Title & Description             │
├─────────────────────────────────────────┤
│ [Stats Bar - Light Background]         │ ← Grid layout
│ Rating | Category | Access Type        │
├─────────────────────────────────────────┤
│ [Scrollable Content Area]              │ ← max-height calc
│ • Pricing Grid                         │
│ • Feature Badges                        │
│ • Timeline                              │
│ ...scrolls...                           │
├─────────────────────────────────────────┤
│ [Actions Bar - Fixed Bottom]           │
│             [Add to Fav] [Visit →]     │
└─────────────────────────────────────────┘
```

### Modal Sizing
```css
.modal-box {
    max-width: 900px;                    /* Wide enough for content */
    width: 90vw;                         /* Responsive */
    max-height: 85vh;                    /* Never taller than viewport */
    padding: 0;                          /* Sections add their own */
    overflow: hidden;                    /* Scroll inside sections */
}

.modal-content-scroll {
    max-height: calc(85vh - 300px);      /* Account for header + stats + actions */
    overflow-y: auto;
    padding: 1.5rem;
}
```

**Why these values?**
- 900px: Comfortable reading width, fits 3-column pricing grid
- 85vh: Leaves space for browser chrome
- calc(): Ensures header/footer always visible, content scrolls

### Modal Header Gradient
```css
.modal-header {
    background: linear-gradient(
        135deg,
        oklch(var(--p) / 0.1) 0%,        /* Primary at 10% */
        oklch(var(--s) / 0.05) 100%      /* Secondary at 5% */
    );
    border-bottom: 1px solid oklch(var(--bc) / 0.08);
}
```

**Why subtle gradient?** Professional, not distracting from content

---

## 📱 Responsive Design

### Breakpoints
```css
/* Mobile: < 768px */
@media (max-width: 767px) {
    .category-tools-grid {
        display: flex !important;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
    }

    .tool-card {
        flex: 0 0 85%;                   /* Each card 85% of viewport */
        scroll-snap-align: start;
    }
}

/* Tablet: 768px - 1023px */
@media (min-width: 768px) {
    .category-tools-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
    .category-tools-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

### Mobile Optimizations
1. **Horizontal Scroll**: Natural swipe gesture on mobile
2. **Scroll Snap**: Cards align perfectly when scrolling stops
3. **85% Width**: Shows part of next card (indicates more content)
4. **Hide Scrollbar**: Cleaner appearance, gesture is intuitive

---

## ✨ Animation & Transitions

### Hover Effects
```css
/* Subtle lift on cards */
.tool-card:hover {
    transform: translateY(-2px);         /* Lift 2px */
    box-shadow: 0 4px 12px oklch(...);   /* Enhanced shadow */
}

/* Scale on buttons */
.btn-visit:hover, .btn-more:hover {
    transform: scale(1.03);              /* 3% larger */
}

/* Favorite star bounce */
.favorite-corner:hover .favorite-star {
    transform: scale(1.15) rotate(10deg);/* Playful effect */
}

/* Badge highlight */
.corner-badge:hover {
    transform: scale(1.04);
    filter: brightness(1.08);            /* Slight glow */
}
```

**Timing:** All transitions use `0.2s ease` for consistency

### Why These Effects?
- **2px lift**: Noticeable but not jarring
- **Scale 1.03**: Feels responsive, not aggressive
- **Rotate 10deg**: Playful for star icon
- **Brightness 1.08**: Subtle glow effect

---

## 🎭 Theme Compatibility

### Ensuring Cross-Theme Consistency
```css
/* ✅ GOOD: Uses theme variables */
background: oklch(var(--b1));
color: oklch(var(--bc));
border: 1px solid oklch(var(--bc) / 0.1);

/* ❌ BAD: Hardcoded colors */
background: #ffffff;
color: #000000;
border: 1px solid #cccccc;
```

### Testing Themes
**Light themes to test:**
- light (default)
- cupcake (pastel)
- corporate (blue)
- winter (white)

**Dark themes to test:**
- dark (default dark)
- synthwave (neon)
- dracula (purple)
- night (blue-black)

**Quirky themes to test:**
- cyberpunk (yellow)
- halloween (orange)
- forest (green)
- valentine (pink)

---

## 🔍 Typography

### Font Stack
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

**Why Inter?**
- Modern, professional
- Excellent readability at small sizes
- Variable font (loaded from Google Fonts)
- Fallbacks to system fonts if CDN fails

### Size Scale
```css
/* Headers */
h1 (hero-title): 2rem (32px) → 1.5rem mobile
h2 (category): 1.5rem (24px) → 1.25rem mobile
h3 (card title): 1.125rem (18px)

/* Body */
description: 0.875rem (14px)
stats: 0.85rem
badges: 0.7-0.75rem
buttons: 0.65-0.7rem
```

**Logic:** Clear hierarchy, but nothing too small to read

### Letter Spacing
```css
h1, h2, h3 { letter-spacing: -0.02em; }  /* Tighter for headers */
.corner-badge { letter-spacing: 0.05em; } /* Looser for uppercase */
```

---

## 💾 LocalStorage Usage

### Data Stored
1. **Favorites**: `localStorage.getItem('favorites')`
   - Format: Array of strings `["CategoryName::ToolName", ...]`
   - Updated: On star click

2. **Theme**: `localStorage.getItem('theme')`
   - Format: String theme name
   - Updated: On theme change

### Why LocalStorage?
- ✅ Persists across page reloads
- ✅ No backend required
- ✅ Simple to implement
- ⚠️ Cleared if user clears browser data
- ⚠️ Domain-specific (won't transfer across domains)

---

## 🚀 Performance Considerations

### Optimization Techniques Used
1. **Single HTML File**: No additional requests
2. **CDN Resources**: Fast delivery of Tailwind/DaisyUI
3. **Minimal JavaScript**: ~500 lines, no framework
4. **CSS Variables**: Faster than recalculating styles
5. **No Heavy Images**: Tool thumbnails via favicons

### Load Time
- **First Load**: ~500-800ms (depending on CDN)
- **Cached Load**: ~50-100ms
- **JSON Load**: <50ms (small file)

---

## 📝 CSS Best Practices Used

1. **Mobile-First**: Base styles for mobile, `@media` for desktop
2. **CSS Variables**: Single source of truth for dimensions
3. **Theme Variables**: All colors from DaisyUI tokens
4. **BEM-ish Naming**: `.tool-card`, `.modal-box`, `.filter-chip`
5. **Utility Classes**: Tailwind for spacing, layout
6. **Custom Classes**: For complex components
7. **Specificity Management**: Avoid `!important` except overrides

---

## 🎯 Next Session Quick Start

### Common CSS Tasks

**Change All Badge Heights:**
```css
:root {
    --corner-badge-height: 24px;  /* Change this one value */
}
```

**Adjust Card Hover Effect:**
```css
.tool-card:hover {
    transform: translateY(-3px);  /* More lift */
    box-shadow: 0 6px 16px ...;   /* More shadow */
}
```

**Make Buttons Flatter:**
```css
.btn-visit, .btn-more {
    border: 1px solid oklch(var(--bc) / 0.05);  /* Less visible border */
    background: oklch(var(--b3) / 0.6);         /* More transparent */
    box-shadow: none;                            /* Remove any shadow */
}
```

**Change Modal Width:**
```css
.modal-box {
    max-width: 1000px;  /* Wider modals */
}
```

---

**Next Document:** See `workflow-guide.md` for data management and Perplexity integration
