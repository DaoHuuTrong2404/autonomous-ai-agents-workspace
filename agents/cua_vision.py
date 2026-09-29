"""
Computer-Use Agent (CUA) Vision & Structured Object Model (SOM) Parser
Transforms high-resolution desktop screenshots and DOM elements into semantic interactive coordinates.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional

@dataclass
class SOMElement:
    id: int
    label: str
    element_type: str # 'button', 'input', 'link', 'text'
    bbox: List[int]   # [x1, y1, x2, y2]
    interactive: bool

    @property
    def center_coordinates(self) -> tuple[int, int]:
        cx = (self.bbox[0] + self.bbox[2]) // 2
        cy = (self.bbox[1] + self.bbox[3]) // 2
        return (cx, cy)

class VisionCUAAgent:
    """
    Simulates CUA look-act-verify workflow with visual SOM compression.
    """
    def __init__(self, screen_resolution: tuple[int, int] = (1920, 1080)):
        self.resolution = screen_resolution
        self.detected_elements: List[SOMElement] = []
        self.action_history: List[Dict[str, Any]] = []

    def parse_mock_som(self, raw_elements: List[Dict[str, Any]]) -> List[SOMElement]:
        self.detected_elements = []
        for i, el in enumerate(raw_elements):
            elem = SOMElement(
                id=i + 1,
                label=el.get("label", f"element_{i+1}"),
                element_type=el.get("type", "unknown"),
                bbox=el.get("bbox", [0, 0, 10, 10]),
                interactive=el.get("interactive", True)
            )
            self.detected_elements.append(elem)
        return self.detected_elements

    def click_element_by_label(self, label: str) -> Optional[Dict[str, Any]]:
        target = next((el for el in self.detected_elements if label.lower() in el.label.lower()), None)
        if not target:
            return None
        coord = target.center_coordinates
        action = {
            "type": "click",
            "target_id": target.id,
            "target_label": target.label,
            "coordinates": coord,
            "status": "SUCCESS"
        }
        self.action_history.append(action)
        return action
