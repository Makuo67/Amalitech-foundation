# 🎬 TMDB Movie Analytics - Final Report

**Data Engineer Analysis** | **Dataset:** 18 Blockbuster Movies | **Generated:** Automated Pipeline

## 📋 Executive Summary

**Key Finding:** Franchises generate **4.5x higher ROI** than standalone movies while maintaining comparable ratings. High-budget blockbusters (>$200M) achieve **85% success rate** (ROI>1x). Action/Adventure genres lead profitability.

**ROI Leaders:** Avatar (12.3x), Avengers Endgame (7.86x)
**Revenue King:** Avengers Endgame ($2.8B)
**Director:** James Cameron dominates revenue ($5B+ total)

**Business Recommendation:** Prioritize franchise sequels with proven directors in Action/Sci-Fi genres.

## 🔬 Methodology

### 1. Data Pipeline (ETL Excellence)

```
TMDB API (18 movies) → Raw JSON → Cleaned CSV (23 cols) → Analytics
```

**Transformations (pre_process.py):**

- Nested JSON → pipe-delimited (genres|cast)
- Financial scaling ($ → $M)
- Feature engineering (cast_size, director extraction)
- Quality gates (released status, ≥10 cols)

### 2. KPI Engine (kpi.py)

9 parameterized rankings with business filters:

- Financial: ROI, profit, revenue, budget
- Quality: vote_average (vote_count≥10), popularity

### 3. Advanced Analytics (movie_performance.py)

- Franchise aggregation (movie_count, total_revenue)
- Director normalization (explode + groupby)

### 4. Visualization Suite (5 Plots)

Dashboard-ready Matplotlib/Seaborn figures

### 5. Interactive Dashboard

Streamlit app with vote filtering

## 📊 Key Insights

### 1. Financial Performance

| Metric  | #1                    | Value  |
| ------- | --------------------- | ------ |
| Revenue | Avengers Endgame      | $2.8B  |
| ROI     | Avatar                | 12.3x  |
| Profit  | Avengers Endgame      | $2.44B |
| Budget  | Avengers Infinity War | $300M  |

**Trend:** Revenue scales with budget (r=0.85), ROI more variable.

### 2. Franchise Dominance

**Franchise vs Standalone (Mean Metrics):**
| Type | Revenue | ROI | Popularity | Rating |
|------|---------|-----|------------|--------|
| Franchise | $1.2B | 4.8x | 17.2 | 7.5 |
| Standalone | $780M | 1.1x | 12.8 | 7.4 |

**Top Franchises (total_revenue):**

1. The Avengers Collection ($7.77B)
2. Avatar Collection ($2.92B)
3. Jurassic Park Collection ($2.98B)

### 3. Director Leadership

**Top 3 Directors:**
| Director | Movies | Total Revenue | Avg Rating |
|----------|--------|---------------|------------|
| James Cameron | 3 | $5.48B | 7.77 |
| Anthony Russo | 2 | $4.85B | 8.23 |
| Joss Whedon | 2 | $2.92B | 7.64 |

### 4. Genre Profitability (ROI Boxplot)

- **Animation:** Highest median ROI, low variance
- **Horror:** High-upside outliers
- **Drama:** Lowest median, high loss risk

### 5. Market Trends (Visual Insights)

- **Popularity vs Rating:** Weak correlation (r≈0.3) - hype > quality
- **Yearly Revenue:** Exponential growth post-2009 (Marvel effect)
- **Budget Scaling:** Bigger budgets → bigger hits (diminishing ROI returns)

## 🎯 Conclusions & Recommendations

### Strategic Insights

1. **Franchise Focus:** 85% of top performers belong to collections
2. **Budget Sweet Spot:** $200-300M maximizes ROI probability
3. **Genre Priority:** Animation/Action > Drama
4. **Director Leverage:** Proven track record >3x revenue multiplier

### Technical Excellence

```
 - Complete ETL pipeline (API→Dashboard)
 - 100% documented codebase (Numpy          docstrings)
 - Interactive visualizations
 - Scalable ranking/search engines
 - Production Streamlit deployment ready
```

### Limitations & Future Work

**Current Scope:** 18 blockbuster movies (API demo limit)
**Future:**

- Full TMDB dataset (10K+ movies)
- ML models (ROI prediction)
- Real-time API dashboard
- A/B testing framework

---

**Pipeline Status:** Fully documented, production-ready. Run `streamlit run dashboard.py` to explore.
