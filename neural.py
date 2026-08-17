import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Neural Pattern Lab",
    layout="wide"
)

html = Path("neural-pattern-lab.html").read_text(encoding="utf-8")

st.components.v1.html(
    html,
    height=3000,
    scrolling=True
)<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neural Pattern Lab</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
/* ===== Design tokens =====
   bg-void:      #0A0E1F  deep indigo-black, the "space between neurons"
   bg-surface:   #12172C  card surface
   bg-surface-2: #191F3B  raised surface / hover
   line:         #262E52  hairline borders, idle synapses
   ink:          #E9EBF7  primary text
   ink-muted:    #8B92B8  secondary text
   synapse:      #7B61FF  violet - "signal traveling"
   spark:        #4CC9F0  cyan - "activation"
   flare:        #FF9B6B  warm coral - "output / prediction"
   good:         #57D9A3  success / correct
   bad:          #FF6B81  error / incorrect
   Display: Space Grotesk | Body: IBM Plex Sans | Data/mono: IBM Plex Mono
*/
:root{
  --bg-void:#0A0E1F;
  --bg-surface:#12172C;
  --bg-surface-2:#191F3B;
  --line:#262E52;
  --ink:#E9EBF7;
  --ink-muted:#8B92B8;
  --synapse:#7B61FF;
  --spark:#4CC9F0;
  --flare:#FF9B6B;
  --good:#57D9A3;
  --bad:#FF6B81;
  --radius:16px;
}
*{box-sizing:border-box; margin:0; padding:0;}
html{scroll-behavior:smooth;}
@media (prefers-reduced-motion: reduce){
  html{scroll-behavior:auto;}
  *{animation-duration:.001ms !important; animation-iteration-count:1 !important; transition-duration:.001ms !important;}
}
body{
  background:var(--bg-void);
  color:var(--ink);
  font-family:'IBM Plex Sans', sans-serif;
  line-height:1.6;
  overflow-x:hidden;
}
h1,h2,h3,h4{font-family:'Space Grotesk', sans-serif; font-weight:600; letter-spacing:-0.01em;}
.mono{font-family:'IBM Plex Mono', monospace;}
a{color:inherit;}
img,svg{display:block; max-width:100%;}
button{font-family:inherit; cursor:pointer;}
:focus-visible{outline:2px solid var(--spark); outline-offset:3px;}

.wrap{max-width:1120px; margin:0 auto; padding:0 24px;}
section{padding:120px 0; position:relative;}
.eyebrow{
  font-family:'IBM Plex Mono', monospace;
  font-size:12px; letter-spacing:.14em; text-transform:uppercase;
  color:var(--spark); margin-bottom:14px; display:flex; align-items:center; gap:10px;
}
.eyebrow::before{content:""; width:22px; height:1px; background:var(--spark); display:inline-block;}
.section-title{font-size:clamp(28px,4vw,42px); margin-bottom:18px;}
.section-lead{color:var(--ink-muted); max-width:640px; font-size:17px; margin-bottom:56px;}
.card{
  background:var(--bg-surface);
  border:1px solid var(--line);
  border-radius:var(--radius);
  padding:28px;
}

/* ===== Nav ===== */
nav{
  position:fixed; top:0; left:0; right:0; z-index:100;
  backdrop-filter:blur(14px);
  background:rgba(10,14,31,.72);
  border-bottom:1px solid var(--line);
}
nav .wrap{display:flex; align-items:center; justify-content:space-between; padding-top:16px; padding-bottom:16px;}
.brand{display:flex; align-items:center; gap:10px; font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:16px;}
.brand-mark{width:20px; height:20px;}
.navlinks{display:flex; gap:32px; font-size:14px; color:var(--ink-muted);}
.navlinks a{text-decoration:none; transition:color .2s;}
.navlinks a:hover{color:var(--ink);}
.navlinks{display:none;}
@media(min-width:800px){.navlinks{display:flex;}}
.nav-cta{
  font-size:13px; font-family:'IBM Plex Mono',monospace; padding:9px 16px;
  background:var(--synapse); color:white; border:none; border-radius:999px;
}

