import pycountry
from typing import Optional
import whois

def norm_country_name(name: str) -> Optional[str]:
    if not name:
        return None
    name = name.strip()
    c = pycountry.countries.get(alpha_2=name.upper())
    if c:
        return c.alpha_2
    try:
        c = pycountry.countries.lookup(name)
        return c.alpha_2
    except LookupError:
        return None

def whois_country(domain: str) -> Optional[str]:
    try:
        w = whois.whois(domain)
        cand = None
        # python-whois may return single str or list
        for key in ("country", "registrant_country", "registrant_country_code"):
            v = w.get(key)
            if isinstance(v, list):
                v = next((x for x in v if x), None)
            if v:
                cand = v
                break
        return norm_country_name(cand) if cand else None
    except Exception:
        return None