# FraudShield AI Frontend - Implementation Notes

## Quick Reference for Developers

### Color System Usage

#### Primary Theme Colors
```css
/* Use for main headings, buttons, primary actions */
color: var(--primary-color);        /* #0066cc */

/* Use for button hover/dark states */
background-color: var(--primary-dark); /* #004a99 */
```

#### Status Indicators
```css
/* Success/Low Risk */
color: var(--success-color);        /* #00b366 - Green */

/* Warning/Medium Risk */
color: var(--warning-color);        /* #ff9900 - Orange */

/* Error/High Risk/Fraud */
color: var(--danger-color);         /* #cc0000 - Red */

/* Information */
color: var(--info-color);           /* #0891b2 - Cyan */
```

#### Text Hierarchy
```css
/* Main body text, highest priority */
color: var(--text-primary);         /* #1a1a1a - 15:1 contrast */

/* Labels, descriptions, secondary content */
color: var(--text-secondary);       /* #4a4a4a - 10.5:1 contrast */

/* Tertiary info, metadata, timestamps */
color: var(--text-muted);           /* #7a7a7a - 7.5:1 contrast */
```

#### Background Hierarchy
```css
/* White cards, input fields, main content areas */
background-color: var(--bg-primary);    /* #ffffff */

/* Subtle sections, feature groups, alternating rows */
background-color: var(--bg-secondary);  /* #f8f9fa */

/* Disabled states, inactive elements */
background-color: var(--bg-tertiary);   /* #f0f2f5 */

/* Page background, main container */
background-color: var(--bg-page);       /* #f5f6f8 */
```

---

## Component-Specific Guidelines

### TransactionForm Component

#### Form Structure
1. **Title**: Use `h2` with primary color
2. **Description**: Use secondary text color
3. **Feature Groups**: Light background (`--bg-secondary`) with subtle borders
4. **PCA Explanation**: Only show above first PCA section with:
   - Left border: `4px solid var(--primary-color)`
   - Background: `rgba(37, 99, 235, 0.05)` (light blue)
   - Text: `var(--text-secondary)` (secondary grey)

#### Input Field Styling
```css
/* Always use: */
background-color: white;              /* Not --bg-secondary */
color: var(--text-primary);            /* Dark text */
border: 1px solid var(--border-light);

/* Focus state: */
border-color: var(--primary-color);
border-width: 2px;
box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);

/* Placeholder (always visible): */
::placeholder { color: #9ca3af; opacity: 1; }

/* Caret (typing cursor): */
caret-color: var(--text-primary);
```

#### Button States
```
Normal: white bg, light border, primary text
Hover:  --bg-tertiary bg, primary border, primary text
Active: --bg-secondary bg, slight shadow
```

#### Responsive Grid
```
Desktop: grid-template-columns: repeat(auto-fit, minmax(140px, 1fr))
Tablet:  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr))
Mobile:  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr))
```

---

### ResultsDisplay Component

#### Result Sections
```
Fraud Detection:   3px top border = var(--primary-color) [#0066cc]
Risk Assessment:   3px top border = var(--warning-color) [#ff9900]
Investigation:     3px top border = var(--info-color) [#0891b2]
```

#### Result Item Cards
```
Normal State:
  background: #fafbfc (light grey)
  border: 1px solid var(--border-light)

Hover State:
  background: white
  border-color: var(--primary-color)
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04)
```

#### Badge Styling
```
Fraud/High Risk:    bg: rgba(204, 0, 0, 0.1),  text: #cc0000
Legitimate/Low Risk: bg: rgba(0, 179, 102, 0.1), text: #00b366
Medium Risk:        bg: rgba(255, 153, 0, 0.1), text: #ff9900
```

#### Status Indicators
```
ALWAYS use text labels WITH color:
  ✓ Green box + "Low Risk" text
  ✓ Orange box + "Medium Risk" text
  ✓ Red box + "High Risk" text
  ✗ Color alone (not accessible)
```

