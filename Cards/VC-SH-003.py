# ============================================================
# VC-SH-003.py  —  AmpCoreX Visual Card
# Card: Engineer's Note (credibility card)  [mandatory in every video]
# Motion: pill fades in (0.0-0.5s), statement rises (0.4-1.1s),
#         teal rule grows from center (1.0-1.6s), role settles in (1.5-2.0s)
#
# Uses natural text flow (not fixed coordinates), so a longer or shorter
# STATEMENT reflows cleanly. No source slot — this is the engineer's own voice.
# ============================================================

CARD = {
    "id": "VC-SH-003",
    "slots": ["TAG", "STATEMENT", "ROLE"],
    "default_duration": 4.0,          # reading-heavy, so it holds a little longer

    "css": """
        #note{
            position:absolute; top:380px; left:120px; width:840px;
            text-align:center;
        }
        .pill{
            display:inline-block; opacity:0; transform:scale(0.9);
            color:#00D4AA; border:2px solid #00D4AA; border-radius:999px;
            font-family:'Space Grotesk',sans-serif; font-size:30px; font-weight:600;
            letter-spacing:3px; text-transform:uppercase; padding:14px 34px;
        }
        .statement{
            opacity:0; margin:48px 0 0; color:#FFFFFF;
            font-family:'Space Grotesk',sans-serif; font-size:60px; font-weight:600;
            line-height:1.28;
        }
        .rule{
            width:130px; height:5px; background:#00D4AA; margin:44px auto 0;
            border-radius:3px; transform-origin:center; transform:scaleX(0);
        }
        .role{
            opacity:0; margin:40px 0 0; color:#8CA0B8;
            font-family:'Inter',sans-serif; font-size:36px; font-weight:600;
            letter-spacing:1px;
        }
    """,

    "body": """
        <div id="note">
            <div class="pill" id="pill">__TAG__</div>
            <div class="statement" id="stmt">__STATEMENT__</div>
            <div class="rule" id="rule"></div>
            <div class="role" id="role">__ROLE__</div>
        </div>
    """,

    "seek": """
        var pill=document.getElementById('pill');
        var stmt=document.getElementById('stmt');
        var rule=document.getElementById('rule');
        var role=document.getElementById('role');

        // pill: fade + scale in, 0.0-0.5s
        var pe=easeOutCubic(clamp(t/0.5));
        pill.style.opacity=pe;
        pill.style.transform='scale('+(0.9+0.1*pe)+')';

        // statement: fade + rise, 0.4-1.1s
        var se=easeOutCubic(clamp((t-0.4)/0.7));
        stmt.style.opacity=se;
        stmt.style.transform='translateY('+(24*(1-se))+'px)';

        // teal rule: grow from center, 1.0-1.6s
        var re=easeOutCubic(clamp((t-1.0)/0.6));
        rule.style.transform='scaleX('+re+')';

        // role: fade + rise, 1.5-2.0s
        var oe=easeOutCubic(clamp((t-1.5)/0.5));
        role.style.opacity=oe;
        role.style.transform='translateY('+(16*(1-oe))+'px)';
    """,
}
