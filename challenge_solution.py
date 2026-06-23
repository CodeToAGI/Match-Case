"""
CodeToAGI — Episode 44 Challenge
Command Dispatcher using match/case (Structural Pattern Matching)

Task:
1. Create a function that handles text commands using match/case
2. Support: help, quit, go <direction>
3. Use a guard to only allow valid directions (north, south, east, west)
4. Bonus: Also handle dictionary-based commands

Run this file and try different commands!
"""

from typing import Any


def dispatch_command(cmd: str | dict) -> str:
    """
    Advanced command dispatcher using structural pattern matching.
    """
    
    # Handle string commands
    if isinstance(cmd, str):
        parts = cmd.strip().lower().split()
        
        match parts:
            # Literal pattern - exact match
            case ["help"]:
                return "Available commands: help, quit, go <direction>"
            
            # Literal pattern
            case ["quit"]:
                return "Goodbye! 👋"
            
            # Sequence pattern with capture + guard
            case ["go", direction] if direction in {"north", "south", "east", "west"}:
                return f"Moving {direction}..."
            
            # Sequence pattern with wildcard for invalid directions
            case ["go", direction]:
                return f"Invalid direction: {direction}. Use north/south/east/west."
            
            # Sequence pattern with *rest (variable length)
            case ["pick", item, *rest]:
                return f"Picked up {item}. Remaining: {rest}"
            
            # Wildcard (default case)
            case _:
                return f"Unknown command: {' '.join(parts)}"
    
    # Bonus: Handle dictionary-based commands (mapping pattern)
    elif isinstance(cmd, dict):
        match cmd:
            case {"action": "go", "direction": direction} if direction in {"north", "south", "east", "west"}:
                return f"Moving {direction} (from dict)..."
            
            case {"action": "help"}:
                return "Help from dict command"
            
            case {"action": "quit"}:
                return "Quitting from dict command"
            
            case {"action": action, **rest}:
                return f"Action '{action}' received with data: {rest}"
            
            case _:
                return "Invalid command dictionary"
    
    return "Unsupported input type"


# ====================== TEST CASES ======================

if __name__ == "__main__":
    print("=== Command Dispatcher Demo (EP44 Challenge) ===\n")
    
    test_commands = [
        "help",
        "quit",
        "go north",
        "go east",
        "go invalid",
        "pick sword",
        "pick health potion dungeon",
        "attack dragon",
        # Bonus dict commands
        {"action": "go", "direction": "south"},
        {"action": "quit"},
        {"action": "cast", "spell": "fireball", "target": "goblin"},
    ]
    
    for cmd in test_commands:
        result = dispatch_command(cmd)
        print(f"Input: {cmd}")
        print(f"Output: {result}\n")
