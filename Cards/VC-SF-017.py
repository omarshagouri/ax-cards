CARD = {
    "id": "VC-SF-017",
    "slots": ["STEP1", "STEP2", "STEP3", "STEP4"],
    "default_duration": 4.5,
    "css": r""".pr-wrap{position:absolute;left:96px;top:0;width:888px;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:30px;}
.pr-step{width:640px;padding:34px 30px;background:rgba(10,22,40,.6);border:1px solid rgba(0,212,170,.4);border-radius:18px;font-family:'Space Grotesk';font-weight:700;font-size:52px;color:#FFFFFF;text-align:center;opacity:0;transform:translateY(34px);}
.pr-arr{font-size:52px;color:#00D4AA;opacity:0;transform:translateY(10px);line-height:0.6;}""",
    "body": r"""<div class="pr-wrap">
<div class="pr-step" id="ps1">__STEP1__</div><div class="pr-arr" id="pa1">&#9660;</div>
<div class="pr-step" id="ps2">__STEP2__</div><div class="pr-arr" id="pa2">&#9660;</div>
<div class="pr-step" id="ps3">__STEP3__</div><div class="pr-arr" id="pa3">&#9660;</div>
<div class="pr-step" id="ps4">__STEP4__</div></div>""",
    "seek": r"""function show(id,a,b,dy){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.opacity=e;el.style.transform='translateY('+(dy*(1-e))+'px)';}}
function grow(id,a,b){var e=easeOutCubic(clamp((t-a)/(b-a)));var el=document.getElementById(id);if(el){el.style.transform='scaleX('+e+')';}}
[['ps4','pa3'],['ps3','pa2'],['ps2','pa1']].forEach(function(pr){var el=document.getElementById(pr[0]);if(el&&el.textContent.indexOf('__')>-1){el.style.display='none';var a=document.getElementById(pr[1]);if(a)a.style.display='none';}});
show('ps1',0.15,0.85,34);show('pa1',0.7,1.1,10);show('ps2',0.95,1.6,34);show('pa2',1.45,1.85,10);show('ps3',1.7,2.35,34);show('pa3',2.2,2.6,10);show('ps4',2.45,3.1,34);""",
}
