import streamlit as st

st.set_page_config(
    page_title="Adarsha Adhikari — AI & Human Factors",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">

<style>
/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

[data-testid="stAppViewContainer"] {
    background: #0a0a0f;
    color: #e8e4dc;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stSidebar"], footer { display: none !important; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Noise texture overlay ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.6;
}

/* ── Typography ── */
.serif { font-family: 'DM Serif Display', serif; }
.mono  { font-family: 'DM Mono', monospace; }
.sans  { font-family: 'DM Sans', sans-serif; }

/* ── Layout wrapper ── */
.portfolio {
    position: relative;
    z-index: 1;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 2.5rem 6rem;
}

/* ── Hero ── */
.hero {
    padding: 7rem 0 5rem;
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: end;
    gap: 2rem;
    border-bottom: 1px solid rgba(232,228,220,0.08);
}
.hero-kicker {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #7eb8a4;
    margin-bottom: 1.2rem;
}
.hero-name {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    line-height: 1.0;
    color: #f0ece2;
    margin: 0 0 1.5rem;
    letter-spacing: -1px;
}
.hero-name em {
    font-style: italic;
    color: #7eb8a4;
}
.hero-summary {
    font-size: 16px;
    line-height: 1.75;
    color: #9d9990;
    max-width: 520px;
}
.hero-contacts {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-end;
    padding-bottom: 8px;
}
.contact-item {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #6b6760;
    letter-spacing: 0.02em;
    transition: color 0.2s;
}
.contact-item:hover { color: #7eb8a4; }
.contact-item a { color: inherit; text-decoration: none; }

/* ── Section ── */
.section {
    padding: 4rem 0 0;
}
.section-header {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2.5rem;
}
.section-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #3d3c39;
    letter-spacing: 0.1em;
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    color: #f0ece2;
    margin: 0;
    letter-spacing: -0.5px;
}
.section-line {
    flex: 1;
    height: 1px;
    background: rgba(232,228,220,0.07);
}

/* ── Skills ── */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.skill-pill {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.04em;
    padding: 6px 14px;
    border-radius: 2px;
    border: 1px solid rgba(126,184,164,0.25);
    color: #7eb8a4;
    background: rgba(126,184,164,0.05);
    transition: all 0.2s;
}
.skill-pill:hover {
    border-color: rgba(126,184,164,0.6);
    background: rgba(126,184,164,0.1);
}
.skill-pill.gray {
    border-color: rgba(232,228,220,0.12);
    color: #7a7872;
    background: transparent;
}

/* ── Experience ── */
.exp-list { display: flex; flex-direction: column; gap: 0; }
.exp-item {
    display: grid;
    grid-template-columns: 160px 1fr;
    gap: 0 2.5rem;
    padding: 2rem 0;
    border-bottom: 1px solid rgba(232,228,220,0.06);
}
.exp-item:last-child { border-bottom: none; }
.exp-meta { padding-top: 3px; }
.exp-date {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #4a4946;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}
.exp-org {
    font-size: 12px;
    color: #6b6760;
    line-height: 1.5;
}
.exp-role {
    font-size: 17px;
    font-weight: 500;
    color: #e8e4dc;
    margin-bottom: 10px;
    letter-spacing: -0.2px;
}
.exp-bullets { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px; }
.exp-bullets li {
    font-size: 14px;
    color: #7a7872;
    line-height: 1.65;
    padding-left: 18px;
    position: relative;
}
.exp-bullets li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: #3d5c52;
    font-size: 12px;
    top: 2px;
}

/* ── Projects ── */
.projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}
.project-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(232,228,220,0.07);
    border-radius: 4px;
    padding: 2rem;
    transition: border-color 0.25s, background 0.25s;
    position: relative;
    overflow: hidden;
}
.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #7eb8a4, transparent);
    opacity: 0;
    transition: opacity 0.25s;
}
.project-card:hover {
    border-color: rgba(126,184,164,0.2);
    background: rgba(126,184,164,0.03);
}
.project-card:hover::before { opacity: 1; }
.project-card.featured {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
}
.project-card.featured::before { opacity: 1; }
.project-year {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.12em;
    color: #3d5c52;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.project-name {
    font-family: 'DM Serif Display', serif;
    font-size: 1.35rem;
    color: #e8e4dc;
    margin-bottom: 12px;
    line-height: 1.25;
    letter-spacing: -0.3px;
}
.project-desc {
    font-size: 13px;
    color: #6b6760;
    line-height: 1.7;
}
.project-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 1.25rem; }
.project-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.06em;
    padding: 3px 8px;
    border-radius: 2px;
    background: rgba(232,228,220,0.05);
    color: #5a5955;
}
.project-bullets { list-style: none; padding: 0; margin: 12px 0 0; display: flex; flex-direction: column; gap: 6px; }
.project-bullets li {
    font-size: 13px;
    color: #6b6760;
    line-height: 1.6;
    padding-left: 16px;
    position: relative;
}
.project-bullets li::before {
    content: '·';
    position: absolute;
    left: 4px;
    color: #3d5c52;
    font-size: 16px;
    line-height: 1.3;
}