/* ===== Hero ===== */
.hero{
  min-height:100svh; display:flex; align-items:center; position:relative;
  padding-top:120px;
}
#hero-canvas{position:absolute; inset:0; width:100%; height:100%; opacity:.55;}
.hero-inner{position:relative; z-index:2; max-width:760px;}
.hero h1{
  font-size:clamp(44px,7vw,84px); line-height:.98; margin-bottom:22px;
  background:linear-gradient(120deg, var(--ink) 40%, var(--spark) 75%, var(--synapse));
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.hero .sub{font-size:clamp(18px,2.4vw,24px); color:var(--ink-muted); font-family:'Space Grotesk',sans-serif; margin-bottom:18px;}
.hero p{color:var(--ink-muted); max-width:520px; margin-bottom:38px; font-size:16px;}
.btn-row{display:flex; gap:14px; flex-wrap:wrap;}
.btn{
  font-size:15px; font-weight:500; padding:14px 26px; border-radius:999px; border:1px solid var(--line);
  display:inline-flex; align-items:center; gap:8px; transition:transform .15s, border-color .2s, background .2s;
  text-decoration:none;
}
.btn:hover{transform:translateY(-2px);}
.btn-primary{background:var(--synapse); border-color:var(--synapse); color:white;}
.btn-primary:hover{background:#8f78ff;}
.btn-ghost{background:transparent; color:var(--ink);}
.btn-ghost:hover{border-color:var(--spark); color:var(--spark);}

/* ===== Pattern examples ===== */
.pattern-examples{display:grid; grid-template-columns:repeat(2,1fr); gap:16px; margin-top:8px;}
@media(min-width:700px){.pattern-examples{grid-template-columns:repeat(4,1fr);}}
.pex{text-align:center; padding:22px 12px;}
.pex canvas{margin:0 auto 14px; border-radius:8px;}
.pex .label{font-family:'IBM Plex Mono',monospace; font-size:12px; color:var(--ink-muted); letter-spacing:.05em;}
.definition-box{
  border-left:3px solid var(--spark); padding:20px 24px; margin-top:44px;
  background:var(--bg-surface); border-radius:0 12px 12px 0; max-width:680px;
}
.definition-box b{color:var(--spark);}

/* ===== Experiment layout ===== */
.experiment-grid{display:grid; grid-template-columns:1fr; gap:40px;}
@media(min-width:960px){.experiment-grid{grid-template-columns:340px 1fr;}}
.grid-panel{display:flex; flex-direction:column; align-items:center; gap:20px;}
#pattern-canvas{
  border-radius:12px; cursor:pointer; background:var(--bg-surface-2); border:1px solid var(--line);
}
.grid-controls{display:flex; gap:10px; flex-wrap:wrap; justify-content:center;}
.chip-btn{
  font-size:13px; padding:9px 14px; border-radius:8px; background:var(--bg-surface-2);
  border:1px solid var(--line); color:var(--ink-muted); transition:.2s;
}
.chip-btn:hover{border-color:var(--spark); color:var(--ink);}
.sample-row{display:flex; gap:8px; flex-wrap:wrap; justify-content:center;}
.numeric-out{
  width:100%; background:var(--bg-void); border:1px solid var(--line); border-radius:10px;
  padding:14px; font-family:'IBM Plex Mono',monospace; font-size:11px; color:var(--spark);
  white-space:pre; text-align:center; line-height:1.5; overflow-x:auto;
}
.submit-btn{
  background:var(--flare); color:#1a0f08; border:none; padding:14px 30px; border-radius:999px;
  font-weight:600; font-size:15px; width:100%;
}
.submit-btn:hover{filter:brightness(1.08);}

/* ===== NN visualization ===== */
.nn-panel{display:flex; flex-direction:column; gap:24px;}
#nn-svg{width:100%; height:auto; background:var(--bg-surface); border:1px solid var(--line); border-radius:var(--radius);}
.layer-caption{display:flex; justify-content:space-around; font-family:'IBM Plex Mono',monospace; font-size:11px; color:var(--ink-muted); text-transform:uppercase; letter-spacing:.08em;}
.neuron{cursor:pointer;}
.neuron-tip{
  position:fixed; pointer-events:none; background:var(--bg-surface-2); border:1px solid var(--spark);
  border-radius:8px; padding:8px 12px; font-size:12px; max-width:220px; z-index:200; opacity:0; transition:opacity .15s;
}

/* Prediction card */
.pred-card{display:none;}
.pred-card.show{display:block;}
.pred-head{display:flex; justify-content:space-between; align-items:baseline; margin-bottom:6px;}
.pred-main{font-size:44px; font-family:'Space Grotesk',sans-serif; color:var(--flare);}
.confidence{font-family:'IBM Plex Mono',monospace; color:var(--ink-muted); font-size:13px;}
.bars{margin-top:20px; display:flex; flex-direction:column; gap:10px;}
.bar-row{display:grid; grid-template-columns:80px 1fr 44px; align-items:center; gap:10px; font-size:12px; font-family:'IBM Plex Mono',monospace;}
.bar-track{height:10px; background:var(--bg-surface-2); border-radius:6px; overflow:hidden;}
.bar-fill{height:100%; background:linear-gradient(90deg,var(--synapse),var(--spark)); border-radius:6px; width:0%; transition:width .8s ease;}
.why-btn{margin-top:18px; background:transparent; border:1px solid var(--line); color:var(--ink); padding:10px 18px; border-radius:8px; font-size:13px;}
.why-btn:hover{border-color:var(--flare); color:var(--flare);}
.why-list{list-style:none; margin-top:14px; display:none; flex-direction:column; gap:8px; font-size:14px; color:var(--ink-muted);}
.why-list.show{display:flex;}
.why-list li::before{content:"›"; color:var(--flare); margin-right:8px;}

/* ===== Neuron explain ===== */
.neuron-diagram{display:flex; flex-direction:column; align-items:center; gap:0;}
#neuron-svg{width:100%; max-width:680px; height:auto;}
.term-grid{display:grid; grid-template-columns:1fr; gap:14px; margin-top:40px;}
@media(min-width:700px){.term-grid{grid-template-columns:1fr 1fr;}}
.term{padding:18px 20px; border-radius:10px; background:var(--bg-surface); border:1px solid var(--line);}
.term b{color:var(--spark); display:block; margin-bottom:4px; font-family:'Space Grotesk',sans-serif;}
.equation{
  margin-top:32px; text-align:center; font-family:'IBM Plex Mono',monospace; font-size:18px;
  padding:18px; border:1px dashed var(--line); border-radius:10px; color:var(--flare);
}

/* ===== Training ===== */
.training-panel{display:grid; grid-template-columns:1fr; gap:32px;}
@media(min-width:900px){.training-panel{grid-template-columns:1fr 1fr;}}
.train-btn{background:var(--synapse); color:white; border:none; padding:14px 26px; border-radius:999px; font-weight:500;}
.train-btn:disabled{opacity:.5; cursor:not-allowed;}
.epoch-log{margin-top:18px; font-family:'IBM Plex Mono',monospace; font-size:13px; display:flex; flex-direction:column; gap:6px; min-height:120px;}
.epoch-log span{color:var(--ink-muted);}
.epoch-log b{color:var(--good);}
#chart-canvas{width:100%; height:auto; background:var(--bg-surface); border:1px solid var(--line); border-radius:var(--radius);}
.flow-steps{display:flex; flex-wrap:wrap; gap:8px; margin-top:24px; font-family:'IBM Plex Mono',monospace; font-size:12px; color:var(--ink-muted);}
.flow-steps span{padding:6px 12px; border:1px solid var(--line); border-radius:999px;}
.flow-steps span.active{border-color:var(--good); color:var(--good);}

/* ===== Mistake demo ===== */
.mistake-flow{display:flex; flex-direction:column; gap:0; max-width:520px; margin:0 auto;}
.mistake-step{
  display:flex; align-items:center; gap:16px; padding:16px 0; opacity:.35; transition:opacity .3s;
  border-bottom:1px solid var(--line);
}
.mistake-step.active{opacity:1;}
.mistake-step:last-child{border-bottom:none;}
.mistake-num{
  width:34px; height:34px; border-radius:50%; border:1px solid var(--line); display:flex; align-items:center;
  justify-content:center; font-family:'IBM Plex Mono',monospace; font-size:13px; flex-shrink:0;
}
.mistake-step.active .mistake-num{border-color:var(--spark); color:var(--spark);}
.mistake-step.wrong .mistake-num{border-color:var(--bad); color:var(--bad);}
.mistake-step.right .mistake-num{border-color:var(--good); color:var(--good);}
.mistake-title{font-weight:600; font-family:'Space Grotesk',sans-serif;}
.mistake-desc{color:var(--ink-muted); font-size:13px;}
.next-step-btn{display:block; margin:28px auto 0; background:var(--bg-surface-2); border:1px solid var(--line); color:var(--ink); padding:12px 24px; border-radius:8px;}
.next-step-btn:hover{border-color:var(--spark);}

/* ===== Layer cards ===== */
.layer-cards{display:grid; grid-template-columns:1fr; gap:16px;}
@media(min-width:700px){.layer-cards{grid-template-columns:repeat(3,1fr);}}
.layer-card{cursor:pointer; transition:border-color .2s, transform .2s;}
.layer-card:hover{transform:translateY(-3px);}
.layer-card.active{border-color:var(--spark); box-shadow:0 0 0 1px var(--spark) inset;}
.layer-card h3{font-size:17px; margin-bottom:8px;}
.layer-card p{color:var(--ink-muted); font-size:14px;}
.layer-tag{font-family:'IBM Plex Mono',monospace; font-size:11px; color:var(--spark); text-transform:uppercase; letter-spacing:.08em; margin-bottom:10px; display:block;}

/* ===== Applications ===== */
.app-grid{display:grid; grid-template-columns:1fr; gap:16px;}
@media(min-width:700px){.app-grid{grid-template-columns:repeat(2,1fr);}}
@media(min-width:1000px){.app-grid{grid-template-columns:repeat(3,1fr);}}
.app-card{display:flex; gap:14px; align-items:flex-start;}
.app-icon{width:38px; height:38px; flex-shrink:0; color:var(--spark);}
.app-card h4{font-size:15px; margin-bottom:4px;}
.app-card p{font-size:13px; color:var(--ink-muted);}

/* ===== Challenge ===== */
.challenge-box{text-align:center;}
.challenge-box .btn-row{justify-content:center;}

footer{padding:60px 0; border-top:1px solid var(--line); text-align:center; color:var(--ink-muted); font-size:13px;}
footer .mono{color:var(--line); margin-top:8px;}
</style>
</head>
<body>

<nav>
  <div class="wrap">
    <div class="brand">
      <svg class="brand-mark" viewBox="0 0 24 24" fill="none"><circle cx="5" cy="5" r="2.5" fill="#4CC9F0"/><circle cx="19" cy="5" r="2.5" fill="#7B61FF"/><circle cx="12" cy="12" r="2.5" fill="#FF9B6B"/><circle cx="5" cy="19" r="2.5" fill="#7B61FF"/><circle cx="19" cy="19" r="2.5" fill="#4CC9F0"/><path d="M5 5L12 12M19 5L12 12M5 19L12 12M19 19L12 12" stroke="#33395c" stroke-width="1.2"/></svg>
      Neural Pattern Lab
    </div>
    <div class="navlinks">
      <a href="#home">Home</a>
      <a href="#learn">Learn</a>
      <a href="#experiment">Experiment</a>
      <a href="#training">Training</a>
      <a href="#applications">Applications</a>
    </div>
    <a href="#experiment" class="nav-cta">Try it</a>
  </div>
</nav>

<!-- ============ HERO ============ -->
<header class="hero" id="home">
  <canvas id="hero-canvas"></canvas>
  <div class="wrap hero-inner">
    <div class="eyebrow">Class 12 · Interactive Demonstration</div>
    <h1>Neural<br>Pattern Lab</h1>
    <div class="sub">Teach a neural network to recognize patterns.</div>
    <p>Explore how neural networks transform patterns into predictions — and learn from their mistakes, one weight at a time.</p>
    <div class="btn-row">
      <a href="#learn" class="btn btn-primary">Explore Neural Networks</a>
      <a href="#experiment" class="btn btn-ghost">Try Pattern Recognition</a>
    </div>
  </div>
</header>

<!-- ============ WHAT IS PATTERN RECOGNITION ============ -->
<section id="learn">
  <div class="wrap">
    <div class="eyebrow">01 — Concept</div>
    <h2 class="section-title">What is Pattern Recognition?</h2>
    <p class="section-lead">Look at these four shapes. You recognized each one instantly — not because you counted every pixel, but because you spotted a familiar structure.</p>

    <div class="pattern-examples">
      <div class="card pex"><canvas class="tmpl-canvas" data-tmpl="circle" width="120" height="120"></canvas><div class="label">CIRCLE</div></div>
      <div class="card pex"><canvas class="tmpl-canvas" data-tmpl="square" width="120" height="120"></canvas><div class="label">SQUARE</div></div>
      <div class="card pex"><canvas class="tmpl-canvas" data-tmpl="triangle" width="120" height="120"></canvas><div class="label">TRIANGLE</div></div>
      <div class="card pex"><canvas class="tmpl-canvas" data-tmpl="digit1" width="120" height="120"></canvas><div class="label">DIGIT "1"</div></div>
    </div>

    <div class="definition-box">
      <b>Pattern Recognition</b> means finding meaningful similarities or features in data, and identifying what the pattern represents. A neural network does the same thing you just did — except it learns which features matter by looking at thousands of examples.
    </div>
  </div>
</section>

<!-- ============ INTERACTIVE EXPERIMENT ============ -->
<section id="experiment">
  <div class="wrap">
    <div class="eyebrow">02 — Experiment</div>
    <h2 class="section-title">Draw a Pattern, Watch it Think</h2>
    <p class="section-lead">Click cells to draw on the grid. Submit your pattern and watch it travel through the network as glowing signals — layer by layer — until a prediction comes out the other side.</p>

    <div class="experiment-grid">
      <div class="grid-panel card">
        <canvas id="pattern-canvas" width="280" height="280"></canvas>
        <div class="sample-row">
          <button class="chip-btn" data-load="circle">Circle</button>
          <button class="chip-btn" data-load="square">Square</button>
          <button class="chip-btn" data-load="triangle">Triangle</button>
          <button class="chip-btn" data-load="digit0">Digit 0</button>
          <button class="chip-btn" data-load="digit1">Digit 1</button>
        </div>
        <div class="grid-controls">
          <button class="chip-btn" id="clear-grid">Clear Grid</button>
        </div>
        <div class="numeric-out" id="numeric-out">Draw a pattern to see the input values</div>
        <button class="submit-btn" id="submit-pattern">Submit for Recognition →</button>
      </div>

      <div class="nn-panel">
        <div class="card" style="padding:20px;">
          <svg id="nn-svg" viewBox="0 0 640 320"></svg>
          <div class="layer-caption">
            <span>Input Layer</span><span>Hidden Layer</span><span>Output Layer</span>
          </div>
        </div>

        <div class="card pred-card" id="pred-card">
          <div class="pred-head">
            <span class="mono" style="color:var(--ink-muted); font-size:12px;">PREDICTION</span>
          </div>
          <div class="pred-main" id="pred-main">—</div>
          <div class="confidence" id="pred-conf">confidence: —</div>
          <div class="bars" id="pred-bars"></div>
          <button class="why-btn" id="why-btn">Why this prediction?</button>
          <ul class="why-list" id="why-list"></ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ EXPLAIN A NEURON ============ -->
<section id="neuron">
  <div class="wrap">
    <div class="eyebrow">03 — Inside a Neuron</div>
    <h2 class="section-title">What Happens Inside One Neuron?</h2>
    <p class="section-lead">Every glowing circle in the diagram above is doing the same small job. Here's that job, zoomed in.</p>

    <div class="neuron-diagram card">
      <svg id="neuron-svg" viewBox="0 0 680 260"></svg>
    </div>

    <div class="equation">Output = Activation( Weighted Sum + Bias )</div>

    <div class="term-grid">
      <div class="term"><b>Input</b>A value coming from the previous layer — a pixel, or another neuron's output.</div>
      <div class="term"><b>Weight</b>A number that decides how important that input is. Learning = adjusting these.</div>
      <div class="term"><b>Bias</b>An extra nudge added to the sum, so a neuron can fire even with weak inputs.</div>
      <div class="term"><b>Sum</b>Every input × its weight, added together, plus the bias.</div>
      <div class="term"><b>Activation Function</b>Decides whether — and how strongly — the neuron "fires" based on the sum.</div>
      <div class="term"><b>Output</b>The neuron's signal, passed forward to the next layer.</div>
    </div>
  </div>
</section>

<!-- ============ EXPLORE THE LAYERS ============ -->
<section id="layers">
  <div class="wrap">
    <div class="eyebrow">04 — Structure</div>
    <h2 class="section-title">Explore the Layers</h2>
    <p class="section-lead">Click a card. It highlights the matching part of the network diagram back in the Experiment section.</p>

    <div class="layer-cards">
      <div class="card layer-card" data-layer="0">
        <span class="layer-tag">Layer 01</span>
        <h3>Input Layer</h3>
        <p>What the network receives — the raw pixel values of your pattern.</p>
      </div>
      <div class="card layer-card" data-layer="1">
        <span class="layer-tag">Layer 02</span>
        <h3>Hidden Layer</h3>
        <p>Where useful features are detected — curves, corners, edges.</p>
      </div>
      <div class="card layer-card" data-layer="2">
        <span class="layer-tag">Layer 03</span>
        <h3>Output Layer</h3>
        <p>Where the final prediction is produced, one score per shape.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ TRAINING ============ -->
<section id="training">
  <div class="wrap">
    <div class="eyebrow">05 — Learning</div>
    <h2 class="section-title">How Does the Network Learn?</h2>
    <p class="section-lead">A freshly built network is bad at this — it starts by guessing. Training is the process of getting better, one attempt at a time.</p>

    <div class="training-panel">
      <div class="card">
        <button class="train-btn" id="start-training">Start Training</button>
        <div class="flow-steps" id="flow-steps">
          <span data-step="0">Predict</span><span data-step="1">Compare</span><span data-step="2">Calculate Error</span><span data-step="3">Adjust Weights</span><span data-step="4">Try Again</span>
        </div>
        <div class="epoch-log" id="epoch-log"></div>
      </div>
      <div class="card" style="display:flex; flex-direction:column;">
        <canvas id="chart-canvas" width="480" height="280"></canvas>
      </div>
    </div>
  </div>
</section>

<!-- ============ MISTAKE -> LEARNING ============ -->
<section id="mistake">
  <div class="wrap">
    <div class="eyebrow">06 — A Single Mistake</div>
    <h2 class="section-title">Watch One Correction Happen</h2>
    <p class="section-lead">Zooming into a single training step — this is what "adjusting weights" actually looks like.</p>

    <div class="mistake-flow" id="mistake-flow">
      <div class="mistake-step" data-i="0"><div class="mistake-num">1</div><div><div class="mistake-title">Input Pattern</div><div class="mistake-desc">A drawn pattern enters the network.</div></div></div>
      <div class="mistake-step" data-i="1"><div class="mistake-num">2</div><div><div class="mistake-title">Prediction: SQUARE ❌</div><div class="mistake-desc">The network guesses — and gets it wrong.</div></div></div>
      <div class="mistake-step" data-i="2"><div class="mistake-num">3</div><div><div class="mistake-title">Correct Answer: CIRCLE</div><div class="mistake-desc">The true label is revealed for comparison.</div></div></div>
      <div class="mistake-step" data-i="3"><div class="mistake-num">4</div><div><div class="mistake-title">Error Detected</div><div class="mistake-desc">The gap between guess and truth is measured.</div></div></div>
      <div class="mistake-step" data-i="4"><div class="mistake-num">5</div><div><div class="mistake-title">Weights Adjusted</div><div class="mistake-desc">Every connection nudges slightly toward the right answer.</div></div></div>
      <div class="mistake-step" data-i="5"><div class="mistake-num">6</div><div><div class="mistake-title">Prediction: CIRCLE ✓</div><div class="mistake-desc">Shown the same pattern again, the network now gets it right.</div></div></div>
    </div>
    <button class="next-step-btn" id="mistake-next">Play Next Step →</button>
  </div>
</section>

<!-- ============ APPLICATIONS ============ -->
<section id="applications">
  <div class="wrap">
    <div class="eyebrow">07 — Real World</div>
    <h2 class="section-title">Where This Shows Up</h2>
    <p class="section-lead">The same input → hidden → output idea, at a much larger scale, powers systems you use every day.</p>

    <div class="app-grid" id="app-grid"></div>
  </div>
</section>

<!-- ============ FINAL CHALLENGE ============ -->
<section id="challenge">
  <div class="wrap card challenge-box" style="padding:56px 32px;">
    <div class="eyebrow" style="justify-content:center;">08 — Your Turn</div>
    <h2 class="section-title">Can You Fool the Neural Network?</h2>
    <p class="section-lead" style="margin-left:auto; margin-right:auto;">Scroll back up to the drawing grid. Try a half-finished circle, a lopsided square, or something in between — and see how the confidence bars react.</p>
    <div class="btn-row">
      <a href="#experiment" class="btn btn-primary">Back to the Grid</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    Built as an educational simulation — no real machine-learning model runs here, just the ideas behind one.
    <div class="mono">NEURAL PATTERN LAB · CLASS 12 PROJECT</div>
  </div>
</footer>

<script>
/* ============================================================
   TEMPLATES — 8x8 binary patterns used for samples + "training"
   ============================================================ */
const GRID_SIZE = 8;
const TEMPLATES = {
  circle: [
    "00111100",
    "01000010",
    "10000001",
    "10000001",
    "10000001",
    "10000001",
    "01000010",
    "00111100",
  ],
  square: [
    "11111111",
    "10000001",
    "10000001",
    "10000001",
    "10000001",
    "10000001",
    "10000001",
    "11111111",
  ],
  triangle: [
    "00011000",
    "00011000",
    "00100100",
    "00100100",
    "01000010",
    "01000010",
    "10000001",
    "11111111",
  ],
  digit0: [
    "00111100",
    "01100110",
    "01100110",
    "01100110",
    "01100110",
    "01100110",
    "01100110",
    "00111100",
  ],
  digit1: [
    "00011000",
    "00111000",
    "01011000",
    "00011000",
    "00011000",
    "00011000",
    "00011000",
    "01111100",
  ],
};
function tmplToMatrix(key){
  return TEMPLATES[key].map(row => row.split("").map(Number));
}

/* ============================================================
   HERO CANVAS — ambient morphing node network
   ============================================================ */
(function heroCanvas(){
  const canvas = document.getElementById('hero-canvas');
  const ctx = canvas.getContext('2d');
  let w,h,nodes=[];
  function resize(){
    w = canvas.width = canvas.offsetWidth * devicePixelRatio;
    h = canvas.height = canvas.offsetHeight * devicePixelRatio;
  }
  function initNodes(){
    nodes = [];
    const count = window.innerWidth < 700 ? 34 : 60;
    for(let i=0;i<count;i++){
      nodes.push({
        x: Math.random()*w, y: Math.random()*h,
        vx:(Math.random()-0.5)*0.25*devicePixelRatio, vy:(Math.random()-0.5)*0.25*devicePixelRatio,
        r: (Math.random()*1.6+1.2)*devicePixelRatio
      });
    }
  }
  function step(){
    ctx.clearRect(0,0,w,h);
    for(const n of nodes){
      n.x += n.vx; n.y += n.vy;
      if(n.x<0||n.x>w) n.vx*=-1;
      if(n.y<0||n.y>h) n.vy*=-1;
    }
    for(let i=0;i<nodes.length;i++){
      for(let j=i+1;j<nodes.length;j++){
        const a=nodes[i], b=nodes[j];
        const d = Math.hypot(a.x-b.x, a.y-b.y);
        const maxD = 150*devicePixelRatio;
        if(d < maxD){
          ctx.strokeStyle = `rgba(123,97,255,${(1-d/maxD)*0.35})`;
          ctx.lineWidth = devicePixelRatio*0.6;
          ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
        }
      }
    }
    for(const n of nodes){
      ctx.beginPath(); ctx.arc(n.x,n.y,n.r,0,Math.PI*2);
      ctx.fillStyle = 'rgba(76,201,240,0.8)';
      ctx.fill();
    }
    requestAnimationFrame(step);
  }
  window.addEventListener('resize', ()=>{resize(); initNodes();});
  resize(); initNodes(); step();
})();

/* ============================================================
   TEMPLATE MINI-CANVASES (section 2 examples)
   ============================================================ */
document.querySelectorAll('.tmpl-canvas').forEach(cv=>{
  const key = cv.dataset.tmpl;
  const ctx = cv.getContext('2d');
  const m = tmplToMatrix(key);
  const cell = cv.width / GRID_SIZE;
  ctx.fillStyle = '#191F3B'; ctx.fillRect(0,0,cv.width,cv.height);
  for(let r=0;r<GRID_SIZE;r++) for(let c=0;c<GRID_SIZE;c++){
    if(m[r][c]){
      ctx.fillStyle = '#4CC9F0';
      ctx.fillRect(c*cell+1, r*cell+1, cell-2, cell-2);
    }
  }
});

/* ============================================================
   INTERACTIVE PATTERN GRID
   ============================================================ */
const patternCanvas = document.getElementById('pattern-canvas');
const pctx = patternCanvas.getContext('2d');
let grid = Array.from({length:GRID_SIZE},()=>Array(GRID_SIZE).fill(0));
const cellSize = patternCanvas.width / GRID_SIZE;

function drawGrid(){
  pctx.fillStyle = '#191F3B'; pctx.fillRect(0,0,patternCanvas.width,patternCanvas.height);
  for(let r=0;r<GRID_SIZE;r++){
    for(let c=0;c<GRID_SIZE;c++){
      pctx.fillStyle = grid[r][c] ? '#7B61FF' : '#12172C';
      pctx.fillRect(c*cellSize+1.5, r*cellSize+1.5, cellSize-3, cellSize-3);
    }
  }
  pctx.strokeStyle = '#262E52';
  for(let i=0;i<=GRID_SIZE;i++){
    pctx.beginPath(); pctx.moveTo(i*cellSize,0); pctx.lineTo(i*cellSize,patternCanvas.height); pctx.stroke();
    pctx.beginPath(); pctx.moveTo(0,i*cellSize); pctx.lineTo(patternCanvas.width,i*cellSize); pctx.stroke();
  }
}
function updateNumericOut(){
  const out = document.getElementById('numeric-out');
  if(grid.flat().every(v=>v===0)){ out.textContent = "Draw a pattern to see the input values"; return; }
  out.textContent = grid.map(row=>row.join(' ')).join('\n');
}
function cellFromEvent(e){
  const rect = patternCanvas.getBoundingClientRect();
  const x = (e.clientX ?? e.touches?.[0].clientX) - rect.left;
  const y = (e.clientY ?? e.touches?.[0].clientY) - rect.top;
  const c = Math.floor(x / (rect.width/GRID_SIZE));
  const r = Math.floor(y / (rect.height/GRID_SIZE));
  return {r,c};
}
let painting=false, paintValue=1;
patternCanvas.addEventListener('mousedown', e=>{
  const {r,c} = cellFromEvent(e);
  if(r<0||r>=GRID_SIZE||c<0||c>=GRID_SIZE) return;
  paintValue = grid[r][c] ? 0 : 1;
  grid[r][c] = paintValue; painting = true;
  drawGrid(); updateNumericOut();
});
window.addEventListener('mouseup', ()=>painting=false);
patternCanvas.addEventListener('mousemove', e=>{
  if(!painting) return;
  const {r,c} = cellFromEvent(e);
  if(r<0||r>=GRID_SIZE||c<0||c>=GRID_SIZE) return;
  grid[r][c] = paintValue;
  drawGrid(); updateNumericOut();
});
patternCanvas.addEventListener('touchstart', e=>{
  e.preventDefault();
  const {r,c} = cellFromEvent(e);
  if(r<0||r>=GRID_SIZE||c<0||c>=GRID_SIZE) return;
  grid[r][c] = grid[r][c]?0:1;
  drawGrid(); updateNumericOut();
},{passive:false});

document.getElementById('clear-grid').addEventListener('click', ()=>{
  grid = Array.from({length:GRID_SIZE},()=>Array(GRID_SIZE).fill(0));
  drawGrid(); updateNumericOut();
  document.getElementById('pred-card').classList.remove('show');
});
document.querySelectorAll('[data-load]').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    grid = tmplToMatrix(btn.dataset.load).map(r=>r.slice());
    drawGrid(); updateNumericOut();
  });
});
drawGrid();

