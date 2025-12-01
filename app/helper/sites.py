from typing import Optional, Tuple, List, Dict, Any

class SitesHelper:
    def __init__(self):
        pass

    @property
    def auth_level(self) -> int:
        return 2

    @property
    def auth_version(self) -> str:
        return "1.0.0"

    @property
    def indexer_version(self) -> str:
        return "1.0.0"

    async def async_get_indexer(self, domain: str) -> Optional[Dict[str, Any]]:
        return {
            "name": "Mock Site",
            "public": True,
            "category": {
                "movie": [{"id": "1", "name": "Movie"}],
                "tv": [{"id": "2", "name": "TV"}]
            }
        }

    def get_indexer(self, domain: str) -> Optional[Dict[str, Any]]:
        return {
            "name": "Mock Site",
            "public": True,
            "category": {
                "movie": [{"id": "1", "name": "Movie"}],
                "tv": [{"id": "2", "name": "TV"}]
            }
        }

    def get_authsites(self) -> Dict[str, Any]:
        return {}

    def check_user(self, site: str = None, params: Dict[str, Any] = None, **kwargs) -> Tuple[bool, str]:
        return True, "Authentication successful"

    def get_indexsites(self) -> Dict[str, Any]:
        return {}

    def get_indexers(self) -> List[Dict[str, Any]]:
        return []

    def check(self, domain: str) -> Tuple[bool, str]:
        return True, "Site check successful"
