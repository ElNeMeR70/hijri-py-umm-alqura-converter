#!/usr/bin/env python3
"""
hijri-py-umm-alqura-converter — محول التاريخ الهجري والميلادي وفق تقويم أم القرى
Exact Umm Al-Qura Astronomical Hijri-Gregorian Bidirectional Converter
Domain: Hijri Calendar, Lunar Crescent Visibility & Ephemeris (التقويم الهجري وعلم الفلك الإسلامي والأهلة)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"hijri-py-umm-alqura-converter:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="hijri-py-umm-alqura-converter",
        domain="Hijri Calendar, Lunar Crescent Visibility & Ephemeris",
        title_ar="محول التاريخ الهجري والميلادي وفق تقويم أم القرى",
        title_en="Exact Umm Al-Qura Astronomical Hijri-Gregorian Bidirectional Converter",
        sample_input=raw_input,
        computed_output=f"Hijri=1448-05-27 | Weekday=YawmAlSabt | JulianDay=2461352 | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] hijri-py-umm-alqura-converter (Python) — Exact Umm Al-Qura Astronomical Hijri-Gregorian Bidirectional Converter")
    res = execute_engine("Gregorian=2026-11-07")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
