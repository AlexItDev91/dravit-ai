# Spatial reasoning

This is a compact method for reasoning about the user's brief. It does not add runtime fields, a geometry engine, a route graph or new checks to Dravit.

## Function before placement

Identify activities and their participants, sequence, simultaneous use, shared/private spaces, required connections, storage, service and likely changes. Preserve the user's stated purpose. Ask for functional needs where a choice matters; do not invent personal characteristics, diagnoses, household composition or a preferred lifestyle.

Resolve the spatial programme into existing saved Rooms/Levels/objects and explicit assistant-context requirements. A Room name is a hint, not verified occupancy or purpose. Room polygons describe logical zoning; their area/shape alone does not establish enclosure, an entry or a traversable route.

Consider alternatives when requirements conflict. Explain the concrete tradeoff, such as a wider passage reducing storage, or privacy versus a shorter shared route. Preserve hard brief requirements until the user changes them. Recommendations become requirements only when accepted.

## Four different spatial questions

1. **Physical volume:** occupied XYZ geometry, cutouts, assemblies, supported hosts and joins. XY bounding-box overlap can be a broad hint, not a collision verdict. Stacked floors, a proper wall junction and a hosted cut are not automatically defects.
2. **Motion:** the path of the actual leaf, sash, drawer, sliding/folding part or articulated assembly in its required states. Read the true mechanism, side and limits. A drawn swing arc or final open pose does not establish a complete swept volume.
3. **Use:** the human position, reach, transfer, assistance or operating zone needed at the functional side. It is not the object's rectangle or a click radius. Conditions differ for a wardrobe front and rear or the user-selected sides of a bed.
4. **Approach and service:** a continuous path to that usable position and a separate path/space for maintenance, replacement and deliveries. Proximity to an object is not proof of access.

Use the existing read geometry/checks for these questions. If a mechanism, zone or algorithm is absent, record the missing fact/capability. Never invent a universal clearance, expand every object by a fixed margin or create synthetic fields to make a program report pass.

Overlapping working zones can be acceptable when the brief permits sequential use and an actual sequence preserves access in every state. Simultaneous required activities must work together; inventing a schedule does not resolve that conflict.

## Routes, rooms and floors

Trace from the actual entrance through passages and transitions to the required spaces and object positions. Separate ordinary access, moving large items and emergency escape; proving one does not prove the others. Respect the model's known external boundary.

For vertical circulation inspect base approach, landings, runs, slab opening, headroom where measurable and top exit into a reachable space. A stair touching two Levels is insufficient. A ramp/lift/alternative route counts only when it is explicitly selected and actually modeled with adequate evidence. Do not add an unsupported circulation tool to fill the gap.

For the residential brief used in Dravit evaluation, used floors need an access route; the required bedroom needs its entrance/door and a window suited to the requested function; other living spaces need the brief's windows. These are that project's requirements, not universal regulations. Storage, technical shafts/voids, service-only areas and open zones have different requirements. Exceptions must come from an established purpose and explicit brief, not a convenient post-failure relabeling.

## Windows and environmental questions

Resolve whether the window is for outside view, daylight, ventilation, internal glazing or another explicit purpose. Inspect its saved host and orientation and any actual obstruction facts. A decorative picture, opaque infill or internal pane cannot silently replace a requested outside-view opening. A tree may aid shade while limiting a view; surface the tradeoff.

A clear aperture or bright render does not prove daylight quantity, glare, ventilation, acoustic comfort, thermal performance or compliance. These require their own supported calculations and inputs. Report them as unknown/unsupported when absent. The same limit applies to structural capacity and engineering systems.

## Sources and numeric requirements

Numeric clearances and normative claims require the exact source edition/section, jurisdiction, units, user profile, stage, measurements and applicability. Distinguish a project requirement, contextual recommendation and applicable standard. Do not activate a national standard globally or treat one minimum as whole-standard compliance.

The underlying Dravit E8 research recorded sources on 2026-10-16. This reference preserves its scope; consult the original sources for a new numeric/normative decision:

| Source | Adopted contribution | Boundary |
|---|---|---|
| [CEUD Homes Section 3](https://universaldesign.ie/uploads/publications/Section-3-Spaces-for-Living_2024-09-24-123002_xwpl.pdf), 2015 edition, §§3.1/3.3/3.5/3.6/3.7 | Activity, approach, storage, privacy and future use | Irish UD/UD+ guidance; upload date is not edition; no universal dimensions imported |
| [National Design Guide](https://www.gov.uk/government/publications/national-design-guide/national-design-guide-accessible-version), 2021, H1-H3/L1-L3 | Fit for purpose, social/private space, personal control, adaptation | English qualitative guidance, not engineering certification |
| [US Access Board Chapter 4](https://www.access-board.gov/ada/chapter/ch04/), 2010 ADA, §404 | Different useful opening/approach/maneuvering questions | Only ADA-scoped facilities; nominal leaf width alone proves nothing |
| [NDSS](https://www.gov.uk/government/publications/technical-housing-standards-nationally-described-space-standard/technical-housing-standards-nationally-described-space-standard), 2015/2016, §§1-10/Table 1 | Occupancy and whole-home space context | England when adopted; bedroom minima cannot be isolated; not sufficient for Category 3 wheelchair housing |
| [Merrell et al.](https://graphics.stanford.edu/~pmerrell/furnitureLayout2.pdf), SIGGRAPH 2011, §§2/3/5 | Layout criteria and competing objectives | Ground-plane/height limitations; a score is not mandatory-requirement proof |
| [Function2Scene](https://arxiv.org/html/2605.30819v1), v1, §§3-6/C.3 | Activity brief, staged feedback, check/repair as one research reference | No code/assets or dependency imported; LLM/VLM judgment is not deterministic validation |

No regulation, anthropometric numeric default or Function2Scene runtime is bundled. Use [verification](verification.md) to keep evidence and limitations explicit.
