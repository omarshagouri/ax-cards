# VC-SF-018  |  caption-safe-zone pass 2026-08-18
CARD = {
    "id": "VC-SF-018",
    "slots": ["ITEM1", "ITEM2", "ITEM3", "ITEM4"],
    "default_duration": 4.5,
    "css": r'''.ig-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;}
.ig-grid{display:grid;grid-template-columns:1fr 1fr;gap:34px;}
.ig-cell{background:rgba(10,22,40,.55);border:1px solid rgba(0,212,170,.3);border-radius:20px;padding:44px 30px;display:flex;flex-direction:column;align-items:center;gap:24px;text-align:center;opacity:0;transform:translateY(38px);}
.ig-mark{width:70px;height:70px;border-radius:18px;background:rgba(0,212,170,.15);border:2px solid #00D4AA;display:flex;align-items:center;justify-content:center;color:#00D4AA;font-family:'Space Grotesk';font-weight:700;font-size:40px;}
.ig-t{font-family:'Space Grotesk';font-weight:600;font-size:44px;color:#FFFFFF;line-height:1.15;}

/* --- caption-safe-zone pass: keep all text above y=1180 (caption band y1180-1540) --- */
.ig-wrap{top:192px !important;height:988px !important;}

/* ax caption-safe v3: center ~y920, clamp bottom<=1340 (repo band bottom=1540) */
#axsafe{position:absolute;left:0;top:0;width:1080px;height:1920px;transform:translateY(235px);}
''',
    "body": r'''<div id="axsafe"><div class="ig-wrap"><div class="ig-grid">
<div class="ig-cell" id="ig1"><div class="ig-mark">&#9889;</div><div class="ig-t">__ITEM1__</div></div>
<div class="ig-cell" id="ig2"><div class="ig-mark">&#9889;</div><div class="ig-t">__ITEM2__</div></div>
<div class="ig-cell" id="ig3"><div class="ig-mark">&#9889;</div><div class="ig-t">__ITEM3__</div></div>
<div class="ig-cell" id="ig4"><div class="ig-mark">&#9889;</div><div class="ig-t">__ITEM4__</div></div></div></div></div>''',
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

__fit(".ig-t",320,170,0,1);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
['ig1','ig2','ig3','ig4'].forEach(function(id){var el=document.getElementById(id);if(el&&el.querySelector('.ig-t').textContent.indexOf('__')>-1){el.style.display='none';}});
show('ig1',0.15,0.85,38);show('ig2',0.5,1.2,38);show('ig3',0.85,1.55,38);show('ig4',1.2,1.9,38);''',
}
