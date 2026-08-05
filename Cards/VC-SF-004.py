CARD = {
    "id": "VC-SF-004",
    "slots": ["KICKER", "HOOK"],
    "default_duration": 4.0,
    "css": """
.hook-wrap{
  position:absolute; left:96px; top:0;
  width:840px; height:100%;
  display:flex; flex-direction:column; justify-content:center; align-items:flex-start;
}
.hook-krow{ display:flex; align-items:center; gap:22px; margin-bottom:30px; }
.hook-bar{
  width:66px; height:5px; background:#00D4AA; border-radius:2px;
  transform:scaleX(0); transform-origin:left center;
}
.hook-kicker{
  font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:32px;
  letter-spacing:0.14em; text-transform:uppercase; color:#00D4AA;
  opacity:0; transform:translateY(16px);
}
.hook-line{
  font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:92px;
  line-height:1.06; color:#FFFFFF;
  opacity:0; transform:translateY(48px);
}
""",
    "body": """
<div class="hook-wrap">
  <div class="hook-krow">
    <div class="hook-bar" id="hkBar"></div>
    <div class="hook-kicker" id="hkKicker">__KICKER__</div>
  </div>
  <div class="hook-line" id="hkLine">__HOOK__</div>
</div>
""",
    "seek": """
// 1) accent bar wipes in left-to-right (0.00 - 0.60s)
var eBar = easeOutCubic(clamp(t / 0.60));
document.getElementById('hkBar').style.transform = 'scaleX(' + eBar + ')';

// 2) kicker fades + rises (0.55 - 1.15s)
var eK = easeOutCubic(clamp((t - 0.55) / 0.60));
var k = document.getElementById('hkKicker');
k.style.opacity = eK;
k.style.transform = 'translateY(' + (16 * (1 - eK)) + 'px)';

// 3) hook line rises + fades (1.15 - 2.25s), then hold
var eH = easeOutCubic(clamp((t - 1.15) / 1.10));
var line = document.getElementById('hkLine');
line.style.opacity = eH;
line.style.transform = 'translateY(' + (48 * (1 - eH)) + 'px)';
""",
}