/* ============================================================
   NEURAL NETWORK SVG DIAGRAM (input -> hidden -> output)
   ============================================================ */
const nnSvg = document.getElementById('nn-svg');
const LAYER_X = [70, 320, 570];
const NEURON_COUNTS = [8,6,3];
const LABELS_OUT = ['Circle','Square','Triangle'];
let neuronPositions = [[],[],[]];

function buildNN(){
  nnSvg.innerHTML = '';
  const H = 320;
  for(let l=0;l<3;l++){
    const n = NEURON_COUNTS[l];
    const gap = H/(n+1);
    for(let i=0;i<n;i++){
      neuronPositions[l].push({x:LAYER_X[l], y:gap*(i+1)});
    }
  }
  // connections
  const lineGroup = document.createElementNS('http://www.w3.org/2000/svg','g');
  lineGroup.setAttribute('id','nn-lines');
  for(let l=0;l<2;l++){
    for(const a of neuronPositions[l]){
      for(const b of neuronPositions[l+1]){
        const line = document.createElementNS('http://www.w3.org/2000/svg','line');
        line.setAttribute('x1',a.x); line.setAttribute('y1',a.y);
        line.setAttribute('x2',b.x); line.setAttribute('y2',b.y);
        line.setAttribute('stroke', '#262E52');
        line.setAttribute('stroke-width', '1');
        line.classList.add('nn-edge', 'layer-'+l);
        lineGroup.appendChild(line);
      }
    }
  }
  nnSvg.appendChild(lineGroup);

  // neurons
  for(let l=0;l<3;l++){
    for(let i=0;i<neuronPositions[l].length;i++){
      const pos = neuronPositions[l][i];
      const circle = document.createElementNS('http://www.w3.org/2000/svg','circle');
      circle.setAttribute('cx',pos.x); circle.setAttribute('cy',pos.y); circle.setAttribute('r', l===1?11:13);
      circle.setAttribute('fill', l===0?'#191F3B':(l===1?'#191F3B':'#191F3B'));
      circle.setAttribute('stroke', '#4CC9F0');
      circle.setAttribute('stroke-width','1.4');
      circle.classList.add('neuron','layer-node-'+l);
      circle.dataset.layer = l;
      circle.dataset.index = i;
      circle.addEventListener('mouseenter', showNeuronTip);
      circle.addEventListener('mousemove', moveNeuronTip);
      circle.addEventListener('mouseleave', hideNeuronTip);
      nnSvg.appendChild(circle);
      if(l===2){
        const text = document.createElementNS('http://www.w3.org/2000/svg','text');
        text.setAttribute('x', pos.x+22); text.setAttribute('y', pos.y+4);
        text.setAttribute('fill','#8B92B8'); text.setAttribute('font-size','12');
        text.setAttribute('font-family','IBM Plex Mono, monospace');
        text.textContent = LABELS_OUT[i];
        nnSvg.appendChild(text);
      }
    }
  }
}
buildNN();

