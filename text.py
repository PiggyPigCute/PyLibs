
ALMIN = "abcdefghijklmnopqrstuvwxyz"
ALMAJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"
ALPHA = ALMIN + ALMAJ
CHARS = NUM + ALPHA

ALLSUP = "⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖˤʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿˢᵀᵁⱽʷˣᵞᶻ"
ALLINF = "₀₁₂₃₄₅₆₇₈₉ₐ   ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓᵧ                           "
NUMSUP = "⁰¹²³⁴⁵⁶⁷⁸⁹"
NUMINF = "₀₁₂₃₄₅₆₇₈₉"
GREEK = "αβγδεφγηιχκλµνθπςρστυφωξψζABΓΔEΦΓHIXKΛMNΘΠΣPΣTYΦΩΞΨZ"
ITALIC = "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
BOLD = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
MATHBB = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
CURSIVE = "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓧𝓨𝓩"

def sup(text:str|int) -> str:
    return "".join([ALLSUP[CHARS.index(char)] for char in text]) if isinstance(text,str) else "".join([NUMSUP[int(char)] for char in str(text)])

def inf(text:str|int) -> str:
    return "".join([ALLINF[CHARS.index(char)] for char in text]) if isinstance(text,str) else "".join([NUMINF[int(char)] for char in str(text)])

def italic(text:str) -> str:
    return "".join([ITALIC[ALPHA.index(char)] for char in text])

def bold(text:str) -> str:
    return "".join([BOLD[ALPHA.index(char)] for char in text])

def mathbb(text:str) -> str:
    return "".join([MATHBB[ALPHA.index(char)] for char in text])

def cursive(text:str) -> str:
    return "".join([CURSIVE[ALPHA.index(char)] for char in text])

def greek(text:str) -> str:
    return "".join([GREEK[ALPHA.index(char)] for char in text])