#### Gradients
```css
/* Probability bar gradient: green → orange → red */
background: linear-gradient(90deg, 
  #00b366 0%,    /* Green (low risk) */
  #ff9900 50%,   /* Orange (medium risk) */
  #cc0000 100%   /* Red (high risk) */
);
```

---

## Form Field Labels Mapping

### Display Labels vs API Field Names

| Display Label | API Field Name | Type | Example |
|---|---|---|---|
| Transaction Time (seconds) | Time | Number | 0 to 86400 |
| PCA Component 1 (V1) | V1 | Number | -2.5 to 2.5 |
| PCA Component 2 (V2) | V2 | Number | -2.5 to 2.5 |
| ... | ... | ... | ... |
| PCA Component 28 (V28) | V28 | Number | -2.5 to 2.5 |
| Transaction Amount | Amount | Number | 0.01 to 25691.16 |

### Label Mapping Function
```javascript
const getFieldLabel = (fieldName) => {
  if (fieldName === 'Time') return 'Transaction Time (seconds)';
  if (fieldName === 'Amount') return 'Transaction Amount';
  const num = fieldName.replace('V', '');
  return `PCA Component ${num} (${fieldName})`;
};
```

**Important**: The form maintains `formData` with API field names internally. 
Display labels are only for the UI. The API request payload is always:
```json
{
  "Time": 0,
  "V1": -1.36, "V2": -0.07, ... "V28": -0.002,
  "Amount": 149.62
}
```

---

## Accessibility Checklist

When adding new features or components:

- [ ] Text color meets WCAG AA minimum (7:1 contrast)
- [ ] Interactive elements visible on focus
- [ ] Color + text for all status indicators (not color-alone)
- [ ] Proper semantic HTML (`<label>`, `<button>`, etc.)
- [ ] Alt text for any images or icons
- [ ] Keyboard navigation support (Tab, Enter, Escape)
- [ ] Form validation messages clear
- [ ] Error states visible and readable
- [ ] Font sizes minimum 14px for body text
- [ ] Touch targets minimum 44px for mobile

---

## Responsive Breakpoints

```css
/* Mobile First Approach */

/* Mobile (default, < 768px) */
/* Single column layout */
/* Full-width buttons */
/* Smaller padding and margins */

@media (min-width: 768px) {
  /* Tablet: 768px - 1024px */
  /* 1-2 column layouts */
  /* Adjust padding */
}

@media (min-width: 1024px) {
  /* Tablet Large: 1024px - 1400px */
  /* 2 column layouts */
  /* Standard padding */
}

@media (min-width: 1400px) {
  /* Desktop: 1400px+ */
  /* 2 column layouts with max-width constraint */
  /* Full padding and spacing */
}
```

---

## Common CSS Patterns

### Card Styling
```css
.card {
  background-color: var(--bg-primary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: var(--spacing-lg);
  box-shadow: var(--shadow-md);
  transition: all var(--transition-normal);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
```

### Button Styling
```css
.btn {
  padding: var(--spacing-md) var(--spacing-lg);
  border: none;
  border-radius: var(--radius-md);
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition-normal);
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: var(--primary-dark);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
  transform: translateY(-2px);
}
```

### Input Field Styling
```css
input {
  background-color: white;
  color: var(--text-primary);
  border: 1px solid var(--border-light);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
}

input:focus {
  outline: none;
  border-color: var(--primary-color);
  border-width: 2px;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

input::placeholder {
  color: #9ca3af;
  opacity: 1;
}
```

### Grid Layout
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--spacing-lg);
}

@media (max-width: 1024px) {
  .grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: var(--spacing-md);
  }
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
```

---

## Common Mistakes to Avoid

### ❌ Don't

```css
/* Don't use hardcoded colors */
color: #333333;
background-color: #f0f0f0;

/* Don't use color alone for status */
color: red;  /* Is this error or warning? */

/* Don't forget placeholder styling */
input { }  /* Placeholder invisible */

/* Don't add excessive shadows */
box-shadow: 0 0 20px rgba(0,0,0,0.3);  /* Too heavy */

