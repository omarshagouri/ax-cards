# ============================================================
# VC-SH-002.py  —  AmpCoreX Visual Card
# Card: Versus (two bars)
# Motion: title fades in (0.0-0.6s), bars grow up from baseline
#         (0.5-1.3s), value labels rise in above bars (1.3-1.7s)
# ============================================================

CARD = {
    "id": "VC-SH-002",
    "slots": ["TITLE", "VALUE_A", "LABEL_A", "VALUE_B", "LABEL_B", "SOURCE"],
    "default_duration": 3.0,

    "css": """
        #title{
            position:absolute; top:230px; left:0; width:1080px; text-align:center;
            color:#FFFFFF; font-size:76px; font-weight:700; opacity:0;
        }
        .baseline{
            position:absolute; bottom:620px; left:240px; width:600px; height:3px;
            background:#8CA0B8; opacity:0.35;
        }
        .bar{
            position:absolute; bottom:620px; width:200px; height:0;
            transform-origin:bottom center; transform:scaleY(0);
            border-radius:4px 4px 0 0;
        }
        #barA{ left:300px; background:#00D4AA; }
        #barB{ left:600px; background:#FF7A3C; }
        .val{
            position:absolute; width:200px; text-align:center;
            color:#FFFFFF; font-size:64px; font-weight:700; opacity:0;
        }
        #valA{ left:300px; } #valB{ left:600px; }
        .axis{
            position:absolute; bottom:520px;
            width:360px; text-align:center; white-space:nowrap;
            color:#8CA0B8; font-size:40px; font-weight:500; opacity:0;
        }
        #labA{ left:220px; } #labB{ left:520px; }
        #source{
            position:absolute; bottom:340px; left:90px;
            color:#8CA0B8; font-size:30px; font-weight:400; opacity:0;
            border-left:6px solid #00D4AA; padding-left:16px;
        }
    """,

    "body": """
        <div id="title">__TITLE__</div>
        <div class="baseline"></div>
        <div class="bar" id="barA"></div>
        <div class="bar" id="barB"></div>
        <div class="val" id="valA">__VALUE_A__</div>
        <div class="val" id="valB">__VALUE_B__</div>
        <div class="axis" id="labA">__LABEL_A__</div>
        <div class="axis" id="labB">__LABEL_B__</div>
        <div id="source">__SOURCE__</div>
    """,

    "seek": """
        var title=document.getElementById('title');
        var barA=document.getElementById('barA'), barB=document.getElementById('barB');
        var valA=document.getElementById('valA'), valB=document.getElementById('valB');
        var labA=document.getElementById('labA'), labB=document.getElementById('labB');
        var source=document.getElementById('source');

        var a=parseFloat(valA.textContent)||0, b=parseFloat(valB.textContent)||0;
        var maxV=Math.max(a,b,0.0001), maxH=640;
        var hA=maxH*a/maxV, hB=maxH*b/maxV;
        barA.style.height=hA+'px'; barB.style.height=hB+'px';
        valA.style.bottom=(620+hA+18)+'px';
        valB.style.bottom=(620+hB+18)+'px';

        var te=easeOutCubic(clamp(t/0.6));
        title.style.opacity=te;
        title.style.transform='translateY('+(30*(1-te))+'px)';

        var fe=clamp((t-0.4)/0.5);
        labA.style.opacity=fe; labB.style.opacity=fe; source.style.opacity=fe;

        var ge=easeOutCubic(clamp((t-0.5)/0.8));
        barA.style.transform='scaleY('+ge+')';
        barB.style.transform='scaleY('+ge+')';

        var ve=easeOutCubic(clamp((t-1.3)/0.4));
        valA.style.opacity=ve; valB.style.opacity=ve;
        valA.style.transform='translateY('+(18*(1-ve))+'px)';
        valB.style.transform='translateY('+(18*(1-ve))+'px)';
    """,
}
