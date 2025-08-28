import collections
import os
import socket
from typing import Any, Dict, List, Optional

import dns.resolver
import pycountry
import tldextract
import whois  # package name: python-whois
from geoip2.database import Reader as GeoIPReader

from .all_tlds import cc_from_tld
from .whois_country import whois_country


def resolve_ips(domain: str) -> List[str]:
    ips = set()
    try:
        for rtype in ["A", "AAAA"]:
            try:
                answers = dns.resolver.resolve(domain, rtype, lifetime=3.0)
                for r in answers:
                    ips.add(r.address)
            except Exception:
                pass
    except Exception:
        pass
    # fallback via socket
    if not ips:
        try:
            for fam in (socket.AF_INET, socket.AF_INET6):
                try:
                    infos = socket.getaddrinfo(domain, None, family=fam)
                    for info in infos:
                        ips.add(info[4][0])
                except Exception:
                    pass
        except Exception:
            pass
    return list(ips)

def ip_countries(ips: List[str], geoip_db_path: Optional[str]) -> List[str]:
    if not geoip_db_path or not os.path.exists(geoip_db_path):
        return []
    out = []
    try:
        with GeoIPReader(geoip_db_path) as reader:
            for ip in ips:
                try:
                    rec = reader.country(ip)
                    if rec and rec.country and rec.country.iso_code:
                        out.append(rec.country.iso_code.upper())
                except Exception:
                    # Some IPv6 or private ranges
                    continue
    except Exception:
        return []
    return out

def pick_final(cc_from_tld_: Optional[str], whois_cc: Optional[str], ip_ccs: List[str]) -> Dict[str, Any]:
    votes = collections.Counter()
    if cc_from_tld_:
        votes[cc_from_tld_] += 2  # strong signal
    if whois_cc:
        votes[whois_cc] += 2      # strong signal
    for c in ip_ccs:
        votes[c] += 1             # weaker, hosting can be anywhere

    final = votes.most_common(1)[0][0] if votes else None

    return {
        "final_alpha2": final,
        "confidence": "high" if final and votes[final] >= 3 else ("medium" if final else "none"),
        "votes": dict(votes),
    }

def alpha2_to_name(alpha2: Optional[str]) -> Optional[str]:
    if not alpha2:
        return None
    c = pycountry.countries.get(alpha_2=alpha2)
    return c.name if c else None

# --- main --------------------------------------------------------------------

def get_region(domain: str):
    # Get the path to the GeoIP database relative to this package
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geoip_db_path = os.path.join(current_dir, "GeoLite2-Country.mmdb")
    domain = domain.strip().lower()
    if domain.startswith("http://") or domain.startswith("https://"):
        domain = tldextract.extract(domain).registered_domain or domain

    tld_cc = cc_from_tld(domain)
    whois_cc = whois_country(domain)
    ips = resolve_ips(domain)
    ip_ccs = ip_countries(ips, geoip_db_path or os.getenv("GEOIP_DB"))

    choice = pick_final(tld_cc, whois_cc, ip_ccs)

    return choice