const tip = document.createElement('div');
tip.className = 'neuron-tip';
document.body.appendChild(tip);
function showNeuronTip(e){
  const l = e.target.dataset.layer, i = e.target.dataset.index;
  let text;
  if(l==='0') text = `Input neuron ${i}: carries the value of one region of your pattern into the network.`;
  else if(l==='1') text = `Hidden neuron ${i}: activated because part of the input matches a learned feature, like an edge or curve.`;
  else text = `Output neuron "${LABELS_OUT[i]}": its activation level becomes this shape's prediction score.`;
  tip.textContent = text;
  tip.style.opacity = 1;
}
function moveNeuronTip(e){ tip.style.left = (e.clientX+14)+'px'; tip.style.top=(e.clientY+10)+'px'; }
function hideNeuronTip(){ tip.style.opacity = 0; }

function pulseNetwork(){
  document.querySelectorAll('.nn-edge').forEach((line,idx)=>{
    setTimeout(()=>{
      line.setAttribute('stroke', '#7B61FF');
      line.setAttribute('stroke-width','1.8');
      setTimeout(()=>{ line.setAttribute('stroke','#262E52'); line.setAttribute('stroke-width','1'); }, 500);
    }, (line.classList.contains('layer-0')?0:400) + Math.random()*250);
  });
  document.querySelectorAll('.neuron').forEach(n=>{
    const l = n.dataset.layer;
    const delay = l==='0'?100 : l==='1'?550 : 950;
    setTimeout(()=>{
      n.setAttribute('fill', '#4CC9F0');
      setTimeout(()=>n.setAttribute('fill', '#191F3B'), 500);
    }, delay);
  });
}

