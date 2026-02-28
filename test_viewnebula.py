# test_viewnebula.py
"""
Tests for ViewNebula module.
"""

import unittest
from viewnebula import ViewNebula

class TestViewNebula(unittest.TestCase):
    """Test cases for ViewNebula class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ViewNebula()
        self.assertIsInstance(instance, ViewNebula)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ViewNebula()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