/* ── Education ── */
.edu-list { display: flex; flex-direction: column; gap: 0; }
.edu-item {
    display: grid;
    grid-template-columns: 160px 1fr;
    gap: 0 2.5rem;
    padding: 1.75rem 0;
    border-bottom: 1px solid rgba(232,228,220,0.06);
}
.edu-item:last-child { border-bottom: none; }
.edu-year {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #4a4946;
    letter-spacing: 0.05em;
    padding-top: 3px;
}
.edu-degree {
    font-size: 16px;
    font-weight: 500;
    color: #e0dcd4;
    margin-bottom: 4px;
}
.edu-school { font-size: 13px; color: #6b6760; }

/* ── Leadership ── */
.leadership-list { display: flex; flex-direction: column; gap: 10px; }
.leadership-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 18px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(232,228,220,0.06);
    border-radius: 3px;
}
.leadership-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #7eb8a4;
    flex-shrink: 0;
}
.leadership-text { font-size: 14px; color: #7a7872; }

/* ── Footer ── */
.footer {
    margin-top: 5rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(232,228,220,0.07);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-name {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    color: #3d3c39;
    letter-spacing: -0.2px;
}
.footer-note {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #3d3c39;
    letter-spacing: 0.08em;
}

/* ── Animations ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
.hero         { animation: fadeUp 0.7s ease both; }
.section      { animation: fadeUp 0.6s ease both; }

@media (max-width: 700px) {
    .portfolio { padding: 0 1.25rem 4rem; }
    .hero { grid-template-columns: 1fr; padding: 4rem 0 3rem; }
    .hero-contacts { align-items: flex-start; }
    .exp-item, .edu-item { grid-template-columns: 1fr; gap: 6px; }
    .projects-grid { grid-template-columns: 1fr; }
    .project-card.featured { grid-template-columns: 1fr; }
    .footer { flex-direction: column; gap: 8px; text-align: center; }
}
</style>

<div class="portfolio">

  <!-- HERO -->
  <div class="hero">
    <div>
      <div class="hero-kicker">Portfolio · AI &amp; Human Factors</div>
      <h1 class="hero-name serif">Adarsha<br><em>Adhikari</em></h1>
      <p class="hero-summary">
        MSc graduate specialising in human–AI interaction and system safety.
        I design and evaluate Human-in-the-Loop systems — using stochastic modelling,
        signal detection theory, and temporal telemetry — to ensure AI remains
        transparent, reliable, and accountable.
      </p>
    </div>
    <div class="hero-contacts">
      <div class="contact-item">📍 Coventry, UK</div>
      <div class="contact-item"><a href="tel:07350191735">07350 191735</a></div>
      <div class="contact-item"><a href="mailto:adarsha.adhikari555@gmail.com">adarsha.adhikari555@gmail.com</a></div>
    </div>
  </div>

  <!-- SKILLS -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">01</span>
      <h2 class="section-title serif">Skills</h2>
      <div class="section-line"></div>
    </div>
    <div style="display:flex; flex-direction:column; gap:14px;">
      <div>
        <div style="font-family:'DM Mono',monospace;font-size:10px;letter-spacing:0.12em;color:#3d5c52;text-transform:uppercase;margin-bottom:8px;">AI &amp; Data Science</div>
        <div class="skills-grid">
          <span class="skill-pill">Generative AI</span>
          <span class="skill-pill">Machine Learning</span>
          <span class="skill-pill">Signal Detection Theory</span>
          <span class="skill-pill">Monte Carlo Simulation</span>
          <span class="skill-pill">Automation Bias Analysis</span>
          <span class="skill-pill">HITL Evaluation</span>
          <span class="skill-pill">Temporal Telemetry</span>
        </div>
      </div>
      <div>
        <div style="font-family:'DM Mono',monospace;font-size:10px;letter-spacing:0.12em;color:#3d5c52;text-transform:uppercase;margin-bottom:8px;">Development &amp; Tools</div>
        <div class="skills-grid">
          <span class="skill-pill gray">Python</span>
          <span class="skill-pill gray">NumPy · Pandas</span>
          <span class="skill-pill gray">Streamlit</span>
          <span class="skill-pill gray">MATLAB</span>
          <span class="skill-pill gray">Java</span>
          <span class="skill-pill gray">IoT (ESP8266, Arduino)</span>
          <span class="skill-pill gray">System Safety &amp; Reliability</span>
        </div>
      </div>
    </div>
  </div>

  <!-- EXPERIENCE -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">02</span>
      <h2 class="section-title serif">Experience</h2>
      <div class="section-line"></div>
    </div>
    <div class="exp-list">

      <div class="exp-item">
        <div class="exp-meta">
          <div class="exp-date">2025 – Present</div>
          <div class="exp-org">Coventry University<br>UK</div>
        </div>
        <div>
          <div class="exp-role">Student Ambassador</div>
          <ul class="exp-bullets">
            <li>Facilitate open days and admission events through campus tours and administrative support.</li>
            <li>Represent student interests as Course Rep, bridging peer feedback and faculty to improve course delivery.</li>
          </ul>
        </div>
      </div>

      <div class="exp-item">
        <div class="exp-meta">
          <div class="exp-date">2025 – 2026</div>
          <div class="exp-org">Cadent Gas<br>UK</div>
        </div>
        <div>
          <div class="exp-role">Customer Service Representative</div>
          <ul class="exp-bullets">
            <li>Managed high-volume technical inquiries in adherence to strict corporate safety standards.</li>
          </ul>
        </div>
      </div>

      <div class="exp-item">
        <div class="exp-meta">
          <div class="exp-date">Oct 2023 – Jan 2024</div>
          <div class="exp-org">Instapal Technologies<br>Nepal</div>
        </div>
        <div>
          <div class="exp-role">Intern</div>
          <ul class="exp-bullets">
            <li>Assisted in web and ERP development; conducted marketing, auditing, and promotional activities.</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- PROJECTS -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">03</span>
      <h2 class="section-title serif">Projects</h2>
      <div class="section-line"></div>
    </div>
    <div class="projects-grid">

      <div class="project-card featured">
        <div>
          <div class="project-year">2026 · Dissertation</div>
          <div class="project-name serif">Human-in-the-Loop: Manual vs AI-Assisted Security Screening</div>
          <div class="project-tags">
            <span class="project-tag">Python</span>
            <span class="project-tag">Streamlit</span>
            <span class="project-tag">Signal Detection Theory</span>
            <span class="project-tag">Monte Carlo</span>
            <span class="project-tag">Paired T-test</span>
          </div>
        </div>
        <div>
          <ul class="project-bullets">
            <li>Built a Stochastic PCG Engine in Python &amp; Streamlit to simulate baggage screening scenarios.</li>
            <li>Implemented 85% AI reliability logic to study automation bias and verification latency via SDT.</li>
            <li>Ran Monte Carlo simulations (N=10,000) to verify algorithmic convergence and reliability thresholds.</li>
            <li>Analysed N=30 participant data using paired t-tests, revealing a significant speed–accuracy trade-off under AI assistance.</li>
          </ul>
        </div>
      </div>

      <div class="project-card">
        <div class="project-year">Agro-Tech</div>
        <div class="project-name serif">Automated Soil Monitoring</div>
        <p class="project-desc">Automated soil moisture monitoring using ESP8266 and Arduino sensors; integrated deep learning for plant disease detection.</p>
        <div class="project-tags">
          <span class="project-tag">ESP8266</span>
          <span class="project-tag">Arduino</span>
          <span class="project-tag">Deep Learning</span>
          <span class="project-tag">IoT</span>
        </div>
      </div>

      <div class="project-card">
        <div class="project-year">Web App</div>
        <div class="project-name serif">Electricity Billing System</div>
        <p class="project-desc">Developed a web-based Java application to computerise and streamline electricity billing operations.</p>
        <div class="project-tags">
          <span class="project-tag">Java</span>
          <span class="project-tag">Web Application</span>
          <span class="project-tag">ERP</span>
        </div>
      </div>

    </div>
  </div>

  <!-- EDUCATION -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">04</span>
      <h2 class="section-title serif">Education</h2>
      <div class="section-line"></div>
    </div>
    <div class="edu-list">
      <div class="edu-item">
        <div class="edu-year">Expected May 2026</div>
        <div>
          <div class="edu-degree">MSc Artificial Intelligence &amp; Human Factors</div>
          <div class="edu-school">Coventry University, UK</div>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-year">2019 – 2024</div>
        <div>
          <div class="edu-degree">Bachelor of Computer Information Systems</div>
          <div class="edu-school">Boston International College, Nepal</div>
        </div>
      </div>
    </div>
  </div>

  <!-- LEADERSHIP -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">05</span>
      <h2 class="section-title serif">Leadership</h2>
      <div class="section-line"></div>
    </div>
    <div class="leadership-list">
      <div class="leadership-item">
        <div class="leadership-dot"></div>
        <span class="leadership-text">Eco Club Vice President — Narayani English Public School</span>
      </div>
      <div class="leadership-item">
        <div class="leadership-dot"></div>
        <span class="leadership-text">IT Club Coordinator — Boston International College</span>
      </div>
      <div class="leadership-item">
        <div class="leadership-dot"></div>
        <span class="leadership-text">Community Youth Club Member — Nepal (community outreach)</span>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-name serif">Adarsha Adhikari</div>
    <div class="footer-note mono">Available · May 2026</div>
  </div>

</div>
""", unsafe_allow_html=True)