/* ============================================================
   PREDICTION LOGIC (similarity-based educational simulation)
   ============================================================ */
function similarity(a,b){
  let match=0;
  for(let r=0;r<GRID_SIZE;r++) for(let c=0;c<GRID_SIZE;c++) if(a[r][c]===b[r][c]) match++;
  return match / (GRID_SIZE*GRID_SIZE);
}
function predict(userGrid){
  const keys = ['circle','square','triangle'];
  const scores = keys.map(k=>similarity(userGrid, tmplToMatrix(k)));
  // softmax-ish sharpening for a confident-looking distribution
  const sharp = scores.map(s=>Math.pow(s,6));
  const sum = sharp.reduce((a,b)=>a+b,0) || 1;
  const probs = sharp.map(s=> sum ? s/sum : 1/keys.length);
  return keys.map((k,i)=>({label:k, prob:probs[i]})).sort((a,b)=>b.prob-a.prob);
}
const FEATURES = {
  circle:['Curved, closed outline detected','Roughly equal width and height','Few sharp corners found','High overlap with learned circle template'],
  square:['Straight edges on all four sides detected','Sharp 90° corners found','Symmetric width and height','High overlap with learned square template'],
  triangle:['Pattern narrows toward the top','Three dominant edges detected','Wide flat base found','High overlap with learned triangle template'],
};

