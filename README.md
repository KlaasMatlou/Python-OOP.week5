# OOP Assignment

## Description

This repository contains the solution for the Object-Oriented Programming (OOP) assignment. The assignment consists of two main parts:

**Assignment 1: Design Your Own Class!**

This section involves the creation of a custom class representing a Superhero, specifically Tanjiro Kamado from Demon Slayer. The `Tanjiro` class demonstrates key OOP principles such as:

* **Class Definition:** Creating a blueprint for a Tanjiro object.
* **Attributes:** Defining characteristics of a Tanjiro object (e.g., name, breathing style, health).
* **Methods:** Implementing actions that a Tanjiro object can perform (e.g., perform breathing technique, take damage).
* **Constructors (`__init__`)**: Initializing Tanjiro objects with specific starting values.
* **Inheritance:** Utilizing a base class `DemonSlayer` to establish a hierarchy and share common properties and behaviors with other potential demon slayers.

**Activity 2: Polymorphism Challenge!**

This section demonstrates polymorphism by creating a program with different animal classes that share a common `move()` action. Each animal class (`Dog`, `Bird`, `Fish`, `Snake`) implements the `move()` method in its own way, showcasing how objects of different classes can respond to the same method call in a manner specific to their type.

## Files Included

* `oop_assignment.py`: This file contains the Python code for both Assignment 1 (the `DemonSlayer` and `Tanjiro` classes) and Activity 2 (the `Animal` and its subclasses).

## How to Run the Code

1.  Ensure you have Python 3 installed on your system.
2.  Save the `oop_assignment.py` file to your local machine.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command: `python oop_assignment.py`

The output will show the instantiation and usage of the `Tanjiro` object from Assignment 1, as well as the demonstration of polymorphism with the different animal objects in Activity 2.

## Assignment Breakdown

### Assignment 1: Tanjiro Kamado Class

* **`DemonSlayer` Class (Base Class):**
    * `__init__(self, name, corps_rank)`: Initializes the name and Demon Slayer Corps rank.
    * `get_demon_slayer_info(self)`: Returns basic information about the demon slayer.
    * `slay_demon(self, demon_name)`: Records a demon being slain.
* **`Tanjiro` Class (Subclass of `DemonSlayer`):**
    * `__init__(self, corps_rank)`: Initializes Tanjiro's specific attributes, calling the parent constructor.
    * `perform_breathing_technique(self, technique_name)`: Simulates Tanjiro using a breathing technique.
    * `achieve_total_concentration(self)`: Sets Tanjiro's total concentration status.
    * `lose_total_concentration(self)`: Resets Tanjiro's total concentration status.
    * `take_damage(self, amount)`: Simulates Tanjiro taking damage and updates his health status.
    * `get_info(self)`: Returns a comprehensive overview of Tanjiro's current state.

### Activity 2: Polymorphism Challenge

* **`Animal` Class (Base Class):**
    * `__init__(self, name)`: Initializes the animal's name.
    * `move(self)`: A generic move method.
* **Subclasses (`Dog`, `Bird`, `Fish`, `Snake`):**
    * Each subclass inherits from `Animal`.
    * Each subclass overrides the `move()` method to provide a specific movement description for that animal.
* **Demonstration:** A list of different animal objects is created, and the `move()` method is called on each, showcasing polymorphic behavior.
