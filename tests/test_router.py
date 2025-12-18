import unittest
import os
from src.router import Router
from exceptions.not_found import NotFoundException
from exceptions.forbidden import ForbiddenException

class RouterTest(unittest.TestCase):
    def test_simple_path(self):
        path = Router._full_path("hello.html")
        expected_path = os.path.join(Router.ASSET_DIR, "hello.html")
        self.assertEqual(path, expected_path)
    
    def test_resolve_returns_content_and_type(self):
        content, mime_type = Router.resolve("/about")
        self.assertIsInstance(content, bytes)
        self.assertEqual(mime_type, "text/html")
        
    def test_correct_mime_type_is_returned(self):
        content, mime_type = Router.resolve("/example.png")
        self.assertIsInstance(content, bytes)
        self.assertEqual(mime_type, "image/png")
        
    def test_path_with_leading_slash(self):
        path = Router._full_path("/hello.html")
        expected_path = os.path.join(Router.ASSET_DIR, "hello.html")
        self.assertEqual(path, expected_path)
        
    def test_path_with_trailing_slash(self):
        path = Router._full_path("hello.html/")
        expected_path = os.path.join(Router.ASSET_DIR, "hello.html")
        self.assertEqual(path, expected_path)
        
    def test_path_without_html_extension(self):
        path = Router._full_path("hello")
        expected_path = os.path.join(Router.ASSET_DIR, "hello.html")
        self.assertEqual(path, expected_path)
    
    def test_path_that_does_not_exist_raises_exception(self):
        with self.assertRaises(NotFoundException) as context:
            Router.resolve("404")
            
    def test_malicious_path_traversal_raises_exception(self):
        with self.assertRaises(ForbiddenException) as context:
            Router.resolve("../index.py")
            
if __name__ == '__main__':
    unittest.main()