document.getElementById('submit-pattern').addEventListener('click', ()=>{
  pulseNetwork();
  setTimeout(()=>{
    const ranked = predict(grid);
    const top = ranked[0];
    document.getElementById('pred-main').textContent = top.label.toUpperCase();
    document.getElementById('pred-conf').textContent = `confidence: ${Math.round(top.prob*100)}%`;
    const barsEl = document.getElementById('pred-bars');
    barsEl.innerHTML = '';
    ranked.forEach(r=>{
      const row = document.createElement('div'); row.className='bar-row';
      row.innerHTML = `<span>${r.label}</span><div class="bar-track"><div class="bar-fill"></div></div><span>${Math.round(r.prob*100)}%</span>`;
      barsEl.appendChild(row);
      requestAnimationFrame(()=>{ row.querySelector('.bar-fill').style.width = (r.prob*100)+'%'; });
    });
    document.getElementById('pred-card').classList.add('show');
    document.getElementById('why-list').classList.remove('show');
    document.getElementById('why-list').innerHTML = FEATURES[top.label].map(f=>`<li>${f}</li>`).join('');
  }, 1300);
});
document.getElementById('why-btn').addEventListener('click', ()=>{
  document.getElementById('why-list').classList.toggle('show');
});

/* ============================================================
   NEURON EXPLAIN DIAGRAM
   ============================================================ */
