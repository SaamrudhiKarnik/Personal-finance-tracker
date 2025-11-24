# Create run.py file

#!/usr/bin/env python3
"""
Personal Finance Tracker - Main Entry Point
"""

import sys
import os  

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Main entry point for the application"""
    try:
        from src.ui.main_window import MainWindow # type: ignore
        import tkinter as tk
        
        print("Starting Personal Finance Tracker...")
        
        # Create and run the application
        root = tk.Tk()
        app = MainWindow(root)
        root.mainloop()
        
    except ImportError as e:
        print(f"Error: {e}")
        print("Please make sure all dependencies are installed:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()