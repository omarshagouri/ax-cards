# VC-SF-010  |  caption-safe-zone pass 2026-08-18
CARD = {
    "id": "VC-SF-010",
    "slots": ["COL1_TITLE", "COL1_POINT", "COL2_TITLE", "COL2_POINT", "COL3_TITLE", "COL3_POINT"],
    "default_duration": 4.5,
    "css": r'''.col-wrap{position:absolute;left:0;top:0;width:1080px;height:100%;display:flex;justify-content:center;align-items:center;gap:40px;}
.col{width:270px;min-height:360px;background:rgba(10,22,40,.55);border:1px solid rgba(0,212,170,.35);border-radius:20px;padding:36px 26px;opacity:0;transform:translateY(40px);}
.col-t{font-family:'Space Grotesk';font-weight:700;font-size:40px;color:#00D4AA;line-height:1.1;}
.col-bar{width:52px;height:4px;background:#00D4AA;border-radius:2px;margin:20px 0 24px;}
.col-p{font-family:Inter;font-weight:400;font-size:38px;line-height:1.32;color:#FFFFFF;}

/* --- caption-safe-zone pass: keep all text above y=1180 (caption band y1180-1540) --- */
.col-wrap{top:192px !important;height:988px !important;}
''',
    "body": r'''<div class="col-wrap">
<div class="col" id="c1"><div class="col-t">__COL1_TITLE__</div><div class="col-bar"></div><div class="col-p">__COL1_POINT__</div></div>
<div class="col" id="c2"><div class="col-t">__COL2_TITLE__</div><div class="col-bar"></div><div class="col-p">__COL2_POINT__</div></div>
<div class="col" id="c3"><div class="col-t">__COL3_TITLE__</div><div class="col-bar"></div><div class="col-p">__COL3_POINT__</div></div></div>''',
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

__fit(".col-t",224,0,1,1);__fit(".col-p",224,240,0,1);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
['c1','c2','c3'].forEach(function(id){var el=document.getElementById(id);if(el&&el.textContent.indexOf('__')>-1){el.style.display='none';}});
show('c1',0.15,0.9,40);show('c2',0.6,1.35,40);show('c3',1.05,1.8,40);''',
}