(function neuronDiagram(){
  const svg = document.getElementById('neuron-svg');
  const inputs = [
    {label:'Input 1', val:'0.9', w:'0.4', y:40},
    {label:'Input 2', val:'0.2', w:'-0.6', y:100},
    {label:'Input 3', val:'0.7', w:'0.8', y:160},
    {label:'Bias', val:'', w:'0.1', y:220},
  ];
  let svgContent = '';
  inputs.forEach(inp=>{
    svgContent += `<text x="10" y="${inp.y+5}" fill="#E9EBF7" font-size="13" font-family="IBM Plex Mono, monospace">${inp.label}${inp.val? ' = '+inp.val:''}</text>`;
    svgContent += `<line x1="140" y1="${inp.y}" x2="330" y2="130" stroke="#7B61FF" stroke-width="1.4" opacity="0.7"/>`;
    svgContent += `<text x="200" y="${inp.y + (130-inp.y)/2 - 6}" fill="#4CC9F0" font-size="11" font-family="IBM Plex Mono, monospace">×${inp.w}</text>`;
  });
  svgContent += `<circle cx="360" cy="130" r="34" fill="#191F3B" stroke="#FF9B6B" stroke-width="1.8"/>`;
  svgContent += `<text x="360" y="126" fill="#FF9B6B" font-size="11" text-anchor="middle" font-family="IBM Plex Mono, monospace">Sum +</text>`;
  svgContent += `<text x="360" y="140" fill="#FF9B6B" font-size="11" text-anchor="middle" font-family="IBM Plex Mono, monospace">Activate</text>`;
  svgContent += `<line x1="394" y1="130" x2="600" y2="130" stroke="#FF9B6B" stroke-width="1.8"/>`;
  svgContent += `<circle cx="620" cy="130" r="16" fill="#191F3B" stroke="#57D9A3" stroke-width="1.8"/>`;
  svgContent += `<text x="620" y="165" fill="#57D9A3" font-size="12" text-anchor="middle" font-family="IBM Plex Mono, monospace">Output</text>`;
  svg.innerHTML = svgContent;
})();

/* ============================================================
   TRAINING SIMULATION
   ============================================================ */
