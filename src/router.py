import os
import re

class Router:    
    ASSET_DIR = os.path.join(os.getcwd(), "public")
    
    @staticmethod
    def resolve(path: str) -> bytes:
        with open(Router._abs_path(path), "rb") as file:
            return file.read()
        
    @staticmethod
    def _abs_path(path: str) -> bytes:
        path = path.strip("/")
        
        if not path:
            path = "index.html"
            
        if not Router._has_file_extension(path):
            path += ".html"
        
        return os.path.join(Router.ASSET_DIR, path)
    
    @staticmethod
    def _has_file_extension(path: str) -> bool:
        pattern = r'\.[^.]+$'
        return bool(re.search(pattern, path))