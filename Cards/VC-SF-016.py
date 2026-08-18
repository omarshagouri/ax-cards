# VC-SF-016  |  caption-safe-zone pass 2026-08-18
CARD = {
    "id": "VC-SF-016",
    "slots": ["P1_YEAR", "P1_LABEL", "P2_YEAR", "P2_LABEL", "P3_YEAR", "P3_LABEL", "P4_YEAR", "P4_LABEL"],
    "default_duration": 4.5,
    "css": r'''.tl-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;}
.tl-line{position:relative;height:6px;background:rgba(140,160,184,.25);border-radius:3px;margin:0 20px;}
.tl-prog{position:absolute;left:0;top:0;height:100%;width:100%;background:#00D4AA;transform:scaleX(0);transform-origin:left;border-radius:3px;}
.tl-pts{position:relative;display:flex;justify-content:space-between;margin:0 20px;}
.tl-pt{position:absolute;transform:translateX(-50%);text-align:center;top:-14px;opacity:0;}
.tl-dot{width:30px;height:30px;border-radius:50%;background:#00D4AA;margin:0 auto 18px;box-shadow:0 0 0 8px rgba(0,212,170,.18);}
.tl-yr{font-family:'Space Grotesk';font-weight:700;font-size:44px;color:#FFFFFF;}
.tl-lb{font-family:Inter;font-weight:400;font-size:32px;color:#8CA0B8;max-width:230px;margin:8px auto 0;line-height:1.2;}

/* --- caption-safe-zone pass: keep all text above y=1180 (caption band y1180-1540) --- */
.tl-wrap{top:192px !important;height:988px !important;}
''',
    "body": r'''<div class="tl-wrap"><div class="tl-line"><div class="tl-prog" id="tlProg"></div>
<div class="tl-pts" id="tlPts">
<div class="tl-pt" id="tp1" style="left:8%"><div class="tl-dot"></div><div class="tl-yr">__P1_YEAR__</div><div class="tl-lb">__P1_LABEL__</div></div>
<div class="tl-pt" id="tp2" style="left:36%"><div class="tl-dot"></div><div class="tl-yr">__P2_YEAR__</div><div class="tl-lb">__P2_LABEL__</div></div>
<div class="tl-pt" id="tp3" style="left:64%"><div class="tl-dot"></div><div class="tl-yr">__P3_YEAR__</div><div class="tl-lb">__P3_LABEL__</div></div>
<div class="tl-pt" id="tp4" style="left:92%"><div class="tl-dot"></div><div class="tl-yr">__P4_YEAR__</div><div class="tl-lb">__P4_LABEL__</div></div>
</div></div></div>''',
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

__fit(".tl-yr",200,0,1,0);__fit(".tl-lb",230,150,0,0);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
['tp1','tp2','tp3','tp4'].forEach(function(id){var el=document.getElementById(id);if(el&&el.textContent.indexOf('__')>-1){el.style.display='none';}});
grow('tlProg',0.2,1.8);
show('tp1',0.4,1.0,18);show('tp2',0.85,1.45,18);show('tp3',1.3,1.9,18);show('tp4',1.75,2.35,18);''',
}
