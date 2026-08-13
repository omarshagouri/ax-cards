# VC-SF-028  |  Thumbnail / first-frame card (static composite)
# Rendered by ax-render /thumbnail, composited by agent 4_a.
# Render-time placeholders filled by the /thumbnail route (NOT dataset slots):
#   __BG_SRC__   = background image source (data URI or URL) from background_file_id
#   __LOGO_SRC__ = AmpCoreX logo source (data URI or URL) from logo_file_id (fixed asset, never restyled)
# Dataset text slots (from the writer agent):  HEADLINE, SUBHEAD
#   HEADLINE: wrap the key word in *asterisks* to colour it teal, e.g. "YOUR EV *PAYS* YOU"
#   SUBHEAD : optional; leave blank to render nothing.
CARD = {
    "id": "VC-SF-028",
    "slots": ["HEADLINE", "SUBHEAD"],
    "default_duration": 1.0,
    "css": r'''
.tc-root{ position:absolute; inset:0; background:#0A1628; overflow:hidden; }
.tc-bg{ position:absolute; inset:0; background-image:url("__BG_SRC__");
        background-size:cover; background-position:center; background-repeat:no-repeat; }
.tc-veil{ position:absolute; inset:0; background:
    linear-gradient(180deg, rgba(10,22,40,.72) 0%, rgba(10,22,40,.30) 22%,
      rgba(10,22,40,.00) 42%, rgba(10,22,40,.00) 60%, rgba(10,22,40,.55) 84%, rgba(10,22,40,.90) 100%); }
.tc-top{ position:absolute; top:214px; left:96px; width:840px; display:flex; flex-direction:column; gap:30px; }
.tc-head{ margin:0; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:104px;
          line-height:1.08; letter-spacing:-1px; color:#FFFFFF; text-shadow:0 4px 30px rgba(0,0,0,.5); }
.tc-head .key{ color:#00D4AA; }
.tc-sub{ margin:0; font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:54px;
         line-height:1.2; color:#FFFFFF; text-shadow:0 3px 22px rgba(0,0,0,.5); }
.tc-logo{ position:absolute; left:0; bottom:380px; width:1080px; text-align:center; }
.tc-logo img{ height:112px; width:auto; display:inline-block; }
''',
    "body": r'''
<div class="tc-root">
  <div class="tc-bg" id="tcBg"></div>
  <div class="tc-veil"></div>
  <div class="tc-top">
    <h1 class="tc-head" id="tcHead">__HEADLINE__</h1>
    <p class="tc-sub" id="tcSub">__SUBHEAD__</p>
  </div>
  <div class="tc-logo" id="tcLogo"><img id="tcLogoImg" src="__LOGO_SRC__" alt=""></div>
</div>
''',
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

// teal keyword: wrap any *word* in HEADLINE with the teal span, then strip the markers
var h=document.getElementById('tcHead');
if(h && h.dataset.kw!=='1'){ h.innerHTML=h.textContent.replace(/\*([^*]+)\*/g,'<span class="key">$1</span>'); h.dataset.kw='1'; }
// optional SUBHEAD: if empty or unfilled, render nothing (no gap)
var s=document.getElementById('tcSub');
if(s){ var st=s.textContent.trim(); if(!st || st.indexOf('__SUB')>-1){ s.style.display='none'; } }
// logo: hide the lockup if no logo source was injected
var li=document.getElementById('tcLogoImg');
if(li){ var src=li.getAttribute('src')||''; if(!src || src.indexOf('__LOGO')>-1){ var lw=document.getElementById('tcLogo'); if(lw) lw.style.display='none'; } }
// background: if unfilled, the invalid url simply shows the navy root underneath
// safe-zone text fit (static first frame)
__fit('.tc-head',840,560,0,0);
__fit('.tc-sub',840,180,0,0);
''',
}
