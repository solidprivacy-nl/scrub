"""User-facing review guidance text for Scrub Legal.

These strings keep the review workflow understandable for non-technical legal
users. Keep them short, practical and action-oriented.
"""

REVIEW_INTRO_GUIDANCE = (
    "Controleer de gevonden gegevens voordat je exporteert. Alleen aangevinkte "
    "regels worden meegenomen in de opgeschoonde output."
)

CANDIDATE_GUIDANCE = (
    "Rijen met status 'Controle nodig' zijn mogelijke gemiste waarden. Ze staan "
    "niet automatisch aan. Controleer ze handmatig en vink ze alleen aan wanneer "
    "ze echt vervangen moeten worden."
)

FOCUS_FILTER_GUIDANCE = (
    "De focusfilter helpt alleen om sneller te kijken. De volledige vervangtabel "
    "blijft leidend voor de export."
)

TECHNICAL_DETAILS_GUIDANCE = (
    "Technische details zijn bedoeld voor controle, debugging en verbetering van "
    "herkenners. Voor normaal gebruik hoef je deze meestal niet te openen."
)

AI_USAGE_GUIDANCE = (
    "Gebruik AI pas nadat het document is gecontroleerd en gescrubd. Deel nooit de "
    "originele tekst of een Scrub Key met een externe AI-dienst tenzij dat bewust "
    "en toegestaan is."
)

EXPORT_GUIDANCE = (
    "Download pas wanneer je de vervangtabel hebt gecontroleerd. Scrub helpt bij "
    "het vinden van gevoelige gegevens, maar handmatige controle blijft nodig."
)


def review_guidance_items() -> list[str]:
    return [
        REVIEW_INTRO_GUIDANCE,
        CANDIDATE_GUIDANCE,
        FOCUS_FILTER_GUIDANCE,
        TECHNICAL_DETAILS_GUIDANCE,
        AI_USAGE_GUIDANCE,
    ]


def review_guidance_markdown() -> str:
    return "\n".join(f"- {item}" for item in review_guidance_items())
