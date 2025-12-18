import os
import re
import mimetypes
from exceptions.forbidden import ForbiddenException
from exceptions.not_found import NotFoundException

class Router:    
    ASSET_DIR = os.path.join(os.getcwd(), "public")
    
    @staticmethod
    def resolve(path: str) -> bytes:
        full_path = Router._full_path(path)
        real_path = os.path.abspath(full_path)
  
        if not Router._is_in_public_dir(real_path):
            raise ForbiddenException()
        
        mime_type, _ = mimetypes.guess_type(path)
        if not mime_type:
             mime_type = "text/html"
             
        if not os.path.exists(real_path):
            raise NotFoundException()
        
        with open(real_path, "rb") as file:
            return file.read(), mime_type
        
    @staticmethod
    def _full_path(path: str) -> bytes:
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
    
    @staticmethod
    def _is_in_public_dir(path: str) -> bool:
        public_dir = os.path.abspath(Router.ASSET_DIR)
        return path.startswith(public_dir)