# Phase 3 – Project Design

## 1. System Architecture

FitBuddy follows a simple AI-based application architecture.

User
↓
Web Interface
↓
FastAPI Backend
↓
Gemini API
↓
AI Generated Fitness Plan
↓
Web Interface

## 2. Main Components

### User Interface
Collects user information such as name, age, weight, height, fitness level and fitness goal.

### Backend
The FastAPI backend receives user information, validates the input and communicates with the Gemini API.

### Gemini AI
The Gemini model processes the user's requirements and generates a personalized fitness plan.

### Output
The generated fitness plan is displayed to the user through the web interface.

## 3. Data Flow

1. User opens FitBuddy.
2. User enters fitness details.
3. Backend receives the information.
4. Backend sends a suitable prompt to Gemini.
5. Gemini generates the fitness plan.
6. Backend receives the response.
7. The fitness plan is displayed to the user.

## 4. Basic Database Design

User Details:
- User ID
- Name
- Age
- Weight
- Height
- Fitness Level
- Fitness Goal

Fitness Plan:
- Plan ID
- User ID
- Workout Plan
- Recommendations

## 5. User Interface Screens

The application will contain:
- Home page
- User details form
- Fitness goal selection
- Generate Plan button
- Generated fitness plan page
