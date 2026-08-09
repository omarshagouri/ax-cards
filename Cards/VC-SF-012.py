# VC-SF-012  |  auto-fit safe-zone patch applied 2026-08-09
# Text shrink-to-fit added at top of seek(); css/body unchanged.
CARD = {
    "id": "VC-SF-012",
    "slots": ["LOW_PCT", "HIGH_PCT", "CAPTION"],
    "default_duration": 4.0,
    "css": r'''.soc-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;}
.soc-cap{font-family:'Space Grotesk';font-weight:700;font-size:56px;color:#FFFFFF;margin-bottom:60px;text-align:center;opacity:0;transform:translateY(28px);}
.soc-track{position:relative;width:820px;height:96px;background:rgba(140,160,184,.18);border-radius:16px;overflow:hidden;}
.soc-fill{position:absolute;top:0;height:100%;background:#00D4AA;transform:scaleX(0);transform-origin:left;}
.soc-lab{position:absolute;top:-56px;font-family:'Space Grotesk';font-weight:700;font-size:40px;color:#00D4AA;opacity:0;}
.soc-ends{width:820px;display:flex;justify-content:space-between;margin-top:22px;font-family:Inter;font-weight:600;font-size:32px;color:#8CA0B8;}''',
    "body": r'''<div class="soc-wrap"><div class="soc-cap" id="socCap">__CAPTION__</div>
<div class="soc-track"><div class="soc-fill" id="socFill"></div><div class="soc-lab" id="socLo">__LOW_PCT__%</div><div class="soc-lab" id="socHi">__HIGH_PCT__%</div></div>
<div class="soc-ends"><span>0%</span><span>100%</span></div></div>''',
    "seek": r'''
if(!window.__fit){window.__fit=function(sel,maxW,maxH,line,center){
var els=document.querySelectorAll(sel);var ready=(!document.fonts)||document.fonts.status==='loaded';
for(var i=0;i<els.length;i++){var el=els[i];
if(el.dataset.fitok==='1'){el.style.fontSize=el.dataset.fitpx+'px';continue;}
if(!el.dataset.fbase){el.dataset.fbase=(parseFloat(getComputedStyle(el).fontSize)||40);}
if(maxW){el.style.maxWidth=maxW+'px';if(center){el.style.marginLeft='auto';el.style.marginRight='auto';}}
el.style.whiteSpace=line?'nowrap':'normal';if(!line){el.style.overflowWrap='break-word';el.style.wordBreak='break-word';}
var size=parseFloat(el.dataset.fbase);el.style.fontSize=size+'px';var g=0;
while(size>16&&g<240&&(el.scrollWidth>el.clientWidth+0.5||(maxH&&el.scrollHeight>maxH+0.5))){size-=2;el.style.fontSize=size+'px';g++;}
if(ready){el.dataset.fitpx=size;el.dataset.fitok='1';}}
};}

__fit(".soc-cap",820,180,0,1);__fit(".soc-lab",110,0,1,0);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
show('socCap',0.1,0.85,28);
var lo=parseFloat(('__LOW_PCT__'.match(/[\d.]+/)||[20])[0]);var hi=parseFloat(('__HIGH_PCT__'.match(/[\d.]+/)||[80])[0]);
// NOTE: preview substitutes real values; renderer fills the slots before this runs.
var fill=document.getElementById('socFill');var track=820;
var loF=lo/100, hiF=hi/100;var e=easeOutCubic(clamp((t-0.7)/0.9));
fill.style.left=(loF*track)+'px';fill.style.width=(track*(hiF-loF))+'px';fill.style.transform='scaleX('+e+')';fill.style.transformOrigin='left';
var elo=document.getElementById('socLo'),ehi=document.getElementById('socHi');
elo.style.left=(loF*track-10)+'px';ehi.style.left=(hiF*track-70)+'px';
elo.style.opacity=easeOutCubic(clamp((t-1.4)/0.5));ehi.style.opacity=easeOutCubic(clamp((t-1.6)/0.5));''',
}
