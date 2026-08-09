# VC-SF-020  |  auto-fit safe-zone patch applied 2026-08-09
# Text shrink-to-fit added at top of seek(); css/body unchanged.
CARD = {
    "id": "VC-SF-020",
    "slots": ["TAG_TEXT"],
    "default_duration": 3.0,
    "css": r'''.tag-chip{position:absolute;left:96px;top:300px;display:inline-flex;align-items:center;gap:16px;background:rgba(10,22,40,.82);border:2px solid #00D4AA;border-radius:14px;padding:20px 30px;opacity:0;transform:translateX(-30px);}
.tag-dot{width:16px;height:16px;border-radius:50%;background:#00D4AA;}
.tag-t{font-family:'Space Grotesk';font-weight:600;font-size:40px;letter-spacing:.06em;color:#FFFFFF;text-transform:uppercase;}''',
    "body": r'''<div class="tag-chip" id="tagChip"><div class="tag-dot"></div><div class="tag-t">__TAG_TEXT__</div></div>''',
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

__fit(".tag-t",700,0,1,0);
function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
var e=easeOutCubic(clamp((t-0.1)/0.6));var c=document.getElementById('tagChip');c.style.opacity=e;c.style.transform='translateX('+(-30*(1-e))+'px)';''',
}
