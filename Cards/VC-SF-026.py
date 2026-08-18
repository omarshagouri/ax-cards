# VC-SF-026  |  caption-safe-zone pass 2026-08-18
CARD = {
    "id": "VC-SF-026",
    "slots": ["SOURCE_NAME"],
    "default_duration": 2.5,
    "css": r'''.st-tag{position:absolute;left:96px;bottom:320px;display:flex;align-items:center;gap:20px;opacity:0;transform:translateX(-24px);}
.st-bar{width:12px;height:48px;background:#00D4AA;border-radius:3px;}
.st-txt{font-family:Inter;font-weight:600;font-size:32px;color:#FFFFFF;letter-spacing:.02em;}

/* --- caption-safe-zone pass: keep all text above y=1180 (caption band y1180-1540) --- */
.st-tag{bottom:820px !important;}
''',
    "body": r'''<div class="st-tag" id="stTag"><div class="st-bar"></div><div class="st-txt">SOURCE: __SOURCE_NAME__</div></div>''',
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

__fit(".st-txt",860,0,1,0);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var e=easeOutCubic(clamp((t-0.1)/0.6));var el=document.getElementById('stTag');el.style.opacity=e;el.style.transform='translateX('+(-24*(1-e))+'px)';''',
}
