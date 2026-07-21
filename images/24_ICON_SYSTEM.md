# Med Bot by Zakaria - Icon System

## Complete Icon Library

---

## Icon Specifications

### Grid System
- **Base Size:** 24x24px
- **Padding:** 2px on all sides
- **Stroke Width:** 2px
- **Corner Radius:** 2px

### Size Variants
| Size | Dimensions | Use Case |
|------|------------|----------|
| XS | 12x12px | Inline text, badges |
| S | 16x16px | Small buttons, labels |
| M | 24x24px | Default, navigation |
| L | 32x32px | Feature highlights |
| XL | 48x48px | Hero sections |

---

## Icon Categories

### Medical Icons

#### Tooth Icon
- **File:** `icon_tooth.png`
- **Use:** Dental services
- **Color:** Teal (#0D9488)
- **Category:** medical

#### Heart Icon
- **File:** `icon_heart.png`
- **Use:** Cardiology, general health
- **Color:** Red (#EF4444)
- **Category:** medical

#### Stethoscope Icon
- **File:** `icon_stethoscope.png`
- **Use:** General practice
- **Color:** Emerald (#10B981)
- **Category:** medical

#### Syringe Icon
- **File:** `icon_syringe.png`
- **Use:** Injections, vaccines
- **Color:** Blue (#3B82F6)
- **Category:** medical

#### Eye Icon
- **File:** `icon_eye.png`
- **Use:** Ophthalmology
- **Color:** Purple (#A855F7)
- **Category:** medical

### Navigation Icons

#### Calendar Icon
- **File:** `icon_calendar.png`
- **Use:** Appointments, scheduling
- **Color:** Amber (#F59E0B)
- **Category:** navigation

---

## Icon Naming Convention

```
icon-[category]-[name]-[variant].[format]
```

### Examples
- `icon-medical-tooth.png`
- `icon-medical-heart.png`
- `icon-navigation-calendar.png`
- `icon-action-phone.png`

---

## Icon Usage Guidelines

### Do's
✓ Use consistent colors from brand palette
✓ Maintain proper spacing around icons
✓ Use appropriate size for context
✓ Pair with text for clarity
✓ Ensure sufficient contrast

### Don'ts
✗ Stretch or distort icons
✗ Change icon colors arbitrarily
✗ Use without labels for critical actions
✗ Place on busy backgrounds
✗ Use at sizes smaller than 12px

---

## Icon Accessibility

### Requirements
- **Contrast Ratio:** 3:1 minimum against background
- **Touch Target:** 44x44px minimum for interactive icons
- **Labels:** Always pair with text for critical actions
- **Alt Text:** Provide descriptive alt text for screen readers

### Color Contrast Examples
| Icon Color | Background | Ratio | Status |
|------------|------------|-------|--------|
| #0D9488 | #FFFFFF | 4.6:1 | ✓ Pass |
| #0D9488 | #F8FAFC | 4.5:1 | ✓ Pass |
| #FFFFFF | #0D9488 | 4.6:1 | ✓ Pass |

---

## Icon Delivery Formats

### Available Formats
- **PNG:** Raster images for web
- **SVG:** Scalable vector (source)
- **ICO:** Favicon format

### File Locations
```
demo_images/
├── icon_tooth.png
├── icon_heart.png
├── icon_stethoscope.png
├── icon_syringe.png
├── icon_eye.png
└── icon_calendar.png
```

---

## Icon Usage in Demo Sites

### Dental Site
```html
<img src="icon_tooth.png" alt="Dental Services" width="48" height="48">
```

### Medical Site
```html
<img src="icon_stethoscope.png" alt="General Practice" width="48" height="48">
```

### Dermo Site
```html
<img src="icon_eye.png" alt="Dermatology Services" width="48" height="48">
```

---

## Icon Creation Guidelines

### For New Icons
1. Start with 24x24px grid
2. Use 2px stroke width
3. Apply brand colors
4. Test at all sizes
5. Ensure accessibility

### Color Application
- **Primary:** Use brand teal (#0D9488)
- **Secondary:** Use category color
- **Interactive:** Add hover state

---

**Icons ensure visual consistency and brand recognition across all platforms.**