const chartCanvas = document.getElementById('chart-canvas');
const cctx = chartCanvas.getContext('2d');
let epochData = [];
function drawChart(){
  const W = chartCanvas.width, H = chartCanvas.height, pad=36;
  cctx.clearRect(0,0,W,H);
  cctx.strokeStyle = '#262E52'; cctx.lineWidth=1;
  for(let i=0;i<=4;i++){
    const y = pad + (H-2*pad)*i/4;
    cctx.beginPath(); cctx.moveTo(pad,y); cctx.lineTo(W-pad,y); cctx.stroke();
    cctx.fillStyle='#8B92B8'; cctx.font='10px IBM Plex Mono';
    cctx.fillText(`${100-i*25}%`, 2, y+3);
  }
  if(epochData.length<2) return;
  cctx.beginPath();
  epochData.forEach((v,i)=>{
    const x = pad + (W-2*pad)*(i/(Math.max(epochData.length-1,1)));
    const y = pad + (H-2*pad)*(1-v/100);
    if(i===0) cctx.moveTo(x,y); else cctx.lineTo(x,y);
  });
  const grad = cctx.createLinearGradient(0,0,W,0);
  grad.addColorStop(0,'#7B61FF'); grad.addColorStop(1,'#4CC9F0');
  cctx.strokeStyle = grad; cctx.lineWidth=2.4; cctx.stroke();
}
drawChart();

const flowSteps = document.querySelectorAll('#flow-steps span');
let trainingRunning = false;
document.getElementById('start-training').addEventListener('click', function(){
  if(trainingRunning) return;
  trainingRunning = true;
  this.disabled = true;
  epochData = [];
  const log = document.getElementById('epoch-log');
  log.innerHTML = '';
  const checkpoints = [1,10,25,50,75,100];
  let idx = 0;
  let acc = 8 + Math.random()*10;
  const interval = setInterval(()=>{
    flowSteps.forEach(s=>s.classList.remove('active'));
    flowSteps[idx % flowSteps.length].classList.add('active');
    idx++;

    acc = Math.min(97, acc + (97-acc)*0.14 + Math.random()*2);
    epochData.push(acc);
    drawChart();

    const epochNum = epochData.length*2;
    if(checkpoints.includes(epochNum) || epochNum>=100){
      const line = document.createElement('span');
      line.innerHTML = `Epoch <b>${Math.min(epochNum,100)}</b> &nbsp;&nbsp; Accuracy: <b>${acc.toFixed(0)}%</b>`;
      log.appendChild(line);
    }
    if(epochData.length >= 50){
      clearInterval(interval);
      flowSteps.forEach(s=>s.classList.remove('active'));
      trainingRunning = false;
      document.getElementById('start-training').disabled = false;
    }
  }, 90);
});

/* ============================================================
   LAYER CARD -> highlight NN diagram
   ============================================================ */
document.querySelectorAll('.layer-card').forEach(card=>{
  card.addEventListener('click', ()=>{
    document.querySelectorAll('.layer-card').forEach(c=>c.classList.remove('active'));
    card.classList.add('active');
    const layer = card.dataset.layer;
    document.querySelectorAll('.neuron').forEach(n=>{
      if(n.dataset.layer === layer){
        n.setAttribute('stroke', '#FF9B6B'); n.setAttribute('stroke-width','2.4');
      } else {
        n.setAttribute('stroke', '#4CC9F0'); n.setAttribute('stroke-width','1.4');
      }
    });
    document.getElementById('experiment').scrollIntoView({behavior:'smooth', block:'center'});
  });
});

/* ============================================================
   MISTAKE -> LEARNING DEMO
   ============================================================ */
const mistakeSteps = document.querySelectorAll('.mistake-step');
let mistakeIdx = -1;
const mistakeBtn = document.getElementById('mistake-next');
function playMistakeStep(){
  mistakeIdx++;
  if(mistakeIdx >= mistakeSteps.length){
    mistakeSteps.forEach(s=>s.classList.remove('active','wrong','right'));
    mistakeIdx = -1;
    mistakeBtn.textContent = 'Play Next Step →';
    return;
  }
  const step = mistakeSteps[mistakeIdx];
  step.classList.add('active');
  if(mistakeIdx===1) step.classList.add('wrong');
  if(mistakeIdx===5) step.classList.add('right');
  mistakeBtn.textContent = mistakeIdx === mistakeSteps.length-1 ? 'Restart ↺' : 'Play Next Step →';
}
mistakeBtn.addEventListener('click', playMistakeStep);

/* ============================================================
   APPLICATIONS GRID
   ============================================================ */
const APPS = [
  {name:'Handwriting Recognition', desc:'Turns scribbled letters and digits into typed text.', icon:'M4 20h16M4 20l6-14 3 8 2-4 5 10'},
  {name:'Face Recognition', desc:'Identifies a person by the pattern of their facial features.', icon:'M12 3a9 9 0 100 18 9 9 0 000-18zM8 10h.01M16 10h.01M8 15c1.5 1.5 6.5 1.5 8 0'},
  {name:'Medical Image Analysis', desc:'Spots patterns in scans that can indicate disease.', icon:'M3 12h4l2-7 4 14 2-7h6'},
  {name:'Speech Recognition', desc:'Recognizes patterns in sound waves to transcribe speech.', icon:'M12 3v6m0 0a3 3 0 003-3V6a3 3 0 10-6 0v0a3 3 0 003 3zm-7 7a7 7 0 0014 0M12 19v3'},
  {name:'Object Detection', desc:'Locates and labels known shapes and objects in images.', icon:'M4 4h6v6H4V4zm10 10h6v6h-6v-6zM4 20l6-6M20 4l-6 6'},
  {name:'Fraud Detection', desc:'Flags transactions whose pattern differs from normal behavior.', icon:'M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6l8-4z'},
];
const appGrid = document.getElementById('app-grid');
APPS.forEach(a=>{
  const el = document.createElement('div');
  el.className = 'card app-card';
  el.innerHTML = `<svg class="app-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="${a.icon}"/></svg>
    <div><h4>${a.name}</h4><p>${a.desc}</p></div>`;
  appGrid.appendChild(el);
});
</script>
</body>
</html>