/* Don't forget focus states */
input:focus { outline: none; }  /* Inaccessible */

/* Don't use dark mode without light theme */
@media (prefers-color-scheme: dark) { }  /* Breaks light theme */
```

### ✅ Do

```css
/* Use CSS custom properties */
color: var(--text-primary);
background-color: var(--bg-secondary);

/* Use color + text */
<span class="badge badge-high">High Risk</span>

/* Always style placeholders */
input::placeholder { color: #9ca3af; opacity: 1; }

/* Use subtle shadows */
box-shadow: 0 1px 3px rgba(0,0,0,0.08);

/* Always add visible focus states */
input:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Keep light theme as primary */
/* Only add dark mode if needed */
```

---

## Performance Tips

1. **CSS Variables**: Use `--spacing-*` and `--color-*` for consistency
2. **Transitions**: Prefer `transform` and `opacity` for smooth 60fps animations
3. **Shadows**: Layer multiple subtle shadows instead of one heavy shadow
4. **Gradients**: Pre-compute gradients for probability bars
5. **Grid Layouts**: Use `auto-fit` for responsive layouts without media queries
6. **Font Loading**: System fonts load faster than custom fonts
7. **Bundle Size**: Minimal CSS (~15KB before minification for all styles)

---

## Testing Checklist

### Visual Testing
- [ ] Light theme colors display correctly
- [ ] No dark mode fallback visible
- [ ] All text readable on white backgrounds
- [ ] Buttons have clear hover states
- [ ] Form inputs clearly editable
- [ ] Result cards display with proper styling
- [ ] Badges show correct colors
- [ ] Gradients render smoothly

### Functional Testing
- [ ] Form labels display user-friendly names
- [ ] API payload uses original field names (Time, V1-V28, Amount)
- [ ] Load Sample button populates all fields
- [ ] Clear button resets form
- [ ] Analyze button sends request
- [ ] Results display after analysis
- [ ] Error messages display on failures
- [ ] Empty state shows before analysis

### Responsive Testing
- [ ] Mobile (320px): Single column, readable
- [ ] Tablet (768px): 1-2 column layout
- [ ] Desktop (1024px+): 2 column layout
- [ ] No horizontal scrolling
- [ ] All buttons accessible/tappable
- [ ] Touch targets > 44px

### Accessibility Testing
- [ ] Text contrast > 7:1 (WCAG AAA)
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] No color-only indicators
- [ ] Alt text present
- [ ] Form labels associated
- [ ] Error messages clear

---

## Deployment Checklist

Before deploying to production:

- [ ] Run `npm run build` without errors
- [ ] Verify `.env` file not committed (use `.env.example`)
- [ ] Test with actual backend API
- [ ] Verify CORS configuration on backend
- [ ] Check all API endpoints accessible
- [ ] Test error handling (bad input, network errors)
- [ ] Verify responsive on mobile devices
- [ ] Check browser compatibility (Chrome, Firefox, Safari, Edge)
- [ ] Remove console.log statements
- [ ] Optimize images and assets
- [ ] Enable gzip compression on server
- [ ] Set proper cache headers
- [ ] Test on slow network (3G throttling)

---

## Support & Maintenance

### Common Issues

**Q: Input fields look invisible**
A: Ensure `input { background-color: white; color: var(--text-primary); }` is set

**Q: Focus states not visible**
A: Add `border-color: var(--primary-color);` and `box-shadow` on focus

**Q: Results not displaying**
A: Check API response format matches expected structure

**Q: Mobile layout broken**
A: Verify media queries use `max-width` for mobile-first approach

**Q: Colors look wrong**
A: Verify CSS custom properties are defined in `index.css`

### Getting Help

For issues or questions:
1. Check [DESIGN_REDESIGN_SUMMARY.md](./DESIGN_REDESIGN_SUMMARY.md)
2. Review component CSS files
3. Check responsive behavior
4. Verify API integration
5. Test in different browsers

---

**Last Updated**: 2024
**Version**: 1.0
**Status**: Production Ready ✓
