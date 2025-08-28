from typing import Optional
import tldextract

ALL_CC_TLDS = {
    "ac","ad","ae","af","ag","ai","al","am","ao","aq","ar","as","at","au","aw","ax","az",
    "ba","bb","bd","be","bf","bg","bh","bi","bj","bm","bn","bo","bq","br","bs","bt","bv","bw","by","bz",
    "ca","cc","cd","cf","cg","ch","ci","ck","cl","cm","cn","co","cr","cu","cv","cw","cx","cy","cz",
    "de","dj","dk","dm","do","dz",
    "ec","ee","eg","eh","er","es","et","eu",
    "fi","fj","fk","fm","fo","fr",
    "ga","gb","gd","ge","gf","gg","gh","gi","gl","gm","gn","gp","gq","gr","gs","gt","gu","gw","gy",
    "hk","hm","hn","hr","ht","hu",
    "id","ie","il","im","in","io","iq","ir","is","it",
    "je","jm","jo","jp",
    "ke","kg","kh","ki","km","kn","kp","kr","kw","ky","kz",
    "la","lb","lc","li","lk","lr","ls","lt","lu","lv","ly",
    "ma","mc","md","me","mf","mg","mh","mk","ml","mm","mn","mo","mp","mq","mr","ms","mt","mu","mv","mw","mx","my","mz",
    "na","nc","ne","nf","ng","ni","nl","no","np","nr","nu","nz",
    "om",
    "pa","pe","pf","pg","ph","pk","pl","pm","pn","pr","ps","pt","pw","py",
    "qa",
    "re","ro","rs","ru","rw",
    "sa","sb","sc","sd","se","sg","sh","si","sj","sk","sl","sm","sn","so","sr","ss","st","sv","sx","sy","sz",
    "tc","td","tf","tg","th","tj","tk","tl","tm","tn","to","tr","tt","tv","tw","tz",
    "ua","ug","uk","um","us","uy","uz",
    "va","vc","ve","vg","vi","vn","vu",
    "wf","ws",
    "ye","yt",
    "za","zm","zw",
    "xk"
}


def cc_from_tld(domain: str) -> Optional[str]:
    """
    Extract country code from a domain's TLD if it's a valid ccTLD.
    Handles both pure ccTLDs (".de", ".fr") and second-level ones (".co.uk", ".com.au").
    """
    ext = tldextract.extract(domain)
    sfx = ext.suffix.lower()  # e.g., "bd", "co.uk", "com.au"

    parts = sfx.split(".")
    
    if len(parts) == 1 and sfx in ALL_CC_TLDS:
        return sfx.upper()

    if len(parts) == 2 and parts[-1] in ALL_CC_TLDS:
        return parts[-1].upper()

    return None